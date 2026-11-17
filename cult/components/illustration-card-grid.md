# illustration-card-grid

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/illustration-card-grid.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/illustration-card-grid.tsx); SHA-256 `c1722922626544db12ce4062b214b65e0ab4c5a88d74f4a466ea4c27611cfb1c`; 135 lines.

Imports: `react`, `@/lib/utils`, `@/registry/default/ui/gateway-endpoint-illustration`, `@/registry/default/ui/gateway-route-illustration`, `@/registry/default/ui/gateway-svg-illustration`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | True | 9 |
| title | ReactNode | False | 10 |
| description | ReactNode | False | 11 |
| illustration | ReactNode | False | 12 |
| className | string | True | 13 |
| contentClassName | string | True | 14 |
| titleClassName | string | True | 15 |
| descriptionClassName | string | True | 16 |
| illustrationClassName | string | True | 17 |
| items | IllustrationCardGridItem[] | True | 21 |
| cardClassName | string | True | 22 |
| contentClassName | string | True | 23 |
| titleClassName | string | True | 24 |
| descriptionClassName | string | True | 25 |
| illustrationClassName | string | True | 26 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
