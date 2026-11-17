# hide-on-scroll

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/hide-on-scroll.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/hide-on-scroll.tsx); SHA-256 `eeae80262a4bf245240693dd9bb30802e8fc41010c6bc99694c89594c2670a11`; 226 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| hideAfter | number | True | 10 |
| revealAfter | number | True | 11 |
| topGuard | number | True | 12 |
| pinned | boolean | True | 13 |
| disabled | boolean | True | 14 |
| ref | React.RefObject<T \| null> | False | 18 |
| hidden | boolean | False | 19 |
| atTop | boolean | False | 20 |
| bar | React.ReactNode | False | 132 |
| children | React.ReactNode | False | 133 |
| barHeight | number | True | 134 |
| hideAfter | number | True | 135 |
| revealAfter | number | True | 136 |
| topGuard | number | True | 137 |
| pinned | boolean | True | 138 |
| maxHeight | number | True | 139 |
| label | string | True | 140 |
| onHiddenChange | (hidden: boolean) => void | True | 141 |
| className | string | True | 142 |

### Defaults and motion

- Default `hideAfter` = `14` (line 24).
- Default `revealAfter` = `10` (line 25).
- Default `topGuard` = `24` (line 26).
- Default `pinned` = `false` (line 27).
- Default `disabled` = `false` (line 28).
- Default `barHeight` = `44` (line 148).
- Default `hideAfter` = `14` (line 149).
- Default `revealAfter` = `10` (line 150).
- Default `topGuard` = `24` (line 151).
- Default `pinned` = `false` (line 152).
- Default `maxHeight` = `320` (line 153).
- Default `label` = `"Scrollable content"` (line 154).
- Default `className` = `""` (line 156).
- `stiffness`: 150 (line 6).
- `damping`: 27 (line 6).
- `mass`: 1 (line 6).
- `stiffness`: 260 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.8 (line 7).
- `duration`: 0 (line 168).
- `duration`: 0 (line 169).

### Input, style and lifecycle

Events: scroll (line 110); resize (line 111); onFocus (line 184); onBlur (line 185).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, focus, cleanup, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Direction is decided by accumulated travel, not by the sign of the last scroll event, so a two-pixel trackpad wobble or a momentum stutter cannot flap the bar open and shut while someone reads.
- The bar leaves on a transform above a spacer that permanently reserves its height, so no line of content reflows when it yields or returns.
- Overscroll past either end is discarded rather than read as a direction change, so a rubber-band bounce at the bottom of an iOS list does not hide the bar.
- Focus entering the bar pins it open before the control lands, and `pinned` holds it open for a menu the bar owns, so a focusable action is never parked off-screen.
- Inside the top guard, and whenever the content is too short to scroll, the bar is unconditionally shown; a resize or a shrinking list cannot strand it above the frame.
- Scroll reads are coalesced into one animation frame and collapse to a single boolean, so React renders on the transition rather than per frame, and under `prefers-reduced-motion` the bar changes place without the trip.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| bar | React.ReactNode | not specified | Contents of the toolbar. Laid out in a flex row; give the title min-w-0 flex-1 truncate so long titles shrink instead of pushing the actions out. |
| children | React.ReactNode | not specified | The scrolling content. A spacer of barHeight is inserted above it so nothing starts underneath the bar. |
| barHeight | number | 44 | Height of the bar in pixels, and the exact distance it travels when it yields. |
| hideAfter | number | 14 | Pixels of uninterrupted downward travel required before the bar yields. Raise it if your surface has coarse momentum. |
| revealAfter | number | 10 | Pixels of upward travel required to bring the bar back. Kept below hideAfter so returning is cheaper than leaving. |
| topGuard | number | 24 | Distance from the top inside which the bar is always shown, so a short scroll never hides it a few pixels in. |
| pinned | boolean | false | Forces the bar open and holds it there. Set it while a menu, popover or search field the bar owns is on screen. |
| maxHeight | number | 320 | Height cap on the scroll region. The component scrolls inside it rather than growing the page. |
| label | string | "Scrollable content" | Accessible name for the scroll region, which is focusable so keyboard users can scroll it. |
| onHiddenChange | (hidden: boolean) => void | not specified | Called once per transition, never per frame. Use it to fade a floating action button in step with the bar. |
| className | string | "" | Appended last to the outer frame, so radius, border and background are overridable. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
