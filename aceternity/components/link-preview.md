# link-preview

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/link-preview/components/ui/link-preview.tsx

[Original source](https://ui.aceternity.com/registry/link-preview.json); SHA-256 `c140609b59685342ed3b62bf7d5d90ac5ca099ed90fbb7cda1fe6c2dedd46475`; 152 lines.

Imports: `@radix-ui/react-hover-card`, `qss`, `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 16 |
| url | string | False | 17 |
| className | string | True | 18 |
| width | number | True | 19 |
| height | number | True | 20 |
| quality | number | True | 21 |
| layout | string | True | 22 |
| isStatic | true | False | 24 |
| imageSrc | string | False | 24 |
| isStatic | false | True | 25 |
| imageSrc | never | True | 25 |

### Defaults and motion

- Default `width` = `200` (line 32).
- Default `height` = `125` (line 33).
- Default `quality` = `50` (line 34).
- Default `layout` = `"fixed"` (line 35).
- Default `isStatic` = `false` (line 36).
- Default `imageSrc` = `""` (line 37).
- `stiffness`: 100 (line 65).
- `damping`: 15 (line 65).
- `stiffness`: 260 (line 121).
- `damping`: 20 (line 122).

### Input, style and lifecycle

Events: onOpenChange (line 93); onMouseMove (line 98).

Typography/style anchors: 119.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
