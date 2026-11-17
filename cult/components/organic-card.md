# organic-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/organic-card.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/organic-card.tsx); SHA-256 `a0194b527af2519b882725dc4e364b9c2afc91b295a08ca6cb73f0aec7b24fcd`; 308 lines.

Imports: `react`, `next/dist/shared/lib/get-img-props`, `next/image`, `next/link`, `lucide-react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| backgroundColor | string | False | 18 |
| children | ReactNode | False | 34 |
| backgroundColor | string | True | 35 |
| className | string | True | 36 |
| href | ComponentPropsWithoutRef<typeof Link>["href"] | False | 44 |
| href | never | True | 49 |
| src | string \| StaticImport | False | 133 |
| alt | string | True | 134 |

### Defaults and motion

- Default `backgroundColor` = `"hsl(var(--card))"` (line 70).
- Default `alt` = `"Card image"` (line 138).
- Default `height` = `208` (line 141).
- Default `width` = `670` (line 142).
- Default `children` = `"Read more"` (line 268).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
