# cover

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/cover/components/ui/cover.tsx

[Original source](https://ui.aceternity.com/registry/cover.json); SHA-256 `9b983f47f290ec34633bc7bd457193a4fa8582c62e4ca5555bcadb35930ec6c4`; 229 lines.

Imports: `react`, `motion/react`, `react`, `@/lib/utils`, `@/components/ui/sparkles`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | True | 12 |
| className | string | True | 13 |
| className | string | True | 156 |
| delay | number | True | 157 |
| duration | number | True | 158 |
| hovered | boolean | True | 159 |
| width | number | True | 160 |
| className | string | True | 217 |
| delay | number | True | 218 |

### Defaults and motion

- Default `width` = `600` (line 153).
- `duration`: 0.2 (line 51).
- `duration`: 10 (line 62).
- `ease`: "linear" (line 63).
- `duration`: 0.2 (line 115).
- `duration`: 0.2 (line 117).
- `duration`: 0.2 (line 122).
- `duration`: 0.2 (line 127).
- `duration`: 0.2 (line 130).
- `duration`: computed; inspect expression (line 197).
- `ease`: "linear" (line 198).
- `delay`: computed; inspect expression (line 200).

### Input, style and lifecycle

Events: onMouseEnter (line 38); onMouseLeave (line 39).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
