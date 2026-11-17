# lamp

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/lamp/components/ui/lamp.tsx

[Original source](https://ui.aceternity.com/registry/lamp.json); SHA-256 `dfbfe0609b4a9e48912ce44601e77a478b7b7b145de34a0163e124de4e86862f`; 105 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 29 |
| className | string | True | 30 |

### Defaults and motion

- `delay`: 0.3 (line 13).
- `duration`: 0.8 (line 14).
- `ease`: "easeInOut" (line 15).
- `delay`: 0.3 (line 44).
- `duration`: 0.8 (line 45).
- `ease`: "easeInOut" (line 46).
- `delay`: 0.3 (line 60).
- `duration`: 0.8 (line 61).
- `ease`: "easeInOut" (line 62).
- `delay`: 0.3 (line 79).
- `duration`: 0.8 (line 80).
- `ease`: "easeInOut" (line 81).
- `delay`: 0.3 (line 89).
- `duration`: 0.8 (line 90).
- `ease`: "easeInOut" (line 91).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
