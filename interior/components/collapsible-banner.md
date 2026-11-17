# collapsible-banner

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/collapsible-banner.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/collapsible-banner.tsx); SHA-256 `567283024afccf52542b76e3e564b137179cee49eb47c181eff83a91cc4307f7`; 292 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | BannerState | True | 14 |
| defaultState | BannerState | True | 15 |
| onStateChange | (state: BannerState) => void | True | 16 |
| onDismiss | () => void | True | 17 |
| state | BannerState | False | 21 |
| open | boolean | False | 22 |
| folded | boolean | False | 23 |
| dismissed | boolean | False | 24 |
| fold | () => void | False | 25 |
| expand | () => void | False | 26 |
| toggle | () => void | False | 27 |
| dismiss | () => void | False | 28 |
| restore | () => void | False | 29 |
| title | React.ReactNode | False | 128 |
| description | React.ReactNode | True | 129 |
| children | React.ReactNode | True | 130 |
| action | React.ReactNode | True | 131 |
| icon | React.ReactNode | True | 132 |
| dismissible | boolean | True | 134 |
| state | BannerState | True | 135 |
| defaultState | BannerState | True | 136 |
| onStateChange | (state: BannerState) => void | True | 137 |
| onDismiss | () => void | True | 138 |
| dismissLabel | string | True | 139 |
| dismissedMessage | string | True | 140 |
| className | string | True | 141 |

### Defaults and motion

- Default `defaultState` = `"open"` (line 34).
- Default `dismissible` = `true` (line 150).
- Default `defaultState` = `"open"` (line 152).
- Default `dismissLabel` = `"Dismiss notice"` (line 155).
- Default `dismissedMessage` = `"Notice dismissed."` (line 156).
- Default `className` = `""` (line 157).
- `stiffness`: 190 (line 7).
- `damping`: 30 (line 7).
- `mass`: 1 (line 7).
- `stiffness`: 700 (line 8).
- `damping`: 46 (line 8).
- `mass`: 0.5 (line 8).
- `duration`: 0 (line 9).
- `duration`: 0.14 (line 177).
- `ease`: computed; inspect expression (line 177).
- `delay`: computed; inspect expression (line 177).
- `duration`: 0.14 (line 189).
- `ease`: computed; inspect expression (line 189).

### Input, style and lifecycle

Events: onClick (line 210); onKeyDown (line 211); onClick (line 248).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Severity is carried by the sentence, not by a coloured icon. Three notices in a column read as three messages rather than three components, and the one that matters is the one you wrote the clearest.
- A notice has three resting places, not two. It can be read, folded down to the line that names it, or let go. A banner whose only control is a close button is not collapsible — it is disposable, and the difference matters when the thing it says is still true after you stop looking at it.
- `dismissible={false}` is the point of the fold. An incident, an overdue invoice, a degraded region: you may move it out of the way, you may not make it untrue. Without the fold the only options are a permanent wall of text or a lie.
- The header never moves. Only the body's box changes, so the title, the mark and both controls hold still while the notice folds underneath them — the fold reads as the box closing, not as the page reflowing.
- Opacity leads on the way out and trails 50ms on the way in. Finishing first on the fold is what hides the reflow; starting late on the unfold keeps text from appearing in a box that has not opened yet.
- Height animates to `auto` and is measured by the animation itself, so a description that grows — a longer error, a second line after a webfont lands — needs no ResizeObserver and no measured pixel value living in React state.
- The folded body is inert, so a zero-height notice cannot be tabbed into or read out, and the toggle carries aria-expanded and aria-controls rather than a decorative chevron. Escape folds an open banner from its own header.
- Under prefers-reduced-motion every height, opacity and rotation resolves on the same frame: the notice is still folded, still gone, still correct, only the trip is skipped.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| title | React.ReactNode | not specified | The one line the banner exists to say, and the only thing left when it is folded. Names the region for screen readers. |
| description | React.ReactNode | not specified | The part that folds away. Omitted entirely rather than reserved as empty space. |
| children | React.ReactNode | not specified | Extra content below the description, inside the fold. |
| action | React.ReactNode | not specified | The control the notice is asking for, rendered at the bottom of the fold. Unreachable by keyboard while folded. |
| icon | React.ReactNode | info glyph | Replaces the leading mark. The defaults are Phosphor regular geometry inlined, so the icons match the rest of the set without the file taking on an icon package. |
| dismissible | boolean | true | False removes the close button and leaves only the fold. This is the prop for a notice that must stay reachable — an active incident, an unpaid invoice. |
| state | "open" \| "folded" \| "dismissed" | not specified | Controlled state. When passed, the component never changes itself, it only reports. |
| defaultState | BannerState | "open" | Uncontrolled starting state. Starting folded costs no flash: the body is laid out at zero height on first paint. |
| onStateChange | (state: BannerState) => void | not specified | Fires on every transition, so a folded notice can be remembered per user rather than re-opened on each visit. |
| onDismiss | () => void | not specified | Fires only on dismiss, once. |
| dismissLabel | string | "Dismiss notice" | Accessible name of the close button. Set it per banner when a page has several. |
| dismissedMessage | string | "Notice dismissed." | Announced once, from a live region outside the collapsing frame, so the confirmation is not clipped away with it. |
| className | string | "" | Appended to the banner surface. Margins set here sit inside the collapsing box, so a dismissed banner leaves no residual gap. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
