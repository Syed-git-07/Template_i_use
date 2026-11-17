# meteors

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/meteors/components/ui/meteors.tsx

[Original source](https://ui.aceternity.com/registry/meteors.json); SHA-256 `f5bacbd0e30396d56d0f14b08b48b33490095221f322a00ea68a6643c468eb92`; 45 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| number | number | True | 10 |
| className | string | True | 11 |

### Defaults and motion

- `duration`: 0.5 (line 18).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
