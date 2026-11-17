# toggle-group

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/toggle-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/toggle-group.tsx); SHA-256 `c0bd5f64f083c43a0003e0f827c96d36624302cbeabe3e43474e7f3f3129976a`; 97 lines.

Imports: `react`, `class-variance-authority`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/toggle`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| spacing | number | True | 17 |
| orientation | "horizontal" \| "vertical" | True | 18 |
| spacing | number | True | 37 |
| orientation | "horizontal" \| "vertical" | True | 38 |
| children | React.ReactNode | True | 39 |

### Defaults and motion

- Default `spacing` = `2` (line 31).
- Default `orientation` = `"horizontal"` (line 32).
- Default `variant` = `"default"` (line 69).
- Default `size` = `"default"` (line 70).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/toggle-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/toggle-group.tsx); SHA-256 `58edf607bd626509d41af506a0fdd48b43ed7c5d43ccca52e6d6fff73d0947ae`; 90 lines.

Imports: `react`, `@base-ui/react/toggle`, `@base-ui/react/toggle-group`, `class-variance-authority`, `cn`, `@/registry/bases/base/ui/toggle`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| spacing | number | True | 13 |
| orientation | "horizontal" \| "vertical" | True | 14 |
| spacing | number | True | 33 |
| orientation | "horizontal" \| "vertical" | True | 34 |

### Defaults and motion

- Default `spacing` = `2` (line 27).
- Default `orientation` = `"horizontal"` (line 28).
- Default `variant` = `"default"` (line 62).
- Default `size` = `"default"` (line 63).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/toggle-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/toggle-group.tsx); SHA-256 `0f2265dbfe0d8e647b691c088060df9b28b779b344d23f752502e89e5614ea44`; 90 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`, `@/registry/bases/radix/ui/toggle`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| spacing | number | True | 12 |
| orientation | "horizontal" \| "vertical" | True | 13 |
| spacing | number | True | 32 |
| orientation | "horizontal" \| "vertical" | True | 33 |

### Defaults and motion

- Default `spacing` = `2` (line 26).
- Default `orientation` = `"horizontal"` (line 27).
- Default `variant` = `"default"` (line 61).
- Default `size` = `"default"` (line 62).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/toggle-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/toggle-group.tsx); SHA-256 `ec2ad9b6f11d6e1b523f50fd6993da83947c633733d04faa21fa37b45438b0f8`; 84 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`, `@/registry/new-york-v4/ui/toggle`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| spacing | number | True | 12 |
| spacing | number | True | 29 |

### Defaults and motion

- Default `spacing` = `0` (line 24).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
