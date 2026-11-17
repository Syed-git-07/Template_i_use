# command-palette

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/command-palette.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/command-palette.tsx); SHA-256 `c9b0021188e469c30f30eb3e1c15696d5ad853642db2f8fe6ae8f77cc3596b22`; 492 lines.

Imports: `react`, `react-dom`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 15 |
| label | string | False | 16 |
| hint | string | True | 17 |
| keywords | string | True | 18 |
| shortcut | string[] | True | 19 |
| items | CommandItem[] | False | 23 |
| onSelect | (item: CommandItem) => void | False | 24 |
| onDismiss | () => void | True | 25 |
| item | CommandItem | False | 51 |
| score | number | False | 51 |
| order | number | False | 51 |
| items | CommandItem[] | False | 168 |
| onSelect | (item: CommandItem) => void | False | 169 |
| onDismiss | () => void | True | 170 |
| open | boolean | True | 172 |
| placeholder | string | True | 173 |
| emptyLabel | string | True | 174 |
| label | string | True | 175 |
| maxRows | number | True | 176 |
| autoFocus | boolean | True | 177 |
| className | string | True | 178 |
| open | boolean | False | 380 |
| onDismiss | () => void | True | 381 |
| reduced | boolean | False | 382 |
| panelRef | React.RefObject<HTMLDivElement \| null> | False | 383 |
| children | React.ReactNode | False | 384 |

### Defaults and motion

- Default `placeholder` = `"Search commands"` (line 186).
- Default `emptyLabel` = `"No command matches"` (line 187).
- Default `label` = `"Command palette"` (line 188).
- Default `maxRows` = `6` (line 189).
- Default `autoFocus` = `false` (line 190).
- Default `className` = `""` (line 191).
- `stiffness`: 520 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.45 (line 7).
- `stiffness`: 260 (line 8).
- `damping`: 34 (line 8).
- `mass`: 0.8 (line 8).
- `duration`: 0 (line 233).
- `duration`: 0 (line 309).
- `duration`: 0 (line 345).
- `stiffness`: 420 (line 371).
- `damping`: 36 (line 371).
- `mass`: 0.9 (line 371).
- `duration`: 0 (line 451).
- `duration`: 0.2 (line 452).
- `ease`: computed; inspect expression (line 452).
- `duration`: 0 (line 457).
- `duration`: 0.15 (line 458).
- `ease`: computed; inspect expression (line 458).
- `duration`: 0 (line 471).
- `duration`: 0.16 (line 472).
- `ease`: computed; inspect expression (line 472).
- `duration`: 0 (line 475).
- `duration`: 0.15 (line 480).
- `ease`: computed; inspect expression (line 480).

### Input, style and lifecycle

Events: onChange (line 272); onKeyDown (line 273); onMouseDown (line 287); onPointerMove (line 301); onClick (line 302); onDismiss (line 360); keydown (line 401); onPointerDown (line 431); onClick (line 435).

Typography/style anchors: 450, 456, 470, 475, 480.

Source signals: reduced_motion, keyboard, focus, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Selection is anchored to a command id, not to a row index, so a keystroke that reranks the list cannot slide a different command under the highlight between the moment you press Enter and the moment it fires.
- The list box reserves its height from the item count at mount and scrolls inside, so filtering eight commands down to one never resizes the panel or moves the input under the cursor.
- Rows respond to onPointerMove and ignore repeated coordinates, so a reordering list sliding beneath a stationary mouse cannot steal the highlight from the keyboard.
- Ranking is a deterministic subsequence score with a stable index tiebreak: equal scores keep their authored order, so results never shuffle for reasons the typist cannot see.
- Rows move with layout="position" and their own background opacity rather than a shared highlight that flies across the list, and no layout property is animated.
- The result count is written to a polite live region through a ref after a 400ms pause, so a screen reader hears one total instead of one per keystroke, and reduced motion drops every spring while keeping the selection visible.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | CommandItem[] | not specified | The full command set. Each item needs a stable id; label, optional hint, keywords for alias matching, and shortcut keycaps. |
| onSelect | (item: CommandItem) => void | not specified | Runs the highlighted command on Enter or click. Receives the item, never an index. |
| onDismiss | () => void | undefined | Called by Escape only once the query is already empty, so the first Escape clears rather than closes. |
| placeholder | string | "Search commands" | Input placeholder. |
| emptyLabel | string | "No command matches" | Shown inside the reserved list box when nothing matches, and announced to screen readers. |
| label | string | "Command palette" | Accessible name for the combobox and the listbox. |
| maxRows | number | 6 | Rows of height the list reserves. The box is sized once from the item count and never resizes while typing. |
| autoFocus | boolean | false | Focuses the input on mount with preventScroll, so opening the palette never scrolls the page behind it. |
| className | string | not specified | Appended last to the outer panel, so callers can override width, radius or surface. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
