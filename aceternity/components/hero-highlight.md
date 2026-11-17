# hero-highlight

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/hero-highlight/components/ui/hero-highlight.tsx

[Original source](https://ui.aceternity.com/registry/hero-highlight.json); SHA-256 `22ba0ea6a206dfef79d266c296eac3d542df6cbfa1378a977d4986b00f575616`; 141 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 11 |
| className | string | True | 12 |
| containerClassName | string | True | 13 |
| children | React.ReactNode | False | 111 |
| className | string | True | 112 |

### Defaults and motion

- `duration`: 2 (line 123).
- `ease`: "linear" (line 124).
- `delay`: 0.5 (line 125).

### Input, style and lifecycle

Events: onMouseMove (line 47).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
