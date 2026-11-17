# hover-border-gradient

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/hover-border-gradient/components/ui/hover-border-gradient.tsx

[Original source](https://ui.aceternity.com/registry/hover-border-gradient.json); SHA-256 `587453eb0ab551fe3ac444ea017d4e9620a212ef5dde20dd943619db5850d0a7`; 100 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| as | React.ElementType | True | 19 |
| containerClassName | string | True | 20 |
| className | string | True | 21 |
| duration | number | True | 22 |
| clockwise | boolean | True | 23 |

### Defaults and motion

- Default `Tag` = `"button"` (line 13).
- Default `duration` = `1` (line 14).
- Default `clockwise` = `true` (line 15).
- `ease`: "linear" (line 94).
- `duration`: computed; inspect expression (line 94).

### Input, style and lifecycle

Events: onMouseEnter (line 60); onMouseLeave (line 63).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
