# 周报文档模板

生成飞书云文档的 XML 内容模板。

## 模板结构（带汇总示例）

以「惊喜红包券测试周」为例，展示汇总后的效果：

```xml
<title>周报 - 2026-06-W2</title>

<p><cite type="user" user-id="ou_1bbe28db44e9aeca3d8112badebb38ac"></cite></p>

<h2>📋 本周重点工作</h2>

<callout emoji="📋" background-color="light-blue" border-color="blue">
  <p><b>一句话总结：</b>本周主要推进惊喜红包券全量测试，完成资损核对计划评审与用例编写，发现并修复 3 个 Bug，测试进度 100%</p>
  <p>📅 2026-06-W2（06/08 - 06/14）· 本周日报：3 篇</p>
</callout>

<h3>🔹 惊喜红包券 — 功能测试</h3>

<p><b>📊 本周进度：</b>已完成 100%</p>

<p><b>📌 工作概况</b></p>
<p>本周对「惊喜红包券」需求进行了全量功能测试，覆盖创券接口和查券接口，通过 Java 自动化脚本执行，累计覆盖 60 条用例。</p>

<p><b>✅ 关键成果：</b></p>
<p>1. 正向场景 40 条 — 全部通过<br/>
   2. 边界场景 10 条 — 全部通过<br/>
   3. 异常场景 10 条 — 全部通过<br/>
   4. 共发现 3 个 Bug，已全部修复</p>

<p><b>📊 趋势小结：</b></p>
<p>· 周一~周三：核心链路测试（80%）→ 周四：异常场景收尾（70%）→ 周五：全量验证（100%）<br/>
   · Bug 发现呈收敛趋势：周一 0 → 周二 1 → 周三 2 → 周四 0（已无新 Bug）<br/>
   · 测试环境稳定性问题已于周四恢复</p>

<h3>🔹 资损核对计划</h3>

<p><b>📌 工作概况</b></p>
<p>本周完成了惊喜红包券需求的资损核对计划编写，与研发同学和上游营销中心测试同学完成评审通过，并开始编写核对用例。</p>

<p><b>✅ 关键成果：</b></p>
<p>1. 核对计划覆盖：券属性信息核对、数量核对、上游券数据信息核对 3 个维度<br/>
   2. 评审意见：通过（需上游同学提供离线表）<br/>
   3. 核对用例编写进度：3/6</p>

<p><b>📌 待推进：</b></p>
<p>上游离线表确认中，待数据到位后执行核对验证。</p>

<hr/>

<h2>⚠️ 遇到的问题与风险</h2>

<callout emoji="🟢" background-color="light-green" border-color="green">
  <p><b>✅ [已解决] 测试环境不稳定</b></p>
  <p><b>问题描述：</b>上游服务在测试环境接口频繁抛异常，导致测试执行被打断。</p>
  <p><b>持续时间：</b>周一 ~ 周三（3 天）</p>
  <p><b>影响评估：</b>依赖上游接口的异常场景用例执行受阻，整体测试进度存在延期风险。</p>
  <p><b>解决方案：</b>已拉群同步产品同学，产品反馈需求不紧急可接受延期；周四环境恢复，阻塞解除。</p>
</callout>

<callout emoji="🟡" background-color="light-yellow" border-color="yellow">
  <p><b>📌 [遗留中] 上游离线表待提供</b></p>
  <p><b>问题描述：</b>资损核对执行需上游同学提供离线券数据表。</p>
  <p><b>当前进展：</b>已沟通确认，预期下周初提供。</p>
  <p><b>后续：</b>数据到位后执行核对验证，预计 2 个工作日完成。</p>
</callout>

<hr/>

<h2>💡 经验沉淀</h2>

<h3>▎并发竞争场景的测试设计方法</h3>
<p>本周在红包券测试中，通过构造并发领取请求、观察数据库版本号变化、对比多次执行结果，深入理解了分布式乐观锁在金额扣减中的应用。这类竞争场景在传统功能测试中容易被忽略。</p>
<p><b>📌 可复用：</b>可将并发测试场景的设计思路沉淀为「金额/库存类功能测试 CheckList」，后续其他类似需求可直接复用。</p>

<h3>▎AI 辅助排查与测试</h3>
<p>本周尝试用 AI 辅助分析了异常日志、编写自动化脚本的边界场景处理逻辑，提升了排查效率。AI 能从大量日志中快速提取关键信息，帮助定位根因。</p>
<p><b>📌 可复用：</b>将「排查流程 + AI 辅助方法」沉淀为 SOP 文档，团队可参照执行提升排查效率。</p>

<hr/>

<h2>📅 下周计划</h2>

<table>
  <colgroup>
    <col span="1" width="60"/>
    <col span="1" width="280"/>
    <col span="1" width="60"/>
    <col span="1" width="120"/>
  </colgroup>
  <thead>
    <tr>
      <th background-color="light-gray">优先级</th>
      <th background-color="light-gray">目标</th>
      <th background-color="light-gray">项目</th>
      <th background-color="light-gray">ETA</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>🔴 高</td><td>完成资损核对用例编写（剩余 3/6）并执行核对验证</td><td>红包券</td><td>下周中</td></tr>
    <tr><td>🔴 高</td><td>跟进上游离线表到位后的核对执行</td><td>红包券</td><td>下周中</td></tr>
    <tr><td>🟡 中</td><td>输出惊喜红包券测试报告初稿</td><td>红包券</td><td>下周 EOD</td></tr>
  </tbody>
</table>

<hr/>

<p><em>本周报由 my-report-create Skill 自动生成</em></p>
```

