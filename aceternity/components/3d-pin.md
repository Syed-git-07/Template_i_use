# 3d-pin

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/3d-pin/components/ui/3d-pin.tsx

[Original source](https://ui.aceternity.com/registry/3d-pin.json); SHA-256 `3eab7bf90257ddf144e33021f759656aab51bf218ef7c1e486b0438763156dc7`; 167 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 14 |
| title | string | True | 15 |
| href | string | True | 16 |
| className | string | True | 17 |
| containerClassName | string | True | 18 |
| title | string | True | 66 |
| href | string | True | 67 |

### Defaults and motion

- `duration`: 6 (line 108).
- `delay`: 0 (line 110).
- `duration`: 6 (line 128).
- `delay`: 2 (line 130).
- `duration`: 6 (line 148).
- `delay`: 4 (line 150).

### Input, style and lifecycle

Events: onMouseEnter (line 37); onMouseLeave (line 38).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
