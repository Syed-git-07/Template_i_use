# trace

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/trace.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/trace.tsx); SHA-256 `efd5e72241e8a211727c74f6d5593ec6a79ac2a098dfb7355c81dc4b2b032378`; 191 lines.

Imports: `react`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/collapsible`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| status | "running" \| "error" \| "pending" | True | 34 |
| isExpanded | undefined | True | 97 |
| isExpanded | boolean | False | 99 |
| onExpandedChange | NonNullable<           React.ComponentProps<typeof Collapsible>["onExpandedChange"]         > | False | 100 |
| className | string | True | 105 |
| className | string | True | 124 |
| children | React.ReactNode | True | 125 |
| className | string | True | 159 |
| children | React.ReactNode | True | 160 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/trace.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/trace.tsx); SHA-256 `f57b931925ce9521077c3f2a748d35a44de4fb35ba2a97c5580b2ae8d64264b2`; 174 lines.

Imports: `react`, `cn`, `@/registry/bases/base/ui/collapsible`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| status | "running" \| "error" \| "pending" | True | 29 |
| open | undefined | True | 92 |
| open | boolean | False | 94 |
| onOpenChange | NonNullable<           React.ComponentProps<typeof Collapsible>["onOpenChange"]         > | False | 95 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/trace.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/trace.tsx); SHA-256 `de3e4ef32676ef792e4766d3dcdf868c8f90af0b46a4268b9f58aa21d681b0bd`; 174 lines.

Imports: `react`, `cn`, `@/registry/bases/radix/ui/collapsible`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| status | "running" \| "error" \| "pending" | True | 29 |
| open | undefined | True | 92 |
| open | boolean | False | 94 |
| onOpenChange | NonNullable<           React.ComponentProps<typeof Collapsible>["onOpenChange"]         > | False | 95 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
