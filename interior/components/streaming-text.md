# streaming-text

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/streaming-text.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/streaming-text.tsx); SHA-256 `5858dd357ff6c203d23317c438446a84f6ab474157aa289b7b5d03f5f2d83023`; 271 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| word | string | False | 19 |
| gap | string | False | 19 |
| text | string | False | 37 |
| tokensPerSecond | number | True | 38 |
| autoStart | boolean | True | 39 |
| onDone | () => void | True | 40 |
| text | string | False | 155 |
| tokensPerSecond | number | True | 156 |
| autoStart | boolean | True | 157 |
| showSkip | boolean | True | 158 |
| label | string | True | 159 |
| onDone | () => void | True | 160 |
| className | string | True | 161 |

### Defaults and motion

- Default `tokensPerSecond` = `18` (line 45).
- Default `autoStart` = `true` (line 46).
- Default `tokensPerSecond` = `18` (line 166).
- Default `autoStart` = `true` (line 167).
- Default `showSkip` = `true` (line 168).
- Default `label` = `"Streamed response"` (line 169).
- Default `className` = `""` (line 171).
- `stiffness`: 260 (line 10).
- `damping`: 34 (line 11).
- `mass`: 0.8 (line 12).
- `duration`: 1.06 (line 197).
- `ease`: "linear" (line 200).
- `duration`: 0 (line 252).
- `duration`: 0 (line 261).

### Input, style and lifecycle

Events: onClick (line 232).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, cleanup, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The finished paragraph is laid out on the first frame and unrevealed words are held at opacity zero, so a growing answer never pushes the actions beneath it down the page.
- The caret is drawn inside a collapsed inline box with no width, so advancing it through the sentence cannot nudge a word onto the next line.
- Screen readers receive the completed text once from a polite status region and the visible token layer is aria-hidden, rather than sixty interruptions as words arrive.
- Tokens advance on accumulated elapsed time with the per-frame delta clamped, so a tab returning from the background does not dump the remainder of the answer in a single frame.
- Under prefers-reduced-motion the whole answer is present immediately and reports done; the text is never withheld behind an effect someone asked not to see.
- The reveal is stepped per token rather than per frame, and every animation frame is cancelled when the status changes or the component unmounts.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| text | string | not specified | The full string to stream. Changing it restarts the stream from the first token. |
| tokensPerSecond | number | 18 | Reveal rate in words per second. Time is accumulated, not counted in frames, so the rate holds on a slow display. |
| autoStart | boolean | true | When false the component sits at zero tokens with a blinking caret until start() is called on the hook. |
| showSkip | boolean | true | Renders the keyboard-reachable skip control. Its row is present in every state, so hiding it is a layout decision, not a runtime one. |
| label | string | "Streamed response" | Accessible name for the group and the basis of the skip button's label. |
| onDone | () => void | not specified | Fires once when the last token lands, including when reduced motion skips the stream entirely. |
| className | string | "" | Appended last on the root, which carries the type styles, so size, colour and measure are all overridable. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
