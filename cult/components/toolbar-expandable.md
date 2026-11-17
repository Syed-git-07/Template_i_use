# toolbar-expandable

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/toolbar-expandable.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/toolbar-expandable.tsx); SHA-256 `550e799382461fa697680da6395c757b08f6de239ca0ecaa81f62470022801ca`; 682 lines.

Imports: `react`, `@radix-ui/react-scroll-area`, `motion/react`, `@/lib/utils`, `@/components/ui/badge`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 24 |
| title | string | False | 25 |
| description | string | False | 26 |
| icon | \| React.ComponentType<{ className?: string }>     \| React.ReactElement<{ className?: string }> | False | 27 |
| className | string | True | 28 |
| className | string | True | 29 |
| content | React.ReactNode | False | 30 |
| steps | DynamicStep[] | False | 34 |
| badgeText | string | True | 35 |
| className | string | True | 37 |
| expanded | boolean | True | 38 |
| onExpandedChange | (expanded: boolean) => void | True | 39 |
| activeStep | string \| null | True | 40 |
| onActiveStepChange | (stepId: string \| null) => void | True | 41 |
| left | number | False | 321 |
| top | number | False | 322 |
| width | number | False | 323 |
| height | number | False | 324 |
| top | boolean | False | 434 |
| bottom | boolean | False | 435 |
| left | boolean | False | 436 |
| right | boolean | False | 437 |
| viewportClassName | string | True | 443 |
| maskHeight | number | True | 449 |
| maskClassName | string | True | 450 |
| showMask | Mask | False | 626 |
| maskHeight | number | False | 627 |

### Defaults and motion

- Default `scrollHideDelay` = `0` (line 457).
- Default `maskHeight` = `30` (line 460).
- Default `orientation` = `"vertical"` (line 586).
- `bounce`: 0.1 (line 19).
- `duration`: 0.25 (line 20).

### Input, style and lifecycle

Events: onClick (line 281); mousedown (line 392); touchstart (line 393); change (line 418); pointerdown (line 419); scroll (line 507); resize (line 508).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
