# collab-avatar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/collab-avatar.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/collab-avatar.tsx); SHA-256 `8c7aa94dfde31bfdf9b292acdb9c018a0e98a3edabb15240066d4c603e9691d2`; 90 lines.

Imports: `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 31 |
| color | string | False | 32 |
| size | number | True | 33 |
| className | string | True | 34 |

### Defaults and motion

- Default `size` = `24` (line 28).
- `duration`: 0 (line 55).
- `duration`: 0.22 (line 55).
- `ease`: computed; inspect expression (line 55).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
