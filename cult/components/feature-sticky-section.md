# feature-sticky-section

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/feature-sticky-section.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/feature-sticky-section.tsx); SHA-256 `af7a4b4cbab56ed35485980766ab735ee9c08dcea86a9b03546f3c27c6ff2dd4`; 852 lines.

Imports: `react`, `next/image`, `@radix-ui/react-slot`, `@radix-ui/react-use-controllable-state`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| activeIndex | number | False | 26 |
| registerPanel | (index: number, el: HTMLElement \| null) => void | False | 27 |
| unregisterPanel | (index: number) => void | False | 28 |
| scrollToPanel | (index: number) => void | False | 29 |
| value | number | True | 53 |
| defaultValue | number | True | 55 |
| onValueChange | (value: number) => void | True | 57 |
| asChild | boolean | True | 59 |
| asChild | boolean | True | 177 |
| index | number | False | 199 |
| asChild | boolean | True | 200 |
| index | number | False | 230 |
| asChild | boolean | True | 231 |
| asChild | boolean | True | 282 |
| index | number | False | 305 |
| asChild | boolean | True | 306 |
| id | string | False | 389 |
| name | string | False | 390 |
| tagline | string | False | 391 |
| description | string | False | 392 |
| stars | string | False | 393 |
| contributors | string | False | 394 |
| exploreUrl | string | False | 395 |
| image | string | False | 396 |
| icon | ReactNode | False | 397 |
| projects | OSSProject[] | True | 402 |
| className | string | True | 405 |
| className | string | True | 449 |
| className | string | True | 484 |
| className | string | True | 498 |
| className | string | True | 563 |
| withBottomBorder | boolean | True | 684 |
| src | string | False | 732 |
| alt | string | False | 733 |

### Defaults and motion

- Default `defaultValue` = `0` (line 64).
- Default `asChild` = `false` (line 66).
- Default `asChild` = `false` (line 181).
- Default `asChild` = `false` (line 205).
- Default `asChild` = `false` (line 237).
- Default `asChild` = `false` (line 286).
- Default `asChild` = `false` (line 310).
- Default `withBottomBorder` = `false` (line 689).
- `threshold`: computed; inspect expression (line 144).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: visibility, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
