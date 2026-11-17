# tabs

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/tabs/components/ui/tabs.tsx

[Original source](https://ui.aceternity.com/registry/tabs.json); SHA-256 `0d34660aeb2d49d912b1216343bf7a86edf6dc2e0eb097ad53c30068e6950a71`; 125 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| title | string | False | 8 |
| value | string | False | 9 |
| content | string \| React.ReactNode \| any | True | 10 |
| tabs | Tab[] | False | 20 |
| containerClassName | string | True | 21 |
| activeTabClassName | string | True | 22 |
| tabClassName | string | True | 23 |
| contentClassName | string | True | 24 |
| className | string | True | 93 |
| key | string | True | 94 |
| tabs | Tab[] | False | 95 |
| active | Tab | False | 96 |
| hovering | boolean | True | 97 |

### Defaults and motion

- `bounce`: 0.3 (line 63).
- `duration`: 0.6 (line 63).

### Input, style and lifecycle

Events: onClick (line 50); onMouseEnter (line 53); onMouseLeave (line 54).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
