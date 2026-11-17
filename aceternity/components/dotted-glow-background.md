# dotted-glow-background

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/dotted-glow-background/components/ui/dotted-glow-background.tsx

[Original source](https://ui.aceternity.com/registry/dotted-glow-background.json); SHA-256 `12820db19fead2d91f374165389258f28ff45633cc893974e80eb65036e649f1`; 321 lines.

Imports: `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| className | string | True | 6 |
| gap | number | True | 8 |
| radius | number | True | 10 |
| color | string | True | 12 |
| darkColor | string | True | 14 |
| glowColor | string | True | 16 |
| darkGlowColor | string | True | 18 |
| colorLightVar | string | True | 20 |
| colorDarkVar | string | True | 22 |
| glowColorLightVar | string | True | 24 |
| glowColorDarkVar | string | True | 26 |
| opacity | number | True | 28 |
| backgroundOpacity | number | True | 30 |
| speedMin | number | True | 32 |
| speedMax | number | True | 34 |
| speedScale | number | True | 36 |
| x | number | False | 179 |
| y | number | False | 179 |
| phase | number | False | 179 |
| speed | number | False | 179 |

### Defaults and motion

- Default `gap` = `12` (line 47).
- Default `radius` = `2` (line 48).
- Default `color` = `"rgba(0,0,0,0.7)"` (line 49).
- Default `glowColor` = `"rgba(0, 170, 255, 0.85)"` (line 51).
- Default `opacity` = `0.6` (line 57).
- Default `backgroundOpacity` = `0` (line 58).
- Default `speedMin` = `0.4` (line 59).
- Default `speedMax` = `1.3` (line 60).
- Default `speedScale` = `1` (line 61).
- `threshold`: 0.1 (line 282).

### Input, style and lifecycle

Events: change (line 128); resize (line 286).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, resize, visibility.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
