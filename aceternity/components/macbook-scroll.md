# macbook-scroll

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/macbook-scroll/components/ui/macbook-scroll.tsx

[Original source](https://ui.aceternity.com/registry/macbook-scroll.json); SHA-256 `49a5f5deef177892ca107052b8a3c07ed13731335c8a527cceaef5d976e08b99`; 656 lines.

Imports: `react`, `motion/react`, `@/lib/utils`, `@tabler/icons-react`, `@tabler/icons-react`, `@tabler/icons-react`, `@tabler/icons-react`, `@tabler/icons-react`, `@tabler/icons-react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| src | string | True | 34 |
| showGradient | boolean | True | 35 |
| title | string \| React.ReactNode | True | 36 |
| badge | React.ReactNode | True | 37 |
| scaleX | MotionValue<number> | False | 129 |
| scaleY | MotionValue<number> | False | 130 |
| rotate | MotionValue<number> | False | 131 |
| translate | MotionValue<number> | False | 132 |
| src | string | True | 133 |
| className | string | True | 553 |
| children | React.ReactNode | True | 554 |
| childrenClassName | string | True | 555 |
| backlit | boolean | True | 556 |
| className | string | False | 602 |

### Defaults and motion

- Default `backlit` = `true` (line 551).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
