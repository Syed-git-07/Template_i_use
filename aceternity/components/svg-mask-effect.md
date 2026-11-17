# svg-mask-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/svg-mask-effect/components/ui/svg-mask-effect.tsx

[Original source](https://ui.aceternity.com/registry/svg-mask-effect.json); SHA-256 `8ce6017e2f55eeb266ba459f7c5bb73f54678f9693a026fe2ec55bddbe902506`; 84 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | string \| React.ReactNode | True | 13 |
| revealText | string \| React.ReactNode | True | 14 |
| size | number | True | 15 |
| revealSize | number | True | 16 |
| className | string | True | 17 |

### Defaults and motion

- Default `size` = `10` (line 9).
- Default `revealSize` = `600` (line 10).
- `duration`: 0.3 (line 48).
- `duration`: 0.3 (line 60).
- `ease`: "easeInOut" (line 60).
- `duration`: 0.15 (line 61).
- `ease`: "linear" (line 61).

### Input, style and lifecycle

Events: mousemove (line 28); onMouseEnter (line 66); onMouseLeave (line 69).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
