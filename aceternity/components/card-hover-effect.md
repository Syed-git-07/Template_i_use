# card-hover-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/card-hover-effect/components/ui/card-hover-effect.tsx

[Original source](https://ui.aceternity.com/registry/card-hover-effect.json); SHA-256 `af736705935d3cda78f5ec03d23c808ed52e881902f0d03180b194a9cf67c309`; 112 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| items | {     title: string;     description: string;     link: string;   }[] | False | 10 |
| title | string | False | 11 |
| description | string | False | 12 |
| link | string | False | 13 |
| className | string | True | 15 |
| className | string | True | 65 |
| children | React.ReactNode | False | 66 |
| className | string | True | 85 |
| children | React.ReactNode | False | 86 |
| className | string | True | 98 |
| children | React.ReactNode | False | 99 |

### Defaults and motion

- `duration`: 0.15 (line 42).
- `duration`: 0.15 (line 46).
- `delay`: 0.2 (line 46).

### Input, style and lifecycle

Events: onMouseEnter (line 31); onMouseLeave (line 32).

Typography/style anchors: 42, 46.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
