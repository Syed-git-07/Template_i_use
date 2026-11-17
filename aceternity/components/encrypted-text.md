# encrypted-text

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/encrypted-text/components/ui/encrypted-text.tsx

[Original source](https://ui.aceternity.com/registry/encrypted-text.json); SHA-256 `90c8efe74118294f8ddf39ced79178182946e469eec88fd4d531efc5d8e0d76b`; 157 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| text | string | False | 7 |
| className | string | True | 8 |
| revealDelayMs | number | True | 13 |
| charset | string | True | 15 |
| flipDelayMs | number | True | 20 |
| encryptedClassName | string | True | 22 |
| revealedClassName | string | True | 24 |

### Defaults and motion

- Default `revealDelayMs` = `50` (line 51).
- Default `flipDelayMs` = `50` (line 53).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
