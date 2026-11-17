# card-stack

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/card-stack/components/ui/card-stack.tsx

[Original source](https://ui.aceternity.com/registry/card-stack.json); SHA-256 `7d38e4667f81ccef7e641d0ebf492f7ec5b4f3d9d154e04c9bf00a413320df9e`; 75 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | number | False | 8 |
| name | string | False | 9 |
| designation | string | False | 10 |
| content | React.ReactNode | False | 11 |
| items | Card[] | False | 19 |
| offset | number | True | 20 |
| scaleFactor | number | True | 21 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
