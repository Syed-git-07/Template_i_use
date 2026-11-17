# halo-toast

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-toast.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-toast.tsx); SHA-256 `d1e8ed2ab15a2e8bbc8cd0a8ff9f12ffe28c56e4a7bd1d19cebee031f699fa91`; 705 lines.

Imports: `react`, `motion/react`, `sonner`, `sonner`, `sonner/dist/styles.css`, `lucide-react`, `@/lib/utils`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| primaryBg | string | False | 53 |
| secondaryBg | string | False | 53 |
| tertiaryBg | string | False | 53 |
| ambientGradient | string | False | 75 |
| ambientGlow | string | False | 76 |
| coreGradient | string | False | 77 |
| coreGlow | string | False | 78 |
| active | boolean | False | 118 |
| rimVariant | RimVariant | True | 119 |
| borderGlow | ToastBorderGlowState | False | 231 |
| reduceMotion | boolean | False | 232 |
| children | ReactNode | False | 310 |
| translucent | boolean | True | 311 |
| interactive | boolean | True | 312 |
| padding | keyof typeof paddingClass | True | 313 |
| rimVariant | RimVariant | True | 314 |
| as | "span" \| "p" | True | 445 |
| className | string | True | 446 |
| delayChildrenSec | number | True | 447 |
| messageKey | string | False | 448 |
| reduceMotion | boolean | False | 449 |
| text | string | False | 450 |
| title | string | False | 516 |
| description | string | True | 517 |
| messageKey | string | True | 518 |
| politeness | "status" \| "alert" | True | 519 |
| translucent | boolean | True | 520 |
| rimVariant | RimVariant | True | 521 |
| toastId | number \| string | True | 523 |
| closeButton | boolean | True | 525 |
| className | string | True | 526 |
| title | string | False | 608 |
| description | string | True | 609 |
| messageKey | string | True | 610 |
| politeness | "status" \| "alert" | True | 611 |
| rimVariant | RimVariant | True | 612 |

### Defaults and motion

- Default `rimVariant` = `"default"` (line 116).
- Default `translucent` = `true` (line 322).
- Default `interactive` = `true` (line 323).
- Default `padding` = `"md"` (line 324).
- Default `rimVariant` = `"default"` (line 325).
- Default `ariaLabel` = `"Card"` (line 326).
- Default `Tag` = `"span"` (line 438).
- Default `delayChildrenSec` = `0` (line 440).
- Default `politeness` = `"status"` (line 537).
- Default `translucent` = `true` (line 538).
- Default `rimVariant` = `"default"` (line 539).
- Default `closeButton` = `false` (line 541).
- Default `politeness` = `"status"` (line 624).
- Default `rimVariant` = `"default"` (line 625).
- Default `closeButton` = `true` (line 627).
- `duration`: 0.25 (line 243).
- `ease`: "easeOut" (line 243).
- `duration`: computed; inspect expression (line 254).
- `ease`: "easeInOut" (line 256).
- `duration`: computed; inspect expression (line 268).
- `ease`: "easeInOut" (line 270).
- `duration`: computed; inspect expression (line 282).
- `ease`: "easeInOut" (line 284).
- `duration`: computed; inspect expression (line 488).
- `ease`: "easeOut" (line 489).
- `duration`: computed; inspect expression (line 647).

### Input, style and lifecycle

Events: onBlur (line 361); onFocus (line 367); onMouseEnter (line 373); onMouseLeave (line 379); onClick (line 591).

Typography/style anchors: 476, 683, 694, 699.

Source signals: reduced_motion, focus, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
