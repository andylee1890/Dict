from __future__ import annotations

from datetime import datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


REPOSITORY = "andylee1890/Dict"
BRANCH = "main"
R2_PUBLIC_BASE_URL = "https://media.englishanchor.online"
R2_PREFIX = "dict"

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

DICTIONARY_STARS = {
    "CollinsCOBUILDOverhaul v2.30": 3,
    "LDOCE6++ En-Cn V3-0": 5,
    "单词释义比例": 4,
    "新概念英语句典": 3,
    "朗文当代反查词典": None,
    "柯林斯汉英大词典": 3,
    "牛津高阶双解8-oalecd8e": 5,
    "牛津高阶反查词典": 3,
    "简明必应版-css": 3,
    "英语近义词辨析v6": 4,
    "词根词缀词典": 3,
    "词根词缀词源 （合集词典）": 3,
    "词根词缀词频词源": 3,
    "译典通英汉双向字典": 4,
    "近义词词语辨析": 3,
    "韦氏高阶英汉双解词典": 3,
}

PUBLISHED_RELEASES = {
    "collins-cobuild-overhaul-v2-30",
    "ldoce6-en-cn-v3-0",
    "new-concept-english-sentence-dictionary",
    "longman-reverse-dictionary",
    "collins-chinese-english-dictionary",
    "oxford-advanced-learner-dictionary-8-oalecd8e",
    "oxford-advanced-reverse-dictionary",
    "concise-bing-css",
    "synonym-differentiation",
    "word-definition-ratio",
    "word-root-affix-dictionary",
    "word-root-affix-etymology-collection",
    "english-synonym-differentiation-v6",
    "word-root-affix-frequency-etymology",
    "dr-eye-bilingual-dictionary",
    "webster-advanced-english-chinese-dictionary",
}

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

RELEASE_ASSET_NAMES = {
    ("collins-cobuild-overhaul-v2-30", "colcobuildoverhaul_switch的副本.js"): "colcobuildoverhaul_switch.js",
    ("collins-cobuild-overhaul-v2-30", "CollinsCOBUILDOverhaul V 2-30.mdx"): "collins-cobuild-overhaul-v2-30.mdx",
    ("collins-cobuild-overhaul-v2-30", "CollinsCOBUILDOverhaul V 2-30.png"): "CollinsCOBUILDOverhaul.V.2-30.png",
    ("collins-cobuild-overhaul-v2-30", "柯林斯双解预览图.PNG"): "default.PNG",
    ("collins-cobuild-overhaul-v2-30", "柯林斯英英预览图.PNG"): "-2.PNG",
    ("word-definition-ratio", "单词释义比例词典-带词性.mdx"): "word-definition-ratio.mdx",
    ("collins-chinese-english-dictionary", "柯林斯汉英大词典.mdx"): "default.mdx",
    ("ldoce6-en-cn-v3-0", "LDOCE6++ En-Cn V3-0.mdd"): "LDOCE6++.En-Cn.V3-0.mdd",
    ("new-concept-english-sentence-dictionary", "[英-汉] 《新概念英語句典》[5486](090523).mdx"): "new-concept-english-sentence-dictionary.mdx",
    ("longman-reverse-dictionary", "朗文当代高级英语辞典（第5版 汉英+同义词+例句反查）.mdx"): "longman-reverse-dictionary.mdx",
    ("longman-reverse-dictionary", "朗文当代高级英语辞典（第5版 汉英+同义词+例句反查）.jpg"): "longman-reverse-dictionary.jpg",
    ("oxford-advanced-learner-dictionary-8-oalecd8e", "牛津高阶双解8双解预览图.PNG"): "oalecd8e-chinese-preview.png",
    ("oxford-advanced-learner-dictionary-8-oalecd8e", "牛津高阶双解8英英预览图.PNG"): "oalecd8e-english-preview.png",
    ("oxford-advanced-learner-dictionary-8-oalecd8e", "牛津高阶英汉双解词典(第8版).png"): "8.PNG",
    ("oxford-advanced-learner-dictionary-8-oalecd8e", "牛津高阶英汉双解词典(第8版).1.mdd"): "8.1.mdd",
    ("oxford-advanced-learner-dictionary-8-oalecd8e", "牛津高阶英汉双解词典(第8版).mdd"): "8.mdd",
    ("oxford-advanced-learner-dictionary-8-oalecd8e", "牛津高阶英汉双解词典(第8版).mdx"): "8.mdx",
    ("oxford-advanced-reverse-dictionary", "牛津高阶英汉双解词典（第9版 汉英+同义词+例句反查）.mdx"): "9.+.+.mdx",
    ("oxford-advanced-reverse-dictionary", "牛津高阶英汉双解词典（第9版 汉英+同义词+例句反查）.jpg"): "9.+.+.jpg",
    ("word-root-affix-dictionary", "[英-汉] 词根词缀词典(應网友要求)[12120](090528).mdx"): "word-root-affix-dictionary.mdx",
    ("word-root-affix-etymology-collection", "The Affix Root of Vocabulary.mdx"): "The.Affix.Root.of.Vocabulary.mdx",
    ("dr-eye-bilingual-dictionary", "译典通英汉双向字典.mdx"): "default.mdx",
    ("synonym-differentiation", "近义词词语辨析.mdx"): "synonym-differentiation.mdx",
    ("webster-advanced-english-chinese-dictionary", "韦氏高阶英汉双解词典.mdx"): "default.mdx",
    ("english-synonym-differentiation-v6", "英语近义词辨析.jpg"): "english-synonym-differentiation-v6.jpg",
    ("english-synonym-differentiation-v6", "英语近义词辨析.mdx"): "english-synonym-differentiation-v6.mdx",
    ("ldoce6-en-cn-v3-0", "LDOCE6++ En-Cn V3-0.mdx"): "LDOCE6++.En-Cn.V3-0.mdx",
    ("word-root-affix-frequency-etymology", "优词英语词源词典 (aepicure on 六月的风8, 2016-09-09) 紧凑版.mdd"): "word-root-affix-frequency-etymology.mdd",
    ("word-root-affix-frequency-etymology", "优词英语词源词典 (aepicure on 六月的风8, 2016-09-09) 紧凑版.mdx"): "word-root-affix-frequency-etymology-1.mdx",
    ("word-root-affix-frequency-etymology", "李平武+蒋真 词根 (7291).mdx"): "word-root-affix-frequency-etymology-2.mdx",
    ("word-root-affix-frequency-etymology", "童哥词根(23528).mdx"): "word-root-affix-frequency-etymology-3.mdx",
    ("word-root-affix-frequency-etymology", "英语词根词缀词频.mdx"): "word-root-affix-frequency-etymology-4.mdx",
}


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