## 填充规则

1. **文档标题** — 格式 `周报-YYYY-MM-W{月内周数}`，例 `周报-2026-06-W2`
2. **@本人** — 使用用户 open_id：`ou_1bbe28db44e9aeca3d8112badebb38ac`
3. **本周日报数** — 在顶部 callout 中显示收集到的日报数量，便于确认覆盖完整性
4. **空板块跳过** — 汇总后如果某个板块没有内容，不生成对应的标题和段落
5. **问题分类** — 按状态使用不同的 callout 颜色：
   - 已解决 → `background-color="light-green"` `border-color="green"` emoji="🟢"
   - 遗留中 → `background-color="light-yellow"` `border-color="yellow"` emoji="🟡"
   - 阻塞 → `background-color="light-red"` `border-color="red"` emoji="🔴"
6. **下周计划表** — 根据实际条目数动态生成行；包含优先级、目标、项目、ETA 四列
7. **转义规则** — 与日报一致：
   - `<` → `&lt;`
   - `>` → `&gt;`
   - `&` → `&amp;`
   - 换行 → `<br/>`
   - 标签本身不要转义

## 通用属性参考

| 标签 | 用途 | 关键属性 |
|------|------|----------|
| `<title>` | 文档标题 | 每篇唯一 |
| `<callout>` | 高亮框 | `emoji`, `background-color`, `border-color` |
| `<table>` | 表格 | 标准 HTML table 结构 |
| `<th/td>` | 表头/单元格 | `background-color` |
| `<hr/>` | 分割线 | — |
| `<p>` | 段落 | — |
| `<h2>` | 二级标题 | — |
| `<h3>` | 三级标题 | — |
| `<b>` | 加粗 | — |
| `<em>` | 斜体 | — |
| `<cite>` | @用户/@文档 | `type="user"` `user-id="xxx"` |

## 创建命令

```bash
lark-cli docs +create --api-version v2 \
  --content '<完整XML内容>' \
  --parent-token SAbrfpzQXl0p7ediqMfcG8FsnYc \
  --as user
```

> `SAbrfpzQXl0p7ediqMfcG8FsnYc` = 周报集文件夹 token
