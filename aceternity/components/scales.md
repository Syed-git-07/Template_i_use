# scales

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/scales/components/ui/scales.tsx

[Original source](https://ui.aceternity.com/registry/scales.json); SHA-256 `0bc985c6bb477a5fda766bbe8747bbe6149aeb0409e7d507ac7bbe95c24ea691`; 82 lines.

Imports: `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| orientation | "horizontal" \| "vertical" \| "diagonal" | True | 5 |
| size | number | True | 6 |
| className | string | True | 7 |
| color | string | True | 8 |
| children | React.ReactNode | True | 56 |
| containerClassName | string | True | 57 |

### Defaults and motion

- Default `orientation` = `"diagonal"` (line 12).
- Default `size` = `10` (line 13).
- Default `orientation` = `"diagonal"` (line 62).
- Default `size` = `10` (line 63).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
