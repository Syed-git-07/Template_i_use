# 3d-card

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/3d-card/components/ui/3d-card.tsx

[Original source](https://ui.aceternity.com/registry/3d-card.json); SHA-256 `ec2f994a294aa81bb10d8a4a8512e1d9d90acdccf2fb1c8eadf83874c5be34e8`; 156 lines.

Imports: `@/lib/utils`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | True | 22 |
| className | string | True | 23 |
| containerClassName | string | True | 24 |
| children | React.ReactNode | False | 83 |
| className | string | True | 84 |
| as | React.ElementType | True | 110 |
| children | React.ReactNode | False | 111 |
| className | string | True | 112 |
| translateX | number \| string | True | 113 |
| translateY | number \| string | True | 114 |
| translateZ | number \| string | True | 115 |
| rotateX | number \| string | True | 116 |
| rotateY | number \| string | True | 117 |
| rotateZ | number \| string | True | 118 |

### Defaults and motion

- Default `Tag` = `"div"` (line 99).
- Default `translateX` = `0` (line 102).
- Default `translateY` = `0` (line 103).
- Default `translateZ` = `0` (line 104).
- Default `rotateX` = `0` (line 105).
- Default `rotateY` = `0` (line 106).
- Default `rotateZ` = `0` (line 107).

### Input, style and lifecycle

Events: onMouseEnter (line 61); onMouseMove (line 62); onMouseLeave (line 63).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
