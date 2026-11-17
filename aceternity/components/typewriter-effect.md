# typewriter-effect

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/typewriter-effect/components/ui/typewriter-effect.tsx

[Original source](https://ui.aceternity.com/registry/typewriter-effect.json); SHA-256 `9954fcc8d561014f650aeee24b1dc712bcd8da4292480e2c013dc47ebdb8d112`; 188 lines.

Imports: `@/lib/utils`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| words | {     text: string;     className?: string;   }[] | False | 12 |
| text | string | False | 13 |
| className | string | True | 14 |
| className | string | True | 16 |
| cursorClassName | string | True | 17 |
| words | {     text: string;     className?: string;   }[] | False | 106 |
| text | string | False | 107 |
| className | string | True | 108 |
| className | string | True | 110 |
| cursorClassName | string | True | 111 |

### Defaults and motion

- `duration`: 0.3 (line 39).
- `delay`: computed; inspect expression (line 40).
- `ease`: "easeInOut" (line 41).
- `duration`: 0.8 (line 88).
- `duration`: 2 (line 153).
- `ease`: "linear" (line 154).
- `delay`: 1 (line 155).
- `duration`: 0.8 (line 175).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
