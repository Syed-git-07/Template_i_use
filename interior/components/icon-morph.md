# icon-morph

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/icon-morph.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/icon-morph.tsx); SHA-256 `2debead252da7551a1773b2e42b1f583c4764aa6a0617806138995781550a2b1`; 269 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| d | readonly string[] | False | 14 |
| rotate | number | True | 15 |
| key | number | False | 27 |
| d | string | False | 28 |
| visible | boolean | False | 29 |
| mode | IconMorphMode | False | 36 |
| labels | readonly string[] | False | 36 |
| shapes | readonly MorphShape[] | False | 36 |
| preset | IconMorphPreset | True | 112 |
| shapes | readonly MorphShape[] | True | 113 |
| mode | IconMorphMode | True | 114 |
| labels | readonly string[] | True | 115 |
| active | number \| boolean | True | 116 |
| defaultActive | number \| boolean | True | 117 |
| onActiveChange | (index: number) => void | True | 118 |
| size | number | True | 171 |
| strokeWidth | number | True | 172 |
| showLabel | boolean | True | 173 |
| semantics | IconMorphSemantics | True | 174 |
| disabled | boolean | True | 175 |
| className | string | True | 176 |

### Defaults and motion

- Default `preset` = `"menu-close"` (line 122).
- Default `defaultActive` = `0` (line 127).
- Default `size` = `20` (line 180).
- Default `strokeWidth` = `1.75` (line 181).
- Default `showLabel` = `false` (line 182).
- Default `semantics` = `"label"` (line 183).
- Default `disabled` = `false` (line 184).
- Default `className` = `""` (line 185).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `stiffness`: 260 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.8 (line 7).
- `duration`: 0 (line 8).

### Input, style and lifecycle

Events: onClick (line 206).

Typography/style anchors: 163.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Two icons crossfaded over each other draw both shapes at once through the middle of the transition; this renders one path list and interpolates its coordinates, so there is never a second icon on screen to catch.
- Every state is padded to the same slot count, and a slot a state does not use collapses to a zero-length path and fades, so the number of paths never changes mid-flight and no stroke pops into existence.
- The icon box and the label cell are reserved before the first paint — all labels stack in one grid cell — so swapping Play for Pause or Menu for Close cannot widen the button or push the row beside it.
- Activating the control mid-transition resumes the spring from the geometry currently on screen, rather than snapping back to the previous shape and replaying.
- Under prefers-reduced-motion the target geometry is applied in one frame; the icon still shows the correct state instead of being hidden or left mid-morph.
- It is a real button with aria-pressed or aria-expanded and an accessible name that changes once per state, so a screen reader announces the new state on activation and nothing repeats it.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| preset | "menu-close" \| "play-pause" \| "plus-minus" \| "check-close" | "menu-close" | Built-in shape pair. Each preset ships its paths on a shared command signature so the geometry interpolates. |
| shapes | readonly MorphShape[] | not specified | Your own states: `{ d: string[]; rotate?: number }` per state. Two or more; the button cycles through them. |
| mode | "stroke" \| "fill" | preset's mode | Whether the paths are stroked outlines or filled bodies. Play/pause is filled, the rest are stroked. |
| labels | readonly string[] | preset's labels | One per state. Becomes the accessible name, and the visible text when showLabel is set. |
| active | number \| boolean | not specified | Controlled state index. A boolean maps to 0 and 1. Omit to let the component own its state. |
| defaultActive | number \| boolean | 0 | Starting state when uncontrolled. |
| onActiveChange | (index: number) => void | not specified | Fires with the next index on activation, in both controlled and uncontrolled mode. |
| semantics | "label" \| "pressed" \| "expanded" | "label" | Which ARIA state the second index reports: none, aria-pressed, or aria-expanded. |
| showLabel | boolean | false | Renders the labels beside the icon. All of them share one grid cell, so the button is as wide as the longest. |
| size | number | 20 | Icon box in px. The 24-unit viewBox scales to it; the button stays 36px tall. |
| strokeWidth | number | 1.75 | Stroke mode only. |
| disabled | boolean | false | Blocks activation and the press displacement. |
| className | string | "" | Appended last, so any of the button chrome can be overridden. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
