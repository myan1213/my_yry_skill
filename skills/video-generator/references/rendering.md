# Rendering

## Install Dependencies

```bash
npm install
```

## Render Video

```bash
npx remotion render src/index.ts BrandVideo <video-name>-<version>.mp4 --codec h264 --crf 18
```

### Parameters

| Param | Value | Description |
|-------|-------|-------------|
| `--codec` | `h264` | Standard MP4 format |
| `--crf` | `18` | High quality (lower = better, 18 is visually lossless) |
| `--concurrency` | auto | Uses all available CPU cores |

## Verify Output

Check the output file:

```bash
ls -lh *.mp4
```

The file should be non-zero and playable in any video player.

## Cleanup (Optional)

Remove generated audio files if they are no longer needed:

```bash
rm -rf public/voiceover/
```
