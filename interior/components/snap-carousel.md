# snap-carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/snap-carousel.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/snap-carousel.tsx); SHA-256 `134f01aae958a97a3c97759c82f5761bb3839ab722387968486fdce69897fd20`; 448 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| offset | { x: number; y: number } | False | 47 |
| x | number | False | 47 |
| y | number | False | 47 |
| velocity | { x: number; y: number } | False | 48 |
| x | number | False | 48 |
| y | number | False | 48 |
| count | number | False | 52 |
| index | number | True | 53 |
| defaultIndex | number | True | 54 |
| onIndexChange | (index: number) => void | True | 55 |
| gap | number | True | 56 |
| momentum | number | True | 57 |
| maxFlick | number | True | 58 |
| disabled | boolean | True | 59 |
| stop | () => void | False | 85 |
| children | React.ReactNode | False | 315 |
| label | string | False | 316 |
| index | number | True | 317 |
| defaultIndex | number | True | 318 |
| onIndexChange | (index: number) => void | True | 319 |
| gap | number | True | 320 |
| peek | number | True | 321 |
| momentum | number | True | 322 |
| maxFlick | number | True | 323 |
| prevLabel | string | True | 324 |
| nextLabel | string | True | 325 |
| className | string | True | 326 |

### Defaults and motion

- Default `defaultIndex` = `0` (line 65).
- Default `gap` = `12` (line 67).
- Default `momentum` = `0.14` (line 68).
- Default `maxFlick` = `1` (line 69).
- Default `disabled` = `false` (line 70).
- Default `defaultIndex` = `0` (line 333).
- Default `gap` = `12` (line 335).
- Default `peek` = `0` (line 336).
- Default `momentum` = `0.14` (line 337).
- Default `maxFlick` = `1` (line 338).
- Default `prevLabel` = `"Previous slide"` (line 339).
- Default `nextLabel` = `"Next slide"` (line 340).
- Default `className` = `""` (line 341).
- `stiffness`: 520 (line 22).
- `damping`: 34 (line 23).
- `mass`: 0.45 (line 24).
- `stiffness`: 260 (line 29).
- `damping`: 34 (line 30).
- `mass`: 0.8 (line 31).
- `stiffness`: 700 (line 36).
- `damping`: 30 (line 37).
- `mass`: 0.5 (line 38).
- `duration`: 0 (line 106).
- `duration`: 0 (line 136).
- `dragMomentum`: false (line 261).
- `dragElastic`: 0.14 (line 262).
- `duration`: 0 (line 398).
- `duration`: 0 (line 424).

### Input, style and lifecycle

Events: onClick (line 412); onClick (line 431); onClick (line 434).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- A flick resolves to a slide index before the landing spring starts, so the track cannot come to rest halfway between two slides, and it cannot leave a sliver of the wrong slide on screen when the finger lifts mid-gap.
- Momentum is projected from release velocity but capped at maxFlick slides past where the finger actually let go, so a hard throw advances one slide instead of flinging the reader four deep into a gallery they never saw.
- The landing spring is handed the gesture's exit velocity and can be caught mid-flight: grabbing the track again picks it up from where it currently is, never from where the last animation started.
- Every slide is one viewport wide and the track stretches to the tallest of them, so moving between slides resizes nothing and the content below never jumps.
- Only the resting slide is interactive; the rest are inert, which stops Tab from landing inside a slide nobody can see, and a scroll guard returns the viewport to zero if anything else tries to scroll the clipped track out of alignment.
- The horizontal offset is a motion value written straight to the node, so React renders only when the target index crosses a boundary, and the polite live region announces the settled slide once rather than sixty times a second; under prefers-reduced-motion the same index is reached with the travel removed.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| children | React.ReactNode | not specified | One element per slide. Each is wrapped in a full-width, non-shrinking cell, so slides never disagree about width. |
| label | string | not specified | Accessible name for the carousel group. Required, because an unnamed region is a dead end for a screen reader. |
| index | number | — | Controlled resting slide. If the parent refuses a change, the track glides back to the index it was given. |
| defaultIndex | number | 0 | Uncontrolled starting slide, clamped into range. |
| onIndexChange | (index: number) => void | — | Fires once per landing, with the settled index. Never fires mid-gesture. |
| gap | number | 12 | Pixels between slides. Folded into the snap step, so the gap can never accumulate into drift. |
| peek | number | 0 | Pixels of the neighbouring slides left visible at each edge. Applied as viewport padding, so the slide width shrinks with it instead of overflowing. |
| momentum | number | 0.14 | Seconds of release velocity projected forward when choosing the target slide. Higher means a lighter flick carries. |
| maxFlick | number | 1 | Hard ceiling on how many slides momentum may add past where the finger let go. |
| prevLabel | string | "Previous slide" | Accessible name for the back control. |
| nextLabel | string | "Next slide" | Accessible name for the forward control. |
| className | string | "" | Appended last to the outer element, so callers win. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
