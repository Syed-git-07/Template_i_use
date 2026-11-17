# prompt-composer

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/prompt-composer.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/prompt-composer.tsx); SHA-256 `e96f648afbc7ce92a447712bb4eb161967d0a1e7f17d7abf9818f2ddbda729ca`; 814 lines.

Imports: `react`, `@base-ui/react/button`, `@paper-design/shaders-react`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| primaryBg | string | False | 42 |
| secondaryBg | string | False | 42 |
| tertiaryBg | string | False | 42 |
| borderGlow | ComposerBorderGlowState | False | 95 |
| reduceMotion | boolean | False | 96 |
| pulseDurationSec | number | True | 174 |
| warpProps | Partial<WarpProps> | True | 175 |
| className | string | True | 279 |
| reduceMotion | boolean | False | 280 |
| text | string | False | 329 |
| animateKey | number | False | 330 |
| reduceMotion | boolean | False | 331 |
| staggerSec | number | True | 332 |
| charDurationSec | number | True | 333 |
| className | string | True | 334 |
| alignTop | boolean | True | 335 |
| reduceMotion | boolean | False | 387 |
| reduceMotion | boolean | False | 413 |
| disabled | boolean | False | 414 |
| onClick | () => void | False | 415 |
| reduceMotion | boolean | False | 455 |
| emphasis | boolean | False | 456 |
| blobTranslucent | boolean | True | 522 |
| isLoading | boolean | True | 523 |
| loadingText | string | True | 524 |
| loadingStaggerSec | number | True | 525 |
| loadingCharDurationSec | number | True | 526 |
| onSend | () => void | True | 528 |
| onAttach | () => void | True | 530 |
| showAttach | boolean | True | 531 |
| autoGrow | boolean | True | 533 |
| maxAutoGrowPx | number | True | 534 |

### Defaults and motion

- Default `pulseDurationSec` = `5.2` (line 182).
- Default `placeholder` = `"Write a prompt…"` (line 547).
- Default `blobTranslucent` = `false` (line 548).
- Default `isLoading` = `false` (line 549).
- Default `loadingText` = `"Sending…"` (line 550).
- Default `autoGrow` = `true` (line 558).
- Default `maxAutoGrowPx` = `280` (line 559).
- `duration`: 0.25 (line 107).
- `ease`: "easeOut" (line 107).
- `duration`: computed; inspect expression (line 118).
- `ease`: "easeInOut" (line 120).
- `duration`: computed; inspect expression (line 132).
- `ease`: "easeInOut" (line 134).
- `duration`: computed; inspect expression (line 146).
- `ease`: "easeInOut" (line 148).
- `duration`: computed; inspect expression (line 233).
- `ease`: "easeInOut" (line 234).
- `duration`: computed; inspect expression (line 260).
- `ease`: computed; inspect expression (line 261).
- `duration`: computed; inspect expression (line 372).
- `ease`: "easeOut" (line 373).
- `duration`: 0 (line 459).
- `duration`: 18 (line 461).
- `ease`: computed; inspect expression (line 463).
- `duration`: computed; inspect expression (line 502).

### Input, style and lifecycle

Events: onClick (line 440); onBlur (line 732); onChange (line 733); onFocus (line 737); onKeyDown (line 738); onClick (line 781); onClick (line 796).

Typography/style anchors: 361, 507.

Source signals: reduced_motion, keyboard, focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
