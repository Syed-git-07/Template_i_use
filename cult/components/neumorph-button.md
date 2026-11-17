# neumorph-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/neumorph-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/neumorph-button.tsx); SHA-256 `6b49023169dc273a9408fcd450c046c6ce2624836024a4b5b728126ff6c86a36`; 123 lines.

Imports: `react`, `class-variance-authority`, `lucide-react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 87 |
| loading | boolean | True | 88 |

### Defaults and motion

- Default `loading` = `false` (line 97).
- `stiffness`: 400 (line 107).
- `damping`: 10 (line 107).
- `duration`: 0.2 (line 114).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
