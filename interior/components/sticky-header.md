# sticky-header

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/sticky-header.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/sticky-header.tsx); SHA-256 `5a8bd7d740148d0875ed10d0d4638f114ca7f2834d2bfb69de425a607ee8b96e`; 183 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| range | number | True | 17 |
| ref | React.RefObject<T \| null> | False | 21 |
| progress | MotionValue<number> | False | 22 |
| condensed | boolean | False | 23 |
| title | string | False | 46 |
| children | React.ReactNode | False | 47 |
| subtitle | string | True | 48 |
| leading | React.ReactNode | True | 49 |
| actions | React.ReactNode | True | 50 |
| expandedHeight | number | True | 51 |
| compactHeight | number | True | 52 |
| maxHeight | number | True | 53 |
| className | string | True | 54 |

### Defaults and motion

- Default `range` = `48` (line 27).
- Default `expandedHeight` = `68` (line 63).
- Default `compactHeight` = `48` (line 64).
- Default `maxHeight` = `320` (line 65).
- Default `className` = `""` (line 66).
- `stiffness`: 240 (line 14).
- `damping`: 44 (line 14).
- `mass`: 0.6 (line 14).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The expanded height is reserved by a spacer from the first paint, so condensing moves nothing below it; a header that shrinks inside the flow instead pulls its own scroll position and oscillates around the threshold.
- The bar's edge is driven by a scaleY on a plain plate and a translate on the hairline, so no height, top or width property is animated while you scroll — and every value is a MotionValue read off the scroll position, so React renders once, at the threshold.
- The two titles never share a frame: the large one is gone by 0.45, the compact one arrives after 0.55, so the handoff has a beat of silence in it instead of two crossfading ghosts mid-scroll.
- Content is never guillotined at the bar. As rows pass underneath, a hairline, a dissolving gradient and a cast shadow arrive together on the same edge — the shadow baked onto a strip whose opacity is composited, never a box-shadow repainted per scroll frame — and the foot of the box fades the same way.
- One copy of the title reaches the accessibility tree; the compact duplicate is aria-hidden, so the region is announced once rather than twice per scroll. The region itself is focusable, with scroll-padding equal to the condensed height so tabbing to a row never parks it under the bar.
- The condense is decoupled from the geometry — the header moves ~20px but the transition is paid out over ~64px of scroll, through a spring, so a hard flick lands as a settle instead of a cut. Under prefers-reduced-motion the spring is bypassed and every value resolves on the frame it is scrolled to.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| title | string | not specified | The large title, and the label the compact bar crossfades to. Reaches the accessibility tree exactly once. |
| children | React.ReactNode | not specified | The scrollable content. Passed as a prop, so a condense step never re-renders it. |
| subtitle | string | undefined | Secondary line under the title. Its text can change length freely; it is out of flow, so nothing reflows. |
| leading | React.ReactNode | undefined | Left slot in the compact bar, present in every state. Interactive, unlike the rest of the header. |
| actions | React.ReactNode | undefined | Right slot in the compact bar. Stays at a fixed height so condensing never moves it. |
| expandedHeight | number | 68 | Height reserved at rest, in pixels. The spacer under the header matches it from the first paint. There is no reserved bar zone above the title — the large title, leading and actions share one band, so this only needs room for the title and its subtitle. |
| compactHeight | number | 48 | Height of the condensed bar. Also the scroll-padding-top of the region. |
| maxHeight | number | 320 | Cap on the scroll region. The panel never animates toward an unbounded height. |
| className | string | "" | Appended last to the outer panel so callers can override the surface, border and radius. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
