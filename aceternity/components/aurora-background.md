# aurora-background

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/aurora-background/components/ui/aurora-background.tsx

[Original source](https://ui.aceternity.com/registry/aurora-background.json); SHA-256 `6b40cb23961819bb3619e61cbf971990c797133a29e767814fb5d578d1d83f3c`; 62 lines.

Imports: `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | ReactNode | False | 6 |
| showRadialGradient | boolean | True | 7 |

### Defaults and motion

- Default `showRadialGradient` = `true` (line 13).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
