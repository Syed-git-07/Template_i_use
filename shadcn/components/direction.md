# direction

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/direction.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/direction.tsx); SHA-256 `8babf8e559c2e36da6ecc0b00d033ccf79e3e1e32b7cde6b890195262c13a98c`; 30 lines.

Imports: `react`, `react-aria-components`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| direction | "ltr" \| "rtl" | True | 8 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/direction.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/direction.tsx); SHA-256 `0fd9e12ece15ec2ac5b32018664deb9e1df0977d1f0a4d3ee65e070b3e7df04b`; 7 lines.

Imports:

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/direction.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/direction.tsx); SHA-256 `cd2c00d9757eea6dcf3242d71de8f397d29291a67fba5c39fb03c4c60746f36c`; 23 lines.

Imports: `react`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| direction | React.ComponentProps<typeof Direction.DirectionProvider>["dir"] | True | 11 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/direction.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/direction.tsx); SHA-256 `cd2c00d9757eea6dcf3242d71de8f397d29291a67fba5c39fb03c4c60746f36c`; 23 lines.

Imports: `react`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| direction | React.ComponentProps<typeof Direction.DirectionProvider>["dir"] | True | 11 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
