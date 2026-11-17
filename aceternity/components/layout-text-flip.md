# layout-text-flip

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/layout-text-flip/components/ui/layout-text-flip.tsx

[Original source](https://ui.aceternity.com/registry/layout-text-flip.json); SHA-256 `7eb45448a2815b4f86492cf6192ff5a9ae4c15cd995b9a70199b7f40ba5393d4`; 59 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 11 |
| words | string[] | False | 12 |
| duration | number | True | 13 |

### Defaults and motion

- Default `text` = `"Build Amazing"` (line 7).
- Default `duration` = `3000` (line 9).
- `duration`: 0.5 (line 48).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
