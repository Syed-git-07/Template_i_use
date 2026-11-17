# terminal-animation

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/terminal-animation.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/terminal-animation.tsx); SHA-256 `3cc7f4627bb42ff3e4ff5db4fb63dd6487125e28dd7f90291d5e7efa2f7e01af`; 809 lines.

Imports: `react`, `@radix-ui/react-slot`, `@radix-ui/react-use-controllable-state`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 22 |
| color | string | True | 23 |
| delay | number | True | 24 |
| label | string | False | 28 |
| command | string | False | 29 |
| lines | TerminalLine[] | False | 30 |
| tabs | TabContent[] | False | 35 |
| defaultActiveTab | number | True | 37 |
| activeTab | number | True | 39 |
| onActiveTabChange | (index: number) => void | True | 41 |
| backgroundImage | string | True | 43 |
| alwaysDark | boolean | True | 45 |
| hideCursorOnComplete | boolean | True | 47 |
| activeTab | number | False | 55 |
| setActiveTab | (index: number) => void | False | 56 |
| commandTyped | string | False | 57 |
| isTypingCommand | boolean | False | 58 |
| showCursor | boolean | False | 59 |
| visibleLines | number | False | 60 |
| currentTab | TabContent | False | 61 |
| tabs | TabContent[] | False | 62 |
| backgroundColor | string | True | 483 |
| minHeight | string | True | 485 |
| animateOnVisible | boolean | True | 487 |
| cursor | ReactNode | True | 594 |
| line | TerminalLine | False | 624 |
| visible | boolean | False | 625 |
| renderLine | (     line: TerminalLine,     index: number,     visible: boolean   ) => ReactNode | True | 654 |
| index | number | False | 764 |
| asChild | boolean | True | 766 |

### Defaults and motion

- Default `defaultActiveTab` = `0` (line 313).
- Default `alwaysDark` = `false` (line 317).
- Default `hideCursorOnComplete` = `true` (line 318).
- Default `minHeight` = `"28rem"` (line 495).
- Default `animateOnVisible` = `true` (line 496).
- Default `asChild` = `false` (line 771).
- `delay`: 80 (line 88).
- `delay`: 400 (line 92).
- `delay`: 80 (line 94).
- `delay`: 200 (line 95).
- `delay`: 80 (line 96).
- `delay`: 80 (line 97).
- `delay`: 80 (line 98).
- `delay`: 80 (line 99).
- `delay`: 80 (line 100).
- `delay`: 200 (line 101).
- `delay`: 200 (line 102).
- `delay`: 80 (line 103).
- `delay`: 200 (line 104).
- `delay`: 300 (line 105).
- `delay`: 50 (line 106).
- `delay`: 100 (line 107).
- `delay`: 100 (line 108).
- `delay`: 80 (line 115).
- `delay`: 400 (line 119).
- `delay`: 80 (line 121).
- `delay`: 200 (line 125).
- `delay`: 100 (line 130).
- `delay`: 100 (line 135).
- `delay`: 300 (line 137).
- `delay`: 600 (line 141).
- `delay`: 400 (line 146).
- `delay`: 80 (line 154).
- `delay`: 300 (line 158).
- `delay`: 80 (line 160).
- `delay`: 150 (line 161).
- `delay`: 100 (line 165).
- `delay`: 80 (line 167).
- `delay`: 150 (line 168).
- `delay`: 100 (line 172).
- `delay`: 80 (line 174).
- `delay`: 150 (line 178).
- `delay`: 100 (line 183).
- `delay`: 80 (line 185).
- `delay`: 300 (line 189).
- `delay`: 80 (line 197).
- `delay`: 200 (line 201).
- `delay`: 80 (line 203).
- `delay`: 150 (line 204).
- `delay`: 100 (line 208).
- `delay`: 100 (line 213).
- `delay`: 80 (line 215).
- `delay`: 200 (line 216).
- `delay`: 100 (line 217).
- `delay`: 80 (line 218).
- `delay`: 200 (line 219).
- `delay`: 80 (line 226).
- `delay`: 300 (line 227).
- `delay`: 80 (line 228).
- `delay`: 200 (line 229).
- `delay`: 150 (line 233).
- `delay`: 100 (line 238).
- `delay`: 100 (line 243).
- `delay`: 200 (line 245).
- `delay`: 100 (line 249).
- `delay`: 100 (line 254).
- `delay`: 80 (line 256).
- `delay`: 200 (line 257).
- `delay`: 100 (line 258).
- `delay`: 80 (line 265).
- `delay`: 400 (line 269).
- `delay`: 80 (line 271).
- `delay`: 300 (line 272).
- `delay`: 300 (line 276).
- `delay`: 80 (line 278).
- `delay`: 200 (line 279).
- `delay`: 200 (line 283).
- `delay`: 80 (line 285).
- `delay`: 100 (line 289).
- `delay`: 80 (line 294).
- `delay`: 80 (line 299).
- `delay`: 80 (line 301).
- `delay`: 300 (line 302).
- `threshold`: 0.1 (line 514).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: visibility, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
