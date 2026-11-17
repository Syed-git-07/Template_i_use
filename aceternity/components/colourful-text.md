# colourful-text

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/colourful-text/components/ui/colourful-text.tsx

[Original source](https://ui.aceternity.com/registry/colourful-text.json); SHA-256 `c3cdf9b013cc75b02855ef469b4a96da395e2c36396f6f7acd95b553c2e08ea5`; 55 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 5 |

### Defaults and motion

- `duration`: 0.5 (line 46).
- `delay`: computed; inspect expression (line 47).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
