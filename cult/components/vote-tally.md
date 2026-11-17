# vote-tally

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/vote-tally.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/vote-tally.tsx); SHA-256 `dc029c01650c0aafb90fd4b46fccfdf60f708244d919cb310e27b2c54936332c`; 410 lines.

Imports: `react`, `@radix-ui/react-use-controllable-state`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | VoteTallyValue | True | 24 |
| defaultValue | VoteTallyValue | True | 26 |
| onValueChange | (value: VoteTallyValue) => void | True | 28 |
| votedItems | Set<string> | True | 30 |
| defaultVotedItems | Set<string> | True | 32 |
| onVotedItemsChange | (votedItems: Set<string>) => void | True | 34 |
| disabled | boolean | True | 36 |
| value | string | False | 41 |
| disabled | boolean | True | 43 |
| sortBy | "votes-asc" \| "votes-desc" \| "none" | True | 56 |
| votes | VoteTallyValue | False | 64 |
| votedItems | Set<string> | False | 65 |
| disabled | boolean | False | 66 |
| vote | (itemId: string) => void | False | 67 |
| unvote | (itemId: string) => void | False | 68 |
| toggleVote | (itemId: string) => void | False | 69 |
| getVoteCount | (itemId: string) => number | False | 70 |
| hasVoted | (itemId: string) => boolean | False | 71 |
| itemId | string | False | 85 |
| disabled | boolean | False | 86 |

### Defaults and motion

- Default `disabled` = `false` (line 114).
- Default `sortBy` = `"none"` (line 224).
- Default `itemDisabled` = `false` (line 260).

### Input, style and lifecycle

Events: onClick (line 326).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
