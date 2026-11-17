# code-block

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/code-block.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/code-block.tsx); SHA-256 `f3b11899b8d7db3ff6e9c670867df4e0b7e388ed1982e39727a40b76b8349d10`; 297 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| label | string | False | 10 |
| code | string | False | 11 |
| language | string | True | 12 |
| tabs | CodeTab[] | True | 16 |
| code | string | True | 17 |
| language | string | True | 18 |
| className | string | True | 19 |
| left | number | False | 36 |
| width | number | False | 37 |

### Defaults and motion

- Default `language` = `"bash"` (line 25).
- `stiffness`: 500 (line 184).
- `damping`: 35 (line 185).
- `duration`: 0.2 (line 222).
- `duration`: 0.2 (line 234).
- `duration`: 0.15 (line 284).
- `ease`: "easeOut" (line 285).

### Input, style and lifecycle

Events: onClick (line 158); onClick (line 198).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: async, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
