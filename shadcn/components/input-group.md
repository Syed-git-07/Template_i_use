# input-group

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/input-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/input-group.tsx); SHA-256 `da623b6b119a39bb5f9353af3a702bb9fb5941aefd02def56ea4e50cd52dee9c`; 150 lines.

Imports: `react`, `class-variance-authority`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/button`, `@/registry/bases/aria/ui/input`, `@/registry/bases/aria/ui/textarea`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| type | "button" \| "submit" \| "reset" | True | 91 |

### Defaults and motion

- Default `align` = `"inline-start"` (line 46).
- Default `type` = `"button"` (line 85).
- Default `variant` = `"ghost"` (line 86).
- Default `size` = `"xs"` (line 87).

### Input, style and lifecycle

Events: onClick (line 55).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: focus, aria.

## apps/v4/registry/bases/base/ui/input-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/input-group.tsx); SHA-256 `dfeb45670f59f0746459644342c1d1dd0e8f2886bfc51ec918582ea72e047df9`; 150 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/base/ui/button`, `@/registry/bases/base/ui/input`, `@/registry/bases/base/ui/textarea`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| type | "button" \| "submit" \| "reset" | True | 91 |

### Defaults and motion

- Default `align` = `"inline-start"` (line 46).
- Default `type` = `"button"` (line 85).
- Default `variant` = `"ghost"` (line 86).
- Default `size` = `"xs"` (line 87).

### Input, style and lifecycle

Events: onClick (line 55).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: focus, aria.

## apps/v4/registry/bases/radix/ui/input-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/input-group.tsx); SHA-256 `078737186a3918f12e4b7ebaddc408deecdbd89b18d9c52cb6e84e1de73c3453`; 148 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/radix/ui/button`, `@/registry/bases/radix/ui/input`, `@/registry/bases/radix/ui/textarea`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `align` = `"inline-start"` (line 46).
- Default `type` = `"button"` (line 85).
- Default `variant` = `"ghost"` (line 86).
- Default `size` = `"xs"` (line 87).

### Input, style and lifecycle

Events: onClick (line 55).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: focus, aria.

## apps/v4/registry/new-york-v4/ui/input-group.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/input-group.tsx); SHA-256 `2f09b18ea8d59238bbc0e1d329c1014bd5417159094f6f7465ad837e5ea511e2`; 171 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/new-york-v4/ui/button`, `@/registry/new-york-v4/ui/input`, `@/registry/new-york-v4/ui/textarea`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `align` = `"inline-start"` (line 62).
- Default `type` = `"button"` (line 102).
- Default `variant` = `"ghost"` (line 103).
- Default `size` = `"xs"` (line 104).

### Input, style and lifecycle

Events: onClick (line 71).

Typography/style anchors: 40, 87, 90.

Source signals: focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
