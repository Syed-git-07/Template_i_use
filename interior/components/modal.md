# modal

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/modal.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/modal.tsx); SHA-256 `4ea9cad96c2685dcc4e24c31b04753a2890cbeaca74779d39bd4744551e01c0e`; 463 lines.

Imports: `react`, `react-dom`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| open | boolean | False | 81 |
| onClose | () => void | False | 82 |
| closeOnEscape | boolean | True | 83 |
| closeOnBackdrop | boolean | True | 84 |
| lockScroll | boolean | True | 85 |
| initialFocusRef | React.RefObject<HTMLElement \| null> | True | 86 |
| container | HTMLElement \| null | True | 87 |
| ref | React.RefObject<HTMLDivElement \| null> | False | 91 |
| onPointerDown | (event: React.PointerEvent) => void | False | 92 |
| onClick | (event: React.MouseEvent) => void | False | 93 |
| ref | React.RefObject<HTMLDivElement \| null> | False | 97 |
| role | "dialog" | False | 98 |
| "aria-modal" | true | False | 99 |
| "aria-labelledby" | string | False | 100 |
| tabIndex | -1 | False | 101 |
| onKeyDown | (event: React.KeyboardEvent) => void | False | 102 |
| target | HTMLElement \| null | False | 106 |
| titleId | string | False | 107 |
| descriptionId | string | False | 108 |
| overlayProps | ModalOverlayProps | False | 109 |
| panelProps | ModalPanelProps | False | 110 |
| close | () => void | False | 111 |
| open | boolean | False | 300 |
| onClose | () => void | False | 301 |
| title | React.ReactNode | False | 302 |
| description | React.ReactNode | True | 303 |
| children | React.ReactNode | True | 304 |
| footer | React.ReactNode | True | 305 |
| closeLabel | string | True | 306 |
| showClose | boolean | True | 307 |
| closeOnEscape | boolean | True | 308 |
| closeOnBackdrop | boolean | True | 309 |
| lockScroll | boolean | True | 310 |
| initialFocusRef | React.RefObject<HTMLElement \| null> | True | 311 |
| container | HTMLElement \| null | True | 312 |
| maxWidth | number | True | 313 |
| maxHeight | string | True | 314 |
| className | string | True | 315 |

### Defaults and motion

- Default `closeOnEscape` = `true` (line 117).
- Default `closeOnBackdrop` = `true` (line 118).
- Default `lockScroll` = `true` (line 119).
- Default `closeLabel` = `"Close dialog"` (line 325).
- Default `showClose` = `true` (line 326).
- Default `closeOnEscape` = `true` (line 327).
- Default `closeOnBackdrop` = `true` (line 328).
- Default `lockScroll` = `true` (line 329).
- Default `maxWidth` = `440` (line 332).
- Default `maxHeight` = `"min(78vh, 620px)"` (line 333).
- Default `className` = `""` (line 334).
- `stiffness`: 420 (line 19).
- `damping`: 36 (line 19).
- `mass`: 0.9 (line 19).
- `duration`: 0 (line 353).
- `duration`: 0 (line 354).
- `duration`: 0 (line 358).
- `duration`: 0 (line 359).
- `duration`: 0.2 (line 366).
- `ease`: computed; inspect expression (line 366).
- `duration`: 0.15 (line 367).
- `ease`: computed; inspect expression (line 367).
- `duration`: 0.16 (line 375).
- `ease`: computed; inspect expression (line 375).
- `duration`: 0.15 (line 382).
- `ease`: computed; inspect expression (line 382).

### Input, style and lifecycle

Events: keydown (line 183); focusin (line 199); onClick (line 436).

Typography/style anchors: 353, 354, 358, 359, 366, 367, 375, 382.

Source signals: reduced_motion, keyboard, focus, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The scrollbar's width is measured and added back as body padding for as long as the lock is held, so the page behind does not jump sideways when the dialog opens or closes.
- The scroll lock is reference counted and the Escape stack is ordered, so a dialog opened from inside another one does not hand scrolling back when only the inner one closes, and Escape reaches the topmost dialog only.
- Tab and Shift-Tab wrap at the ends of the panel, a focusin guard pulls stray focus back, and on close focus returns to the element that opened the dialog with preventScroll, so the page never scrolls to a control the user cannot see.
- Every sibling of the overlay is marked inert while the dialog is open and restored to its prior value on close, so a screen reader reads the dialog instead of the page underneath it, and the background cannot be reached by pointer or keyboard.
- A backdrop press dismisses only when it both starts and ends outside the panel, so a text selection dragged past the edge of the dialog does not throw the dialog away.
- The overlay is portalled out of the tree, so a transformed, filtered or overflow-hidden ancestor cannot re-anchor or clip the fixed layer; the panel height is capped and scrolls internally rather than animating toward an unbounded height; under prefers-reduced-motion the same dialog arrives at zero duration rather than being withheld. Behaviour is available on its own through the exported useModal hook.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| open | boolean | not specified | Controlled visibility. The overlay mounts and unmounts with it; exit runs before removal. |
| onClose | () => void | not specified | Called by Escape, the backdrop, and the close button. The component never closes itself. |
| title | React.ReactNode | not specified | Rendered as the h2 the dialog is labelled by. |
| description | React.ReactNode | undefined | Optional. Present only when set, and only then is aria-describedby applied. |
| children | React.ReactNode | not specified | Body content. Scrolls inside the capped panel rather than growing it. |
| footer | React.ReactNode | undefined | Action row on a hairline divider. Stays put while the body scrolls. |
| initialFocusRef | React.RefObject<HTMLElement \| null> | first focusable element | Element focused on open. Point it at the safe action when the dialog is destructive. |
| closeOnEscape | boolean | true | Escape is answered by the topmost open dialog only. |
| closeOnBackdrop | boolean | true | Requires the press to both start and end outside the panel. |
| lockScroll | boolean | true | Holds a reference-counted lock on document scrolling for as long as any dialog is open. |
| showClose | boolean | true | Hides the corner close button for dialogs that demand an explicit choice. |
| closeLabel | string | "Close dialog" | Accessible name for the close button. |
| container | HTMLElement \| null | document.body | Portal target. Pass null to render nothing; pass an element to scope the overlay and the inert treatment to it. |
| maxWidth | number | 440 | Panel width cap in pixels. |
| maxHeight | string | "min(78vh, 620px)" | Panel height cap. The body scrolls once content passes it. |
| className | string | "" | Appended last to the panel. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
