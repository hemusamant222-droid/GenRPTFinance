# GenRPT Finance Demo

React + TypeScript + Remotion project for a product-demo video using actual GenRPT Finance screenshots.

## Development

Requires Node.js 22 or newer and npm. From this repository:

```sh
npm ci
npm run dev
```

Studio runs on port 3000. Select **GenRPTFinanceDemo**: 1920 × 1080, 30 FPS, 450 frames (15 seconds). The initial composition is an animated test scene with an explicitly labeled screenshot placeholder.

## Product screenshots

Place approved screenshots in `public/screenshots/`. Set the composition's `screenshot` prop to a public-relative path such as `screenshots/dashboard.png` in Studio or in `src/Root.tsx`. Do not include `public/` in the path. The image is contained without cropping. No actual product UI is bundled yet.

## Validation and output

```sh
npm run typecheck
npm run build
npm run compositions
npm run still
npm run render
```

The production browser bundle goes to `build/`; images and videos go to `out/`. Remotion downloads Chrome Headless Shell when needed. To use an installed Chromium instead, append `--browser-executable=/usr/bin/chromium` to compositions, still, or render commands. No API keys, databases, or external services are required.

The visual scene is in `src/GenRPTFinanceDemo.tsx`; composition dimensions, duration, and default props are in `src/Root.tsx`. All animation uses Remotion frames for deterministic rendering.

Review Remotion's licensing terms before commercial use: https://www.remotion.dev/docs/license
