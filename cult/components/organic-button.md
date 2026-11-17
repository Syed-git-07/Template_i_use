# organic-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/organic-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/organic-button.tsx); SHA-256 `9ab816f0ad393451c641a2ea6b10d053a4cb9054752f5cfbebb27ad9f98a7d91`; 237 lines.

Imports: `react`, `@radix-ui/react-slot`, `class-variance-authority`, `lucide-react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| asChild | boolean | True | 46 |
| label | string | False | 47 |
| icon | ReactNode | True | 48 |
| animationSpeed | "slow" \| "normal" \| "fast" | True | 49 |

### Defaults and motion

- Default `size` = `"md"` (line 79).
- Default `variantColor` = `"primary"` (line 80).
- Default `animationSpeed` = `"normal"` (line 81).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
