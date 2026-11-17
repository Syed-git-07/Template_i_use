# timer

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/timer.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/timer.tsx); SHA-256 `a96f86d187f64f7467165c97b347150a9e7d637e75347d3deedae693ccc5c3db`; 359 lines.

Imports: `react`, `class-variance-authority`, `lucide-react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| loading | boolean | True | 71 |
| icon | React.ComponentType<{ className?: string }> | True | 77 |
| className | string | True | 77 |
| time | string | False | 83 |
| label | string | True | 85 |
| loading | boolean | True | 91 |
| onTick | (seconds: number, milliseconds: number) => void | True | 93 |
| resetOnLoadingChange | boolean | True | 95 |
| format | "SS.MS" \| "MM:SS" \| "HH:MM:SS" | True | 97 |
| elapsedTime | number | False | 102 |
| milliseconds | number | False | 104 |
| formattedTime | {     seconds: string     milliseconds: string     display: string   } | False | 106 |
| seconds | string | False | 107 |
| milliseconds | string | False | 108 |
| display | string | False | 109 |
| isRunning | boolean | False | 112 |
| reset | () => void | False | 114 |
| start | () => void | False | 116 |
| stop | () => void | False | 118 |
| format | "SS.MS" \| "MM:SS" \| "HH:MM:SS" | True | 182 |

### Defaults and motion

- Default `loading` = `false` (line 188).
- Default `resetOnLoadingChange` = `true` (line 190).
- Default `format` = `"SS.MS"` (line 191).
- Default `loading` = `false` (line 227).
- Default `resetOnLoadingChange` = `true` (line 229).
- Default `format` = `"SS.MS"` (line 230).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
