# 发布记录

这里保存每个词典目录对应的发布记录和主索引。

## 结构

- `index.json`：机器可读主索引，给前端和自动化流程使用。
- `<tag>.json`：单个词典的详细记录，包含该目录的资产清单与链接。

## 约定

- 每个顶层文件夹对应一个 release。
- `.mdx`、`.mdd`、`.db` 不进 Git 历史，其中 `.mdx` 和 `.mdd` 只通过 release 发布。
- 公开资产会同时保留 GitHub Raw 和 jsDelivr 链接。
- `Example.png` 作为主封面。

