# poll-widget

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/poll-widget.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/poll-widget.tsx); SHA-256 `fd7b214ed946180379e7703a75b43020db093f5d1dc952029505148519094554`; 1288 lines.

Imports: `react`, `@radix-ui/react-use-controllable-state`, `class-variance-authority`, `lucide-react`, `motion/react`, `@/lib/utils`, `@/components/ui/button`, `@/components/ui/dialog`, `@/components/ui/popover`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 50 |
| label | string | False | 52 |
| description | string | True | 54 |
| icon | ReactNode | True | 56 |
| question | string | False | 66 |
| description | string | True | 68 |
| options | PollOption[] | False | 70 |
| value | string \| string[] | True | 72 |
| defaultValue | string \| string[] | True | 74 |
| onValueChange | (value: string \| string[]) => void | True | 76 |
| multiple | boolean | True | 78 |
| disabled | boolean | True | 80 |
| votes | Record<string, number> | True | 82 |
| hasVoted | boolean | True | 84 |
| onVote | (selectedIds: string[]) => void | True | 86 |
| mode | PollWidgetMode | True | 88 |
| open | boolean | True | 90 |
| onOpenChange | (open: boolean) => void | True | 92 |
| autoCollapseDelay | number | True | 94 |
| successDuration | number | True | 96 |
| successTitle | string | True | 98 |
| successDescription | string | True | 100 |
| children | ReactNode | False | 102 |
| question | string | False | 110 |
| description | string | True | 111 |
| options | PollOption[] | False | 112 |
| selected | string[] | False | 113 |
| multiple | boolean | False | 114 |
| disabled | boolean | False | 115 |
| showResults | boolean | False | 116 |
| votes | Record<string, number> | False | 117 |
| totalVotes | number | False | 118 |
| hasVoted | boolean | False | 119 |
| mode | PollWidgetMode | False | 120 |
| open | boolean | False | 121 |
| setOpen | (open: boolean) => void | False | 122 |
| select | (optionId: string) => void | False | 123 |
| isSelected | (optionId: string) => boolean | False | 124 |
| getPercentage | (optionId: string) => number | False | 125 |
| submitVote | () => void | False | 126 |
| canSubmit | boolean | False | 127 |
| animationPhase | PollWidgetAnimationPhase | False | 129 |
| successTitle | string | False | 130 |
| successDescription | string | False | 131 |
| optionId | string | False | 149 |
| disabled | boolean | False | 150 |
| isSelected | boolean | False | 151 |
| percentage | number | False | 152 |
| label | ReactNode | True | 484 |
| title | string | True | 638 |
| description | string | True | 640 |
| value | string | False | 859 |
| disabled | boolean | True | 861 |
| loadingText | string | True | 1137 |

### Defaults and motion

- Default `multiple` = `false` (line 256).
- Default `disabled` = `false` (line 257).
- Default `hasVoted` = `false` (line 259).
- Default `mode` = `"inline"` (line 261).
- Default `autoCollapseDelay` = `2500` (line 264).
- Default `successDuration` = `1500` (line 265).
- Default `successTitle` = `"Thanks for voting!"` (line 266).
- Default `successDescription` = `"Your vote has been recorded"` (line 267).
- Default `optionDisabled` = `false` (line 869).
- Default `loadingText` = `"Submitting..."` (line 1148).
- `duration`: 0.4 (line 566).
- `bounce`: 0 (line 567).
- `duration`: 0.4 (line 580).
- `bounce`: 0 (line 581).
- `duration`: 0.5 (line 674).
- `bounce`: 0.4 (line 675).
- `delay`: 0.1 (line 676).
- `delay`: 0.2 (line 706).
- `duration`: 0.3 (line 706).
- `duration`: 0.8 (line 950).
- `bounce`: 0.1 (line 951).
- `delay`: 0.1 (line 952).
- `duration`: 0.3 (line 1183).
- `bounce`: 0 (line 1184).
- `duration`: 1 (line 1193).
- `ease`: "linear" (line 1195).

### Input, style and lifecycle

Events: onOpenChange (line 451); onOpenChange (line 461); onKeyDown (line 843); onClick (line 934); onClick (line 1220); onClick (line 1235).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
