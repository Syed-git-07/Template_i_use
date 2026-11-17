# slider

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/slider.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/slider.tsx); SHA-256 `8547c1831a9967147484056b7b1572e01d4396fdb344ff492279a51abae6ffb4`; 61 lines.

Imports: `cn`, `react-aria-components`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 17 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/slider.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/slider.tsx); SHA-256 `be9573bd0be17f0f27d24f87597be8e0d00cd83777c193ef5b09d341311b9b52`; 52 lines.

Imports: `@base-ui/react/slider`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `min` = `0` (line 8).
- Default `max` = `100` (line 9).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/slider.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/slider.tsx); SHA-256 `58618685db83897dfa715dc351f9494685dc66cd260252b818bbca6c7746ad8b`; 59 lines.

Imports: `react`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `min` = `0` (line 11).
- Default `max` = `100` (line 12).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/slider.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/slider.tsx); SHA-256 `114d4c9eb8f73d1ab900445ce551b29fbfb9ff9fc94bbec50bd12fd7c05c0872`; 63 lines.

Imports: `react`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `min` = `0` (line 11).
- Default `max` = `100` (line 12).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
