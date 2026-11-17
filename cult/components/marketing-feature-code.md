# marketing-feature-code

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/marketing-feature-code.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/marketing-feature-code.tsx); SHA-256 `b580446801a0310aa8a4c5cc3ed99ee7774389497d3132290ec6082d9f01b658`; 541 lines.

Imports: `react`, `lucide-react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| icon | LucideIcon | False | 17 |
| title | string | False | 18 |
| description | string | False | 19 |
| codeToCopy | string | True | 254 |
| features | NetworkPolicyFeature[] | True | 383 |

### Defaults and motion


### Input, style and lifecycle

Events: onClick (line 281).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: async, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
