# compare

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/compare/components/ui/compare.tsx

[Original source](https://ui.aceternity.com/registry/compare.json); SHA-256 `fd0801ffcb425cf02693aa7c9db752050d3e2aac2766a2bd8a0f4cb64fc16c08`; 241 lines.

Imports: `react`, `@/components/ui/sparkles`, `motion/react`, `@/lib/utils`, `@tabler/icons-react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| firstImage | string | True | 9 |
| secondImage | string | True | 10 |
| className | string | True | 11 |
| firstImageClassName | string | True | 12 |
| secondImageClassname | string | True | 13 |
| initialSliderPercentage | number | True | 14 |
| slideMode | "hover" \| "drag" | True | 15 |
| showHandlebar | boolean | True | 16 |
| autoplay | boolean | True | 17 |
| autoplayDuration | number | True | 18 |

### Defaults and motion

- Default `firstImage` = `""` (line 21).
- Default `secondImage` = `""` (line 22).
- Default `initialSliderPercentage` = `50` (line 26).
- Default `slideMode` = `"hover"` (line 27).
- Default `showHandlebar` = `true` (line 28).
- Default `autoplay` = `false` (line 29).
- Default `autoplayDuration` = `5000` (line 30).
- `duration`: 0 (line 175).
- `duration`: 0 (line 207).

### Input, style and lifecycle

Events: onMouseMove (line 158); onMouseLeave (line 159); onMouseEnter (line 160); onMouseDown (line 161); onMouseUp (line 162); onTouchStart (line 163); onTouchEnd (line 164); onTouchMove (line 165).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
