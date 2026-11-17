# value-flash

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/value-flash.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/value-flash.tsx); SHA-256 `9758bfbacd2eb73c44b619044495988d0eff7cba071d74ae28f3ed1ac3029010`; 219 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| hold | number | True | 28 |
| compare | (next: T, previous: T) => number | True | 29 |
| direction | FlashDirection \| null | False | 33 |
| from | T | False | 34 |
| changeId | number | False | 35 |
| flashing | boolean | False | 36 |
| value | number | False | 97 |
| format | (value: number) => string | True | 98 |
| label | string | True | 99 |
| hold | number | True | 100 |
| announceAfter | number | True | 101 |
| className | string | True | 102 |

### Defaults and motion

- Default `hold` = `900` (line 41).
- Default `hold` = `900` (line 109).
- Default `announceAfter` = `700` (line 110).
- Default `className` = `""` (line 111).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `stiffness`: 460 (line 8).
- `damping`: 32 (line 8).
- `mass`: 0.55 (line 8).
- `stiffness`: 640 (line 10).
- `damping`: 22 (line 10).
- `mass`: 0.7 (line 10).
- `stiffness`: 380 (line 12).
- `damping`: 26 (line 12).
- `mass`: 0.7 (line 12).
- `stiffness`: 260 (line 14).
- `damping`: 34 (line 14).
- `mass`: 0.8 (line 14).
- `duration`: 0.16 (line 16).
- `ease`: computed; inspect expression (line 16).
- `duration`: 0.14 (line 17).
- `ease`: computed; inspect expression (line 17).
- `duration`: 0 (line 18).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 168, 173, 202, 203.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Nothing flashes on first paint: the previous value is seeded at mount, so a hydrated table does not light every row before the user has done anything.
- A re-render that leaves the value identical is ignored under Object.is, and a change whose delta is zero is ignored too — there is no third, directionless flash, because a blink with no direction is the one nobody can read.
- Direction speaks three ways at once — moss or flag tint for the glance, a solid triangle in a permanently reserved cell for greyscale and colour blindness, and the new number rolling in from the side it moved — so the row never reflows and the change is legible at any speed.
- The tint is an absolutely positioned overlay fading its opacity on a spring, never a width, height or mask animation, and it decays once instead of looping so a stale figure can never keep looking fresh.
- Screen readers get one announcement per settled value: each tick restarts a quiet period, so a fast feed does not read sixty numbers a second into the live region.
- Every timer is cleared on the next change and on unmount, so a row removed mid-flash leaves nothing scheduled and no state set on a dead component.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| value | number | not specified | The number to watch. A change of identity, not of render, is what marks it. |
| format | (value: number) => string | String | Formats the displayed text. Rendered with tabular-nums so equal-length values never jitter. |
| label | string | not specified | Prefixes the live-region announcement, so a screen reader hears which figure moved. |
| hold | number | 900 | Milliseconds the tint and direction mark stay lit before clearing themselves. |
| announceAfter | number | 700 | Quiet period before the settled value is announced. Each new change restarts it. |
| className | string | "" | Appended last, so callers can override type size, weight and colour. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
