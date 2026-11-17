# images-badge

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/images-badge/components/ui/images-badge.tsx

[Original source](https://ui.aceternity.com/registry/images-badge.json); SHA-256 `fff13566e4ab29c761de8fb4cee8dba311ce7a3a28ddfb80b217d84f7a3d4973`; 178 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 8 |
| images | string[] | False | 9 |
| className | string | True | 10 |
| href | string | True | 12 |
| target | string | True | 14 |
| folderSize | { width: number; height: number } | True | 16 |
| width | number | False | 16 |
| height | number | False | 16 |
| teaserImageSize | { width: number; height: number } | True | 18 |
| width | number | False | 18 |
| height | number | False | 18 |
| hoverImageSize | { width: number; height: number } | True | 20 |
| width | number | False | 20 |
| height | number | False | 20 |
| hoverTranslateY | number | True | 22 |
| hoverSpread | number | True | 24 |
| hoverRotation | number | True | 26 |

### Defaults and motion

- Default `hoverTranslateY` = `-35` (line 38).
- Default `hoverSpread` = `20` (line 39).
- Default `hoverRotation` = `15` (line 40).
- `stiffness`: 400 (line 132).
- `damping`: 25 (line 133).
- `delay`: computed; inspect expression (line 134).
- `stiffness`: 400 (line 158).
- `damping`: 25 (line 159).

### Input, style and lifecycle

Events: onMouseEnter (line 62); onMouseLeave (line 63).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
