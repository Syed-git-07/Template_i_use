# text-flipping-board

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/text-flipping-board/components/ui/text-flipping-board.tsx

[Original source](https://ui.aceternity.com/registry/text-flipping-board.json); SHA-256 `f33799e3ab6e0a407d26330853131d3332cf2c882e8bd406a8c60e0c3574830f`; 441 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| top | string | False | 23 |
| bottom | string | False | 24 |
| text | string | False | 25 |
| target | string | False | 51 |
| delay | number | False | 52 |
| stepMs | number | False | 53 |
| flipDuration | number | False | 54 |
| color | string | False | 277 |
| type | "char" | False | 289 |
| value | string | False | 289 |
| type | "color" | False | 290 |
| hex | string | False | 290 |
| rows | string[] | True | 352 |
| text | string | True | 353 |
| className | string | True | 354 |
| duration | number | True | 356 |

### Defaults and motion

- `duration`: computed; inspect expression (line 180).
- `ease`: "easeOut" (line 180).
- `duration`: computed; inspect expression (line 196).
- `ease`: computed; inspect expression (line 197).
- `duration`: computed; inspect expression (line 210).
- `duration`: computed; inspect expression (line 226).
- `delay`: computed; inspect expression (line 227).
- `ease`: computed; inspect expression (line 228).
- `duration`: computed; inspect expression (line 242).
- `delay`: computed; inspect expression (line 243).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
