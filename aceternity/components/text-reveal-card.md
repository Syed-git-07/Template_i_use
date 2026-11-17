# text-reveal-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/text-reveal-card/components/ui/text-reveal-card.tsx

[Original source](https://ui.aceternity.com/registry/text-reveal-card.json); SHA-256 `70db36b2988130c58486954b533147055cd6a6d2c022d0d341c2fb5a8f9266e2`; 188 lines.

Imports: `react`, `motion/react`, `tailwind-merge`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 13 |
| revealText | string | False | 14 |
| children | React.ReactNode | True | 15 |
| className | string | True | 16 |
| children | React.ReactNode | False | 128 |
| className | string | True | 129 |
| children | React.ReactNode | False | 142 |
| className | string | True | 143 |

### Defaults and motion

- `duration`: 0 (line 91).
- `duration`: 0.4 (line 91).
- `duration`: 0 (line 109).
- `duration`: 0.4 (line 109).
- `duration`: computed; inspect expression (line 166).
- `ease`: "linear" (line 168).

### Input, style and lifecycle

Events: onMouseEnter (line 62); onMouseLeave (line 63); onMouseMove (line 64); onTouchStart (line 65); onTouchEnd (line 66); onTouchMove (line 67).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
