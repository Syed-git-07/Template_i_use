# collab-toolbar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/collab-toolbar.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/collab-toolbar.tsx); SHA-256 `a97534e45ceb647b83baa33f45b195bae783da786a2e7846b9b74ae4c7f613cb`; 290 lines.

Imports: `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 181 |
| color | string | True | 182 |
| imageUrl | string | True | 183 |
| name | string | False | 191 |
| size | number | True | 192 |
| imageUrl | string | True | 193 |
| icon | IconKey | False | 216 |
| groups | ToolbarGroup[] | False | 242 |
| avatars | Collaborator[] | True | 243 |

### Defaults and motion

- Default `size` = `24` (line 188).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 250.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
