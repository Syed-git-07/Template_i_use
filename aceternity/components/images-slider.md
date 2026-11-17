# images-slider

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/images-slider/components/ui/images-slider.tsx

[Original source](https://ui.aceternity.com/registry/images-slider.json); SHA-256 `dbc41d3dee94c121daaf44c2c58e4578d125c95f040e4fd7a8f6518b9ca64a9a`; 152 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| images | string[] | False | 15 |
| children | React.ReactNode | False | 16 |
| overlay | React.ReactNode | True | 17 |
| overlayClassName | string | True | 18 |
| className | string | True | 19 |
| autoplay | boolean | True | 20 |
| direction | "up" \| "down" | True | 21 |

### Defaults and motion

- Default `overlay` = `true` (line 9).
- Default `autoplay` = `true` (line 12).
- Default `direction` = `"up"` (line 13).
- `duration`: 0.5 (line 97).
- `ease`: computed; inspect expression (line 98).
- `duration`: 1 (line 105).
- `duration`: 1 (line 112).

### Input, style and lifecycle

Events: keydown (line 70).

Typography/style anchors: 96, 104, 111.

Source signals: keyboard, cleanup, async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
