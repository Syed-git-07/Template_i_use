# feature-poll

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/feature-poll.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/feature-poll.tsx); SHA-256 `657adf3a3981b6ae5daa0166ed3b44a00b022fe81bc576d69f18af7c15354b91`; 748 lines.

Imports: `react`, `@radix-ui/react-use-controllable-state`, `class-variance-authority`, `lucide-react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string \| string[] | True | 26 |
| defaultValue | string \| string[] | True | 28 |
| onValueChange | (value: string \| string[]) => void | True | 30 |
| multiple | boolean | True | 32 |
| disabled | boolean | True | 34 |
| showResults | boolean | True | 36 |
| votes | Record<string, number> | True | 38 |
| hasVoted | boolean | True | 40 |
| value | string | False | 45 |
| disabled | boolean | True | 47 |
| totalVotes | number | True | 68 |
| selected | string[] | False | 76 |
| multiple | boolean | False | 77 |
| disabled | boolean | False | 78 |
| showResults | boolean | False | 79 |
| votes | Record<string, number> | False | 80 |
| totalVotes | number | False | 81 |
| hasVoted | boolean | False | 82 |
| select | (optionId: string) => void | False | 83 |
| isSelected | (optionId: string) => boolean | False | 84 |
| getPercentage | (optionId: string) => number | False | 85 |
| optionId | string | False | 101 |
| disabled | boolean | False | 102 |
| isSelected | boolean | False | 103 |
| percentage | number | False | 104 |

### Defaults and motion

- Default `multiple` = `false` (line 201).
- Default `disabled` = `false` (line 202).
- Default `showResults` = `false` (line 203).
- Default `hasVoted` = `false` (line 205).
- Default `optionDisabled` = `false` (line 451).

### Input, style and lifecycle

Events: onKeyDown (line 435); onClick (line 514).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
