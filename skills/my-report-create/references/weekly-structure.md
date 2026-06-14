# 周报架构（数据层）

> Skill 自动收集本周日报 → AI 梳理汇总 → 用户补充 → 填充模板

```yaml
---
date: "2026-06-11"            # 周报编写日期
week_label: "2026-06-W2"       # 年-月-月内周数（同标题）
week_range: "06/08 - 06/14"    # 可读日期范围
core_summary: ""               # 本周一句话总结
daily_count: 0                 # 收集到的日报数量
---

highlights:
  - project: ""                # 项目名称
    summary: ""                # 本周在该项目上的主要工作
    status: ""                 # 已完成 | 进行中 | 阻塞
    metrics:                   # 关键指标
      items: 0                 # 完成事项数
      bugs: 0                  # 发现 Bug 数
      cases: 0                 # 用例数
      coverage: ""             # 覆盖情况
    results: []                # 关键成果列表
    details: ""                # 详细描述

problems:
  - type: ""                   # 阻塞 | 风险 | 普通
    description: ""
    impact: ""
    status: ""                 # 已解决 | 遗留中 | 已规避
    resolution: ""             # 解决方案 / 处理进展

learnings:
  - topic: ""                  # 学习主题
    insight: ""                # 收获与洞察（经过提炼而非原始叙述）
    application: ""            # 如何复用
    is_key_takeaway: false     # 是否本周最重要的收获

next_plan:
  - project: ""                # 项目名称
    goals: []                  # 下周目标列表
    priority: ""               # 高 | 中 | 低
    dependencies: []           # 前置依赖
    eta: ""                    # 预期完成时间

attachments: []                # 关联文档/链接
```

## 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `core_summary` | ✅ | 一句话总结本周核心进展（AI从日报提炼） |
| `daily_count` | ✅ | 本周收集到的日报数量，用于确认覆盖完整度 |
| `highlights` | ✅ | 按项目汇总的关键交付（非逐天罗列） |
| `problems` | ✅ | 合并所有问题，区分已解决/遗留 |
| `learnings` | ✅ | 提取最重要的收获，升华到方法论层面 |
| `next_plan` | ✅ | 下周目标 + 关键结果 + 依赖 |
| `attachments` | ❌ | 关联文档链接 |

## 日报 → 周报映射关系

| 日报字段 | 周报映射 |
|----------|---------|
| progress[].project | highlights[].project（按 project 去重合并） |
| progress[].details | highlights[].details + results |
| progress[].status | highlights[].status |
| problems[] | problems[]（去重、归纳已解决/遗留） |
| learnings[] | learnings[]（提取最重要的，做方法论升华） |
| tomorrow_plan[] | next_plan[].goals（去重 + 按项目归类） |
