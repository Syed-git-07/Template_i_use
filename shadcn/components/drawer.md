# drawer

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/drawer.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/drawer.tsx); SHA-256 `55d32749ee8628abb5d82f11e9548e4ba1c09e9f5c81a8d9b885fb01162ab4cc`; 228 lines.

Imports: `react`, `@base-ui/react/drawer`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| hasSnapPoints | boolean | False | 8 |
| modal | DrawerPrimitive.Root.Props["modal"] | False | 9 |
| showSwipeHandle | boolean | False | 10 |
| swipeDirection | NonNullable<DrawerPrimitive.Root.Props["swipeDirection"]> | False | 11 |
| showSwipeHandle | boolean | True | 33 |

### Defaults and motion

- Default `modal` = `true` (line 27).
- Default `showSwipeHandle` = `false` (line 28).
- Default `swipeDirection` = `"down"` (line 30).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/drawer.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/drawer.tsx); SHA-256 `55d32749ee8628abb5d82f11e9548e4ba1c09e9f5c81a8d9b885fb01162ab4cc`; 228 lines.

Imports: `react`, `@base-ui/react/drawer`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| hasSnapPoints | boolean | False | 8 |
| modal | DrawerPrimitive.Root.Props["modal"] | False | 9 |
| showSwipeHandle | boolean | False | 10 |
| swipeDirection | NonNullable<DrawerPrimitive.Root.Props["swipeDirection"]> | False | 11 |
| showSwipeHandle | boolean | True | 33 |

### Defaults and motion

- Default `modal` = `true` (line 27).
- Default `showSwipeHandle` = `false` (line 28).
- Default `swipeDirection` = `"down"` (line 30).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/drawer.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/drawer.tsx); SHA-256 `12cecac4cefc858ac81d30448d06a1e64755596814e3ae205113435a8ca046a2`; 131 lines.

Imports: `react`, `cn`, `vaul`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/drawer.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/drawer.tsx); SHA-256 `75447b658be4e4ae68d0c67d5dd4cdfc140dbada24ac2a6aae496dcd2d9779f6`; 135 lines.

Imports: `react`, `cn`, `vaul`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
