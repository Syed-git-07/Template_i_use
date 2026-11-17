# attachment

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/attachment.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/attachment.tsx); SHA-256 `2fd9ebf9bc2c158246e9d2f6e8a9c0d8646b89a814f9885e03716708a8a152cc`; 223 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/aria/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | "idle" \| "uploading" \| "processing" \| "error" \| "done" | True | 32 |
| render | (props: React.HTMLAttributes<HTMLElement>) => React.ReactNode | True | 168 |

### Defaults and motion

- Default `state` = `"done"` (line 26).
- Default `size` = `"default"` (line 27).
- Default `orientation` = `"horizontal"` (line 28).
- Default `variant` = `"icon"` (line 66).
- Default `size` = `"icon-xs"` (line 147).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/base/ui/attachment.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/attachment.tsx); SHA-256 `ac8f3001547012b930365a6fecb8bf0f346727eea339c093dc2f1e5c0e52ee21`; 210 lines.

Imports: `react`, `@base-ui/react/merge-props`, `@base-ui/react/use-render`, `class-variance-authority`, `cn`, `@/registry/bases/base/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | "idle" \| "uploading" \| "processing" \| "error" \| "done" | True | 34 |

### Defaults and motion

- Default `state` = `"done"` (line 28).
- Default `size` = `"default"` (line 29).
- Default `orientation` = `"horizontal"` (line 30).
- Default `variant` = `"icon"` (line 66).
- Default `size` = `"icon-xs"` (line 147).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/attachment.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/attachment.tsx); SHA-256 `d08c02488eac9d9ea8875e53ecdad19ce37703091cc9776828da14c6d77282eb`; 207 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`, `@/registry/bases/radix/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | "idle" \| "uploading" \| "processing" \| "error" \| "done" | True | 33 |
| asChild | boolean | True | 166 |

### Defaults and motion

- Default `state` = `"done"` (line 27).
- Default `size` = `"default"` (line 28).
- Default `orientation` = `"horizontal"` (line 29).
- Default `variant` = `"icon"` (line 65).
- Default `size` = `"icon-xs"` (line 146).
- Default `asChild` = `false` (line 162).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/attachment.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/attachment.tsx); SHA-256 `9f3ea5b662f13227e4918304a66d9de5c7e2e91f8dbd40c6916e6fc6ccc2c8a9`; 205 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`, `@/registry/new-york-v4/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | "idle" \| "uploading" \| "processing" \| "error" \| "done" | True | 34 |
| asChild | boolean | True | 167 |

### Defaults and motion

- Default `state` = `"done"` (line 28).
- Default `size` = `"default"` (line 29).
- Default `orientation` = `"horizontal"` (line 30).
- Default `variant` = `"icon"` (line 66).
- Default `size` = `"icon-xs"` (line 147).
- Default `asChild` = `false` (line 163).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
