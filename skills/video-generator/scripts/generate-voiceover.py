import asyncio
import edge_tts
import os

# ─── CONFIGURE THESE ───
VOICE = "zh-CN-XiaoxiaoNeural"  # or zh-CN-YunyangNeural for male
OUTPUT_DIR = "public/voiceover/<video-name>"  # update this

SCENES = [
    {
        "id": "scene-01-intro",
        "text": "在这里填写开场配音文案。品牌名，一句话定位。"
    },
    {
        "id": "scene-02-<name>",
        "text": "在这里填写场景二的配音文案。"
    },
    {
        "id": "scene-03-<name>",
        "text": "在这里填写场景三的配音文案。"
    },
    {
        "id": "scene-04-closing",
        "text": "在这里填写结尾配音文案。品牌名，品牌标语。"
    },
]

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for scene in SCENES:
        path = os.path.join(OUTPUT_DIR, f"{scene['id']}.mp3")
        print(f"Generating: {scene['id']}.mp3 ...")
        communicate = edge_tts.Communicate(scene["text"], VOICE)
        await communicate.save(path)
        print(f"  Saved {path}")

    print("\nAll done!")

asyncio.run(main())
