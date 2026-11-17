# agent-suggest-card-stack

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/agent-suggest-card-stack.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/agent-suggest-card-stack.tsx); SHA-256 `9ea0dde3eb4ab37c93d11213287b8d4ec49e0191090780afe7c736914d4c33a0`; 591 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 8 |
| title | string | False | 9 |
| progress | number | False | 10 |
| status | "success" \| "error" \| "mixed" | True | 11 |
| mixedProgress | { success: number; error: number } | True | 12 |
| success | number | False | 12 |
| error | number | False | 12 |
| width | number | True | 17 |
| height | number | True | 18 |
| backgroundColor | string | True | 19 |
| cardFill | string | True | 20 |
| cardStroke | string | True | 21 |
| borderColor | string | True | 22 |
| textColor | string | True | 23 |
| mutedTextColor | string | True | 24 |
| badgeColor | string | True | 25 |
| badgeTextColor | string | True | 26 |
| botBadgeColor | string | True | 27 |
| botBadgeTextColor | string | True | 28 |
| botBadgeStrokeColor | string | True | 29 |
| eyeIconColor | string | True | 30 |
| progressBarBackground | string | True | 31 |
| progressBarStrokeColor | string | True | 32 |
| mixedProgressSeparatorColor | string | True | 33 |
| successColor | string | True | 34 |
| errorColor | string | True | 35 |
| commitButtonFill | string | True | 36 |
| commitButtonStroke | string | True | 37 |
| commitButtonTextColor | string | True | 38 |
| headerTitle | string | True | 39 |
| headerBadge | string | True | 40 |
| suggestions | SuggestionItem[] | True | 41 |
| commitButtonText | string | True | 42 |
| logoIcon | React.ReactNode | True | 43 |
| color | string | True | 50 |
| size | number | True | 51 |
| color | string | True | 75 |
| size | number | True | 76 |
| backShadowId | string | False | 102 |
| frontShadowId | string | False | 103 |
| firstProgressClipId | string | False | 104 |
| secondProgressClipId | string | False | 105 |
| x | number | False | 176 |
| y | number | False | 177 |
| width | number | False | 178 |
| height | number | False | 179 |
| fill | string | False | 180 |
| stroke | string | False | 181 |
| radius | number | True | 182 |
| x | number | False | 206 |
| y | number | False | 207 |
| strokeColor | string | False | 208 |
| textColor | string | False | 209 |
| text | string | False | 242 |
| fill | string | False | 243 |
| stroke | string | False | 244 |
| textColor | string | False | 245 |

### Defaults and motion

- Default `color` = `"#171717"` (line 47).
- Default `size` = `16` (line 48).
- Default `color` = `"#7D7D7D"` (line 72).
- Default `size` = `14` (line 73).
- Default `radius` = `12` (line 174).
- Default `width` = `444` (line 275).
- Default `height` = `178` (line 276).
- Default `backgroundColor` = `"transparent"` (line 277).
- Default `cardFill` = `"var(--card)"` (line 278).
- Default `cardStroke` = `"var(--border)"` (line 279).
- Default `textColor` = `"var(--foreground)"` (line 281).
- Default `mutedTextColor` = `"var(--muted-foreground)"` (line 282).
- Default `badgeColor` = `"#388E4A"` (line 283).
- Default `badgeTextColor` = `"var(--primary-foreground)"` (line 284).
- Default `botBadgeColor` = `"var(--muted)"` (line 285).
- Default `botBadgeTextColor` = `"var(--muted-foreground)"` (line 286).
- Default `botBadgeStrokeColor` = `"var(--border)"` (line 287).
- Default `eyeIconColor` = `"var(--muted-foreground)"` (line 288).
- Default `progressBarBackground` = `"color-mix(in oklab, var(--muted) 85%, #388e4a 15%)"` (line 289).
- Default `progressBarStrokeColor` = `"var(--border)"` (line 290).
- Default `mixedProgressSeparatorColor` = `"color-mix(in oklab, var(--foreground) 12%, transparent)"` (line 291).
- Default `successColor` = `"color-mix(in oklab, #388e4a 50%, var(--muted))"` (line 292).
- Default `errorColor` = `"color-mix(in oklab, #c63d3d 50%, var(--muted))"` (line 293).
- Default `commitButtonFill` = `"var(--muted)"` (line 294).
- Default `commitButtonStroke` = `"var(--border)"` (line 295).
- Default `commitButtonTextColor` = `"var(--foreground)"` (line 296).
- Default `headerTitle` = `"Adding a #5347"` (line 297).
- Default `headerBadge` = `"Open"` (line 298).
- Default `commitButtonText` = `"Commit to main"` (line 309).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 224, 261, 281, 291, 296, 400, 411, 421, 448, 492, 508.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
