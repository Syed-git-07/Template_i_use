# tooltip-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/tooltip-card/components/ui/tooltip-card.tsx

[Original source](https://ui.aceternity.com/registry/tooltip-card.json); SHA-256 `aa43fee7024ea59de28e9a4ae5bf704e99b39109e478426f7fa116f6748334db`; 189 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| content | string \| React.ReactNode | False | 11 |
| children | React.ReactNode | False | 12 |
| containerClassName | string | True | 13 |
| x | number | False | 16 |
| y | number | False | 16 |
| x | number | False | 18 |
| y | number | False | 18 |

### Defaults and motion

- `stiffness`: 200 (line 168).
- `damping`: 20 (line 169).

### Input, style and lifecycle

Events: onMouseEnter (line 151); onMouseLeave (line 152); onMouseMove (line 153); onTouchStart (line 154); onTouchEnd (line 155); onClick (line 156).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
