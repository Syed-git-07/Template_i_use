# pixel-heading-word

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/pixel-heading-word.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/pixel-heading-word.tsx); SHA-256 `2bc1150b7367b47f8aff89e704f48c875fb5f704068cb9d951166154773d0953`; 337 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| as | "h1" \| "h2" \| "h3" \| "h4" \| "h5" \| "h6" | True | 84 |
| initialFont | PixelFont | True | 89 |
| hoverFont | PixelFont | True | 95 |
| cycleInterval | number | True | 101 |
| defaultFontIndex | number | True | 107 |
| onFontIndexChange | (index: number) => void | True | 111 |
| showLabel | boolean | True | 116 |
| disableHover | boolean | True | 122 |
| disableCycling | boolean | True | 128 |

### Defaults and motion

- Default `Tag` = `"h1"` (line 156).
- Default `cycleInterval` = `300` (line 160).
- Default `defaultFontIndex` = `0` (line 161).
- Default `showLabel` = `false` (line 163).
- Default `disableHover` = `false` (line 164).
- Default `disableCycling` = `false` (line 165).

### Input, style and lifecycle

Events: onMouseEnter (line 313); onMouseLeave (line 314); onFocus (line 315); onBlur (line 316); onKeyDown (line 317).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
