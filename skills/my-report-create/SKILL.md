---
name: my-report-create
description: 统一入口，先询问用户创建日报还是周报，再按对应流程执行。支持日报问答生成和周报自动汇总。
metadata:
  tags: report, daily-report, weekly-report, feishu-doc
---

# my-report-create 报告生成 Skill

## When to Use

用户说以下内容时使用本 Skill：
- "帮我生成一份报告/日报/周报"
- "写一下今天的日报"
- "写一下这周的周报"
- "/my-report-create"
- 任何写日报或周报的需求

## Workflow Overview

```
用户触发
    │
    ▼
询问："今天要写日报还是周报？"
    │
    ├── 日报 ──→ 问答收集 → 整理数据 → 润色内容 → 生成文档 → 存入日报集
    │               (refs/daily-interview-flow)  (refs/daily-template)
    │
    └── 周报 ──→ 搜索本周日报 → 读取内容 → AI汇总 → 询问补充 → 生成文档 → 存入周报集
                       (refs/weekly-summarize-rules)  (refs/weekly-template)
```

## 日报流程

### Step 1: 问答收集

按 `references/daily-interview-flow.md` 执行 4 轮引导式问答，每轮一问一答。

### Step 2: 整理数据

将问答结果按 [日报架构](references/daily-structure.md) 整理为结构化数据。

### Step 2.5: 润色内容

对用户原始回答做三层扩展（补充背景/方法/结果 → 提炼价值），参考 `references/daily-polish-rules.md` 中的**内容润色原则**。

### Step 3: 生成文档

按 `assets/daily-template.md` 中的 XML 模板生成，执行：

```bash
lark-cli docs +create --api-version v2 \
  --content '<xml>' \
  --parent-token SB9ofwDKTlJfqNdL1AoczPxJnyh \
  --as user
```

> `SB9ofwDKTlJfqNdL1AoczPxJnyh` = 日报集文件夹 token

## 周报流程

### Step 1: 搜索本周日报

在日报集文件夹中搜索本周所有日报文档：

```bash
lark-cli drive +search \
  --folder-tokens SB9ofwDKTlJfqNdL1AoczPxJnyh \
  --doc-types docx \
  --only-title \
  --query "日报-"
```

筛选日期范围匹配本周的文档。

### Step 2: 读取日报内容

对每个日报文档，用以下命令读取 Markdown 内容：

```bash
lark-cli docs +fetch --api-version v2 --doc <token> --doc-format markdown
```

### Step 3: AI 梳理汇总

按 `references/weekly-summarize-rules.md` 中的规则，将多篇日报汇总为周报 4 个板块。

### Step 4: 询问补充

将汇总初稿展示给用户，确认：
- "是否有遗漏的内容？"
- "有没有日报之外需要补充的事项？"
- "下周计划是否需要调整？"

### Step 5: 生成文档

按 `assets/weekly-template.md` 中的 XML 模板生成，执行：

```bash
lark-cli docs +create --api-version v2 \
  --content '<xml>' \
  --parent-token SAbrfpzQXl0p7ediqMfcG8FsnYc \
  --as user
```

> `SAbrfpzQXl0p7ediqMfcG8FsnYc` = 周报集文件夹 token

## Permissions

| Scope | 用途 |
|-------|------|
| `docx:document:create` | 创建飞书云文档 |
| `space:document:retrieve` | 读取文档内容（周报汇总用） |

当前用户已授权，无需额外操作。

## References

| 文件 | 用途 |
|------|------|
| [日报问答流程](references/daily-interview-flow.md) | 日报 4 轮问答详情 |
| [内容润色原则](references/daily-polish-rules.md) | 问答数据的润色扩展方法 |
| [日报 XML 模板](assets/daily-template.md) | 日报文档生成模板 |
| [周报汇总规则](references/weekly-summarize-rules.md) | 日报→周报的 AI 汇总方法 |
| [周报 XML 模板](assets/weekly-template.md) | 周报文档生成模板 |
| [日报架构](references/daily-structure.md) | 日报结构化数据定义 |
| [周报架构](references/weekly-structure.md) | 周报结构化数据定义 |
