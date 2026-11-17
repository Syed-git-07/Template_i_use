# scroll-spy

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/scroll-spy.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/scroll-spy.tsx); SHA-256 `1ec84464a6048a4dc0ff3a252951da0508418ad617329022965e7cd8123e1bb0`; 313 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 11 |
| label | string | False | 12 |
| sections | ScrollSpySection[] | False | 16 |
| offset | number | True | 17 |
| root | React.RefObject<HTMLElement \| null> | True | 18 |
| onChange | (id: string) => void | True | 19 |
| sections | ScrollSpySection[] | False | 222 |
| offset | number | True | 223 |
| root | React.RefObject<HTMLElement \| null> | True | 224 |
| onChange | (id: string) => void | True | 225 |
| label | string | True | 226 |
| className | string | True | 227 |

### Defaults and motion

- Default `offset` = `96` (line 24).
- Default `offset` = `96` (line 232).
- Default `label` = `"On this page"` (line 235).
- Default `className` = `""` (line 236).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).

### Input, style and lifecycle

Events: scroll (line 112); resize (line 113); wheel (line 114); touchstart (line 115).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, focus, cleanup, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Clicking a link does not make the rail flip through every heading the smooth scroll passes over: the destination is locked in until the scroll arrives, and the lock is abandoned the instant a wheel or touch takes the scroll back, so the rail never argues with the person driving.
- The reading line is not pinned: it starts under the top edge and slides to the bottom as the scroll runs out. A pinned line skips every short section near the end — their headings can never climb above it before the scroll is over — which is why the tail links in a hand-rolled spy are dead. On the sliding line each one still gets its turn, and the true end still clamps to the last section.
- Positions are read from live rects in one rAF per scroll event rather than from offsets cached on mount, and a ResizeObserver covers the rest, so an accordion opening or an image loading late does not leave the rail pointing at the wrong heading.
- The spy is a strip, not a sidebar: every section is a chip in a recessed track and the current one is carried by a single ink thumb sliding chip to chip — the same object the tabs and the segmented control already taught. The row scrolls sideways when the page has more sections than the strip has width, and the active chip keeps itself in view.
- The active section is one discrete id, so React renders when the section changes and not once per scroll frame; nothing in the strip is driven by a float.
- Every chip's label is drawn over an invisible medium twin in the same grid cell, so the weight arriving with the thumb cannot change the chip's width and reflow the row.
- Screen readers get the section name once, after the scroll settles, instead of a running commentary; a click moves focus to the heading itself so the keyboard lands where the eye does, and under prefers-reduced-motion the scroll jumps rather than glides.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| sections | ScrollSpySection[] | not specified | Ordered list of { id, label }. Each id is resolved from the document, so the content markup needs no wiring beyond the id it already has. |
| offset | number | 96 | Distance in px from the top of the scroll root to the reading line. Set it to the height of whatever sticky header covers the content. |
| root | React.RefObject<HTMLElement \| null> | undefined | A scroll container to watch. Omitted, the window is the scroller. |
| onChange | (id: string) => void | undefined | Fires once per section change, never per frame. Held in a ref, so an inline arrow does not re-bind the listeners. |
| label | string | "On this page" | Accessible name for the nav landmark. |
| className | string | "" | Appended last on the nav element. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
