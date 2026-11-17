# button-group

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/button-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/button-group.tsx); SHA-256 `df12d45a27aef3cc49d9a6f72645dc1630eb6e205acaedf0e782375928951f71`; 95 lines.

Imports: `class-variance-authority`, `cn`, `@/registry/bases/aria/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| render | (props: React.HTMLAttributes<HTMLElement>) => React.ReactNode | True | 44 |

### Defaults and motion

- Default `orientation` = `"vertical"` (line 73).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/button-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/button-group.tsx); SHA-256 `f33bb886a025cf5e4a0b2a81deab5ebf23242fda81bab0472f47418bc8b337f7`; 88 lines.

Imports: `@base-ui/react/merge-props`, `@base-ui/react/use-render`, `class-variance-authority`, `cn`, `@/registry/bases/base/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `orientation` = `"vertical"` (line 66).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/button-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/button-group.tsx); SHA-256 `baaedc7ab3e4550eedf3f8f025018685ec6c5953cdf145c6e1785bc8eb7b281c`; 84 lines.

Imports: `class-variance-authority`, `cn`, `radix-ui`, `@/registry/bases/radix/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 45 |

### Defaults and motion

- Default `asChild` = `false` (line 42).
- Default `orientation` = `"vertical"` (line 62).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/new-york-v4/ui/button-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/button-group.tsx); SHA-256 `8dcb0caf8d78f8ecddfc3db7c8bb435b041d7d315595dff001e5baa28c23665c`; 84 lines.

Imports: `class-variance-authority`, `cn`, `radix-ui`, `@/registry/new-york-v4/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 45 |

### Defaults and motion

- Default `asChild` = `false` (line 42).
- Default `orientation` = `"vertical"` (line 62).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
