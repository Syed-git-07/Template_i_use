# glowing-stars

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/glowing-stars/components/ui/glowing-stars.tsx

[Original source](https://ui.aceternity.com/registry/glowing-stars.json); SHA-256 `e69fe3e5d991a7ba96544db11afd92b8363526f4fa4f9b73f21c5fb527a938c5`; 159 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 11 |
| children | React.ReactNode | True | 12 |
| className | string | True | 41 |
| children | React.ReactNode | True | 42 |
| className | string | True | 55 |
| children | React.ReactNode | True | 56 |
| mouseEnter | boolean | False | 65 |
| isGlowing | boolean | False | 117 |
| delay | number | False | 117 |
| delay | number | False | 138 |

### Defaults and motion

- `duration`: 2 (line 129).
- `ease`: "easeInOut" (line 130).
- `delay`: computed; inspect expression (line 131).
- `duration`: 2 (line 148).
- `ease`: "easeInOut" (line 149).
- `delay`: computed; inspect expression (line 150).

### Input, style and lifecycle

Events: onMouseEnter (line 18); onMouseLeave (line 21).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
