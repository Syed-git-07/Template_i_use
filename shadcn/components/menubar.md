# menubar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/base/ui/menubar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/menubar.tsx); SHA-256 `b11116a338cefa8cc8bdfe59c7e9df964eb49c5ae3a3f96c64094e8cbd9e10cf`; 282 lines.

Imports: `react`, `@base-ui/react/menu`, `@base-ui/react/menubar`, `cn`, `@/registry/bases/base/ui/dropdown-menu`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inset | boolean | True | 113 |
| inset | boolean | True | 154 |
| inset | boolean | True | 187 |
| inset | boolean | True | 236 |

### Defaults and motion

- Default `align` = `"start"` (line 69).
- Default `alignOffset` = `-4` (line 70).
- Default `sideOffset` = `8` (line 71).
- Default `variant` = `"default"` (line 92).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/menubar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/menubar.tsx); SHA-256 `b6c2c45f33b873fd7dcb5e712fa4cd50fb60588c374dc615101bb828b3711dc7`; 295 lines.

Imports: `react`, `cn`, `radix-ui`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inset | boolean | True | 94 |
| variant | "default" \| "destructive" | True | 95 |
| inset | boolean | True | 118 |
| inset | boolean | True | 153 |
| inset | boolean | True | 186 |
| inset | boolean | True | 236 |

### Defaults and motion

- Default `align` = `"start"` (line 66).
- Default `alignOffset` = `-4` (line 67).
- Default `sideOffset` = `8` (line 68).
- Default `variant` = `"default"` (line 91).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/menubar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/menubar.tsx); SHA-256 `1581a509109058d42d485558c09e57d621d4f161b8ce24864e2ecd28221dd753`; 276 lines.

Imports: `react`, `cn`, `lucide-react`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inset | boolean | True | 96 |
| variant | "default" \| "destructive" | True | 97 |
| inset | boolean | True | 168 |
| inset | boolean | True | 224 |

### Defaults and motion

- Default `align` = `"start"` (line 68).
- Default `alignOffset` = `-4` (line 69).
- Default `sideOffset` = `8` (line 70).
- Default `variant` = `"default"` (line 93).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
