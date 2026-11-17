# badge

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/badge.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/badge.tsx); SHA-256 `13a950da87c8e29bb08a17855a765d0712207ea93dfeae8d516ae737266dfd2c`; 54 lines.

Imports: `class-variance-authority`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| render | (props: React.HTMLAttributes<HTMLElement>) => React.ReactNode | True | 30 |

### Defaults and motion

- Default `variant` = `"default"` (line 25).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/badge.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/badge.tsx); SHA-256 `f044c63ca01f16d90c434c22bea61c3cb5946cfa281fea6d3ae3c9238182d0d7`; 48 lines.

Imports: `@base-ui/react/merge-props`, `@base-ui/react/use-render`, `class-variance-authority`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `variant` = `"default"` (line 27).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/badge.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/badge.tsx); SHA-256 `4723890747d894cde4d93074b40dc0fdf57dc15a289b2bcc4f5bdb4a78ef43ef`; 45 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 31 |

### Defaults and motion

- Default `variant` = `"default"` (line 27).
- Default `asChild` = `false` (line 28).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/new-york-v4/ui/badge.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/badge.tsx); SHA-256 `0cff0b6678e979f66c0d3f6a67ed01bf1692bafc312c27689bbe2c45b7c1ecb6`; 48 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 34 |

### Defaults and motion

- Default `variant` = `"default"` (line 30).
- Default `asChild` = `false` (line 31).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
