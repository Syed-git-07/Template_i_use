# presence-avatars

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/presence-avatars.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/presence-avatars.tsx); SHA-256 `3fed8e9c4740b385a2aec1073892da2cd08d01620b25e79e58dacced14ce8dd4`; 307 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 16 |
| name | string | False | 17 |
| src | string | True | 18 |
| people | PresencePerson[] | False | 22 |
| max | number | True | 23 |
| announceAfter | number | True | 24 |
| ordered | PresencePerson[] | False | 28 |
| visible | PresencePerson[] | False | 29 |
| hidden | PresencePerson[] | False | 30 |
| overflow | number | False | 31 |
| total | number | False | 32 |
| summary | string | False | 33 |
| announcement | string | False | 34 |
| person | PresencePerson | False | 103 |
| index | number | False | 104 |
| step | number | False | 105 |
| size | number | False | 106 |
| zIndex | number | False | 107 |
| reduced | boolean | False | 108 |
| status | FaceStatus | False | 115 |
| instant | boolean | False | 115 |
| people | PresencePerson[] | False | 200 |
| max | number | True | 201 |
| size | number | True | 202 |
| overlap | number | True | 203 |
| label | string | True | 204 |
| announceAfter | number | True | 205 |
| onOverflowSelect | (hidden: PresencePerson[]) => void | True | 206 |
| className | string | True | 207 |

### Defaults and motion

- Default `max` = `5` (line 55).
- Default `announceAfter` = `900` (line 56).
- Default `max` = `5` (line 212).
- Default `size` = `28` (line 213).
- Default `overlap` = `9` (line 214).
- Default `label` = `"People here"` (line 215).
- Default `className` = `""` (line 218).
- `stiffness`: 520 (line 11).
- `damping`: 34 (line 11).
- `mass`: 0.45 (line 11).
- `duration`: 0.24 (line 12).
- `ease`: computed; inspect expression (line 12).
- `duration`: 0 (line 13).

### Input, style and lifecycle

Events: load (line 151); error (line 152); onClick (line 275).

Typography/style anchors: 243.

Source signals: reduced_motion, cleanup, async, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The rail is exactly as wide as who is actually here, and it grows on the same spring the arriving avatar rides in on. A rail padded out to its widest reachable state leaves a hole where nobody is standing; one that snaps open around a person reads as two events instead of one.
- First-seen order is held in a ref, so an arrival cannot reshuffle the people already present, and someone who reconnects returns to the slot they had.
- Avatars are placed by transform inside a positioned rail, never by layout: a leaver exits on opacity and scale while the survivors spring into the freed slots.
- The photo is laid over the initials and fades in when it decodes, so a slow avatar is a name rather than an empty square, and one that never arrives stays a name.
- Each tile is two shells. The outer one is the hairline given 2px of thickness rather than one, so the rim around a face is a single colour instead of a border with a lighter band trapped inside it; outside that, 2px of the surface keeps neighbouring faces apart. A photo that runs straight into its own edge reads as a sticker.
- The overflow chip is a tabular cell that caps at +99, so counting from +9 to +12 changes the digits and nothing else.
- Screen readers get one debounced summary of the room instead of one announcement per arrival, and the roster behind the chip stays readable as a list rather than disappearing into a number.
- Under prefers-reduced-motion the slots fill and empty instantly; no avatar and no count is withheld, only the trip between positions.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| people | PresencePerson[] | not specified | The room, in any order. Each entry is { id, name, src? }; id is the identity that survives a re-render, name supplies the initials and the spoken roster, src is the photo laid over them. |
| max | number | 5 | Avatar slots drawn before the overflow chip takes over. |
| size | number | 28 | Edge of one square tile in pixels. Font size and the rail width are derived from it. |
| overlap | number | 9 | Pixels each tile hides of the one before it. The step between slots is size minus overlap. |
| label | string | "People here" | Accessible name for the group wrapping the rail, the roster list and the live region. |
| announceAfter | number | 900 | Quiet period in milliseconds before the roster summary reaches the live region. A burst of joins collapses into one announcement. |
| onOverflowSelect | (hidden: PresencePerson[]) => void | not specified | Given, the overflow chip becomes a real button with a focus ring and receives the people it is standing in for. Omitted, the chip is decorative and hidden from assistive tech. |
| className | string | "" | Appended last to the outer group, so callers can override spacing and alignment. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
