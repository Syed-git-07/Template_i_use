# ai-blob-warp

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/ai-blob-warp.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/ai-blob-warp.tsx); SHA-256 `7f787b72454c9593aeab44e3961381eba4a7dc6b8b966baf12b0fcc862d7b226`; 105 lines.

Imports: `react`, `@paper-design/shaders-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| warpProps | Partial<WarpProps> | True | 27 |

### Defaults and motion

- `duration`: 5.2 (line 89).
- `ease`: "easeInOut" (line 90).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 32.

Source signals: reduced_motion, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
