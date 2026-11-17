# gooey-input

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/gooey-input/components/ui/gooey-input.tsx

[Original source](https://ui.aceternity.com/registry/gooey-input.json); SHA-256 `4e1a126cb6b621e911c99f0fafac2efc213d16802d145ed5f71cfa84131409e2`; 263 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| filterId | string | False | 19 |
| blur | number | False | 20 |
| layoutId | string | False | 40 |
| root | string | True | 71 |
| filterWrap | string | True | 72 |
| buttonRow | string | True | 73 |
| trigger | string | True | 74 |
| input | string | True | 75 |
| bubble | string | True | 76 |
| bubbleSurface | string | True | 77 |
| placeholder | string | True | 81 |
| className | string | True | 82 |
| classNames | GooeyInputClassNames | True | 83 |
| collapsedWidth | number | True | 85 |
| expandedWidth | number | True | 87 |
| expandedOffset | number | True | 89 |
| gooeyBlur | number | True | 91 |
| value | string | True | 92 |
| defaultValue | string | True | 93 |
| onValueChange | (value: string) => void | True | 94 |
| onOpenChange | (open: boolean) => void | True | 95 |
| disabled | boolean | True | 96 |

### Defaults and motion

- Default `placeholder` = `"Type to search..."` (line 100).
- Default `collapsedWidth` = `115` (line 103).
- Default `expandedWidth` = `200` (line 104).
- Default `expandedOffset` = `50` (line 105).
- Default `gooeyBlur` = `5` (line 106).
- Default `defaultValue` = `""` (line 108).
- Default `disabled` = `false` (line 111).
- `duration`: 0.4 (line 60).
- `bounce`: 0.25 (line 62).

### Input, style and lifecycle

Events: onClick (line 207); onChange (line 224); onBlur (line 225).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
