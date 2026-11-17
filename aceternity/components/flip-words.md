# flip-words

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/flip-words/components/ui/flip-words.tsx

[Original source](https://ui.aceternity.com/registry/flip-words.json); SHA-256 `5fccf682bd6e999104a2d52fcec126c5f1acc8097b4eab4e874d01ff93bfa635`; 99 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| words | string[] | False | 11 |
| duration | number | True | 12 |
| className | string | True | 13 |

### Defaults and motion

- Default `duration` = `3000` (line 8).
- `stiffness`: 100 (line 49).
- `damping`: 10 (line 50).
- `delay`: computed; inspect expression (line 73).
- `duration`: 0.3 (line 74).
- `delay`: computed; inspect expression (line 84).
- `duration`: 0.2 (line 85).

### Input, style and lifecycle

Events: onExitComplete (line 34).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
