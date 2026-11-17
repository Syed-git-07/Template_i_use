# background-beams

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/background-beams/components/ui/background-beams.tsx

[Original source](https://ui.aceternity.com/registry/background-beams.json); SHA-256 `a6cb4847ec4af2602d523b34eb1d3fd991f1b47b803635b114fc8313199f3682`; 142 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 7 |

### Defaults and motion

- `duration`: computed; inspect expression (line 109).
- `ease`: "easeInOut" (line 110).
- `delay`: computed; inspect expression (line 112).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
