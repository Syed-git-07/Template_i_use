# dropdown

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/dropdown.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/dropdown.tsx); SHA-256 `f937fb38b4dc40b5c3d88165fc674e362f4c0b402feb4e462456a39764ca2b93`; 430 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string | False | 21 |
| label | string | False | 22 |
| hint | string | True | 23 |
| disabled | boolean | True | 24 |
| items | DropdownItem[] | False | 28 |
| value | string | True | 29 |
| defaultValue | string | True | 30 |
| onChange | (value: string) => void | True | 31 |
| disabled | boolean | True | 32 |
| typeaheadDelay | number | True | 33 |
| items | DropdownItem[] | False | 264 |
| value | string | True | 265 |
| defaultValue | string | True | 266 |
| onChange | (value: string) => void | True | 267 |
| label | string | True | 268 |
| placeholder | string | True | 269 |
| disabled | boolean | True | 270 |
| emptyLabel | string | True | 271 |
| className | string | True | 272 |

### Defaults and motion

- Default `disabled` = `false` (line 41).
- Default `typeaheadDelay` = `600` (line 42).
- Default `label` = `"Options"` (line 280).
- Default `placeholder` = `"Select an option"` (line 281).
- Default `disabled` = `false` (line 282).
- Default `emptyLabel` = `"Nothing to choose"` (line 283).
- Default `className` = `""` (line 284).
- `stiffness`: 520 (line 9).
- `damping`: 34 (line 9).
- `mass`: 0.45 (line 9).
- `stiffness`: 700 (line 11).
- `damping`: 46 (line 11).
- `mass`: 0.5 (line 11).
- `duration`: 0 (line 12).
- `stiffness`: 700 (line 14).
- `damping`: 46 (line 14).
- `mass`: 0.5 (line 14).
- `stiffness`: 620 (line 18).
- `damping`: 38 (line 18).
- `mass`: 0.6 (line 18).
- `duration`: 0.12 (line 341).
- `ease`: computed; inspect expression (line 341).
- `duration`: 0.12 (line 346).
- `ease`: computed; inspect expression (line 346).
- `duration`: 0.1 (line 367).
- `ease`: computed; inspect expression (line 367).

### Input, style and lifecycle

Events: pointerdown (line 151); blur (line 152).

Typography/style anchors: 341.

Source signals: reduced_motion, keyboard, focus, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The active highlight is one element carrying a layoutId, so moving down the list is a single travel rather than one row's background fading out while another fades in — hold ArrowDown and there is never a frame with two rows lit or none.
- Every label lives stacked in one grid cell inside the trigger, so committing to a longer option cannot widen the button or push the row beside it sideways.
- The list is capped at 216px and scrolls inside itself, so a hundred options never animate a panel toward an unbounded height, and keyboard navigation reveals the active row with block: "nearest" instead of yanking the list to center it.
- Disabled options are skipped by the arrow keys, by Home and End, and by typeahead, and refuse their own click, so the highlight cannot park somewhere Enter does nothing.
- Under prefers-reduced-motion the highlight jumps to its new row and the panel arrives without blur or scale: the selection still reads, only the trip is skipped, and nothing is hidden.
- Focus is handled rather than assumed — opening moves focus into the listbox, aria-activedescendant names the active option so a screen reader hears the landing and not the journey, and Escape, Tab, a click outside or a window blur all close it without leaving focus stranded on a removed node; useDropdown exports the same behaviour for a different surface.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | DropdownItem[] | not specified | Options, each { value, label, hint?, disabled? }. Disabled options are rendered but skipped by every form of navigation. |
| value | string | not specified | Controlled selection. Omit for uncontrolled, in which case the component keeps its own. |
| defaultValue | string | not specified | Initial selection when uncontrolled. Nothing is selected without it, and the placeholder holds the trigger's width. |
| onChange | (value: string) => void | not specified | Fires once per commit, after the menu has closed and focus is back on the trigger. |
| label | string | "Options" | Accessible name for both the trigger and the listbox. It is read with the current value, never in place of it. |
| placeholder | string | "Select an option" | Shown until something is selected. It is measured with the real labels, so adopting a selection cannot resize the trigger. |
| disabled | boolean | false | Blocks opening from pointer and keyboard alike. |
| emptyLabel | string | "Nothing to choose" | Rendered as inert text when items is empty, so the listbox never opens onto nothing. |
| className | string | "" | Appended last on the root. The root is width-full and unsized, so the caller owns the measurement. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
