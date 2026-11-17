# halo-toggle-group

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-toggle-group.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-toggle-group.tsx); SHA-256 `b81c3268b9b056d949906a80612fccb333eee9ab1845f6ea0b73cc7c890c716e`; 225 lines.

Imports: `react`, `@base-ui/react/toggle`, `@base-ui/react/toggle-group`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string | False | 30 |
| label | ReactNode | False | 31 |
| disabled | boolean | True | 32 |
| items | HaloToggleGroupItem[] | False | 36 |
| value | string | True | 38 |
| defaultValue | string | True | 39 |
| onValueChange | (next: string) => void | True | 40 |
| className | string | True | 41 |
| translucent | boolean | True | 43 |
| disabled | boolean | True | 44 |

### Defaults and motion

- Default `translucent` = `true` (line 53).
- Default `disabled` = `false` (line 54).
- `bounce`: 0.12 (line 24).
- `damping`: 34 (line 25).
- `stiffness`: 420 (line 26).
- `duration`: 0.25 (line 121).
- `ease`: "easeOut" (line 121).
- `duration`: computed; inspect expression (line 131).
- `ease`: "easeInOut" (line 132).
- `duration`: computed; inspect expression (line 143).
- `ease`: "easeInOut" (line 144).
- `duration`: 0 (line 180).

### Input, style and lifecycle

Events: onValueChange (line 187).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
