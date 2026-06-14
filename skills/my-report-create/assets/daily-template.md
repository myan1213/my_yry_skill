# 日报文档模板

生成飞书云文档的 XML 内容模板。

## 模板结构（带丰富内容示例）

下面模板以「惊喜红包券测试」日报为例，展示润色后的内容效果：

```xml
<title>日报 - 2026-06-11</title>

<p><cite type="user" user-id="ou_1bbe28db44e9aeca3d8112badebb38ac"></cite></p>

<h2>📋 今日进展</h2>

<callout emoji="📋" background-color="light-blue" border-color="blue">
  <p><b>一句话总结：</b>核心进展描述</p>
  <p>📅 2026-06-11 星期四 · 当前状态：👍 进行中 · 核心链路 80%</p>
</callout>

<h3>🔹 惊喜红包券 — 功能测试</h3>

<p><b>📌 工作概述</b></p>
<p>今天围绕「惊喜红包券」需求进行功能测试，重点覆盖了红包领取→发放的核心链路，包括正常发放、过期回收、重复领取、资格校验等主要场景。</p>

<p><b>📊 当前进度：</b>进行中 80%</p>

<p><b>✅ 已完成：</b></p>
<p>1. 核心链路正向用例全部通过（12/12），发放和领取流程验证正常<br/>
   2. 异常场景覆盖完成率 65%，包括过期回收、资格校验边界等<br/>
   3. 发现 2 个低概率 Bug，已提单追踪（涉及并发领取时的金额展示异常）</p>

<p><b>🔄 进行中：</b></p>
<p>1. 异常场景收尾（并发领取的金额扣减一致性、用户资格校验时序）<br/>
   2. 预发布环境数据配置差异问题，正在推动修复</p>

<p><b>🔗 关联链接：</b><br/>
   · 需求文档：https://xxx.feishu.cn/docx/xxxx<br/>
   · Bug 单 #001：https://xxx.feishu.cn/bug/001<br/>
   · Bug 单 #002：https://xxx.feishu.cn/bug/002</p>

<hr/>

<h2>⚠️ 遇到的问题与风险</h2>

<callout emoji="🔴" background-color="light-red" border-color="red">
  <p><b>🔴 [阻塞] 预发布环境数据配置与生产不一致</b></p>
  <p><b>根因分析：</b>预发布环境在部署时部分 OAuth 数据源配置未被正确初始化，导致依赖外部服务的 3 个异常场景用例无法正常执行。具体差异在于：数据源的访问凭证在预发布环境中使用了旧的密钥，而服务端已更新为新的密钥体系。</p>
  <p><b>当前影响：</b>3 个涉及金额计算验证的异常场景用例被阻塞，占异常场景总量的约 20%。若无法及时修复，可能影响整体测试进度的完整性。</p>
  <p><b>已采取措施：</b></p>
  <p>1. 已定位到具体差异点，并与运维同学确认修复方案（更新 OAuth 配置）<br/>
     2. 临时方案：对阻塞的用例切换为 mock 数据验证逻辑正确性，确保不空等</p>
  <p><b>🕐 预期修复：</b>明天上午由运维完成配置更新</p>
</callout>

<callout emoji="🟡" background-color="light-yellow" border-color="yellow">
  <p><b>🟡 [风险] 全量回归排期偏紧</b></p>
  <p>周五计划进行全量回归测试，但当前环境问题尚未完全解决，若持续顺延可能压缩回归窗口。</p>
  <p><b>应对策略：</b>已与 PM 同步风险，评估是否需要调整测试范围优先级或临时补充人力。同时内部将回归用例按优先级排序，确保核心 P0 用例优先覆盖。</p>
</callout>

<h3>🔵 其他积累问题</h3>
<p>测试过程中发现需求文档中关于「红包过期时间计算规则」的描述与实际行为存在偏差（文档写的是自然日过期，实际按业务逻辑是 24 小时制），已反馈给产品同学确认是否需要统一。</p>

<hr/>

<h2>💡 成长心得</h2>

<h3>▎对红包场景的并发控制有了更深的理解</h3>
<p>这次测试中遇到的并发领取场景，让我实际看到了分布式乐观锁在金额扣减中的应用。之前的测试更多是功能层面的正向验证，这次通过构造并发请求、观察数据库中的版本号变化、对比多次执行的结果，才真正理解了为什么需要「乐观锁 + 重试机制」来保证金额扣减的一致性。</p>
<p><b>📌 后续可复用：</b>对类似涉及金额/库存扣减的功能测试，可以提前设计并发竞争场景的测试用例，而不是等上线后再发现。</p>

<h3>▎异常场景设计的思路转变</h3>
<p>在覆盖异常场景时，开始尝试「错误注入 + 监控验证」的方法——不仅看接口返回是否报错，还去观测日志、监控指标、数据库状态是否一致。这种方法比纯功能断言更能发现隐蔽问题。</p>
<p><b>📌 后续可复用：</b>这些并发测试场景的设计思路，可以沉淀为「红包类功能测试 CheckList」，后续其他同学做类似测试时可以直接复用。</p>

<hr/>

<h2>📅 明日计划</h2>

<table>
  <colgroup>
    <col span="1" width="60"/>
    <col span="1" width="270"/>
    <col span="1" width="80"/>
    <col span="1" width="80"/>
    <col span="1" width="80"/>
  </colgroup>
  <thead>
    <tr>
      <th background-color="light-gray">优先级</th>
      <th background-color="light-gray">任务</th>
      <th background-color="light-gray">状态</th>
      <th background-color="light-gray">负责人</th>
      <th background-color="light-gray">ETA</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>🔴 高</td><td>惊喜红包券异常场景收尾（并发领取/金额扣减一致性/资格校验时序）</td><td>待执行</td><td>本人</td><td>明天 EOD</td></tr>
    <tr><td>🟡 中</td><td>跟进预发布环境修复验证 + 确认阻塞用例通过</td><td>依赖运维</td><td>运维 + 本人</td><td>明天上午</td></tr>
    <tr><td>🟢 低</td><td>整理惊喜红包券测试报告初稿，同步给 PM</td><td>待执行</td><td>本人</td><td>后天中午</td></tr>
  </tbody>
</table>

<hr/>

<p><em>本日报由 my-report-create Skill 自动生成</em></p>
```

