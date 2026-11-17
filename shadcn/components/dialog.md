# dialog

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/dialog.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/dialog.tsx); SHA-256 `7620f10666157f90f17cfcd38ae4945df0bee625ae0cc391da6157f278efb723`; 183 lines.

Imports: `react`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 46 |
| children | React.ReactNode | False | 47 |
| className | string | True | 71 |
| children | React.ReactNode | False | 72 |
| showCloseButton | boolean | True | 73 |
| showCloseButton | boolean | True | 127 |

### Defaults and motion

- Default `variant` = `"outline"` (line 25).
- Default `size` = `"default"` (line 26).
- Default `showCloseButton` = `true` (line 66).
- Default `isDismissable` = `true` (line 67).
- Default `showCloseButton` = `false` (line 123).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/dialog.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/dialog.tsx); SHA-256 `ce619a8c7b9446aa6052a4b2e5ac32de28be76300063044493f1be5eee60f5f1`; 157 lines.

Imports: `react`, `@base-ui/react/dialog`, `cn`, `@/registry/bases/base/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| showCloseButton | boolean | True | 45 |
| showCloseButton | boolean | True | 101 |

### Defaults and motion

- Default `showCloseButton` = `true` (line 42).
- Default `showCloseButton` = `false` (line 97).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/dialog.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/dialog.tsx); SHA-256 `8958a4624e6e4a4514647f14a6fb28bd3877557e599254a58c7e9f2e258037e8`; 161 lines.

Imports: `react`, `cn`, `radix-ui`, `@/registry/bases/radix/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| showCloseButton | boolean | True | 53 |
| showCloseButton | boolean | True | 102 |

### Defaults and motion

- Default `showCloseButton` = `true` (line 50).
- Default `showCloseButton` = `false` (line 98).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/dialog.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/dialog.tsx); SHA-256 `6dab27ba10039648dfbc570ef878f4701ed77464581492e82eddca8af1153720`; 159 lines.

Imports: `react`, `cn`, `lucide-react`, `radix-ui`, `@/registry/new-york-v4/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| showCloseButton | boolean | True | 56 |
| showCloseButton | boolean | True | 100 |

### Defaults and motion

- Default `showCloseButton` = `true` (line 53).
- Default `showCloseButton` = `false` (line 96).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
