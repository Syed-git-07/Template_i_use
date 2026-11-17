# text-reveal

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/text-reveal.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/text-reveal.tsx); SHA-256 `52cb3aa2ad494bfe4b20a27100db8205be454c227dd706f4770df08ccae21eaa`; 148 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| key | string | False | 15 |
| text | string | False | 16 |
| index | number | False | 17 |
| key | string | False | 21 |
| units | TextRevealUnit[] | False | 22 |
| text | string | False | 26 |
| by | TextRevealSplit | True | 27 |
| stagger | number | True | 28 |
| maxDuration | number | True | 29 |
| startOnView | boolean | True | 30 |
| play | boolean | True | 31 |
| once | boolean | True | 32 |
| amount | number | True | 33 |
| className | string | True | 95 |

### Defaults and motion

- Default `by` = `"word"` (line 38).
- Default `stagger` = `0.055` (line 39).
- Default `maxDuration` = `1.6` (line 40).
- Default `startOnView` = `true` (line 41).
- Default `play` = `true` (line 42).
- Default `once` = `true` (line 43).
- Default `amount` = `0.35` (line 44).
- Default `by` = `"word"` (line 100).
- Default `stagger` = `0.055` (line 101).
- Default `maxDuration` = `1.6` (line 102).
- Default `startOnView` = `true` (line 103).
- Default `play` = `true` (line 104).
- Default `once` = `true` (line 105).
- Default `amount` = `0.35` (line 106).
- Default `className` = `""` (line 107).
- `duration`: computed; inspect expression (line 90).
- `duration`: 0 (line 130).
- `duration`: computed; inspect expression (line 132).
- `ease`: computed; inspect expression (line 133).
- `delay`: computed; inspect expression (line 134).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Every word occupies its final wrap position before the first one lights up, so the paragraph never re-wraps mid-reveal and nothing below it moves.
- Only opacity and transform are animated; no width, height, blur or mask-image, so a long paragraph neither relayouts nor repaints a filter on any frame.
- The stagger is clamped by maxDuration, so a four-hundred-word block finishes in the same window as a twelve-word one instead of running for half a minute.
- Screen readers get one complete copy of the sentence and the animated spans are aria-hidden, so nobody hears the text delivered a word at a time.
- Under prefers-reduced-motion the delay and the blur are dropped and the text lands at its final state; the words still arrive, only the trip is skipped.
- Order comes from the unit index, never from a random offset or a timer, so server and client markup agree and there is nothing left running after unmount.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| text | string | not specified | The sentence to reveal. It is rendered in full for assistive technology and split for display, so it is never truncated or reordered. |
| by | "word" \| "character" | "word" | Unit of the stagger. Characters stay grouped inside their word, which cannot break across a line. |
| stagger | number | 0.055 | Seconds between two units, before clamping. This is the reading cadence, not a decoration. |
| maxDuration | number | 1.6 | Ceiling in seconds for the whole reveal. Long text tightens its stagger to fit instead of running for a minute. |
| startOnView | boolean | true | Wait until the element is on screen. Set false when a click or a response, not scrolling, is the trigger. |
| play | boolean | true | External gate. The reveal runs once this and the viewport condition are both satisfied. |
| once | boolean | true | Keep the text revealed after the first pass instead of re-hiding it when it scrolls away. |
| amount | number | 0.35 | Fraction of the element that must be visible before the viewport trigger fires. |
| className | string | "" | Appended last. Set display, size and color here; the root is an inline span until you say otherwise. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
