# feature-voting

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/feature-voting.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/feature-voting.tsx); SHA-256 `3d8e6c4e210478122b904c13ee53b33ab050b8cbf41c6f9aa990b671e5a941b4`; 424 lines.

Imports: `react`, `@radix-ui/react-use-controllable-state`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | FeatureVotingValue | True | 24 |
| defaultValue | FeatureVotingValue | True | 26 |
| onValueChange | (value: FeatureVotingValue) => void | True | 28 |
| votedFeatures | Set<string> | True | 30 |
| defaultVotedFeatures | Set<string> | True | 32 |
| onVotedFeaturesChange | (votedFeatures: Set<string>) => void | True | 34 |
| disabled | boolean | True | 36 |
| value | string | False | 41 |
| disabled | boolean | True | 43 |
| sortBy | "votes-asc" \| "votes-desc" \| "none" | True | 56 |
| votes | FeatureVotingValue | False | 64 |
| votedFeatures | Set<string> | False | 65 |
| disabled | boolean | False | 66 |
| vote | (featureId: string) => void | False | 67 |
| unvote | (featureId: string) => void | False | 68 |
| toggleVote | (featureId: string) => void | False | 69 |
| getVoteCount | (featureId: string) => number | False | 70 |
| hasVoted | (featureId: string) => boolean | False | 71 |
| featureId | string | False | 89 |
| disabled | boolean | False | 90 |

### Defaults and motion

- Default `disabled` = `false` (line 117).
- Default `sortBy` = `"none"` (line 234).
- Default `itemDisabled` = `false` (line 270).

### Input, style and lifecycle

Events: onClick (line 340).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
