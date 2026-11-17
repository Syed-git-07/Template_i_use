# halo-search

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-search.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-search.tsx); SHA-256 `8881db0dd7974d1aaaabd4c10a486c3408e2012d8f4724da8458e4ea648da197`; 999 lines.

Imports: `react`, `@paper-design/shaders-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| sweepDurationMs | number | False | 48 |
| animatedCount | number | False | 50 |
| staggerGlyphCount | number | False | 52 |
| onClear | () => void | True | 85 |
| blobTranslucent | boolean | True | 90 |
| isLoading | boolean | True | 95 |
| loadingText | string | True | 97 |
| loadingStaggerSec | number | True | 99 |
| loadingCharDurationSec | number | True | 101 |
| className | string | True | 104 |
| className | string | True | 128 |
| reduceMotion | boolean | False | 129 |
| reduceMotion | boolean | False | 185 |
| reduceMotion | boolean | False | 210 |
| onClear | () => void | False | 211 |
| hasValue | boolean | False | 244 |
| isLoading | boolean | False | 245 |
| reduceMotion | boolean | False | 246 |
| onClear | () => void | False | 247 |
| text | string | False | 274 |
| animateKey | number | False | 275 |
| reduceMotion | boolean | False | 276 |
| staggerSec | number | True | 278 |
| charDurationSec | number | True | 280 |
| text | string | False | 691 |
| animatedIndexes | number[] | True | 692 |
| reduceMotion | boolean | True | 693 |
| className | string | True | 694 |
| textClassName | string | True | 695 |
| clipDurationMs | number | True | 696 |
| blurPx | number | True | 697 |
| saturatePercent | number | True | 698 |
| showSweep | boolean | True | 700 |
| pulseDurationSec | number | True | 921 |
| warpProps | Partial<WarpProps> | True | 923 |

### Defaults and motion

- Default `placeholder` = `"Ask anything or search"` (line 333).
- Default `blobTranslucent` = `false` (line 334).
- Default `isLoading` = `false` (line 335).
- Default `loadingText` = `"Searching…"` (line 336).
- Default `reduceMotion` = `false` (line 710).
- Default `clipDurationMs` = `340` (line 713).
- Default `blurPx` = `10` (line 714).
- Default `saturatePercent` = `220` (line 715).
- Default `showSweep` = `true` (line 716).
- Default `pulseDurationSec` = `5.2` (line 934).
- `duration`: computed; inspect expression (line 170).
- `ease`: computed; inspect expression (line 171).
- `duration`: computed; inspect expression (line 313).
- `ease`: "easeOut" (line 314).
- `duration`: 0.25 (line 550).
- `ease`: "easeOut" (line 550).
- `duration`: computed; inspect expression (line 563).
- `ease`: "easeInOut" (line 565).
- `duration`: computed; inspect expression (line 579).
- `ease`: "easeInOut" (line 581).
- `duration`: computed; inspect expression (line 595).
- `ease`: "easeInOut" (line 597).
- `duration`: computed; inspect expression (line 764).
- `delay`: computed; inspect expression (line 765).
- `ease`: "easeOut" (line 766).
- `duration`: 0 (line 783).
- `ease`: "easeOut" (line 784).
- `duration`: computed; inspect expression (line 822).
- `ease`: "easeOut" (line 827).
- `delay`: computed; inspect expression (line 829).
- `duration`: computed; inspect expression (line 855).
- `ease`: "easeOut" (line 856).
- `duration`: computed; inspect expression (line 874).
- `ease`: "easeOut" (line 875).
- `duration`: computed; inspect expression (line 985).
- `ease`: "easeInOut" (line 986).

### Input, style and lifecycle

Events: onClick (line 229); onClear (line 259); onBlur (line 637); onChange (line 638); onFocus (line 639); onClear (line 681).

Typography/style anchors: 302, 763, 928.

Source signals: reduced_motion, focus, async, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
