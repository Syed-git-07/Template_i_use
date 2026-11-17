# halo-notification

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-notification.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-notification.tsx); SHA-256 `70c1c962de66f500f82f553a938112708f9ad5838a0468389e5beb1e9cc84d59`; 680 lines.

Imports: `react`, `@base-ui/react/button`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| primaryBg | string | False | 47 |
| secondaryBg | string | False | 47 |
| tertiaryBg | string | False | 47 |
| ambientGradient | string | False | 69 |
| ambientGlow | string | False | 70 |
| coreGradient | string | False | 71 |
| coreGlow | string | False | 72 |
| active | boolean | False | 112 |
| rimVariant | RimVariant | True | 113 |
| borderGlow | NotificationBorderGlowState | False | 227 |
| reduceMotion | boolean | False | 228 |
| children | ReactNode | False | 311 |
| translucent | boolean | True | 312 |
| interactive | boolean | True | 313 |
| padding | keyof typeof paddingClass | True | 314 |
| rimVariant | RimVariant | True | 315 |
| as | "span" \| "p" | True | 453 |
| className | string | True | 454 |
| delayChildrenSec | number | True | 455 |
| messageKey | string | False | 457 |
| reduceMotion | boolean | False | 458 |
| text | string | False | 459 |
| title | string | False | 525 |
| description | string | True | 526 |
| messageKey | string | True | 531 |
| politeness | "status" \| "alert" | True | 533 |
| onDismiss | () => void | True | 534 |
| translucent | boolean | True | 536 |
| rimVariant | RimVariant | True | 538 |
| className | string | True | 539 |
| slideFrom | "top" \| "bottom" | True | 630 |

### Defaults and motion

- Default `rimVariant` = `"default"` (line 110).
- Default `translucent` = `true` (line 323).
- Default `interactive` = `true` (line 324).
- Default `padding` = `"md"` (line 325).
- Default `rimVariant` = `"default"` (line 326).
- Default `ariaLabel` = `"Card"` (line 327).
- Default `Tag` = `"span"` (line 446).
- Default `delayChildrenSec` = `0` (line 448).
- Default `politeness` = `"status"` (line 550).
- Default `translucent` = `true` (line 552).
- Default `rimVariant` = `"default"` (line 553).
- Default `slideFrom` = `"bottom"` (line 643).
- `duration`: 0.25 (line 244).
- `ease`: "easeOut" (line 244).
- `duration`: computed; inspect expression (line 255).
- `ease`: "easeInOut" (line 257).
- `duration`: computed; inspect expression (line 269).
- `ease`: "easeInOut" (line 271).
- `duration`: computed; inspect expression (line 283).
- `ease`: "easeInOut" (line 285).
- `duration`: computed; inspect expression (line 497).
- `ease`: "easeOut" (line 498).
- `ease`: "easeOut" (line 662).

### Input, style and lifecycle

Events: onBlur (line 363); onFocus (line 369); onMouseEnter (line 375); onMouseLeave (line 381); onClick (line 609); onDismiss (line 669).

Typography/style anchors: 485.

Source signals: reduced_motion, focus, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
