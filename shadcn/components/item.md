# item

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/item.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/item.tsx); SHA-256 `757b155cd73542a55a200f296dc9e11b638f7a7696ea1ab38afb94ffe2cf6824`; 198 lines.

Imports: `react`, `class-variance-authority`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `variant` = `"default"` (line 62).
- Default `size` = `"default"` (line 63).
- Default `variant` = `"default"` (line 98).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/item.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/item.tsx); SHA-256 `53ea49ba092399e7e1b21c308dc7b5633c72838be1308dca6d0b9d500113ccb5`; 201 lines.

Imports: `react`, `@base-ui/react/merge-props`, `@base-ui/react/use-render`, `class-variance-authority`, `cn`, `@/registry/bases/base/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `variant` = `"default"` (line 61).
- Default `size` = `"default"` (line 62).
- Default `variant` = `"default"` (line 101).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/item.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/item.tsx); SHA-256 `0f37fdeee9bcf4b0e55f3ad0156d485c42181af99af69375c22c2e58b0421488`; 196 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`, `@/registry/bases/radix/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 65 |

### Defaults and motion

- Default `variant` = `"default"` (line 60).
- Default `size` = `"default"` (line 61).
- Default `asChild` = `false` (line 62).
- Default `variant` = `"default"` (line 96).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/new-york-v4/ui/item.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/item.tsx); SHA-256 `e0dd444a19d7067aa3d29469471e09055494495ad86ea594ef3de1506baa976c`; 194 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`, `@/registry/new-york-v4/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 61 |

### Defaults and motion

- Default `variant` = `"default"` (line 56).
- Default `size` = `"default"` (line 57).
- Default `asChild` = `false` (line 58).
- Default `variant` = `"default"` (line 93).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
