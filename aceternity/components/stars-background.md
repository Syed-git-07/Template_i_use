# stars-background

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/stars-background/components/ui/stars-background.tsx

[Original source](https://ui.aceternity.com/registry/stars-background.json); SHA-256 `82801c3eb4f966e6e31a6c24ab629137e7e6db14dfcc142553ccc33821fde3c6`; 144 lines.

Imports: `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| x | number | False | 12 |
| y | number | False | 13 |
| radius | number | False | 14 |
| opacity | number | False | 15 |
| twinkleSpeed | number \| null | False | 16 |
| starDensity | number | True | 20 |
| allStarsTwinkle | boolean | True | 21 |
| twinkleProbability | number | True | 22 |
| minTwinkleSpeed | number | True | 23 |
| maxTwinkleSpeed | number | True | 24 |
| className | string | True | 25 |

### Defaults and motion

- Default `starDensity` = `0.00015` (line 29).
- Default `allStarsTwinkle` = `true` (line 30).
- Default `twinkleProbability` = `0.7` (line 31).
- Default `minTwinkleSpeed` = `0.5` (line 32).
- Default `maxTwinkleSpeed` = `1` (line 33).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, resize.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
