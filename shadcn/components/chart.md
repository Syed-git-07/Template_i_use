# chart

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/chart.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/chart.tsx); SHA-256 `c448ea1d5a356b2aebd68d3e62cbeb96a354e778e8a45ee8677712b12033fba7`; 371 lines.

Imports: `react`, `cn`, `recharts`, `recharts`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| label | React.ReactNode | True | 17 |
| icon | React.ComponentType | True | 18 |
| color | string | True | 20 |
| theme | never | True | 20 |
| color | never | True | 21 |
| theme | Record<keyof typeof THEMES, string> | False | 21 |
| config | ChartConfig | False | 26 |
| config | ChartConfig | False | 49 |
| children | React.ComponentProps<     typeof RechartsPrimitive.ResponsiveContainer   >["children"] | False | 50 |
| initialDimension | {     width: number     height: number   } | True | 53 |
| width | number | False | 54 |
| height | number | False | 55 |
| id | string | False | 83 |
| config | ChartConfig | False | 83 |
| hideLabel | boolean | True | 134 |
| hideIndicator | boolean | True | 135 |
| indicator | "line" \| "dot" \| "dashed" | True | 136 |
| nameKey | string | True | 137 |
| labelKey | string | True | 138 |
| hideIcon | boolean | True | 278 |
| nameKey | string | True | 279 |

### Defaults and motion

- Default `indicator` = `"dot"` (line 122).
- Default `hideLabel` = `false` (line 123).
- Default `hideIndicator` = `false` (line 124).
- Default `hideIcon` = `false` (line 273).
- Default `verticalAlign` = `"bottom"` (line 275).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/base/ui/chart.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/chart.tsx); SHA-256 `2f66d2084d5f30b681d1716a3b641d1cc60c566f9b4a98a383414f4ecac562ae`; 370 lines.

Imports: `react`, `cn`, `recharts`, `recharts`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| label | React.ReactNode | True | 17 |
| icon | React.ComponentType | True | 18 |
| color | string | True | 20 |
| theme | never | True | 20 |
| color | never | True | 21 |
| theme | Record<keyof typeof THEMES, string> | False | 21 |
| config | ChartConfig | False | 26 |
| config | ChartConfig | False | 49 |
| children | React.ComponentProps<     typeof RechartsPrimitive.ResponsiveContainer   >["children"] | False | 50 |
| initialDimension | {     width: number     height: number   } | True | 53 |
| width | number | False | 54 |
| height | number | False | 55 |
| id | string | False | 83 |
| config | ChartConfig | False | 83 |
| hideLabel | boolean | True | 134 |
| hideIndicator | boolean | True | 135 |
| indicator | "line" \| "dot" \| "dashed" | True | 136 |
| nameKey | string | True | 137 |
| labelKey | string | True | 138 |
| hideIcon | boolean | True | 278 |
| nameKey | string | True | 279 |

### Defaults and motion

- Default `indicator` = `"dot"` (line 122).
- Default `hideLabel` = `false` (line 123).
- Default `hideIndicator` = `false` (line 124).
- Default `hideIcon` = `false` (line 273).
- Default `verticalAlign` = `"bottom"` (line 275).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/bases/radix/ui/chart.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/chart.tsx); SHA-256 `2f66d2084d5f30b681d1716a3b641d1cc60c566f9b4a98a383414f4ecac562ae`; 370 lines.

Imports: `react`, `cn`, `recharts`, `recharts`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| label | React.ReactNode | True | 17 |
| icon | React.ComponentType | True | 18 |
| color | string | True | 20 |
| theme | never | True | 20 |
| color | never | True | 21 |
| theme | Record<keyof typeof THEMES, string> | False | 21 |
| config | ChartConfig | False | 26 |
| config | ChartConfig | False | 49 |
| children | React.ComponentProps<     typeof RechartsPrimitive.ResponsiveContainer   >["children"] | False | 50 |
| initialDimension | {     width: number     height: number   } | True | 53 |
| width | number | False | 54 |
| height | number | False | 55 |
| id | string | False | 83 |
| config | ChartConfig | False | 83 |
| hideLabel | boolean | True | 134 |
| hideIndicator | boolean | True | 135 |
| indicator | "line" \| "dot" \| "dashed" | True | 136 |
| nameKey | string | True | 137 |
| labelKey | string | True | 138 |
| hideIcon | boolean | True | 278 |
| nameKey | string | True | 279 |

### Defaults and motion

- Default `indicator` = `"dot"` (line 122).
- Default `hideLabel` = `false` (line 123).
- Default `hideIndicator` = `false` (line 124).
- Default `hideIcon` = `false` (line 273).
- Default `verticalAlign` = `"bottom"` (line 275).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## apps/v4/registry/new-york-v4/ui/chart.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/chart.tsx); SHA-256 `f5b9bf1ebc9054fe05add9ad1f92a22c89c6ac18f4ed4bc4bc1dc4bfe1837d70`; 374 lines.

Imports: `react`, `cn`, `recharts`, `recharts`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| label | React.ReactNode | True | 17 |
| icon | React.ComponentType | True | 18 |
| color | string | True | 20 |
| theme | never | True | 20 |
| color | never | True | 21 |
| theme | Record<keyof typeof THEMES, string> | False | 21 |
| config | ChartConfig | False | 26 |
| config | ChartConfig | False | 49 |
| children | React.ComponentProps<     typeof RechartsPrimitive.ResponsiveContainer   >["children"] | False | 50 |
| initialDimension | {     width: number     height: number   } | True | 53 |
| width | number | False | 54 |
| height | number | False | 55 |
| id | string | False | 83 |
| config | ChartConfig | False | 83 |
| hideLabel | boolean | True | 134 |
| hideIndicator | boolean | True | 135 |
| indicator | "line" \| "dot" \| "dashed" | True | 136 |
| nameKey | string | True | 137 |
| labelKey | string | True | 138 |
| hideIcon | boolean | True | 281 |
| nameKey | string | True | 282 |

### Defaults and motion

- Default `indicator` = `"dot"` (line 122).
- Default `hideLabel` = `false` (line 123).
- Default `hideIndicator` = `false` (line 124).
- Default `hideIcon` = `false` (line 276).
- Default `verticalAlign` = `"bottom"` (line 278).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
