# choice-poll

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/choice-poll.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/choice-poll.tsx); SHA-256 `bc0e23c276daf271df9376354e98cf8a58226674663db624a30e3533ed37e078`; 777 lines.

Imports: `react`, `@radix-ui/react-use-controllable-state`, `class-variance-authority`, `lucide-react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string \| string[] | True | 28 |
| defaultValue | string \| string[] | True | 30 |
| onValueChange | (value: string \| string[]) => void | True | 32 |
| multiple | boolean | True | 34 |
| disabled | boolean | True | 36 |
| showResults | boolean | True | 38 |
| votes | Record<string, number> | True | 40 |
| hasVoted | boolean | True | 42 |
| value | string | False | 47 |
| disabled | boolean | True | 49 |
| totalVotes | number | True | 70 |
| selected | string[] | False | 78 |
| multiple | boolean | False | 79 |
| disabled | boolean | False | 80 |
| showResults | boolean | False | 81 |
| votes | Record<string, number> | False | 82 |
| totalVotes | number | False | 83 |
| hasVoted | boolean | False | 84 |
| select | (optionId: string) => void | False | 85 |
| isSelected | (optionId: string) => boolean | False | 86 |
| getPercentage | (optionId: string) => number | False | 87 |
| optionId | string | False | 101 |
| disabled | boolean | False | 102 |
| isSelected | boolean | False | 103 |
| percentage | number | False | 104 |

### Defaults and motion

- Default `multiple` = `false` (line 222).
- Default `disabled` = `false` (line 223).
- Default `showResults` = `false` (line 224).
- Default `hasVoted` = `false` (line 226).
- Default `optionDisabled` = `false` (line 472).

### Input, style and lifecycle

Events: onKeyDown (line 456); onClick (line 536).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, focus, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
