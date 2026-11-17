# context-menu

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/context-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/context-menu.tsx); SHA-256 `4a17a25445cf7f8e72d4e34396e36330356b63ca85902bcf0b2b5011552753db`; 268 lines.

Imports: `react`, `class-variance-authority`, `cn`, `react-aria-components`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| "data-slot" | string | True | 38 |
| className | string | True | 39 |
| children | React.ReactNode | True | 40 |
| children | React.ReactNode | True | 78 |
| inset | boolean | True | 88 |
| inset | boolean | True | 120 |
| variant | "default" \| "destructive" | True | 121 |
| inset | boolean | True | 178 |

### Defaults and motion

- Default `dataSlot` = `"context-menu-content"` (line 23).
- Default `placement` = `"bottom start"` (line 24).
- Default `offset` = `4` (line 25).
- Default `crossOffset` = `0` (line 26).
- Default `variant` = `"default"` (line 116).
- Default `placement` = `"end top"` (line 209).
- Default `crossOffset` = `-3` (line 210).
- Default `offset` = `0` (line 211).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/context-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/context-menu.tsx); SHA-256 `eb887aca2a6a9134d07b77ad0be6eb698701f520a72caca14e3bfc1996ed5c9c`; 286 lines.

Imports: `react`, `@base-ui/react/context-menu`, `cn`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inset | boolean | True | 77 |
| inset | boolean | True | 95 |
| variant | "default" \| "destructive" | True | 96 |
| inset | boolean | True | 124 |
| inset | boolean | True | 169 |
| inset | boolean | True | 215 |

### Defaults and motion

- Default `align` = `"start"` (line 34).
- Default `alignOffset` = `4` (line 35).
- Default `side` = `"right"` (line 36).
- Default `sideOffset` = `0` (line 37).
- Default `variant` = `"default"` (line 92).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/context-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/context-menu.tsx); SHA-256 `e54b4f887a9b2a5dd8b01d7f5ee62e5b541e0f55a20a282451e268f1e2578a24`; 281 lines.

Imports: `react`, `cn`, `radix-ui`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| side | "top" \| "right" \| "bottom" \| "left" | True | 65 |
| inset | boolean | True | 87 |
| variant | "default" \| "destructive" | True | 88 |
| inset | boolean | True | 110 |
| inset | boolean | True | 158 |
| inset | boolean | True | 193 |
| inset | boolean | True | 226 |

### Defaults and motion

- Default `variant` = `"default"` (line 84).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/context-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/context-menu.tsx); SHA-256 `088cc84710235273d4e855a3a0c7d561f47718cd3f5e8fb90705b9fe10c6943d`; 252 lines.

Imports: `react`, `cn`, `lucide-react`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inset | boolean | True | 61 |
| inset | boolean | True | 119 |
| variant | "default" \| "destructive" | True | 120 |
| inset | boolean | True | 191 |

### Defaults and motion

- Default `variant` = `"default"` (line 116).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
