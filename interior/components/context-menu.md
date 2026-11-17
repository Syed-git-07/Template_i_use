# context-menu

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/context-menu.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/context-menu.tsx); SHA-256 `948a2a2843898b03a0d36509fb1098d6b50d9dfb9c9ce9e4b69af355cb98884d`; 518 lines.

Imports: `react`, `react-dom`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 29 |
| type | "separator" | False | 29 |
| id | string | False | 31 |
| type | "item" | True | 32 |
| label | string | False | 33 |
| shortcut | string | True | 34 |
| icon | ReactNode | True | 35 |
| disabled | boolean | True | 36 |
| onSelect | (id: string) => void | True | 37 |
| left | number | False | 41 |
| top | number | False | 42 |
| width | number | False | 43 |
| maxHeight | number | False | 44 |
| transformOrigin | string | False | 45 |
| items | ContextMenuItem[] | False | 49 |
| onSelect | (id: string) => void | True | 50 |
| width | number | True | 51 |
| margin | number | True | 52 |
| holdDuration | number | True | 53 |
| moveTolerance | number | True | 54 |
| disabled | boolean | True | 55 |
| x | number | False | 86 |
| y | number | False | 86 |
| items | ContextMenuItem[] | False | 381 |
| children | ReactNode | False | 382 |
| onSelect | (id: string) => void | True | 383 |
| label | string | True | 384 |
| width | number | True | 385 |
| disabled | boolean | True | 386 |
| className | string | True | 387 |
| host | HTMLElement \| null | False | 512 |
| children | ReactNode | False | 513 |

### Defaults and motion

- Default `width` = `224` (line 71).
- Default `margin` = `8` (line 72).
- Default `holdDuration` = `460` (line 73).
- Default `moveTolerance` = `8` (line 74).
- Default `disabled` = `false` (line 75).
- Default `label` = `"Context menu"` (line 394).
- Default `width` = `224` (line 395).
- Default `disabled` = `false` (line 396).
- Default `className` = `""` (line 397).
- `duration`: 0 (line 447).
- `duration`: 0.14 (line 448).
- `ease`: computed; inspect expression (line 448).
- `duration`: 0 (line 450).
- `duration`: 0.2 (line 450).
- `ease`: computed; inspect expression (line 450).

### Input, style and lifecycle

Events: pointerdown (line 236); scroll (line 237); keydown (line 238); resize (line 239); blur (line 240).

Typography/style anchors: 447, 448.

Source signals: reduced_motion, keyboard, pointer_cancel, focus, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The menu opens at the pointer and grows out of it: transformOrigin is the exact pixel offset of the click inside the panel, so it never reads as flying in from a corner nobody clicked.
- Near an edge it flips to the other side of the pointer and is then clamped to an 8px margin, so no item is ever pushed under the scrollbar or off the viewport.
- Panel height is derived from the item list before the first paint and capped at the viewport, so the menu never measures itself, never jumps a frame later, and never animates toward an unbounded height — a long list scrolls inside the cap instead.
- Nothing is shared between rows: the active row paints its own background and slides its label 3px, so no highlight flies across the panel and no row blinks when the pointer re-enters it.
- The keyboard is a real opener, not an afterthought — ContextMenu, Shift+F10 and Enter anchor the menu to the element, arrows, Home, End and typeahead move actual DOM focus between menuitems, and Escape or Tab closes it and puts focus back on the trigger.
- An item activates only when its own pointerdown landed on it, so the compatibility click fired as a long-pressing finger lifts cannot select whatever the menu just placed underneath it; scroll, resize, window blur and any outside pointerdown dismiss without stealing focus.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | ContextMenuItem[] | not specified | Rows to draw. Each is either { id, type: "separator" } or { id, label, shortcut?, icon?, disabled?, onSelect? }. Order and count decide the panel's height before it paints. |
| children | React.ReactNode | not specified | The surface the menu belongs to. It becomes the focusable trigger; right-click, long-press, ContextMenu, Shift+F10 and Enter all open from it. |
| onSelect | (id: string) => void | not specified | Fires with the chosen item's id after the menu has closed and focus has returned. Runs in addition to the item's own onSelect. |
| label | string | "Context menu" | aria-label on the menu. Name it after the row it acts on so a screen reader user knows which of twenty menus opened. |
| width | number | 224 | Panel width in px. Narrowed automatically when the viewport is smaller than width plus both margins. |
| disabled | boolean | false | Removes the trigger from the tab order and lets the browser's native menu through untouched. |
| className | string | "" | Appended last to the trigger, so padding, height and radius are yours to set. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
