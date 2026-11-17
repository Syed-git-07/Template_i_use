# skeleton-swap

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/skeleton-swap.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/skeleton-swap.tsx); SHA-256 `5437a2fbec2aa5e7f3254a276577895269f83246977502a6a212a0826ebe7086`; 177 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| ready | boolean | False | 21 |
| delay | number | True | 22 |
| minVisible | number | True | 23 |
| ready | boolean | False | 54 |
| children | React.ReactNode | False | 55 |
| lines | number | True | 56 |
| lineHeight | number | True | 57 |
| barHeight | number | True | 58 |
| reserve | number | True | 59 |
| delay | number | True | 60 |
| minVisible | number | True | 61 |
| label | string | True | 62 |
| skeleton | React.ReactNode | True | 63 |
| className | string | True | 64 |

### Defaults and motion

- Default `delay` = `120` (line 28).
- Default `minVisible` = `380` (line 29).
- Default `lines` = `3` (line 70).
- Default `lineHeight` = `21` (line 71).
- Default `barHeight` = `9` (line 72).
- Default `delay` = `120` (line 74).
- Default `minVisible` = `380` (line 75).
- Default `className` = `""` (line 78).
- `stiffness`: 260 (line 8).
- `damping`: 34 (line 9).
- `mass`: 0.8 (line 10).
- `duration`: 0 (line 126).
- `duration`: 0 (line 144).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The box is sized before the request finishes and never resized after it: skeleton and content occupy the same single grid cell inside a fixed reserve, so the footer under the card cannot be pushed down at the moment data arrives.
- Content that overruns the reserve scrolls inside the box instead of growing the page, and the box takes a tab stop only while it is actually scrollable, so keyboard users get a scroll target and never a dead one.
- A response that returns in 40ms shows no skeleton at all, because nothing paints until the wait passes the delay threshold; a skeleton that has already painted stays for minVisible, so it can never appear and vanish inside the same frame budget.
- The skeleton does not pulse. An idle loop animates while nothing is happening, which reads as progress the network is not making.
- Screen readers get aria-busy while the request is open and one "loaded" announcement at the end; the placeholder bars are aria-hidden and non-focusable, so nothing narrates the shape of absent text.
- Under prefers-reduced-motion the swap is a cut rather than a blur crossfade, the skeleton still appears, and both timers still clean up on unmount along with the ResizeObserver.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| ready | boolean | not specified | Flips to true when the real content is available. Everything else is timing around this one value. |
| children | React.ReactNode | not specified | The real content. Mount it only once the data exists; the component holds the box either way. |
| lines | number | 3 | How many text lines the skeleton draws, and how much height it reserves. |
| lineHeight | number | 21 | Pixel line height of the content this stands in for. Match the text's own leading and the reserve is exact. |
| barHeight | number | 9 | Height of the bar drawn inside each reserved line. Purely visual; it does not change the reserve. |
| reserve | number | lines * lineHeight | Explicit box height in pixels. Use it when the content is not text: media, a chart, a fixed card. |
| delay | number | 120 | Milliseconds of silence before the skeleton is allowed to paint. A response faster than this never shows one. |
| minVisible | number | 380 | Once painted, the skeleton stays at least this long, so it cannot blink. |
| label | string | undefined | Names the region and announces "<label> loaded" once. Omit it and the component stays silent apart from aria-busy. |
| skeleton | React.ReactNode | undefined | Replaces the default bars with your own placeholder shape. Pair it with reserve so the box still matches. |
| className | string | "" | Appended last, so callers win on every utility. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
