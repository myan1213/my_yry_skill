# Consultation Process

Conduct a multi-step interview with the user to determine video specifications.

## Step 1: Core Identity

Ask the user these questions **one at a time**:

1. **Video name / Brand name**: What is the video or brand called? (e.g., "ÉCLAT", "追光科技", "山间茶语")
2. **Industry / Domain**: What industry is it for? (e.g., wine, tech, tea, fashion, education)
3. **Core message**: What is the single most important thing to convey? (1 sentence)

## Step 2: Visual Style

Present the color palette presets from SKILL.md and ask the user to choose:

- **Elegant Gold** — 奢华、高端、传统
- **Tech Blue** — 科技、现代、专业
- **Nature Green** — 自然、有机、健康
- **Minimal Light** — 简洁、干净、现代
- **Bold Red** — 热情、活力、文化

Also offer the option: **Custom** — let them describe colors they want.

Ask: "Do you want a light or dark background?"

## Step 3: Content Scenes

Explain the video structure: **开场 → N个内容场景 → 结尾**.

Ask the user:
- "How many content scenes do you want? (1-3)"
- For each content scene, ask: "What should scene [N] be about?"
  - Provide suggestions based on their industry:
    - Product: brand story, product features, customer testimonials
    - Tech: problem, solution, impact
    - General: philosophy, showcase, vision

## Step 4: Voiceover

Ask:
- **Male or female voice?**
  - Female: `zh-CN-XiaoxiaoNeural`
  - Male: `zh-CN-YunyangNeural`

Ask if the user has any specific text they want included in the voiceover. If not, you will generate it automatically.

## Design Brief Output

After consultation, produce a summary like:

```
## Design Brief

Brand: ÉCLAT
Industry: Wine
Core Message: 传承百年的酿造哲学
Color Palette: Elegant Gold (dark background)
Scenes:
  1. Intro — Brand showcase
  2. Philosophy — 品牌理念与历史
  3. Collection — 产品系列
  4. Closing — 品牌收束
Voice: Female (Xiaoxiao)
```
