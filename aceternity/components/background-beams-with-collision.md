# background-beams-with-collision

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/background-beams-with-collision/components/ui/background-beams-with-collision.tsx

[Original source](https://ui.aceternity.com/registry/background-beams-with-collision.json); SHA-256 `ef1b5d0b32cae6f127773efd227938673d7df5dd10fb61381494b1bb5de0aa54`; 260 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 10 |
| className | string | True | 11 |
| containerRef | React.RefObject<HTMLDivElement> | False | 103 |
| parentRef | React.RefObject<HTMLDivElement> | False | 104 |
| beamOptions | {       initialX?: number;       translateX?: number;       initialY?: number;       translateY?: number;       rotate?: number;       className?: string;       duration?: number;       delay?: number;       repeatDelay?: number;     } | True | 105 |
| initialX | number | True | 106 |
| translateX | number | True | 107 |
| initialY | number | True | 108 |
| translateY | number | True | 109 |
| rotate | number | True | 110 |
| className | string | True | 111 |
| duration | number | True | 112 |
| delay | number | True | 113 |
| repeatDelay | number | True | 114 |
| detected | boolean | False | 120 |
| coordinates | { x: number; y: number } \| null | False | 121 |
| x | number | False | 121 |
| y | number | False | 121 |

### Defaults and motion

- `duration`: 7 (line 20).
- `delay`: 2 (line 22).
- `duration`: 3 (line 27).
- `delay`: 4 (line 29).
- `duration`: 7 (line 34).
- `duration`: 5 (line 41).
- `delay`: 4 (line 43).
- `duration`: 11 (line 48).
- `duration`: 4 (line 55).
- `duration`: 6 (line 62).
- `delay`: 2 (line 64).
- `duration`: computed; inspect expression (line 195).
- `ease`: "linear" (line 198).
- `delay`: computed; inspect expression (line 199).
- `duration`: 1.5 (line 241).
- `ease`: "easeOut" (line 241).
- `duration`: computed; inspect expression (line 253).
- `ease`: "easeOut" (line 253).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
