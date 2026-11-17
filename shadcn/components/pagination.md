# pagination

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/pagination.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/pagination.tsx); SHA-256 `2c0cd63c8044e24dcb19ed3008d6f31407612816b42162d530ab7e0566ac0434`; 151 lines.

Imports: `react`, `cn`, `@/registry/bases/aria/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isActive | boolean | True | 40 |
| text | string | True | 66 |
| text | string | True | 94 |

### Defaults and motion

- Default `size` = `"icon"` (line 46).
- Default `text` = `"Previous"` (line 64).
- Default `text` = `"Next"` (line 92).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/pagination.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/pagination.tsx); SHA-256 `2d0558aace8097098ff2513f1d6e1633545198f913ee1f1283576a63c9d5e2f3`; 157 lines.

Imports: `react`, `cn`, `@/registry/bases/base/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isActive | boolean | True | 40 |
| text | string | True | 72 |
| text | string | True | 100 |

### Defaults and motion

- Default `size` = `"icon"` (line 47).
- Default `text` = `"Previous"` (line 70).
- Default `text` = `"Next"` (line 98).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/pagination.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/pagination.tsx); SHA-256 `e0ee3cca486ddede5cd7f6c9f490f04543342d7ac1a625fed4bdb5bd91f40888`; 156 lines.

Imports: `react`, `cn`, `@/registry/bases/radix/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isActive | boolean | True | 40 |
| text | string | True | 71 |
| text | string | True | 99 |

### Defaults and motion

- Default `size` = `"icon"` (line 47).
- Default `text` = `"Previous"` (line 69).
- Default `text` = `"Next"` (line 97).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/new-york-v4/ui/pagination.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/pagination.tsx); SHA-256 `b3328b9cf755ae9534c984adf5a4e7071bc206727fc361534b11a2ef5a37957f`; 128 lines.

Imports: `react`, `cn`, `lucide-react`, `@/registry/new-york-v4/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isActive | boolean | True | 41 |

### Defaults and motion

- Default `size` = `"icon"` (line 48).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
