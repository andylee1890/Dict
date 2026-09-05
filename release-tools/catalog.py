from __future__ import annotations

from datetime import datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


REPOSITORY = "andylee1890/Dict"
BRANCH = "main"

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT
RECORDS_DIR = ROOT / "release-records"

IGNORED_EXTENSIONS = {".db", ".bak", ".ini"}
RELEASE_ONLY_EXTENSIONS = {".mdx", ".mdd"}

RELEASE_ORDER = [
    "CollinsCOBUILDOverhaul v2.30",
    "LDOCE6++ En-Cn V3-0",
    "单词释义比例",
    "新概念英语句典",
    "朗文当代反查词典",
    "柯林斯汉英大词典",
    "牛津高阶双解8-oalecd8e",
    "牛津高阶反查词典",
    "简明必应版-css",
    "英语近义词辨析v6",
    "词根词缀词典",
    "词根词缀词源 （合集词典）",
    "词根词缀词频词源",
    "译典通英汉双向字典",
    "近义词词语辨析",
    "韦氏高阶英汉双解词典",
]

RELEASE_TAGS = {
    "CollinsCOBUILDOverhaul v2.30": "collins-cobuild-overhaul-v2-30",
    "LDOCE6++ En-Cn V3-0": "ldoce6-en-cn-v3-0",
    "单词释义比例": "word-definition-ratio",
    "新概念英语句典": "new-concept-english-sentence-dictionary",
    "朗文当代反查词典": "longman-reverse-dictionary",
    "柯林斯汉英大词典": "collins-chinese-english-dictionary",
    "牛津高阶双解8-oalecd8e": "oxford-advanced-learner-dictionary-8-oalecd8e",
    "牛津高阶反查词典": "oxford-advanced-reverse-dictionary",
    "简明必应版-css": "concise-bing-css",
    "英语近义词辨析v6": "english-synonym-differentiation-v6",
    "词根词缀词典": "word-root-affix-dictionary",
    "词根词缀词源 （合集词典）": "word-root-affix-etymology-collection",
    "词根词缀词频词源": "word-root-affix-frequency-etymology",
    "译典通英汉双向字典": "dr-eye-bilingual-dictionary",
    "近义词词语辨析": "synonym-differentiation",
    "韦氏高阶英汉双解词典": "webster-advanced-english-chinese-dictionary",
}

PUBLISHED_RELEASES = {
    "collins-cobuild-overhaul-v2-30",
}

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}


@dataclass(frozen=True)
class Asset:
    name: str
    path: str
    extension: str
    kind: str
    release_url: str
    github_raw: str | None = None
    jsdelivr: str | None = None


def _quote_path(path: str) -> str:
    return quote(path, safe="/")


def github_raw_url(path: str) -> str:
    return f"https://raw.githubusercontent.com/{REPOSITORY}/{BRANCH}/{_quote_path(path)}"


def jsdelivr_url(path: str) -> str:
    return f"https://cdn.jsdelivr.net/gh/{REPOSITORY}@{BRANCH}/{_quote_path(path)}"


def release_page_url(tag: str) -> str:
    return f"https://github.com/{REPOSITORY}/releases/tag/{quote(tag, safe='')}"


def release_asset_url(tag: str, asset_name: str) -> str:
    return f"https://github.com/{REPOSITORY}/releases/download/{quote(tag, safe='')}/{quote(asset_name, safe='')}"


def is_tracked(path: Path) -> bool:
    return path.suffix.lower() not in IGNORED_EXTENSIONS and path.suffix.lower() not in RELEASE_ONLY_EXTENSIONS


def classify_asset(path: Path) -> str:
    ext = path.suffix.lower()
    if path.stem == "Example" and ext in IMAGE_EXTENSIONS:
        return "cover"
    if ext in {".css"}:
        return "style"
    if ext in {".js"}:
        return "script"
    if ext in {".ini"}:
        return "config"
    if ext == ".mdx":
        return "dictionary"
    if ext == ".mdd":
        return "resource"
    if ext in IMAGE_EXTENSIONS:
        return "image"
    return "asset"


def list_release_entries() -> list[Path]:
    entries = []
    for name in RELEASE_ORDER:
        folder = SOURCE_ROOT / name
        if folder.is_dir():
            entries.append(folder)
    return entries


def build_assets(folder: Path, tag: str) -> list[dict]:
    assets: list[dict] = []
    for path in sorted(folder.iterdir(), key=lambda p: (p.name.lower() != "example.png", p.name.lower())):
        if not path.is_file():
            continue
        ext = path.suffix.lower()
        if ext in IGNORED_EXTENSIONS:
            continue
        rel_path = f"{folder.name}/{path.name}"
        asset = {
            "name": path.name,
            "path": rel_path,
            "extension": ext,
            "kind": classify_asset(path),
            "releaseUrl": release_asset_url(tag, path.name),
        }
        if is_tracked(path):
            asset["githubRaw"] = github_raw_url(rel_path)
            asset["jsDelivr"] = jsdelivr_url(rel_path)
        assets.append(asset)
    return assets


def build_entry(folder: Path) -> dict:
    tag = RELEASE_TAGS[folder.name]
    assets = build_assets(folder, tag)
    cover = next((a for a in assets if a["kind"] == "cover"), None)
    tracked_assets = [a for a in assets if "githubRaw" in a]
    release_only_assets = [a for a in assets if "githubRaw" not in a]
    return {
        "id": tag,
        "title": folder.name,
        "folder": folder.name,
        "folderPath": folder.name,
        "tag": tag,
        "releaseUrl": release_page_url(tag),
        "recordFile": f"release-records/{tag}.json",
        "recordRaw": github_raw_url(f"release-records/{tag}.json"),
        "recordJsDelivr": jsdelivr_url(f"release-records/{tag}.json"),
        "cover": cover,
        "assetCount": len(assets),
        "trackedAssetCount": len(tracked_assets),
        "releaseOnlyAssetCount": len(release_only_assets),
        "assets": assets,
        "published": tag in PUBLISHED_RELEASES,
    }


def build_index() -> dict:
    folders = list_release_entries()
    entries = [build_entry(folder) for folder in folders]
    return {
        "schemaVersion": 1,
        "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository": REPOSITORY,
        "branch": BRANCH,
        "downloads": "https://downloads.freemdict.com/",
        "rootReadme": {
            "path": "README.md",
            "githubRaw": github_raw_url("README.md"),
            "jsDelivr": jsdelivr_url("README.md"),
        },
        "releaseRecords": {
            "path": "release-records/",
            "indexFile": "release-records/index.json",
            "githubRaw": github_raw_url("release-records/index.json"),
            "jsDelivr": jsdelivr_url("release-records/index.json"),
        },
        "releases": [
            {
                "id": entry["id"],
                "title": entry["title"],
                "folder": entry["folder"],
                "tag": entry["tag"],
                "releaseUrl": entry["releaseUrl"],
                "recordFile": entry["recordFile"],
                "recordRaw": entry["recordRaw"],
                "cover": entry["cover"],
                "assetCount": entry["assetCount"],
                "trackedAssetCount": entry["trackedAssetCount"],
                "releaseOnlyAssetCount": entry["releaseOnlyAssetCount"],
                "published": entry["published"],
            }
            for entry in entries
        ],
    }, entries
