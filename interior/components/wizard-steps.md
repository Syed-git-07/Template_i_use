# wizard-steps

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/wizard-steps.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/wizard-steps.tsx); SHA-256 `82bba1df775b9b528c270d6f7f1ca6bab590fe5367d02dea82fc44b45aff14ad`; 425 lines.

Imports: `react`, `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| total | number | False | 16 |
| index | number | True | 17 |
| defaultIndex | number | True | 18 |
| onIndexChange | (index: number, direction: WizardDirection) => void | True | 19 |
| onComplete | () => void | True | 20 |
| index | number | False | 24 |
| direction | WizardDirection | False | 25 |
| furthest | number | False | 26 |
| total | number | False | 27 |
| isFirst | boolean | False | 28 |
| isLast | boolean | False | 29 |
| next | () => void | False | 30 |
| back | () => void | False | 31 |
| goTo | (index: number) => void | False | 32 |
| index | number | False | 50 |
| direction | WizardDirection | False | 50 |
| id | string | False | 103 |
| label | string | False | 104 |
| content | ReactNode | False | 105 |
| steps | WizardStep[] | False | 109 |
| index | number | True | 110 |
| defaultIndex | number | True | 111 |
| onIndexChange | (index: number, direction: WizardDirection) => void | True | 112 |
| onComplete | () => void | True | 113 |
| complete | boolean | True | 115 |
| height | number | True | 116 |
| backLabel | string | True | 117 |
| nextLabel | string | True | 118 |
| finishLabel | string | True | 119 |
| completeLabel | string | True | 120 |
| completeHint | string | True | 121 |
| label | string | True | 122 |
| className | string | True | 123 |

### Defaults and motion

- Default `defaultIndex` = `0` (line 43).
- Default `defaultIndex` = `0` (line 129).
- Default `complete` = `false` (line 132).
- Default `height` = `184` (line 133).
- Default `backLabel` = `"Back"` (line 134).
- Default `nextLabel` = `"Next"` (line 135).
- Default `finishLabel` = `"Finish"` (line 136).
- Default `completeLabel` = `"All set"` (line 137).
- Default `completeHint` = `"Step back to change anything"` (line 138).
- Default `label` = `"Steps"` (line 139).
- Default `className` = `""` (line 140).
- `stiffness`: 520 (line 10).
- `damping`: 40 (line 10).
- `mass`: 0.5 (line 10).
- `stiffness`: 260 (line 11).
- `damping`: 34 (line 11).
- `mass`: 0.8 (line 11).
- `duration`: 0 (line 175).
- `duration`: 0.14 (line 179).
- `ease`: computed; inspect expression (line 179).
- `duration`: 0 (line 185).
- `duration`: 0 (line 221).
- `duration`: 0 (line 248).
- `duration`: 0 (line 308).
- `duration`: 0 (line 362).
- `duration`: 0.12 (line 362).
- `ease`: computed; inspect expression (line 362).
- `duration`: 0 (line 364).
- `duration`: 0.16 (line 364).
- `ease`: computed; inspect expression (line 364).
- `duration`: 0 (line 391).
- `duration`: 0.14 (line 392).
- `ease`: computed; inspect expression (line 392).
- `duration`: 0 (line 394).
- `duration`: 0 (line 405).
- `duration`: 0 (line 414).

### Input, style and lifecycle

Events: onKeyDown (line 282); onClick (line 283); onClick (line 365); onClick (line 381).

Typography/style anchors: 175, 179, 362, 390.

Source signals: reduced_motion, keyboard, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The index and the direction are held in one state object, so no frame can render a new step with the previous direction — the bug where pressing Back slides forward for one frame and then corrects itself.
- The panel viewport is a fixed height with its own scroll, so a two-line step and a twenty-line step do not resize the page mid-transition and the Back button stays where the cursor left it.
- Next and Finish occupy the same grid cell and only opacity moves between them, so reaching the last step never changes the button's width.
- Under prefers-reduced-motion the panel still swaps and the markers still fill; only the travel and the blur are dropped, and nothing is hidden.
- Back and Next move focus into the new panel, arrow keys move focus along the step markers, and markers past the furthest step reached stay disabled so nobody lands on a step they have not filled in.
- Screen readers get one polite announcement per step — "Step 2 of 4: Billing details" — instead of a stream of updates while the panel is in flight; the behaviour also ships alone as useWizard for anyone drawing their own chrome.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| steps | WizardStep[] | not specified | Ordered steps, each { id, label, content }. The id keys the panel, so it must be stable across renders. |
| index | number | not specified | Controlled step. Direction is still derived from the previous value, so external navigation animates the right way. |
| defaultIndex | number | 0 | Uncontrolled starting step, clamped into range. |
| onIndexChange | (index: number, direction: 1 \| -1) => void | not specified | Fires with the step and the direction of travel, never on a no-op move. |
| onComplete | () => void | not specified | Fires when the primary button is pressed on the last step. |
| height | number | 184 | Fixed height of the panel viewport in px. Content taller than this scrolls inside it. |
| backLabel | string | "Back" | Label for the secondary button, which is disabled rather than removed on the first step. |
| nextLabel | string | "Next" | Primary label before the last step. |
| finishLabel | string | "Finish" | Primary label on the last step. Shares a grid cell with nextLabel so the button never resizes. |
| label | string | "Steps" | Accessible name for the step marker list. |
| className | string | "" | Appended last, so callers can override any of the outer classes. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
