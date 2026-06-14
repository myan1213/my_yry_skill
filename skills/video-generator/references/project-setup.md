# Project Setup

## Directory Structure

Create folder: `<video-name>-video/` under the project root (e.g., `aurora-tech-video/`).

```
<video-name>-video/
├── package.json
├── tsconfig.json
├── remotion.config.ts
├── .prettierrc
├── .gitignore
├── eslint.config.mjs
├── public/
│   └── voiceover/
│       └── <video-name>/
└── src/
    ├── index.ts
    ├── Root.tsx
    ├── EclatVideo.tsx
    ├── style.ts
    ├── index.css
    ├── Intro.tsx
    ├── Scene1.tsx
    ├── Scene2.tsx
    ├── ...
    └── Closing.tsx
```

## Files to Create

### package.json

```json
{
  "name": "<video-name>-video",
  "version": "1.0.0",
  "description": "Remotion video for <video-name>",
  "private": true,
  "dependencies": {
    "@remotion/cli": "4.0.474",
    "@remotion/google-fonts": "4.0.474",
    "@remotion/tailwind-v4": "4.0.474",
    "react": "19.2.3",
    "react-dom": "19.2.3",
    "remotion": "4.0.474",
    "tailwindcss": "4.0.0"
  },
  "devDependencies": {
    "@remotion/eslint-config-flat": "4.0.474",
    "@types/react": "19.2.7",
    "@types/web": "0.0.166",
    "eslint": "9.19.0",
    "prettier": "3.8.1",
    "typescript": "5.9.3"
  },
  "scripts": {
    "dev": "remotion studio",
    "build": "remotion bundle",
    "lint": "eslint src && tsc"
  },
  "sideEffects": ["*.css"]
}
```

### tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2018",
    "module": "commonjs",
    "jsx": "react-jsx",
    "strict": true,
    "noEmit": true,
    "lib": ["es2015"],
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "noUnusedLocals": true
  },
  "exclude": ["remotion.config.ts"]
}
```

### remotion.config.ts

```ts
import { Config } from "@remotion/cli/config";
import { enableTailwind } from "@remotion/tailwind-v4";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
Config.overrideWebpackConfig(enableTailwind);
```

### src/index.ts

```ts
import { registerRoot } from "remotion";
import { RemotionRoot } from "./Root";

registerRoot(RemotionRoot);
```

### src/index.css

```css
@import "tailwindcss";
```

### .prettierrc

```json
{
  "arrowParens": "always",
  "bracketSpacing": true,
  "printWidth": 100,
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "all",
  "useTabs": false
}
```

### .gitignore

```
node_modules
out
.webpack
```

### eslint.config.mjs

```js
import { remotionFlatConfig } from "@remotion/eslint-config-flat";
export default remotionFlatConfig;
```
