# expandable-screen

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/expandable-screen.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/expandable-screen.tsx); SHA-256 `608cd529d3cca99e985650da29788e31b4fd07ec5ea292d1a5cffb5a425bbf15`; 226 lines.

Imports: `react`, `lucide-react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isExpanded | boolean | False | 15 |
| expand | () => void | False | 16 |
| collapse | () => void | False | 17 |
| layoutId | string | False | 18 |
| triggerRadius | string | False | 19 |
| contentRadius | string | False | 20 |
| animationDuration | number | False | 21 |
| children | ReactNode | False | 39 |
| defaultExpanded | boolean | True | 40 |
| onExpandChange | (expanded: boolean) => void | True | 41 |
| layoutId | string | True | 42 |
| triggerRadius | string | True | 43 |
| contentRadius | string | True | 44 |
| animationDuration | number | True | 45 |
| lockScroll | boolean | True | 46 |
| children | ReactNode | False | 100 |
| className | string | True | 101 |
| children | ReactNode | False | 143 |
| className | string | True | 144 |
| showCloseButton | boolean | True | 145 |
| closeButtonClassName | string | True | 146 |
| trigger | ReactNode | True | 202 |
| content | ReactNode | True | 203 |
| className | string | True | 204 |

### Defaults and motion

- Default `defaultExpanded` = `false` (line 51).
- Default `layoutId` = `"expandable-card"` (line 53).
- Default `triggerRadius` = `"100px"` (line 54).
- Default `contentRadius` = `"24px"` (line 55).
- Default `animationDuration` = `0.3` (line 56).
- Default `lockScroll` = `true` (line 57).
- Default `className` = `""` (line 106).
- Default `className` = `""` (line 151).
- Default `showCloseButton` = `true` (line 152).
- Default `closeButtonClassName` = `""` (line 153).
- Default `className` = `""` (line 210).
- `delay`: 0.2 (line 127).
- `duration`: computed; inspect expression (line 165).
- `delay`: 0.15 (line 175).
- `duration`: 0.4 (line 175).

### Input, style and lifecycle

Events: onClick (line 130); onClick (line 183).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
