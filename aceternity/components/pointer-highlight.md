# pointer-highlight

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/pointer-highlight/components/ui/pointer-highlight.tsx

[Original source](https://ui.aceternity.com/registry/pointer-highlight.json); SHA-256 `e32a56b7eeb6dc4bfe8c05bc7c025310f26ab3d43aba6bbb22813b1a47960dc0`; 120 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 12 |
| rectangleClassName | string | True | 13 |
| pointerClassName | string | True | 14 |
| containerClassName | string | True | 15 |

### Defaults and motion

- `duration`: 0.5 (line 55).
- `ease`: "easeOut" (line 55).
- `duration`: 1 (line 71).
- `ease`: "easeInOut" (line 72).
- `duration`: 0.1 (line 87).
- `ease`: "easeInOut" (line 87).
- `duration`: 1 (line 88).
- `ease`: "easeInOut" (line 89).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: resize.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
