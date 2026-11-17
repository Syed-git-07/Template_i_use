# moving-border

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/moving-border/components/ui/moving-border.tsx

[Original source](https://ui.aceternity.com/registry/moving-border.json); SHA-256 `b1cf4ffc66cc3c220383fb0904d7505265bf65ebfbec2e714763114599ea8b25`; 140 lines.

Imports: `react`, `motion/react`, `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| borderRadius | string | True | 23 |
| children | React.ReactNode | False | 24 |
| as | any | True | 25 |
| containerClassName | string | True | 26 |
| borderClassName | string | True | 27 |
| duration | number | True | 28 |
| className | string | True | 29 |
| children | React.ReactNode | False | 79 |
| duration | number | True | 80 |
| rx | string | True | 81 |
| ry | string | True | 82 |

### Defaults and motion

- Default `borderRadius` = `"1.75rem"` (line 14).
- Default `Component` = `"button"` (line 16).
- Default `duration` = `3000` (line 74).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
