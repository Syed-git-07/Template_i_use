# field

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/field.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/field.tsx); SHA-256 `80b94364e925d0c10b2569f7eff6348ee476d03c160e16cf48b0972fe73fbe5d`; 225 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/aria/ui/label`, `@/registry/bases/aria/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | "legend" \| "label" | True | 24 |
| children | React.ReactNode | True | 140 |
| errors | Array<{ message?: string } \| undefined> | True | 168 |
| message | string | True | 168 |

### Defaults and motion

- Default `variant` = `"legend"` (line 22).
- Default `orientation` = `"vertical"` (line 66).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/field.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/field.tsx); SHA-256 `c70bd20234b2ae9dfe4908e0d8d9f6abd15fe261606de2c472c99d2b9e9f6201`; 225 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/base/ui/label`, `@/registry/bases/base/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | "legend" \| "label" | True | 24 |
| children | React.ReactNode | True | 140 |
| errors | Array<{ message?: string } \| undefined> | True | 168 |
| message | string | True | 168 |

### Defaults and motion

- Default `variant` = `"legend"` (line 22).
- Default `orientation` = `"vertical"` (line 66).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/field.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/field.tsx); SHA-256 `bdddd8ccaf68b970a34d4694830a464b13acc36392568533b65b54404de44f66`; 225 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/bases/radix/ui/label`, `@/registry/bases/radix/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | "legend" \| "label" | True | 24 |
| children | React.ReactNode | True | 140 |
| errors | Array<{ message?: string } \| undefined> | True | 168 |
| message | string | True | 168 |

### Defaults and motion

- Default `variant` = `"legend"` (line 22).
- Default `orientation` = `"vertical"` (line 66).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/new-york-v4/ui/field.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/field.tsx); SHA-256 `59feca78767d6e34be8766e6461fb00dd5c10d7485c642d4c73c0349c8634f95`; 249 lines.

Imports: `react`, `class-variance-authority`, `cn`, `@/registry/new-york-v4/ui/label`, `@/registry/new-york-v4/ui/separator`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | "legend" \| "label" | True | 28 |
| children | React.ReactNode | True | 161 |
| errors | Array<{ message?: string } \| undefined> | True | 192 |
| message | string | True | 192 |

### Defaults and motion

- Default `variant` = `"legend"` (line 26).
- Default `orientation` = `"vertical"` (line 83).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
