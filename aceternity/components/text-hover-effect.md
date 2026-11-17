# text-hover-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/text-hover-effect/components/ui/text-hover-effect.tsx

[Original source](https://ui.aceternity.com/registry/text-hover-effect.json); SHA-256 `6921dc858bc64ac90e791720660ceac965df94986867e82d28a6eb2d8fe53518`; 135 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 9 |
| duration | number | True | 10 |
| automatic | boolean | True | 11 |

### Defaults and motion

- `duration`: computed; inspect expression (line 67).
- `ease`: "easeOut" (line 67).
- `duration`: 4 (line 114).
- `ease`: "easeInOut" (line 115).

### Input, style and lifecycle

Events: onMouseEnter (line 37); onMouseLeave (line 38); onMouseMove (line 39).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
