# wobble-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/wobble-card/components/ui/wobble-card.tsx

[Original source](https://ui.aceternity.com/registry/wobble-card.json); SHA-256 `e044c7bc932752221b9e6c724cf304495a26376da27316c1a53fc0d207133516`; 79 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 11 |
| containerClassName | string | True | 12 |
| className | string | True | 13 |

### Defaults and motion


### Input, style and lifecycle

Events: onMouseMove (line 27); onMouseEnter (line 28); onMouseLeave (line 29).

Typography/style anchors: 37, 56.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
