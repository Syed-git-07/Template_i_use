# poll-results

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/poll-results.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/poll-results.tsx); SHA-256 `25df8a7380623fdabf06fb119f98d18185b02dac46be8234b3710b067afb1bea`; 268 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 22 |
| label | string | False | 23 |
| votes | number | False | 24 |
| options | PollOption[] | False | 28 |
| value | string \| null | True | 30 |
| defaultValue | string \| null | True | 31 |
| onVote | (id: string) => void | True | 32 |
| label | string | False | 92 |
| share | number | False | 93 |
| winner | boolean | False | 94 |
| mine | boolean | False | 95 |
| revealed | boolean | False | 96 |
| reduced | boolean | False | 97 |
| onPick | () => void | False | 98 |
| label | string | False | 202 |
| className | string | True | 203 |

### Defaults and motion

- Default `defaultValue` = `null` (line 38).
- Default `className` = `""` (line 212).
- `stiffness`: 210 (line 14).
- `damping`: 34 (line 14).
- `mass`: 0.9 (line 14).
- `stiffness`: 640 (line 16).
- `damping`: 22 (line 16).
- `mass`: 0.7 (line 16).
- `duration`: 0.2 (line 18).
- `ease`: computed; inspect expression (line 18).
- `duration`: 0 (line 19).
- `delay`: 0.4 (line 256).

### Input, style and lifecycle

Events: onClick (line 134); onPick (line 248).

Typography/style anchors: 169.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The reveal is a race run on physics: every bar leaves the line at the same instant on the same spring, so a longer share is simply a longer road — the biggest number arrives last and the winner is announced by its own landing, not by a stage-managed delay.
- Each percentage is its bar's own motion value written straight to the DOM, so the numbers count up in lockstep with the fills while React renders once per vote, not once per frame.
- Your answer runs in the accent and the rest of the field runs in ink — the one bar that is a response to you is the one drawn in the colour reserved for that.
- The fill is a clipPath sweep over a fully-rounded bar, so the corners never stretch, and the winner's check pops only after the winning bar has landed.
- The material tells the story: before the vote every option is a pressable key — cap material, top light, bottom lip, a pixel of travel under the finger — and the vote turns the key into the slot it was hiding, a recessed well the result sweeps inside. Depth is the state change; colour only signs it.
- Nothing moves but the fills: the percent column and the tally line reserve their space before the first vote exists, and a revealed row refuses further clicks with aria-disabled instead of leaving the accessibility tree.
- Screen readers get the outcome once, as a sentence — who leads, with what share, out of how many votes — after the race has settled; under prefers-reduced-motion the bars are simply at their numbers.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| options | PollOption[] | not specified | The choices, each { id, label, votes }. Votes are the truth the reveal draws; update them optimistically in onVote. |
| label | string | not specified | The question. Required — a poll with no name is unreadable, to everyone. |
| value | string \| null | not specified | Controlled choice. null means not voted; anything else reveals the results. |
| defaultValue | string \| null | null | Uncontrolled starting choice, for a poll the person already answered. |
| onVote | (id: string) => void | not specified | Fires once, on the first choice. Later clicks are refused — one person, one vote. |
| className | string | "" | Appended last to the root, so width and spacing are the caller's. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
