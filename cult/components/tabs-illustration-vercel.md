# tabs-illustration-vercel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/tabs-illustration-vercel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/tabs-illustration-vercel.tsx); SHA-256 `022d689f029176fbf05aa241dc1159ac033b204e21932f651811b29010aaefe9`; 904 lines.

Imports: `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 13 |
| title | string | False | 14 |
| description | string | False | 15 |
| badge | string | True | 16 |
| icon | ReactNode | False | 320 |
| children | ReactNode | False | 321 |
| active | boolean | False | 624 |
| title | string | False | 625 |
| badge | string | True | 626 |
| progress | number | False | 627 |
| onClick | () => void | False | 628 |
| title | string | True | 700 |
| features | Feature[] | True | 701 |

### Defaults and motion

- Default `size` = `16` (line 111).
- Default `size` = `16` (line 120).
- Default `size` = `16` (line 129).
- Default `title` = `"Generate anything"` (line 697).

### Input, style and lifecycle

Events: onClick (line 632); onClick (line 833).

Typography/style anchors: 432, 491, 554, 576, 596, 605, 650, 662, 676, 685, 780, 781, 785, 799, 842, 854, 892.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
