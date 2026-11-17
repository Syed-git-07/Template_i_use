# tooltip

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/tooltip.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/tooltip.tsx); SHA-256 `6c065e0fcfa6053aaf1a0e5c04d21fcfa9391d33d5085b618dd225e4efda61d7`; 81 lines.

Imports: `react`, `cn`, `react-aria-components`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 44 |
| children | React.ReactNode | True | 45 |

### Defaults and motion

- Default `delay` = `0` (line 13).
- Default `placement` = `"top"` (line 35).
- Default `offset` = `4` (line 36).
- Default `crossOffset` = `0` (line 37).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/tooltip.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/tooltip.tsx); SHA-256 `d31b68b965032ffe67a20b3f06f5603673cc437de2da6a85fe8bdce5806a10e9`; 66 lines.

Imports: `@base-ui/react/tooltip`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `delay` = `0` (line 7).
- Default `side` = `"top"` (line 29).
- Default `sideOffset` = `4` (line 30).
- Default `align` = `"center"` (line 31).
- Default `alignOffset` = `0` (line 32).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/tooltip.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/tooltip.tsx); SHA-256 `a34f026ce4e4ab568f7bb59f4cc4a3715991fcf079ae0683f5bd7baf0ec4e69d`; 57 lines.

Imports: `react`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `delayDuration` = `0` (line 8).
- Default `sideOffset` = `0` (line 34).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/tooltip.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/tooltip.tsx); SHA-256 `b78431f57c5d3bab8d00fedb47c40246873ee7dab0fc1c8214e34cbc2990889d`; 57 lines.

Imports: `react`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `delayDuration` = `0` (line 8).
- Default `sideOffset` = `0` (line 34).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
