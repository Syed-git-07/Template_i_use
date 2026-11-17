# infinite-moving-cards

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/infinite-moving-cards/components/ui/infinite-moving-cards.tsx

[Original source](https://ui.aceternity.com/registry/infinite-moving-cards.json); SHA-256 `428312dab8233d627625e1b27d34709ac603a5d13fa12bcb0928a801d11031fc`; 118 lines.

Imports: `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| items | {     quote: string;     name: string;     title: string;   }[] | False | 13 |
| quote | string | False | 14 |
| name | string | False | 15 |
| title | string | False | 16 |
| direction | "left" \| "right" | True | 18 |
| speed | "fast" \| "normal" \| "slow" | True | 19 |
| pauseOnHover | boolean | True | 20 |
| className | string | True | 21 |

### Defaults and motion

- Default `direction` = `"left"` (line 8).
- Default `speed` = `"fast"` (line 9).
- Default `pauseOnHover` = `true` (line 10).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
