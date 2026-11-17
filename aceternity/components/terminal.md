# terminal

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/terminal/components/ui/terminal.tsx

[Original source](https://ui.aceternity.com/registry/terminal.json); SHA-256 `a82abc1d669625f53e7465cc658276681ab0edf2b1005ace4b6d96599eb3fbbc`; 524 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| type | TokenType | False | 211 |
| value | string | False | 212 |
| text | string | False | 292 |
| type | "command" \| "output" | False | 307 |
| content | string | False | 308 |
| commands | string[] | False | 312 |
| outputs | Record<number, string[]> | True | 313 |
| username | string | True | 314 |
| className | string | True | 315 |
| typingSpeed | number | True | 316 |
| delayBetweenCommands | number | True | 317 |
| initialDelay | number | True | 318 |
| enableSound | boolean | True | 319 |

### Defaults and motion

- Default `username` = `"Manus-Macbook"` (line 325).
- Default `typingSpeed` = `50` (line 327).
- Default `delayBetweenCommands` = `800` (line 328).
- Default `initialDelay` = `500` (line 329).
- Default `enableSound` = `true` (line 330).
- `threshold`: 0.1 (line 190).

### Input, style and lifecycle

Events: click (line 141); keydown (line 142).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, async, visibility.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
