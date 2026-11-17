# floating-navbar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/floating-navbar/components/ui/floating-navbar.tsx

[Original source](https://ui.aceternity.com/registry/floating-navbar.json); SHA-256 `9ab6f04dcc3bbf02d37db3478034af412e6166a3fb76f4889ca36e29cf4e558b`; 89 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| navItems | {     name: string;     link: string;     icon?: JSX.Element;   }[] | False | 15 |
| name | string | False | 16 |
| link | string | False | 17 |
| icon | JSX.Element | True | 18 |
| className | string | True | 20 |

### Defaults and motion

- `duration`: 0.2 (line 53).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
