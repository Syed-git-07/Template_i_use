# select

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/select.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/select.tsx); SHA-256 `75197547fd1023c343103bcce2cfb94f1a0e010656e9d29cf7245e3a66d415f1`; 298 lines.

Imports: `react`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/input-group`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | True | 82 |
| size | "sm" \| "default" | True | 83 |
| className | string | True | 119 |
| children | React.ReactNode | True | 120 |
| className | string | True | 146 |
| children | React.ReactNode | True | 147 |

### Defaults and motion

- Default `size` = `"default"` (line 78).
- Default `placement` = `"bottom"` (line 111).
- Default `offset` = `4` (line 112).
- Default `crossOffset` = `0` (line 113).
- Default `placement` = `"bottom start"` (line 138).
- Default `offset` = `4` (line 139).
- Default `crossOffset` = `0` (line 140).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/select.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/select.tsx); SHA-256 `b4951a3f50b931d148d152330ba58056eaccacde2704671dbb0f07823bf64806`; 221 lines.

Imports: `react`, `@base-ui/react/select`, `cn`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "sm" \| "default" | True | 37 |

### Defaults and motion

- Default `size` = `"default"` (line 33).
- Default `side` = `"bottom"` (line 69).
- Default `sideOffset` = `4` (line 70).
- Default `align` = `"center"` (line 71).
- Default `alignOffset` = `0` (line 72).
- Default `alignItemWithTrigger` = `true` (line 73).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/select.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/select.tsx); SHA-256 `bcdba6310ad0c219d6435620dac1dae5c04bb05df77af0b17bd9fcccb797a433`; 216 lines.

Imports: `react`, `cn`, `radix-ui`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "sm" \| "default" | True | 40 |

### Defaults and motion

- Default `size` = `"default"` (line 36).
- Default `position` = `"item-aligned"` (line 70).
- Default `align` = `"center"` (line 71).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/select.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/select.tsx); SHA-256 `1af5229ee1eaab89b8469e52108d42f87106b689cd928ee37ab7ad182fea2fad`; 190 lines.

Imports: `react`, `cn`, `lucide-react`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| size | "sm" \| "default" | True | 32 |

### Defaults and motion

- Default `size` = `"default"` (line 28).
- Default `position` = `"item-aligned"` (line 55).
- Default `align` = `"center"` (line 56).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
