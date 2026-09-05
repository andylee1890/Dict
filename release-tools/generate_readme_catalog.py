from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote

from catalog import build_index, github_raw_url


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    index, entries = build_index()
    lines: list[str] = []
    lines.append("# 词典资源仓库")
    lines.append("")
    lines.append("本仓库保存可公开分享的词典资源、样式文件、封面和发布索引。")
    lines.append("")
    lines.append("资源均来自网络，仅供学习和交流；如有权利方要求，请联系处理。")
    lines.append("")
    lines.append("[更多资源下载](https://downloads.freemdict.com/)")
    lines.append("")
    lines.append("## 发布规则")
    lines.append("")
    lines.append("- 每个顶层文件夹对应一个 release。")
    lines.append("- release 里包含该文件夹下可公开下载的资源文件。")
    lines.append("- `Example.png` 作为主封面。")
    lines.append("")
    lines.append("## 索引")
    lines.append("")
    lines.append(f"- [发布记录索引](./release-records/index.json)")
    lines.append(f"- [发布记录目录](./release-records/)")
    lines.append(f"- [README 原始链接]({github_raw_url('README.md')})")
    lines.append("")
    lines.append("## 资源预览")
    lines.append("")
    lines.append("| 词典 | 封面 | 发布记录 |")
    lines.append("| --- | --- | --- |")
    for entry in entries:
        cover = entry["cover"]["path"] if entry["cover"] else f"{entry['folder']}/Example.png"
        cover_src = "./" + quote(cover, safe="/")
        lines.append(
            f"| {entry['title']} | <img src=\"{cover_src}\" alt=\"{entry['title']}\" width=\"160\" /> | "
            f"[{entry['tag']}](./release-records/{entry['id']}.json) |"
        )

    lines.append("")
    lines.append("## 说明")
    lines.append("")
    lines.append("每个词典的详细发布记录会落在 `release-records/<tag>.json`，主索引落在 `release-records/index.json`。")
    lines.append("后续上线 release 时，索引中的 `releaseUrl` 和各文件的下载链接会保持稳定。")

    (ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
