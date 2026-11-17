# texture-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/texture-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/texture-button.tsx); SHA-256 `e1e7a7b4dc5c365ec2c21cd11f36dd6220e1ddf8666cf6d6340699ced2a76bc2`; 114 lines.

Imports: `react`, `@radix-ui/react-slot`, `class-variance-authority`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | \| "primary"     \| "secondary"     \| "accent"     \| "destructive"     \| "minimal"     \| "icon" | True | 70 |
| size | "default" \| "sm" \| "lg" \| "icon" | True | 77 |
| asChild | boolean | True | 78 |

### Defaults and motion

- Default `variant` = `"primary"` (line 85).
- Default `size` = `"default"` (line 86).
- Default `asChild` = `false` (line 87).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
