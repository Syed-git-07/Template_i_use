# logo-marquee

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/logo-marquee.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/logo-marquee.tsx); SHA-256 `011a99f6edeca9cb5cdc2065511ffd8d5a9eb8ad79360a64bf9b858df6dce19c`; 326 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| speed | number | True | 13 |
| direction | MarqueeDirection | True | 14 |
| gap | number | True | 15 |
| paused | boolean | True | 16 |
| id | string | False | 214 |
| label | string | False | 215 |
| href | string | True | 216 |
| mark | React.ReactNode | True | 217 |
| items | LogoMarqueeItem[] | False | 221 |
| label | string | True | 222 |
| speed | number | True | 223 |
| direction | MarqueeDirection | True | 224 |
| gap | number | True | 225 |
| paused | boolean | True | 226 |
| onSelect | (item: LogoMarqueeItem) => void | True | 227 |
| className | string | True | 228 |

### Defaults and motion

- Default `speed` = `44` (line 29).
- Default `direction` = `"left"` (line 30).
- Default `gap` = `40` (line 31).
- Default `paused` = `false` (line 32).
- Default `label` = `"Logos"` (line 249).
- Default `speed` = `44` (line 250).
- Default `direction` = `"left"` (line 251).
- Default `gap` = `40` (line 252).
- Default `paused` = `false` (line 253).
- Default `className` = `""` (line 255).

### Input, style and lifecycle

Events: scroll (line 156); blur (line 162); onClick (line 301).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, pointer_cancel, focus, cleanup, resize, visibility, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Pointer or keyboard entry ramps the strip to a stop and resumes from the pixel it stopped on, so a logo never slides out from under a cursor that was already aiming at it, and leaving never restarts the run from the beginning.
- Tabbing to a logo pulls that logo inside the viewport before its focus ring can be painted off-screen, and the viewport's scrollLeft is pinned to zero so the browser's own focus scrolling can never desync the scroll position from the transform.
- The transport is one requestAnimationFrame writing a single transform to the track through a ref; React never re-renders to move it, the loop is unsubscribed entirely while the strip is off-screen, and the frame delta is clamped so returning from a background tab resumes instead of teleporting.
- The number of repeats is measured from the viewport width and one group's width with a ResizeObserver, so a wide screen never runs out of content and the wrap always lands on a position that is pixel-identical to the one before it.
- Only one copy is real: the repeats are aria-hidden and hold nothing focusable, so a screen reader reads the list of companies once and tab order visits each logo once.
- Under prefers-reduced-motion the strip stops being a transport and becomes a single scrollable row that keyboard users can reach and move; every logo is still present, none of it is hidden.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | LogoMarqueeItem[] | not specified | Each item is { id, label, href?, mark? }. `mark` is the artwork; `label` is what a screen reader gets and what renders when no mark is supplied. |
| label | string | "Logos" | Accessible name for the region, so the strip is announced as one landmark rather than a loose run of links. |
| speed | number | 44 | Travel in pixels per second. Speed is time-based, not frame-based, so a 120Hz display does not run twice as fast. |
| direction | "left" \| "right" | "left" | Which way the strip drifts. Both directions use the same wrap window, so neither one shows a seam. |
| gap | number | 40 | Pixel gap between logos and between repeats, so the spacing across the loop seam matches the spacing everywhere else. |
| paused | boolean | false | Controlled stop from outside, ORed with hover and focus. Clearing it ramps back up from the current position. |
| onSelect | (item: LogoMarqueeItem) => void | not specified | Renders each logo as a button instead of a link. Supply this or `href` if the logos are meant to be clickable. |
| onPauseChange | (paused: boolean) => void | not specified | Fires once per transition between drifting and held, not per frame. Held through a ref, so an inline arrow does not resubscribe. |
| className | string | "" | Appended last on the section, so the surface, radius and border are overridable from outside. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
