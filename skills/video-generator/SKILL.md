---
name: video-generator
description: Generate branded promotional videos with automatic voiceover dubbing. Supports multi-scene structure (intro + content + closing), edge-tts voiceover generation, and automated Remotion rendering. Use when the user asks to create a video, promotional video, brand video, product video, or any motion graphics content.
metadata:
  tags: video, remotion, voiceover, tts, edge-tts, animation, promotional-video
---

# Video Generator Skill

## When to Use

Use this skill when the user asks to:
- "生成一段视频"
- "做个宣传视频"
- "把XXX做成视频"
- "创建品牌视频"
- Any request involving video generation from description

Do **NOT** use this skill if the user is asking about editing an existing video project (use the remotion skill directly instead).

## Workflow Overview

```
Consultation ──→ Project Setup ──→ Scene Generation ──→ Voiceover ──→ Render
   (refs/consultation)  (refs/project-setup)  (refs/scene-template)  (refs/voiceover)  (refs/rendering)
```

## Step-by-Step Guide

### Step 1: Consultation

Follow `references/consultation.md` to conduct a multi-step interview with the user to determine:
- Brand / video name
- Industry and core message
- Visual style (color scheme, tone)
- Content scenes (2-4 scenes between intro and closing)
- Voice gender (male/female)

At the end, produce a **design brief** summarizing all decisions.

### Step 2: Project Setup

Follow `references/project-setup.md` to:
- Create a new folder `<video-name>-video/` under the project root
- Initialize package.json with Remotion dependencies
- Create tsconfig.json, remotion.config.ts
- Create `src/` and `public/` directories

### Step 3: Generate Scene Components

Follow `references/scene-template.md` to:
- Create `src/style.ts` with color palette constants
- Create `src/index.ts`, `src/Root.tsx`, `src/EclatVideo.tsx`
- Create one component per scene (Intro.tsx, Scene1.tsx, ..., Closing.tsx)
- Each scene uses `useCurrentFrame()`, `interpolate()`, `useVideoConfig()`
- Import Google Fonts via `@remotion/google-fonts`
- Wire scenes together in `EclatVideo.tsx` using `<Sequence>`

### Step 4: Voiceover

Follow `references/voiceover.md` to:
- Write voiceover scripts for each scene based on the design brief
- Copy `scripts/generate-voiceover.py` to the project folder
- Run the script to generate MP3 files
- Measure audio durations with Python
- Update `EclatVideo.tsx` to embed `<Audio>` components with correct frame counts

### Step 5: Render

Follow `references/rendering.md` to:
- Install npm dependencies
- Execute `npx remotion render` with proper codec settings
- Verify the output file exists
- Present the result to the user

## Color Palette Presets

| Name | Primary | Secondary | Accent | Background | Use Case |
|------|---------|-----------|--------|------------|----------|
| Elegant Gold | `#c9a96e` | `#e8d5a3` | `#a08040` | `#0a0806` | Luxury, wine, premium |
| Tech Blue | `#4a90d9` | `#7bb3e8` | `#2a5f9e` | `#0a0e1a` | Technology, SaaS |
| Nature Green | `#5a8f53` | `#8ab883` | `#3d6b37` | `#0a1008` | Organic, eco, health |
| Minimal Light | `#333333` | `#666666` | `#999999` | `#f5f5f0` | Clean, modern, corporate |
| Bold Red | `#c43a31` | `#e06060` | `#8a2018` | `#0d0505` | Passion, energy, culture |
