# lightbox

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/lightbox.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/lightbox.tsx); SHA-256 `4cfffe45e6e8dfdaab9fe6f1a5f67f06ef52f52790ef12ec310b77a87a3eb8fd`; 721 lines.

Imports: `react`, `react-dom`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| type | "spring" | False | 63 |
| stiffness | number | False | 64 |
| damping | number | False | 65 |
| mass | number | False | 66 |
| id | number | False | 73 |
| from | { x: number; y: number } | False | 74 |
| x | number | False | 74 |
| y | number | False | 74 |
| x | number | False | 75 |
| y | number | False | 76 |
| maxScale | number | True | 80 |
| steps | number | True | 81 |
| disabled | boolean | True | 82 |
| onDismiss | () => void | True | 83 |
| open | boolean | False | 375 |
| onClose | () => void | False | 376 |
| src | string | False | 377 |
| alt | string | False | 378 |
| originRef | React.RefObject<HTMLElement \| null> | True | 379 |
| caption | string | True | 380 |
| width | number | True | 381 |
| height | number | True | 382 |
| maxScale | number | True | 383 |
| className | string | True | 384 |
| dx | number | False | 387 |
| dy | number | False | 387 |
| s | number | False | 387 |
| o | number | False | 387 |
| r | number | False | 387 |

### Defaults and motion

- Default `maxScale` = `4` (line 90).
- Default `steps` = `8` (line 91).
- Default `disabled` = `false` (line 92).
- Default `maxScale` = `4` (line 397).
- Default `className` = `""` (line 398).
- `stiffness`: 520 (line 22).
- `damping`: 34 (line 23).
- `mass`: 0.45 (line 24).
- `stiffness`: 150 (line 29).
- `damping`: 27 (line 30).
- `mass`: 1 (line 31).
- `stiffness`: 260 (line 36).
- `damping`: 34 (line 37).
- `mass`: 0.8 (line 38).
- `duration`: 0.2 (line 42).
- `ease`: computed; inspect expression (line 42).
- `stiffness`: 700 (line 46).
- `damping`: 46 (line 47).
- `mass`: 0.5 (line 48).
- `duration`: 0.12 (line 491).
- `duration`: 0 (line 509).
- `duration`: 0 (line 584).
- `duration`: 0.3 (line 584).
- `ease`: computed; inspect expression (line 584).
- `duration`: 0 (line 586).
- `duration`: 0 (line 610).
- `duration`: 0.35 (line 611).
- `ease`: computed; inspect expression (line 611).
- `duration`: 0 (line 632).
- `duration`: 0 (line 633).
- `duration`: 0 (line 666).

### Input, style and lifecycle

Events: wheel (line 342); blur (line 350); keydown (line 566); onClick (line 646); onClick (line 673).

Typography/style anchors: 491, 500, 509, 584, 632.

Source signals: reduced_motion, keyboard, pointer_cancel, focus, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The image returns to the rect its trigger occupies at the moment of closing, not the one cached when it opened, so a scroll, a resize, or a reflow behind the overlay cannot make it land beside the thumbnail.
- The wheel zooms toward the cursor, so the detail under the pointer stays under the pointer; double-click toggles between fit and a close-up centred on the click, and a single drag pans while zoomed.
- Pan is clamped against the image's own edges at every scale, so the picture cannot be flung past the frame and abandoned in empty space, and any release under 1.05x snaps back to exactly 1.0 rather than to 1.01.
- Escape unwinds the zoom on the first press and closes on the second, so a close-up is never a one way trip out of the viewer; the trigger gets focus back when the overlay leaves, and only if it is still in the document.
- Scale and offset are written to the node through motion values, so a drag does not re-render React; the zoom readout moves in whole cells and the screen reader is told the settled level once, 220ms after the wheel stops.
- Reduced motion keeps the overlay, the zoom and the return, and drops only the travel between them; the body scroll lock adds the scrollbar's width to the padding the page already had, so nothing underneath shifts.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| open | boolean | not specified | Whether the overlay is mounted. The caller owns it, so the trigger stays the caller's element. |
| onClose | () => void | not specified | Fired by Escape, the close button, and a click on the backdrop while unzoomed. The overlay stays mounted until the return flight finishes. |
| src | string | not specified | Full-size image source. Keep it set through the close animation; clearing it mid-exit leaves a broken image flying home. |
| alt | string | not specified | Names the image and, when no caption is given, labels the dialog. |
| originRef | React.RefObject<HTMLElement \| null> | undefined | The element the image should return to. Point it at the clicked thumbnail in the click handler. Omitted, the overlay falls back to a 0.97 scale enter and exit. |
| caption | string | undefined | Label shown top-left and used as the dialog's accessible name. |
| width | number | undefined | Intrinsic pixel width. Reserves the image box before the file loads so the opening flight has something to measure. |
| height | number | undefined | Intrinsic pixel height, paired with width. |
| maxScale | number | 4 | Ceiling for wheel, double-click and keyboard zoom. Values at or below 1.1 are raised to 1.1. |
| useLightbox.steps | number | 8 | Hook option only. Quantises how often zoom progress reaches React; the component draws no meter. |
| className | string | "" | Appended last to the fixed overlay shell. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
