# family-drawer

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/family-drawer.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/family-drawer.tsx); SHA-256 `5fd592bc1e811291a0c802f9371aaa00c54d5d96dac365b25988dc16ec74c86c`; 582 lines.

Imports: `react`, `@radix-ui/react-slot`, `motion/react`, `react-use-measure`, `vaul`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isOpen | boolean | False | 33 |
| view | string | False | 34 |
| setView | (view: string) => void | False | 35 |
| opacityDuration | number | False | 36 |
| elementRef | ReturnType<typeof useMeasure>[0] | False | 37 |
| bounds | ReturnType<typeof useMeasure>[1] | False | 38 |
| views | ViewsRegistry \| undefined | False | 39 |
| children | ReactNode | False | 61 |
| open | boolean | True | 62 |
| defaultOpen | boolean | True | 63 |
| onOpenChange | (open: boolean) => void | True | 64 |
| defaultView | string | True | 65 |
| onViewChange | (view: string) => void | True | 66 |
| views | ViewsRegistry | True | 67 |
| children | ReactNode | False | 143 |
| asChild | boolean | True | 144 |
| className | string | True | 145 |
| children | ReactNode | False | 180 |
| className | string | True | 189 |
| onClick | () => void | True | 190 |
| children | ReactNode | False | 209 |
| className | string | True | 210 |
| asChild | boolean | True | 211 |
| children | ReactNode | False | 267 |
| className | string | True | 268 |
| children | ReactNode | False | 292 |
| children | ReactNode | True | 323 |
| asChild | boolean | True | 324 |
| className | string | True | 325 |
| icon | ReactNode | False | 401 |
| title | string | False | 402 |
| description | string | False | 403 |
| className | string | True | 404 |
| children | ReactNode | False | 425 |
| onClick | () => void | False | 426 |
| className | string | True | 427 |
| asChild | boolean | True | 428 |
| children | ReactNode | False | 459 |
| onClick | () => void | False | 460 |
| className | string | False | 461 |
| asChild | boolean | True | 462 |
| views | ViewsRegistry | True | 497 |

### Defaults and motion

- Default `defaultOpen` = `false` (line 73).
- Default `defaultView` = `"default"` (line 75).
- Default `asChild` = `false` (line 150).
- Default `asChild` = `false` (line 217).
- Default `asChild` = `false` (line 330).
- Default `asChild` = `false` (line 435).
- Default `asChild` = `false` (line 469).
- `duration`: 0.27 (line 226).
- `ease`: computed; inspect expression (line 227).
- `duration`: computed; inspect expression (line 308).
- `ease`: computed; inspect expression (line 309).

### Input, style and lifecycle

Events: onOpenChange (line 131); onClick (line 199); onClick (line 444); onClick (line 479).

Typography/style anchors: 225.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
