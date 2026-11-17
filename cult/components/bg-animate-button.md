# bg-animate-button

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/bg-animate-button.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/bg-animate-button.tsx); SHA-256 `c19e8ac89fd0f61b650ad5ddb4f807503cd708d1554988b7cc2673390533fcc8`; 177 lines.

Imports: `react`, `@radix-ui/react-slot`, `class-variance-authority`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| variant | "primary" \| "success" \| "secondary" \| "destructive" \| "ghost" | True | 118 |
| size | "sm" \| "lg" \| "default" | True | 119 |
| shadow | "flat" \| "soft" \| "base" \| "deep" \| "deeper" | True | 120 |
| rounded | "full" \| "xl" \| "2xl" \| "3xl" \| "sm" \| "xs" \| "base" | True | 121 |
| asChild | boolean | True | 122 |
| showBackground | boolean | True | 123 |
| animation | "spin" \| "pulse" \| "spin-slow" \| "spin-fast" \| "spin" | True | 124 |
| gradient | \| "sunrise"     \| "ocean"     \| "candy"     \| "default"     \| "forest"     \| "sunset"     \| "nebula" | True | 125 |

### Defaults and motion

- Default `variant` = `"primary"` (line 138).
- Default `size` = `"default"` (line 139).
- Default `showBackground` = `false` (line 140).
- Default `rounded` = `"full"` (line 141).
- Default `shadow` = `"soft"` (line 142).
- Default `gradient` = `null` (line 143).
- Default `animation` = `null` (line 144).
- Default `asChild` = `false` (line 146).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 35, 60, 66.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
