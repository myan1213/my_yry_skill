# Voiceover Generation

## Script Writing Guidelines

For each scene, write a concise voiceover script in Chinese:

| Scene | Length | Content |
|-------|--------|---------|
| Intro | 8-12s | Brand name + tagline + hook |
| Content (each) | 10-18s | Core message per scene, descriptive |
| Closing | 8-14s | Summary + brand reaffirmation |

### Writing Style

- Use a natural, conversational tone
- 使用中文标点符号
- Keep sentences short (< 25 characters each)
- Avoid tongue twisters and difficult pronunciations
- Use pauses naturally (commas, periods)

### Script Structure Template

```
## scene-01-intro
[品牌名]，[一句话定位]。[核心卖点/价值主张]。

## scene-02-<name>
[场景主题阐述]。[具体描述1]。[具体描述2]。

## scene-03-<name>
[场景主题阐述]。[具体描述1]。[具体描述2]。

## scene-05-closing
[总结性语句]。[品牌名]，[品牌标语]。
```

## Audio Generation

### Using edge-tts (Default)

Copy `scripts/generate-voiceover.py` to the project's root directory and update the `SCENES` array with your scripts, then run:

```bash
pip3 install edge-tts -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
python3 generate-voiceover.py
```

### Using ElevenLabs (Placeholder — Not Supported Yet)

```bash
# ELEVENLABS_API_KEY=your_key node generate-voiceover.ts
```

This path is not yet implemented. Advise the user to use edge-tts for now.

## Measuring Audio Duration

After generating MP3 files, measure their exact durations:

```bash
pip3 install mutagen -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
python3 -c "
import os, math
from mutagen.mp3 import MP3
d = 'public/voiceover/<name>'
for f in sorted(os.listdir(d)):
    if f.endswith('.mp3'):
        audio = MP3(os.path.join(d, f))
        dur = audio.info.length
        frames = math.ceil(dur * 30)
        print(f'{f}: {dur:.3f}s → {frames}frames')
"
```

Use the frame counts to populate `audioDurationFrames` in `EclatVideo.tsx`.
