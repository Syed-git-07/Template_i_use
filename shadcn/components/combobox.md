# combobox

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/combobox.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/combobox.tsx); SHA-256 `de373320460e866aabaa656990bd17a9faa1fd448e60a8dc40aea993b38264de`; 405 lines.

Imports: `react`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/button`, `@/registry/bases/aria/ui/input-group`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | True | 54 |
| showTrigger | boolean | True | 117 |
| showClear | boolean | True | 118 |
| className | string | True | 160 |
| children | React.ReactNode | True | 161 |
| anchor | React.RefObject<HTMLDivElement \| null> | True | 162 |
| className | string | True | 291 |
| showRemove | boolean | True | 322 |
| children | React.ReactNode | True | 323 |

### Defaults and motion

- Default `disabled` = `false` (line 112).
- Default `showTrigger` = `true` (line 113).
- Default `showClear` = `false` (line 114).
- Default `placement` = `"bottom"` (line 151).
- Default `offset` = `6` (line 152).
- Default `crossOffset` = `0` (line 153).
- Default `showRemove` = `true` (line 319).

### Input, style and lifecycle

Events: onPress (line 91); onRemove (line 299); onKeyDown (line 366).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, aria.

## apps/v4/registry/bases/base/ui/combobox.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/combobox.tsx); SHA-256 `12e5b0b22ed7acab0789d001f691ab691bf4bf3382c260e75ecd45c70b987f5b`; 324 lines.

Imports: `react`, `@base-ui/react`, `cn`, `@/registry/bases/base/ui/button`, `@/registry/bases/base/ui/input-group`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| showTrigger | boolean | True | 74 |
| showClear | boolean | True | 75 |
| showRemove | boolean | True | 254 |

### Defaults and motion

- Default `disabled` = `false` (line 69).
- Default `showTrigger` = `true` (line 70).
- Default `showClear` = `false` (line 71).
- Default `side` = `"bottom"` (line 103).
- Default `sideOffset` = `6` (line 104).
- Default `align` = `"start"` (line 105).
- Default `alignOffset` = `0` (line 106).
- Default `showRemove` = `true` (line 251).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/combobox.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/combobox.tsx); SHA-256 `0fb3b83003b642d90a0478f3881468ec6a461804575c0d833d25acd65b262880`; 326 lines.

Imports: `react`, `@base-ui/react`, `cn`, `@/registry/bases/radix/ui/button`, `@/registry/bases/radix/ui/input-group`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| showTrigger | boolean | True | 74 |
| showClear | boolean | True | 75 |
| showRemove | boolean | True | 256 |

### Defaults and motion

- Default `disabled` = `false` (line 69).
- Default `showTrigger` = `true` (line 70).
- Default `showClear` = `false` (line 71).
- Default `side` = `"bottom"` (line 105).
- Default `sideOffset` = `6` (line 106).
- Default `align` = `"start"` (line 107).
- Default `alignOffset` = `0` (line 108).
- Default `showRemove` = `true` (line 253).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/combobox.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/combobox.tsx); SHA-256 `664079fb5e9f49ba12918608ea625ed455d213ab1e630be668a5c1463bbb7b61`; 311 lines.

Imports: `react`, `@base-ui/react`, `cn`, `lucide-react`, `@/registry/new-york-v4/ui/button`, `@/registry/new-york-v4/ui/input-group`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| showTrigger | boolean | True | 63 |
| showClear | boolean | True | 64 |
| showRemove | boolean | True | 250 |

### Defaults and motion

- Default `disabled` = `false` (line 58).
- Default `showTrigger` = `true` (line 59).
- Default `showClear` = `false` (line 60).
- Default `side` = `"bottom"` (line 94).
- Default `sideOffset` = `6` (line 95).
- Default `align` = `"start"` (line 96).
- Default `alignOffset` = `0` (line 97).
- Default `showRemove` = `true` (line 247).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
