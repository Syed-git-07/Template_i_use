# marker

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/marker.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/marker.tsx); SHA-256 `af0af00b92e73c8f640cf1604d400a79026cf2c7886cd9af48745a7fbab89572`; 74 lines.

Imports: `react`, `class-variance-authority`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| render | (props: React.HTMLAttributes<HTMLElement>) => React.ReactNode | True | 26 |

### Defaults and motion

- Default `variant` = `"default"` (line 20).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/marker.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/marker.tsx); SHA-256 `bba7a502df626c85d3f56e5900bd63a79944391b1c6480cedea2ca25ffe7483c`; 64 lines.

Imports: `react`, `@base-ui/react/merge-props`, `@base-ui/react/use-render`, `class-variance-authority`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |

Props may be inherited from a primitive, inferred from a function, or defined in another file. Read the original and dependency API; absence here is not absence of props.

### Defaults and motion

- Default `variant` = `"default"` (line 22).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/radix/ui/marker.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/marker.tsx); SHA-256 `756d6f16f4c9ba3794af762764f532de8a93ba1d6bedab0c17870ff0f7f70d80`; 62 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 26 |

### Defaults and motion

- Default `variant` = `"default"` (line 21).
- Default `asChild` = `false` (line 22).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/new-york-v4/ui/marker.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/marker.tsx); SHA-256 `bafd4ef79b0fbeca82ad1e9b30e7efbe357b0fcffd5ffead11d7a0298a7ee315`; 69 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 27 |

### Defaults and motion

- Default `variant` = `"default"` (line 22).
- Default `asChild` = `false` (line 23).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
