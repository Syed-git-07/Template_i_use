# code-block

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/code-block/components/ui/code-block.tsx

[Original source](https://ui.aceternity.com/registry/code-block.json); SHA-256 `3715eb017b80e5c019db8d60a22c1d0e72390cc6c17ec958bd9358548a19b076`; 115 lines.

Imports: `react`, `react-syntax-highlighter`, `react-syntax-highlighter/dist/cjs/styles/prism`, `@tabler/icons-react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| language | string | False | 8 |
| filename | string | False | 9 |
| highlightLines | number[] | True | 10 |
| code | string | False | 13 |
| tabs | never | True | 14 |
| code | never | True | 17 |
| tabs | Array<{         name: string;         code: string;         language?: string;         highlightLines?: number[];       }> | False | 18 |
| name | string | False | 19 |
| code | string | False | 20 |
| language | string | True | 21 |
| highlightLines | number[] | True | 22 |

### Defaults and motion


### Input, style and lifecycle

Events: onClick (line 64); onClick (line 80).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
