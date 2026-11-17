# dropdown-menu

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/dropdown-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/dropdown-menu.tsx); SHA-256 `e180e936ad5781c8786af7cf423686d8a6320d979a560965ed8c8d15c28838ba`; 262 lines.

Imports: `react`, `class-variance-authority`, `cn`, `react-aria-components`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| "data-slot" | string | True | 44 |
| className | string | True | 45 |
| children | React.ReactNode | True | 46 |
| children | React.ReactNode | True | 72 |
| inset | boolean | True | 82 |
| inset | boolean | True | 114 |
| variant | "default" \| "destructive" | True | 115 |
| inset | boolean | True | 172 |

### Defaults and motion

- Default `dataSlot` = `"dropdown-menu-content"` (line 29).
- Default `placement` = `"bottom start"` (line 30).
- Default `offset` = `4` (line 31).
- Default `crossOffset` = `0` (line 32).
- Default `variant` = `"default"` (line 110).
- Default `placement` = `"end top"` (line 203).
- Default `crossOffset` = `-3` (line 204).
- Default `offset` = `0` (line 205).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/dropdown-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/dropdown-menu.tsx); SHA-256 `087ed036f4b4b1fe8a5afa7d49e2e5e1d3ab4887bd2039a17cb85dce1725f43b`; 286 lines.

Imports: `react`, `@base-ui/react/menu`, `cn`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inset | boolean | True | 64 |
| inset | boolean | True | 82 |
| variant | "default" \| "destructive" | True | 83 |
| inset | boolean | True | 109 |
| inset | boolean | True | 165 |
| inset | boolean | True | 212 |

### Defaults and motion

- Default `align` = `"start"` (line 22).
- Default `alignOffset` = `0` (line 23).
- Default `side` = `"bottom"` (line 24).
- Default `sideOffset` = `4` (line 25).
- Default `variant` = `"default"` (line 79).
- Default `align` = `"start"` (line 135).
- Default `alignOffset` = `-3` (line 136).
- Default `side` = `"right"` (line 137).
- Default `sideOffset` = `0` (line 138).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/dropdown-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/dropdown-menu.tsx); SHA-256 `f5a46a6dc0425be5515f2d1c9c097c40f2d94c528d4d094483465eda3f12173b`; 287 lines.

Imports: `react`, `cn`, `radix-ui`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inset | boolean | True | 70 |
| variant | "default" \| "destructive" | True | 71 |
| inset | boolean | True | 94 |
| inset | boolean | True | 143 |
| inset | boolean | True | 179 |
| inset | boolean | True | 229 |

### Defaults and motion

- Default `align` = `"start"` (line 36).
- Default `sideOffset` = `4` (line 37).
- Default `variant` = `"default"` (line 67).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/dropdown-menu.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/dropdown-menu.tsx); SHA-256 `b839ed438b83f36a6c47cfaee60196276621409f0476845c4c6a3db109838caa`; 257 lines.

Imports: `react`, `cn`, `lucide-react`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inset | boolean | True | 67 |
| variant | "default" \| "destructive" | True | 68 |
| inset | boolean | True | 150 |
| inset | boolean | True | 206 |

### Defaults and motion

- Default `sideOffset` = `4` (line 35).
- Default `variant` = `"default"` (line 64).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
