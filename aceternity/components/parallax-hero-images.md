# parallax-hero-images

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/parallax-hero-images/components/ui/parallax-hero-images.tsx

[Original source](https://ui.aceternity.com/registry/parallax-hero-images.json); SHA-256 `b93bea939241620dbec43ad61d78e3928c309e1934c500e3689c67a19287ce11`; 189 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| src | string | False | 13 |
| position | \| "top-left"     \| "top-right"     \| "mid-left"     \| "mid-right"     \| "bottom-left"     \| "bottom-right"     \| "far-left"     \| "far-right" | False | 14 |
| depth | number | False | 23 |
| delay | number | False | 24 |
| top | string | False | 29 |
| left | string | True | 29 |
| right | string | True | 29 |
| images | string[] | False | 62 |
| className | string | True | 63 |
| imageClassName | string | True | 64 |
| variant | DepthVariant | True | 65 |
| imageClassName | string | True | 127 |
| smoothMouseX | MotionValue<number> | False | 128 |
| smoothMouseY | MotionValue<number> | False | 129 |

### Defaults and motion

- Default `variant` = `"default"` (line 72).
- `damping`: 25 (line 59).
- `stiffness`: 120 (line 59).
- `delay`: computed; inspect expression (line 87).
- `duration`: 0.8 (line 171).
- `delay`: computed; inspect expression (line 172).
- `ease`: computed; inspect expression (line 173).

### Input, style and lifecycle

Events: mousemove (line 99).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
