# spotlight-new

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/spotlight-new/components/ui/spotlight-new.tsx

[Original source](https://ui.aceternity.com/registry/spotlight-new.json); SHA-256 `7231f31ab0df6269dfcfce011af4a4b03860b7e157c1cda8c3d329e9a8f12b44`; 129 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| gradientFirst | string | True | 6 |
| gradientSecond | string | True | 7 |
| gradientThird | string | True | 8 |
| translateY | number | True | 9 |
| width | number | True | 10 |
| height | number | True | 11 |
| smallWidth | number | True | 12 |
| duration | number | True | 13 |
| xOffset | number | True | 14 |

### Defaults and motion

- Default `gradientFirst` = `"radial-gradient(68.54% 68.72% at 55.02% 31.46%, hsla(210, 100%, 85%, .08) 0, hsla(210, 100%, 55%, .02) 50%, hsla(210, 100%, 45%, 0) 80%)"` (line 18).
- Default `gradientSecond` = `"radial-gradient(50% 50% at 50% 50%, hsla(210, 100%, 85%, .06) 0, hsla(210, 100%, 55%, .02) 80%, transparent 100%)"` (line 19).
- Default `gradientThird` = `"radial-gradient(50% 50% at 50% 50%, hsla(210, 100%, 85%, .04) 0, hsla(210, 100%, 45%, .02) 80%, transparent 100%)"` (line 20).
- Default `translateY` = `-350` (line 21).
- Default `width` = `560` (line 22).
- Default `height` = `1380` (line 23).
- Default `smallWidth` = `240` (line 24).
- Default `duration` = `7` (line 25).
- Default `xOffset` = `100` (line 26).
- `duration`: 1.5 (line 37).
- `ease`: "easeInOut" (line 49).
- `ease`: "easeInOut" (line 92).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
