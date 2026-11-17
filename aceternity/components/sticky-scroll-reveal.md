# sticky-scroll-reveal

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/sticky-scroll-reveal/components/ui/sticky-scroll-reveal.tsx

[Original source](https://ui.aceternity.com/registry/sticky-scroll-reveal.json); SHA-256 `93dc4f8da9225f1df23bcf7e2567c1267062340ea00f91e0d8ed3573f711bce5`; 113 lines.

Imports: `react`, `motion/react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| content | {     title: string;     description: string;     content?: React.ReactNode \| any;   }[] | False | 11 |
| title | string | False | 12 |
| description | string | False | 13 |
| content | React.ReactNode \| any | True | 14 |
| contentClassName | string | True | 16 |

### Defaults and motion


### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
