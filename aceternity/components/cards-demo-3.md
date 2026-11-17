# cards-demo-3

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/cards-demo-3/components/cards-demo-3.tsx

[Original source](https://ui.aceternity.com/registry/cards-demo-3.json); SHA-256 `0c99d9471b79706c098b433d11b5f997a7354026acd5e5d4614d162b1f157469`; 360 lines.

Imports: `motion/react`, `react`, `@/lib/utils`, `react-icons/go`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 143 |
| children | React.ReactNode | False | 144 |
| children | React.ReactNode | False | 162 |
| className | string | True | 163 |
| children | React.ReactNode | False | 181 |
| className | string | True | 182 |
| className | string | True | 201 |
| children | React.ReactNode | False | 202 |
| showGradient | boolean | True | 203 |
| className | string | True | 223 |
| children | React.ReactNode | False | 224 |
| className | string | True | 240 |
| className | string | True | 262 |
| className | string | True | 278 |
| className | string | True | 308 |

### Defaults and motion

- Default `showGradient` = `true` (line 199).
- `duration`: 0.8 (line 32).
- `duration`: 0.8 (line 40).
- `duration`: 0.8 (line 48).
- `duration`: 0.8 (line 56).
- `duration`: 0.8 (line 64).
- `duration`: computed; inspect expression (line 119).
- `ease`: "linear" (line 121).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
