# sticky-banner

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/sticky-banner/components/ui/sticky-banner.tsx

[Original source](https://ui.aceternity.com/registry/sticky-banner.json); SHA-256 `9708595c9af677b09f9260d0b0be5d1a11a5a6108269ceecdfa5d07e5348bb70`; 84 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 11 |
| children | React.ReactNode | False | 12 |
| hideOnScroll | boolean | True | 13 |

### Defaults and motion

- Default `hideOnScroll` = `false` (line 9).
- `duration`: 0.3 (line 42).
- `ease`: "easeInOut" (line 43).

### Input, style and lifecycle

Events: onClick (line 56).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
