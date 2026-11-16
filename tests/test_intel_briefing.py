"""Production intelligence-briefing profile and config checks."""

from pathlib import Path

from src.models import Config
from src.processing.profiles import ProfileRegistry

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_CONFIG = ROOT / "data" / "config.github.json"

EXPECTED_FEEDS = {
    "The Cipher Brief": "https://www.thecipherbrief.com/feed",
    "CISA News": "https://www.cisa.gov/news.xml",
    "NCSC UK News": "https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml",
    "DefenseScoop": "https://defensescoop.com/feed/",
    "Bellingcat": "https://www.bellingcat.com/feed/",
    "The Record": "https://therecord.media/feed",
    "CyberScoop": "https://cyberscoop.com/feed/",
    "Unit 42": "https://unit42.paloaltonetworks.com/feed/",
    "Krebs on Security": "https://krebsonsecurity.com/feed/",
    "CERT-EU Threat Intelligence": "https://cert.europa.eu/publications/threat-intelligence-rss",
    "Recorded Future": "https://www.recordedfuture.com/feed",
    "Flashpoint Blog": "https://flashpoint.io/blog/feed/",
    "USGIF": "https://usgif.org/feed/",
    "Via Satellite Government/Military": "https://www.satellitetoday.com/government-military/feed/",
}


def _load_profile() -> object:
    return ProfileRegistry.load(ROOT / "profiles", "intel-news").get("intel-news")


def test_intel_news_profile_loads_without_tools():
    profile = _load_profile()

    assert profile.definition.name == "Global Intelligence Industry"
    assert profile.definition.display_names["zh"] == "全球情报行业动态"
    assert "OSINT" in profile.match_prompt
    assert "geospatial" in profile.match_prompt.lower() or "GEOINT" in profile.match_prompt
    assert "generic software or AI" in profile.match_prompt
    assert "unrelated" in profile.match_prompt or "not specifically about intelligence" in profile.match_prompt
    assert "official statement" in profile.enrichment_prompt
    assert "allegations" in profile.enrichment_prompt
    assert "vendor claim" in profile.enrichment_prompt
    assert all(not block.tools for block in profile.definition.enrichment.blocks)
    primary = next(block for block in profile.definition.enrichment.blocks if block.primary)
    assert primary.id == "summary"


def test_production_github_config_is_intel_briefing():
    config = Config.model_validate_json(PRODUCTION_CONFIG.read_text(encoding="utf-8"))
    registry = ProfileRegistry.load(ROOT / "profiles", config.processing.default_profile)
    registry.validate_source_references(config.sources.model_dump())
    registry.validate_digest_references(config.digest)

    assert config.processing.default_profile == "intel-news"
    settings = config.processing.profile_settings["intel-news"]
    assert settings.threshold == 6.5
    assert settings.topic_dedup is True

    assert config.ai.languages == ["zh", "en"]
    assert config.ai.api_key_env == "OPENROUTER_API_KEY"
    assert config.ai.base_url == "https://openrouter.ai/api/v1"
    assert config.ai.model.endswith(":free")
    assert config.ai.analysis_concurrency == 1
    assert config.ai.enrichment_concurrency == 1
    assert config.ai.throttle_sec >= 3
    fallbacks = config.ai.extra_body["models"]
    assert fallbacks[0] == config.ai.model
    assert all(str(model).endswith(":free") for model in fallbacks)

    assert config.collection.time_window_hours == 24
    assert config.digest.max_items == 8
    assert config.digest.profile_order[0] == "intel-news"

    assert config.sources.github == []
    assert config.sources.hackernews.enabled is False
    assert config.sources.reddit.enabled is False
    assert config.sources.ossinsight.enabled is False
    assert config.sources.google_news is None or config.sources.google_news.enabled is False
    assert config.sources.gdelt is None or config.sources.gdelt.enabled is False

    enabled = [source for source in config.sources.rss if source.enabled]
    by_name = {source.name: source for source in enabled}
    assert set(by_name) == set(EXPECTED_FEEDS)
    for name, url in EXPECTED_FEEDS.items():
        source = by_name[name]
        assert str(source.url).rstrip("/") == url.rstrip("/")
        assert source.profile == "intel-news"
        assert source.fetch_limit is not None and source.fetch_limit >= 1
        assert source.category in {
            "agencies-policy",
            "osint",
            "threat-intelligence",
            "commercial-intel",
            "geoint",
        }

    grouped = {
        category
        for group in config.digest.category_groups.values()
        for category in group.categories
    }
    assert grouped == {source.category for source in enabled}


def test_intel_briefing_doc_lists_verified_sources():
    doc = (ROOT / "docs" / "intel-briefing.md").read_text(encoding="utf-8")
    assert "全球情报行业" in doc
    assert "24 小时" in doc or "过去 24 小时" in doc
    assert "暂无重要动态" in doc
    for name, url in EXPECTED_FEEDS.items():
        assert name in doc
        assert url in doc
    # Limitations should mention sources we verified but did not enable.
    assert "ODNI" in doc
    assert "Google News" in doc
