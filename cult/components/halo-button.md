# halo-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-button.tsx); SHA-256 `8ad70eea4ae506bae0a1d5fc16a011dbcfffd6a0708de83773661bd3792fa41c`; 448 lines.

Imports: `react`, `@base-ui/react/button`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 54 |
| reduceMotion | boolean | False | 55 |
| text | string | False | 101 |
| reduceMotion | boolean | False | 102 |
| staggerSec | number | True | 103 |
| charDurationSec | number | True | 104 |
| reduceMotion | boolean | False | 154 |
| reveal | boolean | False | 155 |
| children | ReactNode | False | 188 |
| translucent | boolean | True | 190 |
| isLoading | boolean | True | 192 |
| loadingText | string | True | 194 |
| loadingStaggerSec | number | True | 196 |
| loadingCharDurationSec | number | True | 198 |
| staggerLabel | boolean | True | 203 |
| className | string | True | 204 |

### Defaults and motion

- Default `translucent` = `true` (line 210).
- Default `isLoading` = `false` (line 211).
- Default `loadingText` = `"Working…"` (line 212).
- Default `staggerLabel` = `true` (line 215).
- `bounce`: 0.12 (line 29).
- `damping`: 34 (line 30).
- `stiffness`: 420 (line 31).
- `duration`: computed; inspect expression (line 35).
- `ease`: computed; inspect expression (line 36).
- `duration`: computed; inspect expression (line 135).
- `ease`: "easeOut" (line 136).
- `duration`: 0 (line 175).
- `duration`: 0 (line 178).
- `duration`: 0.25 (line 344).
- `ease`: "easeOut" (line 344).
- `duration`: computed; inspect expression (line 355).
- `ease`: "easeInOut" (line 357).
- `duration`: computed; inspect expression (line 369).
- `ease`: "easeInOut" (line 371).
- `duration`: computed; inspect expression (line 383).
- `ease`: "easeInOut" (line 385).

### Input, style and lifecycle

Events: onLayoutAnimationComplete (line 331); onBlur (line 407); onFocus (line 411); onMouseEnter (line 415); onMouseLeave (line 419).

Typography/style anchors: 124, 170.

Source signals: reduced_motion, focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
