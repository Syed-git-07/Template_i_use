# ascii-art

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/ascii-art/components/ui/ascii-art.tsx

[Original source](https://ui.aceternity.com/registry/ascii-art.json); SHA-256 `6d5c526aafc3b87ce0447b91a7c73cd7bca0b4d3f5c652ab481c412653827baa`; 516 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| src | string | False | 68 |
| resolution | number | True | 70 |
| charset | CharsetPreset \| string | True | 72 |
| color | string | True | 74 |
| backgroundColor | string | True | 76 |
| inverted | boolean | True | 78 |
| colored | boolean | True | 80 |
| animated | boolean | True | 82 |
| animationStyle | "fade" \| "typewriter" \| "matrix" \| "none" | True | 84 |
| animationDuration | number | True | 86 |
| fontFamily | string | True | 88 |
| className | string | True | 90 |
| animateOnView | boolean | True | 92 |
| objectFit | "cover" \| "contain" \| "fill" | True | 94 |
| char | string | False | 99 |
| r | number | False | 100 |
| g | number | False | 101 |
| b | number | False | 102 |

### Defaults and motion

- Default `resolution` = `80` (line 107).
- Default `charset` = `"standard"` (line 108).
- Default `color` = `"#ffffff"` (line 109).
- Default `backgroundColor` = `"transparent"` (line 110).
- Default `inverted` = `false` (line 111).
- Default `colored` = `false` (line 112).
- Default `animated` = `true` (line 113).
- Default `animationStyle` = `"fade"` (line 114).
- Default `animationDuration` = `1` (line 115).
- Default `fontFamily` = `"monospace"` (line 116).
- Default `animateOnView` = `true` (line 118).
- Default `objectFit` = `"cover"` (line 119).
- `duration`: computed; inspect expression (line 493).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 88, 116, 294, 352.

Source signals: cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