## 填充规则

1. **文档标题** — 格式 `日报-YYYY-MM-DD`，从当天日期自动生成
2. **@本人** — 使用用户 open_id：`ou_1bbe28db44e9aeca3d8112badebb38ac`
3. **空板块跳过** — 用户说没有内容时，不生成对应标题和段落
4. **项目进展** — 每个项目用 `<h3>` + 正文独立呈现；如只有一个项目，不用 `<hr/>` 分隔
5. **问题分类** — 按类型使用对应的 callout 颜色：
   - 阻塞 → `background-color="light-red"` `border-color="red"` emoji="🔴"
   - 风险 → `background-color="light-yellow"` `border-color="yellow"` emoji="🟡"
   - 其他 → 普通 `<p>` 或 `<h3>` + `<p>`
6. **明日计划表** — 根据实际条目数动态生成行；每行包含优先级、任务、状态、负责人、ETA 五列
7. **转义规则** — 用户回答中的特殊字符：
   - `<` → `&lt;`
   - `>` → `&gt;`
   - `&` → `&amp;`
   - 换行 → `<br/>`
   - 标签本身不要转义

## 创建命令

```bash
lark-cli docs +create --api-version v2 \
  --content '<完整XML内容>' \
  --parent-token SB9ofwDKTlJfqNdL1AoczPxJnyh \
  --as user
```

> `--parent-token` 为「日报集」文件夹 token。
