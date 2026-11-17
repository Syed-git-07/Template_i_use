# squiggly-text

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/squiggly-text/components/ui/squiggly-text.tsx

[Original source](https://ui.aceternity.com/registry/squiggly-text.json); SHA-256 `7e99133897d9970938a95d3b27966dd1c4dc714519e118c878895de8ed40f783`; 117 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 11 |
| className | string | True | 12 |
| style | React.CSSProperties | True | 13 |
| steps | number | True | 19 |
| stepDuration | number | True | 25 |
| scale | number \| [number, number] | True | 32 |
| baseFrequency | number | True | 38 |
| numOctaves | number | True | 43 |
| as | "span" \| "div" | True | 48 |

### Defaults and motion

- Default `steps` = `5` (line 53).
- Default `stepDuration` = `80` (line 54).
- Default `baseFrequency` = `0.02` (line 56).
- Default `numOctaves` = `3` (line 57).
- Default `as` = `"span"` (line 58).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
