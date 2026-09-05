# Release Tools

这里保存维护这个词典仓库的公开脚本。

## 工具

- `generate_release_index.py`：扫描顶层词典目录，生成 `release-records/index.json` 和每个词典的详细记录。
- `generate_readme_catalog.py`：根据同一份目录数据重写根目录 `README.md` 的目录表。

## 规则

- 只放可重复、可审计的仓库维护工具。
- 不写个人路径、账号、浏览器状态或临时恢复脚本。
- 脚本尽量只用 Python 标准库。

