# Scene Component Generation

## style.ts

Create shared style constants based on the chosen color palette:

```ts
export const COLORS = {
  bg: '#...',
  bgWarm: '#...',
  gold: '#...',
  goldLight: '#...',
  goldDark: '#...',
  cream: '#...',
  creamMuted: '#...',
  accent: '#...',
  accentDark: '#...',
};

export const FONT_TITLE = 'Cinzel, serif';     // or other Google Font
export const FONT_BODY = 'Cormorant Garamond, serif';
```

Choose appropriate Google Fonts for the brand (e.g., Cinzel for luxury, Inter for tech, Noto Serif SC for Chinese brands).

## Scene Component Rules

Every scene must:

1. **Import and load fonts** via `@remotion/google-fonts` at the top level:

```ts
import { loadFont } from '@remotion/google-fonts/Cinzel';
const { fontFamily: cinzelFont } = loadFont('normal', {
  weights: ['400', '700'],
  subsets: ['latin'],
});
```

2. **Use `useCurrentFrame()` and `useVideoConfig()`** for all animations:

```ts
const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const opacity = interpolate(frame, [0, fps], [0, 1], {
  extrapolateRight: 'clamp',
  easing: Easing.bezier(0.16, 1, 0.3, 1),
});
```

3. **Use interpolation helpers consistently** — create a `makeAnim` helper function for reusable fade+slide animations.

4. **Use `<AbsoluteFill>`** as the root container.

5. **Use `<Img>` from remotion** (not `<img>`) for images.

6. **Images** should use pexels.com URLs with `auto=compress` and appropriate sizing params.

## Animation Patterns

### Fade + Slide In (for text elements)

```ts
const makeAnim = (start: number, dur: number, y = 30) => ({
  opacity: interpolate(frame, [start, start + dur], [0, 1], {
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  }),
  transform: `translateY(${interpolate(frame, [start, start + dur], [y, 0], {
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  })}px)`,
});
```

### Slow Background Scale (Ken Burns effect)

```ts
const bgScale = interpolate(frame, [0, fps * 5], [1, 1.08], {
  extrapolateRight: 'clamp',
  easing: Easing.bezier(0.4, 0, 0.6, 1),
});
```

### Pulsing Glow

```ts
const glowOpacity = interpolate(frame % (fps * 4), [0, fps * 2, fps * 4], [0.3, 0.8, 0.3], {
  extrapolateRight: 'clamp',
  extrapolateLeft: 'clamp',
  easing: Easing.bezier(0.4, 0, 0.6, 1),
});
```

## EclatVideo.tsx Pattern

Wire scenes together using `<Sequence>`:

```ts
import { AbsoluteFill, Sequence, Audio, staticFile } from 'remotion';
import { Intro } from './Intro';
// ... imports ...

const SCENE_AUDIO = [
  { id: 'intro', file: 'voiceover/<name>/scene-01-intro.mp3', audioDurationFrames: ... },
  // ...
];

const COMPONENTS: Record<string, React.FC> = {
  intro: Intro,
  // ...
};

export const TOTAL_FRAMES = SCENE_AUDIO.reduce(
  (sum, s) => sum + s.audioDurationFrames + 15, 0
);

export const VideoComponent: React.FC<{ voice?: string }> = ({ voice = 'xiaoxiao' }) => {
  let offset = 0;
  return (
    <AbsoluteFill style={{ backgroundColor: COLORS.bg }}>
      {SCENE_AUDIO.map((scene) => {
        const start = offset;
        offset += scene.audioDurationFrames + 15;
        const Comp = COMPONENTS[scene.id];
        return (
          <Sequence key={scene.id} from={start} durationInFrames={scene.audioDurationFrames + 15}>
            <Comp />
            <Audio src={staticFile(scene.file)} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
```

## Root.tsx Pattern

```ts
import { Composition } from 'remotion';
import { VideoComponent, TOTAL_FRAMES } from './EclatVideo';

export const RemotionRoot = () => (
  <Composition
    id="BrandVideo"
    component={VideoComponent}
    durationInFrames={TOTAL_FRAMES}
    fps={30}
    width={1280}
    height={720}
  />
);
```

## Scene Timing Guidelines

- **Intro**: allow 2-3 seconds for initial animations before voiceover begins
- **Content scenes**: stagger element animations with ~0.3-0.5s delays
- **Closing**: keep it simple, 1-2 animated reveals
- **Padding**: add 15 frames (0.5s) of silence after each scene's audio ends
