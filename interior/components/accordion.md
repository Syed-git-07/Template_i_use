# accordion

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/accordion.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/accordion.tsx); SHA-256 `7e5e4c07ee772973bd4cce728a94e4eb1d1c628dd7e153ddfd2335b2e7e5b07e`; 397 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| inert | boolean | True | 36 |
| ref | React.RefObject<HTMLDivElement \| null> | False | 39 |
| height | number | False | 40 |
| ready | boolean | False | 41 |
| id | string | False | 71 |
| id | string | False | 75 |
| ref | (node: HTMLButtonElement \| null) => void | False | 76 |
| type | "button" | False | 77 |
| onClick | () => void | False | 78 |
| onKeyDown | (event: React.KeyboardEvent) => void | False | 79 |
| "aria-expanded" | boolean | False | 80 |
| "aria-controls" | string | False | 81 |
| id | string | False | 85 |
| role | "region" | False | 86 |
| "aria-labelledby" | string | False | 87 |
| "aria-hidden" | true \| undefined | False | 88 |
| items | readonly AccordionEntry[] | False | 92 |
| type | "single" \| "multiple" | True | 93 |
| defaultOpen | readonly string[] | True | 94 |
| open | readonly string[] | True | 95 |
| onOpenChange | (open: string[]) => void | True | 96 |
| collapsible | boolean | True | 97 |
| open | string[] | False | 101 |
| isOpen | (id: string) => boolean | False | 102 |
| toggle | (id: string) => void | False | 103 |
| headerProps | (id: string) => AccordionHeaderProps | False | 104 |
| panelProps | (id: string) => AccordionPanelProps | False | 105 |
| id | string | False | 223 |
| title | React.ReactNode | False | 224 |
| content | React.ReactNode | False | 225 |
| meta | React.ReactNode | True | 226 |
| items | readonly AccordionItem[] | False | 230 |
| type | "single" \| "multiple" | True | 231 |
| defaultOpen | readonly string[] | True | 232 |
| open | readonly string[] | True | 233 |
| onOpenChange | (open: string[]) => void | True | 234 |
| collapsible | boolean | True | 235 |
| maxPanelHeight | number | True | 236 |
| headingLevel | number | True | 237 |
| className | string | True | 238 |
| item | AccordionItem | False | 294 |
| open | boolean | False | 295 |
| reduced | boolean | False | 296 |
| maxPanelHeight | number | False | 297 |
| headingLevel | number | False | 298 |
| header | AccordionHeaderProps | False | 299 |
| panel | AccordionPanelProps | False | 300 |

### Defaults and motion

- Default `type` = `"single"` (line 110).
- Default `collapsible` = `true` (line 114).
- Default `type` = `"single"` (line 243).
- Default `collapsible` = `true` (line 247).
- Default `maxPanelHeight` = `220` (line 248).
- Default `headingLevel` = `3` (line 249).
- Default `className` = `""` (line 250).
- `stiffness`: 480 (line 19).
- `damping`: 40 (line 20).
- `mass`: 0.6 (line 21).
- `stiffness`: 700 (line 26).
- `damping`: 46 (line 27).
- `mass`: 0.5 (line 28).
- `duration`: 0 (line 345).
- `duration`: 0 (line 360).
- `duration`: 0 (line 383).
- `duration`: 0.18 (line 385).
- `ease`: computed; inspect expression (line 385).
- `duration`: 0.14 (line 386).
- `ease`: computed; inspect expression (line 386).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, focus, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Panel height is measured from the panel's own box with a ResizeObserver rather than read once on open, so a panel that rewraps on resize, or grows when a font or image lands, never animates to a stale target.
- The first paint renders closed panels at zero and open panels at auto and only starts animating once a real measurement exists, so nothing flashes open and snaps shut on hydration.
- A closed panel is inert and aria-hidden, so Tab never lands on a link inside a section nobody can see and a screen reader never reads it out.
- Height is capped and the overflow scrolls inside the cap, so a panel holding two hundred rows cannot animate to an unbounded height or push the rest of the page off screen.
- The height spring is interruptible in both directions: toggling mid-flight, or growing the content while the panel is open, retargets from the current height instead of restarting from zero, and opacity finishes first so the reflow is hidden.
- Headers are real buttons carrying aria-expanded and aria-controls, with Arrow keys, Home and End moving between them; useAccordion exports that state and keyboard behaviour, and useAutoHeight exports the measurement alone, for surfaces you want to draw yourself.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | readonly AccordionItem[] | not specified | Rows to render. Each is { id, title, content, meta? }; id must be stable because it keys both the open set and the aria wiring. |
| type | "single" \| "multiple" | "single" | Whether opening a row closes its siblings or leaves them alone. |
| defaultOpen | readonly string[] | [] | Uncontrolled starting open set. In single mode only the first id is honoured. |
| open | readonly string[] | not specified | Controlled open set. Supplying it makes the parent the source of truth. |
| onOpenChange | (open: string[]) => void | not specified | Fires with the next open set on every toggle, controlled or not. |
| collapsible | boolean | true | In single mode, whether the open row can be clicked shut leaving nothing open. |
| maxPanelHeight | number | 220 | Ceiling in pixels for a panel. Content past it scrolls inside the panel with overscroll contained. |
| headingLevel | number | 3 | aria-level for the header wrapper, so the accordion slots into the surrounding document outline. |
| className | string | "" | Appended last to the outer frame, so callers can override the border, surface and radius. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
