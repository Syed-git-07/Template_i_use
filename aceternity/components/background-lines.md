# background-lines

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/background-lines/components/ui/background-lines.tsx

[Original source](https://ui.aceternity.com/registry/background-lines.json); SHA-256 `72c900efcb60886d5824649bc129106d9bc36e645ca418aca771a7d9fe4d3a96`; 148 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 11 |
| className | string | True | 12 |
| svgOptions | {     duration?: number;   } | True | 13 |
| duration | number | True | 14 |
| svgOptions | {     duration?: number;   } | True | 42 |
| duration | number | True | 43 |

### Defaults and motion

- `duration`: 1 (line 100).
- `duration`: computed; inspect expression (line 113).
- `ease`: "linear" (line 114).
- `delay`: computed; inspect expression (line 117).
- `duration`: computed; inspect expression (line 135).
- `ease`: "linear" (line 136).
- `delay`: computed; inspect expression (line 139).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
