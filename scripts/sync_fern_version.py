#!/usr/bin/env python3
"""Sync Fern's generated SDK version into repo-owned package metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r'^(version\s*=\s*)"([^"]+)"(\s*)$')


def read_fern_version() -> str:
    metadata_path = ROOT / ".fern" / "metadata.json"
    metadata = json.loads(metadata_path.read_text())
    version = metadata.get("sdkVersion")
    if not isinstance(version, str) or not version:
        raise ValueError(f"{metadata_path} does not contain a string sdkVersion")
    return version


def sync_pyproject(version: str, *, write: bool) -> bool:
    path = ROOT / "pyproject.toml"
    lines = path.read_text().splitlines(keepends=True)
    in_project = False

    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "[project]":
            in_project = True
            continue
        if in_project and stripped.startswith("["):
            break
        if in_project and stripped.startswith("version"):
            newline = "\n" if line.endswith("\n") else ""
            content = line[:-1] if newline else line
            match = VERSION_RE.match(content)
            if match is None:
                raise ValueError(f"Unsupported version line in {path}: {line!r}")
            updated = f'{match.group(1)}"{version}"{match.group(3)}{newline}'
            if updated == line:
                return False
            lines[index] = updated
            if write:
                path.write_text("".join(lines))
            return True

    raise ValueError(f"Could not find [project].version in {path}")


def sync_uv_lock(version: str, *, write: bool) -> bool:
    path = ROOT / "uv.lock"
    lines = path.read_text().splitlines(keepends=True)
    in_package = False
    is_islo_package = False

    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "[[package]]":
            in_package = True
            is_islo_package = False
            continue
        if in_package and stripped == 'name = "islo"':
            is_islo_package = True
            continue
        if in_package and is_islo_package and stripped.startswith("version"):
            newline = "\n" if line.endswith("\n") else ""
            content = line[:-1] if newline else line
            match = VERSION_RE.match(content)
            if match is None:
                raise ValueError(f"Unsupported version line in {path}: {line!r}")
            updated = f'{match.group(1)}"{version}"{match.group(3)}{newline}'
            if updated == line:
                return False
            lines[index] = updated
            if write:
                path.write_text("".join(lines))
            return True

    raise ValueError(f"Could not find islo package version in {path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if package metadata is out of sync")
    args = parser.parse_args()

    version = read_fern_version()
    changed_pyproject = sync_pyproject(version, write=not args.check)
    changed_uv_lock = sync_uv_lock(version, write=not args.check)
    changed = changed_pyproject or changed_uv_lock

    if args.check and changed:
        print(f"Package metadata was not synced to Fern SDK version {version}", file=sys.stderr)
        return 1

    if changed:
        print(f"Synced package metadata to Fern SDK version {version}")
    else:
        print(f"Package metadata already matches Fern SDK version {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
