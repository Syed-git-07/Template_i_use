# bubble

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/bubble.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/bubble.tsx); SHA-256 `63f2f5507296d00ff556709471638f7a11d0d2dfa37793e89450eaf3dd2d53f1`; 132 lines.

Imports: `react`, `class-variance-authority`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| align | "start" \| "end" | True | 42 |
| render | (props: React.HTMLAttributes<HTMLElement>) => React.ReactNode | True | 61 |
| align | "start" \| "end" | True | 117 |
| side | "top" \| "bottom" | True | 118 |

### Defaults and motion

- Default `variant` = `"default"` (line 36).
- Default `align` = `"start"` (line 37).
- Default `side` = `"bottom"` (line 112).
- Default `align` = `"end"` (line 113).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/base/ui/bubble.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/bubble.tsx); SHA-256 `7fffecd572b9572f79917695ccc9a3b27f3046d08e3084d859e56ec24f6456f8`; 121 lines.

Imports: `react`, `@base-ui/react/merge-props`, `@base-ui/react/use-render`, `class-variance-authority`, `cn`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| align | "start" \| "end" | True | 44 |
| align | "start" \| "end" | True | 106 |
| side | "top" \| "bottom" | True | 107 |

### Defaults and motion

- Default `variant` = `"default"` (line 38).
- Default `align` = `"start"` (line 39).
- Default `side` = `"bottom"` (line 101).
- Default `align` = `"end"` (line 102).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/bubble.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/bubble.tsx); SHA-256 `f578a972b92dfab11967a732ab84f50196893afcbec3e915261c6ed00d1c9c1a`; 118 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| align | "start" \| "end" | True | 43 |
| asChild | boolean | True | 61 |
| align | "start" \| "end" | True | 103 |
| side | "top" \| "bottom" | True | 104 |

### Defaults and motion

- Default `variant` = `"default"` (line 37).
- Default `align` = `"start"` (line 38).
- Default `asChild` = `false` (line 57).
- Default `side` = `"bottom"` (line 98).
- Default `align` = `"end"` (line 99).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/bubble.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/bubble.tsx); SHA-256 `dbd11d39c9bab692c4f2cc3181d45fbb179d63808b5bb8d239f2ed526a7b22f7`; 125 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| align | "start" \| "end" | True | 50 |
| asChild | boolean | True | 68 |
| align | "start" \| "end" | True | 110 |
| side | "top" \| "bottom" | True | 111 |

### Defaults and motion

- Default `variant` = `"default"` (line 44).
- Default `align` = `"start"` (line 45).
- Default `asChild` = `false` (line 64).
- Default `side` = `"bottom"` (line 105).
- Default `align` = `"end"` (line 106).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 24, 26.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
