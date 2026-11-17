# text-gif

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/text-gif.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/text-gif.tsx); SHA-256 `b70951ea26004ea63a0d543441a341565c5deae7ab91d9681120bdaeb06bc39b`; 165 lines.

Imports: `react`, `next/image`, `class-variance-authority`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| gifUrl | string | False | 46 |
| text | string | False | 47 |
| className | string | True | 48 |
| fallbackColor | string | True | 49 |
| transitionDuration | number | True | 50 |

### Defaults and motion

- Default `fallbackColor` = `"black"` (line 60).
- Default `transitionDuration` = `300` (line 61).

### Input, style and lifecycle

Events: onLoad (line 117); onError (line 121).

Typography/style anchors: 95.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
