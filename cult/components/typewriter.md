# typewriter

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/typewriter.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/typewriter.tsx); SHA-256 `9e0d9f9602a196cffb2fa3c2ff2c5249f24f5aa40bd61dabfc0cf6ff42c2cc88`; 120 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| delay | number | False | 7 |
| texts | string[] | False | 8 |
| baseText | string | True | 9 |
| delay | number | False | 45 |
| texts | string[] | False | 46 |

### Defaults and motion

- Default `baseText` = `""` (line 12).
- `duration`: 1 (line 24).
- `ease`: computed; inspect expression (line 25).
- `duration`: 1 (line 76).
- `ease`: computed; inspect expression (line 77).
- `duration`: 1 (line 102).
- `ease`: computed; inspect expression (line 105).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 101.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
