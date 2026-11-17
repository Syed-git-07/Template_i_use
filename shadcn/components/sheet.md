# sheet

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/sheet.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/sheet.tsx); SHA-256 `cd29d495c440a9bbaf7a3736c60fdca3e27b84fb1cca514eff56ea71c9e34ea0`; 195 lines.

Imports: `react`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 46 |
| children | React.ReactNode | False | 47 |
| className | string | True | 72 |
| children | React.ReactNode | False | 73 |
| side | "top" \| "right" \| "bottom" \| "left" | True | 74 |
| showCloseButton | boolean | True | 75 |
| side | "top" \| "right" \| "bottom" \| "left" | True | 121 |
| showCloseButton | boolean | True | 122 |

### Defaults and motion

- Default `variant` = `"outline"` (line 25).
- Default `size` = `"default"` (line 26).
- Default `side` = `"right"` (line 67).
- Default `showCloseButton` = `true` (line 68).
- Default `side` = `"right"` (line 117).
- Default `showCloseButton` = `true` (line 118).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/sheet.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/sheet.tsx); SHA-256 `d5bb96e6f2e69f64422c1d622087e71e4640f7d3012a265138777a8fb6b845f2`; 141 lines.

Imports: `react`, `@base-ui/react/dialog`, `cn`, `@/registry/bases/base/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| side | "top" \| "right" \| "bottom" \| "left" | True | 46 |
| showCloseButton | boolean | True | 47 |

### Defaults and motion

- Default `side` = `"right"` (line 42).
- Default `showCloseButton` = `true` (line 43).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/sheet.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/sheet.tsx); SHA-256 `6c0f4a9f7107223af3c8bf4d4e816618375f4d5df4df2979d24c5a916ab1f8b8`; 146 lines.

Imports: `react`, `cn`, `radix-ui`, `@/registry/bases/radix/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| side | "top" \| "right" \| "bottom" \| "left" | True | 55 |
| showCloseButton | boolean | True | 56 |

### Defaults and motion

- Default `side` = `"right"` (line 51).
- Default `showCloseButton` = `true` (line 52).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/sheet.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/sheet.tsx); SHA-256 `1c775635fc8d4542c57f5209950e4a7c505f65489fbc9ba886ee64f70f4f05b4`; 143 lines.

Imports: `react`, `cn`, `lucide-react`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| side | "top" \| "right" \| "bottom" \| "left" | True | 53 |
| showCloseButton | boolean | True | 54 |

### Defaults and motion

- Default `side` = `"right"` (line 49).
- Default `showCloseButton` = `true` (line 50).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
