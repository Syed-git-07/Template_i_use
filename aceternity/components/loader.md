# loader

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/loader/components/ui/loader.tsx

[Original source](https://ui.aceternity.com/registry/loader.json); SHA-256 `571e40326045bd67d54a4aede52ca6a2db4bfd5685eca0d2ec9e193b2a0243bb`; 217 lines.

Imports: `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | True | 127 |
| text | string | False | 185 |

### Defaults and motion

- Default `text` = `"Loading..."` (line 127).
- `duration`: 1 (line 8).
- `delay`: computed; inspect expression (line 11).
- `ease`: computed; inspect expression (line 12).
- `duration`: 2 (line 54).
- `delay`: computed; inspect expression (line 57).
- `ease`: computed; inspect expression (line 58).
- `duration`: 2 (line 116).
- `ease`: computed; inspect expression (line 117).
- `duration`: 0.05 (line 136).
- `ease`: computed; inspect expression (line 140).
- `duration`: 0.5 (line 155).
- `ease`: computed; inspect expression (line 158).
- `duration`: 0.8 (line 172).
- `ease`: computed; inspect expression (line 175).
- `duration`: 0.5 (line 203).
- `delay`: computed; inspect expression (line 206).
- `ease`: computed; inspect expression (line 207).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
