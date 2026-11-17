# halo-select

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-select.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-select.tsx); SHA-256 `a5d8067dddf4f010aa4090da4694f1123dd11b0be848944c116f3cfe1563943b`; 839 lines.

Imports: `react`, `@base-ui/react/select`, `lucide-react`, `motion/react`, `@/lib/utils`, `@/registry/default/ui/base-select`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| opacityIdle | number | False | 47 |
| primaryBg | string | False | 48 |
| secondaryBg | string | False | 49 |
| tertiaryBg | string | False | 50 |
| primaryLeft | string[] | False | 51 |
| secondaryLeft | string[] | False | 52 |
| tertiaryLeft | string[] | False | 53 |
| durationMain | number | False | 54 |
| durationSec | number | False | 55 |
| durationTer | number | False | 56 |
| value | string | False | 60 |
| label | string | False | 61 |
| disabled | boolean | True | 62 |
| translucent | boolean | False | 70 |
| isLoading | boolean | False | 71 |
| showSelectionFlash | boolean | False | 72 |
| reduceMotion | boolean | False | 73 |
| open | boolean | False | 74 |
| setOpen | (open: boolean) => void | False | 75 |
| isFocused | boolean | False | 76 |
| setIsFocused | (focused: boolean) => void | False | 77 |
| listBurst | number | False | 78 |
| labelStagger | { key: number; text: string } | False | 79 |
| key | number | False | 79 |
| text | string | False | 79 |
| showStaggerOverlay | boolean | False | 80 |
| placeholder | string | False | 81 |
| borderGlow | BorderGlowConfig | False | 82 |
| trailingMode | "spinner" \| "check" \| "chevron" | False | 83 |
| fieldId | string | False | 84 |
| text | string | False | 105 |
| animateKey | number | False | 106 |
| reduceMotion | boolean | False | 107 |
| className | string | True | 108 |
| className | string | True | 158 |
| reduceMotion | boolean | False | 159 |
| borderGlow | BorderGlowConfig | False | 253 |
| translucent | boolean | False | 254 |
| reduceMotion | boolean | False | 255 |
| children | ReactNode | False | 340 |
| translucent | boolean | True | 342 |
| isLoading | boolean | True | 343 |
| showSelectionFlash | boolean | True | 344 |
| placeholder | string | True | 346 |
| className | string | True | 347 |
| onValueChange | (     value: unknown,     eventDetails: SelectValueChangeDetails   ) => void | True | 348 |
| className | string | True | 668 |
| index | number | True | 778 |

### Defaults and motion

- Default `translucent` = `false` (line 370).
- Default `isLoading` = `false` (line 371).
- Default `showSelectionFlash` = `true` (line 372).
- Default `placeholder` = `"Select an option"` (line 373).
- Default `side` = `"bottom"` (line 744).
- Default `sideOffset` = `6` (line 745).
- Default `align` = `"start"` (line 746).
- Default `index` = `0` (line 774).
- `duration`: computed; inspect expression (line 139).
- `ease`: "easeOut" (line 140).
- `duration`: computed; inspect expression (line 200).
- `ease`: computed; inspect expression (line 201).
- `duration`: 0.25 (line 287).
- `ease`: "easeOut" (line 287).
- `duration`: computed; inspect expression (line 298).
- `ease`: "easeInOut" (line 300).
- `duration`: computed; inspect expression (line 312).
- `ease`: "easeInOut" (line 314).
- `duration`: computed; inspect expression (line 326).
- `ease`: "easeInOut" (line 328).
- `duration`: 0.22 (line 815).
- `ease`: computed; inspect expression (line 816).

### Input, style and lifecycle

Events: onOpenChange (line 534); onValueChange (line 538); onBlur (line 605); onFocus (line 609).

Typography/style anchors: 128.

Source signals: reduced_motion, focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
