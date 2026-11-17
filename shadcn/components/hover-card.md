# hover-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/hover-card.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/hover-card.tsx); SHA-256 `99ed492108174147a79dae8ce2e7603f4bd796ca6d4e2158bddb4e38fa5958bc`; 44 lines.

Imports: `cn`, `react-aria-components`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 26 |

### Defaults and motion

- Default `placement` = `"bottom"` (line 21).
- Default `offset` = `4` (line 22).
- Default `crossOffset` = `0` (line 23).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/hover-card.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/hover-card.tsx); SHA-256 `3663139506c96092ebee645e4bbff6ccad0ed07a2385c6449d97586cb0bee641`; 51 lines.

Imports: `@base-ui/react/preview-card`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `side` = `"bottom"` (line 18).
- Default `sideOffset` = `4` (line 19).
- Default `align` = `"center"` (line 20).
- Default `alignOffset` = `4` (line 21).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/hover-card.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/hover-card.tsx); SHA-256 `3a7cb076793b3e059ba3ba5273102a3a1c6eaa6fe5822cce1d58321c09cf82dc`; 44 lines.

Imports: `react`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `align` = `"center"` (line 23).
- Default `sideOffset` = `4` (line 24).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/hover-card.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/hover-card.tsx); SHA-256 `c2f948a44a6b1d270d142f5ef0b4feab02cc6aebaeb900bc0531b4cc45f6e95e`; 44 lines.

Imports: `react`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `align` = `"center"` (line 23).
- Default `sideOffset` = `4` (line 24).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
