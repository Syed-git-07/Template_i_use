# direction-aware-tabs

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/direction-aware-tabs.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/direction-aware-tabs.tsx); SHA-256 `a801b7bed776690b2d0ab216f7a6551eb60a91d39c5574208f125d070bb85c17`; 138 lines.

Imports: `react`, `motion/react`, `react-use-measure`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | number | False | 10 |
| label | string | False | 11 |
| content | ReactNode | False | 12 |
| tabs | Tab[] | False | 16 |
| className | string | True | 17 |
| rounded | string | True | 19 |
| roundedInner | string | True | 21 |
| onChange | () => void | True | 22 |

### Defaults and motion

- `bounce`: 0.19 (line 98).
- `duration`: 0.4 (line 98).
- `duration`: 0.4 (line 106).
- `bounce`: 0.2 (line 106).

### Input, style and lifecycle

Events: onClick (line 81); onExitComplete (line 116); onAnimationStart (line 125); onAnimationComplete (line 126).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
