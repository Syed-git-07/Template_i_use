# halo-badge

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-badge.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-badge.tsx); SHA-256 `377473dc461972d70f0872be763e966d7c3d02893b6d0df07bdffd564af6b365`; 500 lines.

Imports: `react`, `class-variance-authority`, `motion/react`, `@/lib/utils`, `@/components/ui/badge`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| primaryBg | string | False | 21 |
| secondaryBg | string | False | 21 |
| tertiaryBg | string | False | 21 |
| reduceMotion | boolean | False | 109 |
| borderGlow | ReturnType<typeof badgeBorderGlowConfig> | False | 142 |
| reduceMotion | boolean | False | 143 |
| children | ReactNode | True | 257 |
| live | boolean | True | 259 |
| layout | boolean | True | 264 |
| tabularNums | boolean | True | 266 |
| translucent | boolean | True | 268 |
| interactive | boolean | True | 270 |
| pressScale | boolean | True | 275 |
| borderGlow | ReturnType<typeof badgeBorderGlowConfig> | False | 297 |
| body | ReactNode | False | 298 |
| chromedKey | keyof typeof chromedLabelClasses | False | 299 |
| className | string | True | 300 |
| enableLayout | boolean | False | 301 |
| fillBackground | string | False | 302 |
| interactive | boolean | False | 303 |
| live | boolean | False | 304 |
| onMouseEnter | ComponentProps<typeof motion.span>["onMouseEnter"] | True | 305 |
| onMouseLeave | ComponentProps<typeof motion.span>["onMouseLeave"] | True | 306 |
| pressScale | boolean | False | 307 |
| pulseTransition | { duration: number; ease: "easeInOut"; repeat: number } | False | 308 |
| duration | number | False | 308 |
| ease | "easeInOut" | False | 308 |
| repeat | number | False | 308 |
| reduceMotion | boolean | False | 309 |
| singleDigitCircle | boolean | False | 310 |
| multiDigitTabular | boolean | False | 311 |
| translucent | boolean | False | 312 |

### Defaults and motion

- Default `variant` = `"default"` (line 386).
- Default `live` = `false` (line 389).
- Default `layout` = `true` (line 390).
- Default `tabularNums` = `false` (line 391).
- Default `translucent` = `true` (line 392).
- Default `interactive` = `true` (line 393).
- Default `pressScale` = `true` (line 394).
- `bounce`: 0 (line 87).
- `duration`: 0.32 (line 88).
- `duration`: 0.25 (line 154).
- `ease`: "easeOut" (line 154).
- `duration`: computed; inspect expression (line 165).
- `ease`: "easeInOut" (line 167).
- `duration`: computed; inspect expression (line 179).
- `ease`: "easeInOut" (line 181).
- `duration`: computed; inspect expression (line 193).
- `ease`: "easeInOut" (line 195).
- `duration`: computed; inspect expression (line 405).
- `ease`: computed; inspect expression (line 406).

### Input, style and lifecycle

Events: onMouseEnter (line 324); onMouseLeave (line 325); onMouseEnter (line 483); onMouseLeave (line 487).

Typography/style anchors: 237.

Source signals: reduced_motion, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
