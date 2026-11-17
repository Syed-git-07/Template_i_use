# navigation-menu

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/base/ui/navigation-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/navigation-menu.tsx); SHA-256 `970decde688088e903ff2cc8641af67b59f7b3417dd0437f8d9cd1029b97daaa`; 174 lines.

Imports: `@base-ui/react/navigation-menu`, `class-variance-authority`, `cn`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `align` = `"start"` (line 8).
- Default `side` = `"bottom"` (line 105).
- Default `sideOffset` = `8` (line 106).
- Default `align` = `"start"` (line 107).
- Default `alignOffset` = `0` (line 108).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/navigation-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/navigation-menu.tsx); SHA-256 `062e3873c3eacd99c6e984223f7cb75064db8a396c49b5653149d4bd627c0cf7`; 170 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| viewport | boolean | True | 14 |

### Defaults and motion

- Default `viewport` = `true` (line 11).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/new-york-v4/ui/navigation-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/navigation-menu.tsx); SHA-256 `ab549fd79412fcfd7003a4ede672fae9cad4f86fa75adce7738b8231495a0f52`; 168 lines.

Imports: `react`, `class-variance-authority`, `cn`, `lucide-react`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| viewport | boolean | True | 13 |

### Defaults and motion

- Default `viewport` = `true` (line 10).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
