# code-block

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/code-block.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/code-block.tsx); SHA-256 `7490b596a49d461b7af7ff56754a77bd4d7b91eed07f541e604e9329170fec18`; 258 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/aria/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "default" \| "sm" | True | 31 |
| value | string | False | 92 |
| wrap | boolean | True | 156 |
| lineNumbers | boolean | True | 157 |
| startLine | number | True | 158 |

### Defaults and motion

- Default `variant` = `"default"` (line 27).
- Default `size` = `"default"` (line 28).
- Default `variant` = `"ghost"` (line 87).
- Default `size` = `"icon-xs"` (line 88).
- Default `wrap` = `false` (line 151).
- Default `lineNumbers` = `false` (line 152).
- Default `startLine` = `1` (line 153).
- Default `variant` = `"default"` (line 210).

### Input, style and lifecycle

Events: onPress (line 113).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/code-block.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/code-block.tsx); SHA-256 `2e75d0138b76b7cb38253f0794bcc7632b495ebac55ad4b9d35d1fb0c4e84e10`; 258 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/base/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "default" \| "sm" | True | 31 |
| value | string | False | 92 |
| wrap | boolean | True | 156 |
| lineNumbers | boolean | True | 157 |
| startLine | number | True | 158 |

### Defaults and motion

- Default `variant` = `"default"` (line 27).
- Default `size` = `"default"` (line 28).
- Default `variant` = `"ghost"` (line 87).
- Default `size` = `"icon-xs"` (line 88).
- Default `wrap` = `false` (line 151).
- Default `lineNumbers` = `false` (line 152).
- Default `startLine` = `1` (line 153).
- Default `variant` = `"default"` (line 210).

### Input, style and lifecycle

Events: onClick (line 113).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/code-block.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/code-block.tsx); SHA-256 `0e3cae0ca6b9e287ad4b56a3b3d878639a70caebb5035865a785b93a20d23e15`; 258 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/radix/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "default" \| "sm" | True | 31 |
| value | string | False | 92 |
| wrap | boolean | True | 156 |
| lineNumbers | boolean | True | 157 |
| startLine | number | True | 158 |

### Defaults and motion

- Default `variant` = `"default"` (line 27).
- Default `size` = `"default"` (line 28).
- Default `variant` = `"ghost"` (line 87).
- Default `size` = `"icon-xs"` (line 88).
- Default `wrap` = `false` (line 151).
- Default `lineNumbers` = `false` (line 152).
- Default `startLine` = `1` (line 153).
- Default `variant` = `"default"` (line 210).

### Input, style and lifecycle

Events: onClick (line 113).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
