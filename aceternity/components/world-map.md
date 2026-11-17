# world-map

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/world-map/components/ui/world-map.tsx

[Original source](https://ui.aceternity.com/registry/world-map.json); SHA-256 `a8cace90aee8b4fd3d2b14b74d4fca0583b10ac1b7112df9e5b9b6782948ef00`; 171 lines.

Imports: `react`, `motion/react`, `dotted-map`, `next-themes`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| dots | Array<{     start: { lat: number; lng: number; label?: string };     end: { lat: number; lng: number; label?: string };   }> | True | 10 |
| start | { lat: number; lng: number; label?: string } | False | 11 |
| lat | number | False | 11 |
| lng | number | False | 11 |
| label | string | True | 11 |
| end | { lat: number; lng: number; label?: string } | False | 12 |
| lat | number | False | 12 |
| lng | number | False | 12 |
| label | string | True | 12 |
| lineColor | string | True | 14 |
| x | number | False | 40 |
| y | number | False | 40 |
| x | number | False | 41 |
| y | number | False | 41 |

### Defaults and motion

- Default `lineColor` = `"#0ea5e9"` (line 19).
- `duration`: 1 (line 80).
- `delay`: computed; inspect expression (line 81).
- `ease`: "easeOut" (line 82).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
