# alert-dialog

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/alert-dialog.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/alert-dialog.tsx); SHA-256 `bcf336ea573b2832834deb4c46d8bcc035afd5c61a23f9dd61ac1b4d970c269c`; 206 lines.

Imports: `react`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 29 |
| children | React.ReactNode | False | 30 |
| className | string | True | 53 |
| size | "default" \| "sm" | True | 54 |
| children | React.ReactNode | False | 55 |

### Defaults and motion

- Default `size` = `"default"` (line 48).
- Default `size` = `"default"` (line 81).
- Default `variant` = `"outline"` (line 177).
- Default `size` = `"default"` (line 178).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/alert-dialog.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/alert-dialog.tsx); SHA-256 `eef7d9e7e1982a13fb00e6d210847152ab6360ba05fecdeaf27a42e2d9e103b7`; 176 lines.

Imports: `react`, `@base-ui/react/alert-dialog`, `cn`, `@/registry/bases/base/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "default" \| "sm" | True | 46 |

### Defaults and motion

- Default `size` = `"default"` (line 43).
- Default `variant` = `"outline"` (line 147).
- Default `size` = `"default"` (line 148).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/alert-dialog.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/alert-dialog.tsx); SHA-256 `7f3c668c95e14ffcba91dcea08a8428aee7c86ef6a258ff5505bdf25d7f34d5e`; 185 lines.

Imports: `react`, `cn`, `radix-ui`, `@/registry/bases/radix/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "default" \| "sm" | True | 49 |

### Defaults and motion

- Default `size` = `"default"` (line 46).
- Default `variant` = `"default"` (line 137).
- Default `size` = `"default"` (line 138).
- Default `variant` = `"outline"` (line 155).
- Default `size` = `"default"` (line 156).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/alert-dialog.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/alert-dialog.tsx); SHA-256 `6c8b686177a7327eaa10556e5cd2c9d7dd32d727955b8287dd630bada07befa1`; 197 lines.

Imports: `react`, `cn`, `radix-ui`, `@/registry/new-york-v4/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "default" \| "sm" | True | 52 |

### Defaults and motion

- Default `size` = `"default"` (line 49).
- Default `variant` = `"default"` (line 149).
- Default `size` = `"default"` (line 150).
- Default `variant` = `"outline"` (line 167).
- Default `size` = `"default"` (line 168).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
