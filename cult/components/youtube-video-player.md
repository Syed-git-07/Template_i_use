# youtube-video-player

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/youtube-video-player.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/youtube-video-player.tsx); SHA-256 `47c5078a68514239a549d3f63482ade648bc755c754b8f021c4b825f78ca04d0`; 409 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| videoId | string | False | 11 |
| title | string | True | 12 |
| defaultExpanded | boolean | True | 13 |
| customThumbnail | string | True | 14 |
| className | string | True | 17 |
| containerClassName | string | True | 18 |
| expandedClassName | string | True | 19 |
| thumbnailClassName | string | True | 22 |
| thumbnailImageClassName | string | True | 23 |
| playButtonClassName | string | True | 26 |
| playIconClassName | string | True | 27 |
| titleClassName | string | True | 30 |
| controlsClassName | string | True | 33 |
| expandButtonClassName | string | True | 34 |
| backdropClassName | string | True | 37 |
| playerClassName | string | True | 40 |
| videoId | string | False | 347 |
| expanded | boolean | False | 348 |
| playing | boolean | False | 349 |
| isHovered | boolean | False | 350 |
| onToggleExpand | () => void | False | 351 |
| controlsClassName | string | True | 352 |
| expandButtonClassName | string | True | 353 |

### Defaults and motion

- Default `defaultExpanded` = `false` (line 46).
- `duration`: 0.2 (line 230).
- `duration`: 0.2 (line 375).
- `stiffness`: 300 (line 391).
- `damping`: 20 (line 391).

### Input, style and lifecycle

Events: keydown (line 103); onClick (line 172); onToggleExpand (line 214); onClick (line 235); onClick (line 289); onToggleExpand (line 331); onClick (line 382).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
