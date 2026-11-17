# popover-form

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/popover-form.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/popover-form.tsx); SHA-256 `80911c92297152db07746662429121a5e7513f459734266d7e8b4e099a8f063d`; 333 lines.

Imports: `react`, `lucide-react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| open | boolean | False | 8 |
| setOpen | (open: boolean) => void | False | 9 |
| openChild | ReactNode | True | 10 |
| successChild | ReactNode | True | 11 |
| showSuccess | boolean | False | 12 |
| width | string | True | 13 |
| height | string | True | 14 |
| showCloseButton | boolean | True | 15 |
| title | string | False | 16 |
| loading | boolean | False | 119 |
| text | string | False | 120 |
| width | number \| string | True | 210 |
| height | number | True | 211 |
| width | number | True | 231 |
| height | number | True | 232 |

### Defaults and motion

- Default `width` = `"364px"` (line 25).
- Default `height` = `"192px"` (line 26).
- Default `title` = `"Feedback"` (line 27).
- Default `showCloseButton` = `false` (line 28).
- Default `text` = `"submit"` (line 117).
- Default `title` = `"Success"` (line 172).
- Default `description` = `"Thank you for your submission"` (line 173).
- Default `width` = `352` (line 207).
- Default `height` = `2` (line 208).
- Default `width` = `44` (line 228).
- Default `height` = `30` (line 229).
- `duration`: 0.4 (line 85).
- `bounce`: 0 (line 86).
- `duration`: 0.4 (line 97).
- `bounce`: 0 (line 98).
- `duration`: 0.3 (line 135).
- `bounce`: 0 (line 136).

### Input, style and lifecycle

Events: onClick (line 40); onClick (line 66); mousedown (line 162); touchstart (line 163).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
