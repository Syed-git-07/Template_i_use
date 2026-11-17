# 3d-marquee

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/3d-marquee/components/ui/3d-marquee.tsx

[Original source](https://ui.aceternity.com/registry/3d-marquee.json); SHA-256 `49265fb39272e876a3ff8ce5a1b4b8b5921ad5b266ad74bf270a74c6b8332886`; 143 lines.

Imports: `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| images | string[] | False | 9 |
| className | string | True | 10 |
| className | string | True | 78 |
| offset | string | True | 79 |
| className | string | True | 113 |
| offset | string | True | 114 |

### Defaults and motion

- `duration`: computed; inspect expression (line 37).
- `duration`: 0.3 (line 53).
- `ease`: "easeInOut" (line 54).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 85, 99, 120, 134.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
