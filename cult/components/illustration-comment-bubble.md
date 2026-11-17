# illustration-comment-bubble

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/illustration-comment-bubble.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/illustration-comment-bubble.tsx); SHA-256 `95424f8ffd3cf5bf4de73fe8e13bb45f3b7ac00380e878775f241b5eec8f915a`; 233 lines.

Imports:

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 87 |
| color | string | False | 88 |
| size | number | True | 89 |
| children | React.ReactNode | False | 123 |
| user | string | False | 149 |
| color | string | False | 150 |
| deviceIcons | IconKey[] | True | 151 |
| children | React.ReactNode | False | 152 |
| cursor | React.ReactNode | True | 153 |

### Defaults and motion

- Default `size` = `24` (line 85).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 129, 133, 167, 186.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