def r2_url(path: str) -> str:
    return f"{R2_PUBLIC_BASE_URL}/{R2_PREFIX}/{_quote_path(path)}"


def is_tracked(path: Path) -> bool:
    return path.suffix.lower() not in IGNORED_EXTENSIONS and path.suffix.lower() not in RELEASE_ONLY_EXTENSIONS


def resolve_release_asset_name(path: Path, tag: str, ext_indexes: dict[str, int], ext_totals: dict[str, int]) -> str:
    explicit_name = RELEASE_ASSET_NAMES.get((tag, path.name))
    if explicit_name:
        return explicit_name

    ext = path.suffix.lower()
    if ext not in RELEASE_ONLY_EXTENSIONS:
        return path.name

    if tag in PUBLISHED_RELEASES:
        return path.name

    ext_indexes[ext] = ext_indexes.get(ext, 0) + 1
    if ext_totals.get(ext, 0) == 1:
        return f"{tag}{ext}"
    return f"{tag}-{ext_indexes[ext]}{ext}"


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
    files = [
        path
        for path in sorted(folder.iterdir(), key=lambda p: (p.name.lower() != "example.png", p.name.lower()))
        if path.is_file() and path.suffix.lower() not in IGNORED_EXTENSIONS
    ]
    ext_totals: dict[str, int] = {}
    for path in files:
        ext = path.suffix.lower()
        if ext in RELEASE_ONLY_EXTENSIONS:
            ext_totals[ext] = ext_totals.get(ext, 0) + 1

    ext_indexes: dict[str, int] = {}
    for path in files:
        if not path.is_file():
            continue
        ext = path.suffix.lower()
        if ext in IGNORED_EXTENSIONS:
            continue
        rel_path = f"{folder.name}/{path.name}"
        release_asset_name = resolve_release_asset_name(path, tag, ext_indexes, ext_totals)
        asset = {
            "name": path.name,
            "releaseName": release_asset_name,
            "path": rel_path,
            "extension": ext,
            "kind": classify_asset(path),
            "releaseUrl": release_asset_url(tag, release_asset_name),
        }
        if classify_asset(path) == "cover":
            asset["r2Url"] = r2_url(rel_path)
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
        "star": DICTIONARY_STARS[folder.name],
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
        "r2": {
            "baseUrl": R2_PUBLIC_BASE_URL,
            "prefix": f"{R2_PREFIX}/",
        },
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
                "star": entry["star"],
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
