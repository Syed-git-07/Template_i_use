# sidebar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/sidebar/components/ui/sidebar.tsx

[Original source](https://ui.aceternity.com/registry/sidebar.json); SHA-256 `0ff0812bd2e8ee8fb98d516004c46dfecd7d5bd2cf03b191c1a8d983d815d0ef`; 189 lines.

Imports: `@/lib/utils`, `react`, `motion/react`, `@tabler/icons-react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| label | string | False | 8 |
| href | string | False | 9 |
| icon | React.JSX.Element \| React.ReactNode | False | 10 |
| open | boolean | False | 14 |
| setOpen | React.Dispatch<React.SetStateAction<boolean>> | False | 15 |
| animate | boolean | False | 16 |
| children | React.ReactNode | False | 37 |
| open | boolean | True | 38 |
| setOpen | React.Dispatch<React.SetStateAction<boolean>> | True | 39 |
| animate | boolean | True | 40 |
| children | React.ReactNode | False | 60 |
| open | boolean | True | 61 |
| setOpen | React.Dispatch<React.SetStateAction<boolean>> | True | 62 |
| animate | boolean | True | 63 |
| link | Links | False | 162 |
| className | string | True | 163 |

### Defaults and motion

- Default `animate` = `true` (line 35).
- `duration`: 0.3 (line 134).
- `ease`: "easeInOut" (line 135).

### Input, style and lifecycle

Events: onMouseEnter (line 97); onMouseLeave (line 98); onClick (line 124); onClick (line 144).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
