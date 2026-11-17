# halo-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-card.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-card.tsx); SHA-256 `54c0ecd9fdcf287352f2d1df882ca9487c15f7fcff1d7e7bf25005df5eed7f55`; 686 lines.

Imports: `react`, `@base-ui/react/button`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| active | boolean | False | 49 |
| borderGlow | BorderGlowState | False | 164 |
| reduceMotion | boolean | False | 165 |
| children | ReactNode | False | 243 |
| translucent | boolean | True | 245 |
| interactive | boolean | True | 247 |
| padding | keyof typeof paddingClass | True | 249 |
| children | ReactNode | False | 503 |
| variant | "primary" \| "secondary" | True | 508 |
| size | "default" \| "icon" | True | 509 |

### Defaults and motion

- Default `translucent` = `true` (line 256).
- Default `interactive` = `true` (line 257).
- Default `padding` = `"md"` (line 258).
- Default `ariaLabel` = `"Card"` (line 259).
- Default `variant` = `"primary"` (line 517).
- Default `size` = `"default"` (line 518).
- `duration`: 0.25 (line 176).
- `ease`: "easeOut" (line 176).
- `duration`: computed; inspect expression (line 187).
- `ease`: "easeInOut" (line 189).
- `duration`: computed; inspect expression (line 201).
- `ease`: "easeInOut" (line 203).
- `duration`: computed; inspect expression (line 215).
- `ease`: "easeInOut" (line 217).
- `duration`: 0.25 (line 329).
- `ease`: "easeOut" (line 329).
- `duration`: computed; inspect expression (line 340).
- `ease`: "easeInOut" (line 342).
- `duration`: computed; inspect expression (line 354).
- `ease`: "easeInOut" (line 356).
- `duration`: computed; inspect expression (line 368).
- `ease`: "easeInOut" (line 370).

### Input, style and lifecycle

Events: onBlur (line 294); onFocus (line 300); onMouseEnter (line 306); onMouseLeave (line 312); onBlur (line 577); onFocus (line 581); onMouseEnter (line 585); onMouseLeave (line 589); onBlur (line 634); onFocus (line 638); onMouseEnter (line 642); onMouseLeave (line 646).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, focus, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
