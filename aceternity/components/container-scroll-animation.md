# container-scroll-animation

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/container-scroll-animation/components/ui/container-scroll-animation.tsx

[Original source](https://ui.aceternity.com/registry/container-scroll-animation.json); SHA-256 `dfcc37dc475073f28ed42cf5292622af47071a7bc32f7970073ef82594db4165`; 96 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| titleComponent | string \| React.ReactNode | False | 9 |
| children | React.ReactNode | False | 10 |
| rotate | MotionValue<number> | False | 75 |
| scale | MotionValue<number> | False | 76 |
| translate | MotionValue<number> | False | 77 |
| children | React.ReactNode | False | 78 |

### Defaults and motion


### Input, style and lifecycle

Events: resize (line 23).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
