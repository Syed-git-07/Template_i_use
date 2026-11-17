# marketing-hero-analytics

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/marketing-hero-analytics.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/marketing-hero-analytics.tsx); SHA-256 `c409111a13577d70fdb3b9c954520ecb93a1ae33a7eccc0b666d78b3ae7ba8d0`; 1166 lines.

Imports: `react`, `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| label | string | False | 9 |
| value | number | False | 10 |
| name | string | False | 23 |
| visitors | number | False | 24 |
| icon | AnalyticsHeroSourceIconKey | False | 25 |
| time | string | False | 29 |
| rt | "mw" \| "fe" | False | 30 |
| method | string | False | 31 |
| status | number | False | 32 |
| path | string | False | 33 |
| cols | number | False | 305 |
| rows | number | False | 306 |
| data | AnalyticsHeroChartDatum[] | False | 359 |
| hovered | number \| null | False | 360 |
| onHover | (index: number \| null) => void | False | 361 |
| data | AnalyticsHeroChartDatum[] | False | 486 |
| index | number \| null | False | 487 |
| containerRef | React.RefObject<HTMLDivElement \| null> | False | 488 |
| sectionRef | React.RefObject<HTMLElement \| null> | False | 489 |
| logs | AnalyticsHeroLog[] | False | 575 |
| timestamp | string | True | 576 |
| sources | AnalyticsHeroSource[] | False | 723 |
| visible | boolean | False | 839 |
| title | string | True | 840 |
| description | string | True | 841 |
| deployLabel | string | True | 842 |
| demoLabel | string | True | 843 |
| logs | AnalyticsHeroLog[] | False | 976 |
| sources | AnalyticsHeroSource[] | False | 977 |
| data | AnalyticsHeroChartDatum[] | True | 1011 |
| sources | AnalyticsHeroSource[] | True | 1012 |
| logs | AnalyticsHeroLog[] | True | 1013 |
| logsTimestamp | string | True | 1014 |
| title | string | True | 1015 |
| description | string | True | 1016 |
| deployLabel | string | True | 1017 |
| demoLabel | string | True | 1018 |

### Defaults and motion

- Default `timestamp` = `"13:39"` (line 581).
- Default `title` = `"Understand production from the inside out."` (line 848).
- Default `description` = `"With real-time infrastructure and traffic insights, Vercel is the mission control for frontend applications."` (line 849).
- Default `deployLabel` = `"Deploy Now"` (line 850).
- Default `demoLabel` = `"Get a Demo"` (line 851).

### Input, style and lifecycle

Events: onMouseLeave (line 391); onMouseMove (line 392); onHover (line 1101).

Typography/style anchors: 475, 522, 599, 623, 646, 676, 694, 746, 880, 897, 912, 931, 964, 1067, 1095, 1117.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
