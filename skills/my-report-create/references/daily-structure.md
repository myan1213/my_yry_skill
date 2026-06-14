# 日报架构（数据层）

> 用户提供原始信息 → Skill 整理成此结构化数据 → 再填充到模板中

```yaml
---
date: "YYYY-MM-DD"           # 日报日期
weekday: "星期X"              # 星期几
project: "项目名称"           # 当前主项目
core_summary: ""              # 一句话核心进展（最重要的结论）
---
progress:
  - project: ""               # 项目/模块名称
    task: ""                  # 具体完成事项
    status: ""                # 已完成 | 进行中 (进度%) | 待验证
    links: []                 # 关联链接（PR、文档、实验报告）
    details: ""               # 详细描述

problems:
  - type: ""                  # 阻塞 | 风险 | 普通问题
    description: ""           # 问题描述
    impact: ""                # 影响范围
    needs_help: ""            # 需要谁协助
    action: ""                # 已采取的措施

learnings:
  - topic: ""                 # 学习主题
    insight: ""               # 收获/心得
    application: ""           # 如何应用到后续工作

tomorrow_plan:
  - task: ""                  # 任务
    priority: ""              # 高 | 中 | 低
    owner: ""                 # 负责人
    eta: ""                   # 预计完成时间

attachments: []               # 附件/参考链接
meetings: []                  # 会议与重要沟通
  - topic: ""
    conclusion: ""
    action_items: []
mood: ""                      # 今日状态（👍 顺利 / 🤔 有挑战 / 😤 困难）
```

## 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `core_summary` | ✅ | 一句话总结今日最核心的进展，写在标题下方 |
| `progress` | ✅ | 今日工作进展，按项目分类 |
| `problems` | ✅ | 遇到的问题，区分阻塞/风险/普通问题 |
| `learnings` | ✅ | 成长心得、技术沉淀 |
| `tomorrow_plan` | ✅ | 明日计划，带优先级和ETA |
| `attachments` | ❌ | 关联的PR、文档链接等 |
| `meetings` | ❌ | 重要的会议与结论（如果当天有会议） |
| `mood` | ❌ | 今日工作状态标签 |
