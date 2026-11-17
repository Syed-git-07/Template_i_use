# organic-card-small

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/organic-card-small.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/organic-card-small.tsx); SHA-256 `bb7f9857f95e0925e9a9bb2d7452d576b1417ef37c16f89db89793b0e92cfe7e`; 167 lines.

Imports: `react`, `next/image`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| image | string | False | 24 |
| imageAlt | string | True | 25 |
| category | string | False | 26 |
| date | string | False | 27 |
| title | string | False | 28 |
| href | string | True | 29 |
| className | string | True | 30 |
| surfaceColor | string | True | 32 |

### Defaults and motion

- Default `imageAlt` = `"Card image"` (line 37).
- Default `href` = `"#"` (line 41).
- `duration`: 0.12 (line 53).
- `ease`: computed; inspect expression (line 53).
- `duration`: 0.38 (line 54).
- `bounce`: 0 (line 54).
- `duration`: 0.28 (line 71).
- `bounce`: 0 (line 71).
- `duration`: 0.12 (line 153).
- `duration`: 0.32 (line 154).
- `bounce`: 0 (line 154).

### Input, style and lifecycle

Events: onBlur (line 67); onFocus (line 68); onMouseEnter (line 69); onMouseLeave (line 70).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
