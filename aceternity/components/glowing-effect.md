# glowing-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/glowing-effect/components/ui/glowing-effect.tsx

[Original source](https://ui.aceternity.com/registry/glowing-effect.json); SHA-256 `9d987ef5daada143f84daa1b51261934e4462c14ffb77303b3063575864ba0af`; 191 lines.

Imports: `react`, `@/lib/utils`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| blur | number | True | 8 |
| inactiveZone | number | True | 9 |
| proximity | number | True | 10 |
| spread | number | True | 11 |
| variant | "default" \| "white" | True | 12 |
| glow | boolean | True | 13 |
| className | string | True | 14 |
| disabled | boolean | True | 15 |
| movementDuration | number | True | 16 |
| borderWidth | number | True | 17 |
| x | number | False | 37 |
| y | number | False | 37 |

### Defaults and motion

- Default `blur` = `0` (line 21).
- Default `inactiveZone` = `0.7` (line 22).
- Default `proximity` = `0` (line 23).
- Default `spread` = `20` (line 24).
- Default `variant` = `"default"` (line 25).
- Default `glow` = `false` (line 26).
- Default `movementDuration` = `2` (line 28).
- Default `borderWidth` = `1` (line 29).
- Default `disabled` = `true` (line 30).
- `duration`: computed; inspect expression (line 89).
- `ease`: computed; inspect expression (line 90).

### Input, style and lifecycle

Events: scroll (line 106); pointermove (line 107).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
