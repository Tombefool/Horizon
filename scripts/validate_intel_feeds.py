#!/usr/bin/env python3
"""Fetch and parse RSS feeds listed in the production GitHub Actions config.

This script does not call the LLM. Exit status is 0 only when every enabled
feed returns HTTP 200 and at least one parseable entry.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

import feedparser
import httpx

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "data" / "config.github.json"
UA = "HorizonFeedProbe/1.0 (feed validation; +https://github.com/Tombefool/Horizon)"


def _entry_date(entry) -> datetime | None:
    for key in ("published", "updated", "created"):
        raw = entry.get(key)
        if not raw:
            continue
        try:
            parsed = parsedate_to_datetime(raw)
        except Exception:
            continue
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    for key in ("published_parsed", "updated_parsed", "created_parsed"):
        values = entry.get(key)
        if values:
            try:
                return datetime(*values[:6], tzinfo=timezone.utc)
            except Exception:
                continue
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    feeds = [item for item in config.get("sources", {}).get("rss", []) if item.get("enabled")]
    if not feeds:
        print("No enabled RSS feeds found.", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc)
    failures = 0
    headers = {
        "User-Agent": UA,
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
    }
    with httpx.Client(follow_redirects=True, timeout=30.0, headers=headers) as client:
        for feed in feeds:
            name = feed["name"]
            url = feed["url"]
            try:
                response = client.get(url)
            except Exception as exc:
                print(f"FAIL  {name}: {type(exc).__name__}: {exc}")
                failures += 1
                continue
            parsed = feedparser.parse(response.content)
            entries = parsed.entries or []
            dates = [dt for dt in (_entry_date(entry) for entry in entries) if dt]
            latest = max(dates) if dates else None
            fresh_24h = sum(1 for dt in dates if (now - dt).total_seconds() <= 24 * 3600)
            ok = response.status_code == 200 and len(entries) > 0
            status = "OK  " if ok else "FAIL"
            latest_s = latest.strftime("%Y-%m-%d") if latest else "-"
            print(
                f"{status} HTTP {response.status_code:<3} entries={len(entries):<3} "
                f"fresh_24h={fresh_24h:<2} latest={latest_s} {name}"
            )
            if not ok:
                failures += 1
                if parsed.bozo:
                    print(f"      parse error: {parsed.bozo_exception}")
    if failures:
        print(f"\n{failures}/{len(feeds)} feeds failed.", file=sys.stderr)
        return 1
    print(f"\nAll {len(feeds)} enabled feeds parsed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
