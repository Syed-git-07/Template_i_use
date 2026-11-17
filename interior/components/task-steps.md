# task-steps

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/task-steps.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/task-steps.tsx); SHA-256 `6170cb7db78907dc8faff49bfd5443beb53c94f6e2849c8b7048e8e0ff89e567`; 233 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 11 |
| label | string | False | 12 |
| meta | string | True | 14 |
| steps | TaskStep[] | False | 20 |
| current | number | False | 22 |
| failed | boolean | True | 24 |
| spin | boolean | False | 76 |
| label | string | True | 104 |
| className | string | True | 105 |

### Defaults and motion

- Default `failed` = `false` (line 27).
- Default `failed` = `false` (line 111).
- Default `label` = `"Task progress"` (line 112).
- Default `className` = `""` (line 113).
- `stiffness`: 640 (line 6).
- `damping`: 22 (line 6).
- `mass`: 0.7 (line 6).
- `stiffness`: 520 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.45 (line 7).
- `duration`: 0 (line 8).
- `duration`: 0.8 (line 82).
- `ease`: "linear" (line 82).
- `duration`: 1.6 (line 196).
- `ease`: "linear" (line 196).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 152, 163, 174, 185.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The whole plan is mounted from the first paint with pending steps dimmed, so the run moves through existing rows — a step completing changes colours and marks, never geometry, and the panel never grows a pixel.
- The active label shimmers at one constant speed — the spinner's licence extended to type: an honest signal of an unknown wait, not decoration. Under reduced motion it is simply the medium-weight label.
- A completed step's check lands on an underdamped pop in a cell that was reserved all along, and its duration fades in beside it; a failure lands the same way in the flag colour, and nothing after it pretends to have run.
- State is two values — current and failed — so the component can be driven by anything that counts: a websocket, polling, or server-sent events, with no internal timer to fight.
- Screen readers get one settled sentence per stage — 'Building, step 2 of 4' — after a half-second hold, so a run that hops through three stages in a second is one announcement, not three.
- aria-current='step' rides the active row, and the finish is announced once — complete or failed — from its own polite region.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| steps | TaskStep[] | not specified | The plan, in order. Each step is { id, label, meta? }; meta is a right-aligned mono aside — a duration, a count — revealed when its step completes. |
| current | number | not specified | Index of the step running now. Everything before it is done; at steps.length the run is complete. |
| failed | boolean | false | The run stopped at `current`. The active row becomes the failure, and nothing after it pretends to have run. |
| label | string | "Task progress" | Accessible name for the list. |
| className | string | "" | Appended last to the root, so width and spacing are the caller's. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
