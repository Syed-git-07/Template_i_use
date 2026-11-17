# popover

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/popover.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/popover.tsx); SHA-256 `757c967c836a112e3ce079b83c875fc05e8bff4541b82f6c89cffa2c18cc777d`; 88 lines.

Imports: `react`, `cn`, `react-aria-components`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 28 |

### Defaults and motion

- Default `placement` = `"bottom"` (line 23).
- Default `offset` = `4` (line 24).
- Default `crossOffset` = `0` (line 25).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/popover.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/popover.tsx); SHA-256 `7d01c5ceeeb4b35ceba46eb039e1481dbebbac25d741dbda540a31cc1b3fa589`; 90 lines.

Imports: `react`, `@base-ui/react/popover`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `align` = `"center"` (line 17).
- Default `alignOffset` = `0` (line 18).
- Default `side` = `"bottom"` (line 19).
- Default `sideOffset` = `4` (line 20).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/popover.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/popover.tsx); SHA-256 `36f299a555b4fb9cb54dba9d91dd348458736c4a38092855d8014ddcd3245854`; 89 lines.

Imports: `react`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `align` = `"center"` (line 21).
- Default `sideOffset` = `4` (line 22).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/popover.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/popover.tsx); SHA-256 `579acb68b7feec50eed9a12e69ddea19575f9924cb205c728dc170dfe1e864aa`; 89 lines.

Imports: `react`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `align` = `"center"` (line 21).
- Default `sideOffset` = `4` (line 22).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
