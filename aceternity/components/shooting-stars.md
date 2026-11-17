# shooting-stars

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/shooting-stars/components/ui/shooting-stars.tsx

[Original source](https://ui.aceternity.com/registry/shooting-stars.json); SHA-256 `23da778568b618c0701b42f4b424335dfe7a0c82fe24c31a0e9ba16155fb1d38`; 147 lines.

Imports: `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | number | False | 6 |
| x | number | False | 7 |
| y | number | False | 8 |
| angle | number | False | 9 |
| scale | number | False | 10 |
| speed | number | False | 11 |
| distance | number | False | 12 |
| minSpeed | number | True | 16 |
| maxSpeed | number | True | 17 |
| minDelay | number | True | 18 |
| maxDelay | number | True | 19 |
| starColor | string | True | 20 |
| trailColor | string | True | 21 |
| starWidth | number | True | 22 |
| starHeight | number | True | 23 |
| className | string | True | 24 |

### Defaults and motion

- Default `minSpeed` = `10` (line 45).
- Default `maxSpeed` = `30` (line 46).
- Default `minDelay` = `1200` (line 47).
- Default `maxDelay` = `4200` (line 48).
- Default `starColor` = `"#9E00FF"` (line 49).
- Default `trailColor` = `"#2EB9DF"` (line 50).
- Default `starWidth` = `10` (line 51).
- Default `starHeight` = `1` (line 52).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
