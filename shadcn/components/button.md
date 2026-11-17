# button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/button.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/button.tsx); SHA-256 `68a102380f84fea12dd579e65ea5446d5713e6afa2e7b155371627705d714b62`; 85 lines.

Imports: `react`, `class-variance-authority`, `cn`, `react-aria-components`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 51 |
| className | string | True | 71 |

### Defaults and motion

- Default `variant` = `"default"` (line 45).
- Default `size` = `"default"` (line 46).
- Default `variant` = `"default"` (line 66).
- Default `size` = `"default"` (line 67).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/button.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/button.tsx); SHA-256 `2b4915e960e06f0e752f2b0ef6e4ca17f013e0ed009e0c8fe7cc80461221f1cb`; 51 lines.

Imports: `@base-ui/react/button`, `class-variance-authority`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `variant` = `"default"` (line 37).
- Default `size` = `"default"` (line 38).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/button.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/button.tsx); SHA-256 `0fbfd3b7e15e1921e164d54f92811b8bb86767343c15b4a668ab42fbe847a477`; 60 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 44 |

### Defaults and motion

- Default `variant` = `"default"` (line 38).
- Default `size` = `"default"` (line 39).
- Default `asChild` = `false` (line 40).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/button.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/button.tsx); SHA-256 `53704ac4814885902e76e7d1c4299be470e1fce9719b0298e0871ba352e390e4`; 64 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 48 |

### Defaults and motion

- Default `variant` = `"default"` (line 42).
- Default `size` = `"default"` (line 43).
- Default `asChild` = `false` (line 44).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
