# following-pointer

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/following-pointer/components/ui/following-pointer.tsx

[Original source](https://ui.aceternity.com/registry/following-pointer.json); SHA-256 `ea4c418b3f3dbfc85be0f4ae6d0624b36a3c46aba1207515a8f7287198727dac`; 137 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 11 |
| className | string | True | 12 |
| title | string \| React.ReactNode | True | 13 |
| x | any | False | 66 |
| y | any | False | 67 |
| title | string \| React.ReactNode | True | 68 |

### Defaults and motion


### Input, style and lifecycle

Events: onMouseLeave (line 44); onMouseEnter (line 45); onMouseMove (line 46).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
