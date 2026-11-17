# animated-group

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/animated-group.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/animated-group.tsx); SHA-256 `d2580c93743511784cda57fa945d3197121158a60970677fd837c2fab2113bfe`; 144 lines.

Imports: `react`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | ReactNode | False | 19 |
| className | string | True | 20 |
| variants | {     container?: Variants;     item?: Variants;   } | True | 21 |
| container | Variants | True | 22 |
| item | Variants | True | 23 |
| preset | PresetType | True | 25 |
| as | React.ElementType | True | 26 |
| asChild | React.ElementType | True | 27 |

### Defaults and motion

- Default `as` = `"div"` (line 108).
- Default `asChild` = `"div"` (line 109).
- `stiffness`: 300 (line 65).
- `damping`: 20 (line 65).
- `stiffness`: 300 (line 72).
- `damping`: 20 (line 72).
- `bounce`: computed; inspect expression (line 75).
- `stiffness`: 400 (line 79).
- `damping`: 10 (line 79).
- `stiffness`: 200 (line 86).
- `damping`: 15 (line 86).
- `stiffness`: 300 (line 93).
- `damping`: 8 (line 93).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 32, 65, 72, 79, 86, 93.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
