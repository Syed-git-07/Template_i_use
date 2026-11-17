# command

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/command.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/command.tsx); SHA-256 `b4fac7e87ce077b5424d77304a4d007ff6d41e8fc355280533ed1943cc73c330`; 250 lines.

Imports: `react`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/dialog`, `@/registry/bases/aria/ui/input-group`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 43 |
| dir | React.HTMLAttributes<HTMLDivElement>["dir"] | True | 44 |
| style | React.CSSProperties | True | 45 |
| title | string | True | 78 |
| description | string | True | 79 |
| open | boolean | True | 80 |
| onOpenChange | (isOpen: boolean) => void | True | 81 |
| className | string | True | 82 |
| showCloseButton | boolean | True | 83 |
| children | React.ReactNode | False | 84 |
| heading | string | True | 168 |

### Defaults and motion

- Default `title` = `"Command Palette"` (line 66).
- Default `description` = `"Search for a command to run..."` (line 67).
- Default `showCloseButton` = `false` (line 72).

### Input, style and lifecycle

Events: onOpenChange (line 89).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/command.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/command.tsx); SHA-256 `f73b62c782cf17daf8d33afee124380829ca387aa5ead6f2bdf5126a79bed5bc`; 205 lines.

Imports: `react`, `cmdk`, `cn`, `@/registry/bases/base/ui/dialog`, `@/registry/bases/base/ui/input-group`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| title | string | True | 44 |
| description | string | True | 45 |
| className | string | True | 46 |
| showCloseButton | boolean | True | 47 |
| children | React.ReactNode | False | 48 |

### Defaults and motion

- Default `title` = `"Command Palette"` (line 37).
- Default `description` = `"Search for a command to run..."` (line 38).
- Default `showCloseButton` = `false` (line 41).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/command.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/command.tsx); SHA-256 `1f5616e8dc5ffe83061369d0cb654a0a2b9a7b10aaf4b67baeee795d228ee3cc`; 204 lines.

Imports: `react`, `cmdk`, `cn`, `@/registry/bases/radix/ui/dialog`, `@/registry/bases/radix/ui/input-group`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| title | string | True | 44 |
| description | string | True | 45 |
| className | string | True | 46 |
| showCloseButton | boolean | True | 47 |

### Defaults and motion

- Default `title` = `"Command Palette"` (line 37).
- Default `description` = `"Search for a command to run..."` (line 38).
- Default `showCloseButton` = `false` (line 41).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/command.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/command.tsx); SHA-256 `b803717bdbde47c62763b90176ce472e8a75d7322fa9f5f4807f30f9bf029e9e`; 185 lines.

Imports: `react`, `cmdk`, `cn`, `lucide-react`, `@/registry/new-york-v4/ui/dialog`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| title | string | True | 40 |
| description | string | True | 41 |
| className | string | True | 42 |
| showCloseButton | boolean | True | 43 |

### Defaults and motion

- Default `title` = `"Command Palette"` (line 33).
- Default `description` = `"Search for a command to run..."` (line 34).
- Default `showCloseButton` = `true` (line 37).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
