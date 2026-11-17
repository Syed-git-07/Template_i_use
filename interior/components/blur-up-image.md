# blur-up-image

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/blur-up-image.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/blur-up-image.tsx); SHA-256 `e05cb7fb553be965f70145c7321d2beeb2d04e20683ed82847659559edd59d21`; 225 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| src | string | True | 17 |
| srcSet | string | True | 18 |
| onReady | () => void | True | 19 |
| onError | () => void | True | 20 |
| status | BlurUpStatus | False | 31 |
| instant | boolean | False | 32 |
| src | string | True | 109 |
| alt | string | False | 110 |
| width | number | False | 111 |
| height | number | False | 112 |
| placeholder | string | True | 113 |
| color | string | True | 114 |
| blur | number | True | 115 |
| radius | 5 \| 6 \| 9 \| 11 \| 14 | True | 116 |
| srcSet | string | True | 117 |
| sizes | string | True | 118 |
| loading | "lazy" \| "eager" | True | 119 |
| fetchPriority | "high" \| "low" \| "auto" | True | 120 |
| onReady | () => void | True | 121 |
| onError | () => void | True | 122 |
| className | string | True | 123 |

### Defaults and motion

- Default `blur` = `14` (line 133).
- Default `radius` = `11` (line 134).
- Default `loading` = `"lazy"` (line 137).
- Default `className` = `""` (line 141).
- `duration`: 0.65 (line 10).
- `ease`: computed; inspect expression (line 10).
- `duration`: 0 (line 12).

### Input, style and lifecycle

Events: load (line 90); error (line 91).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, cleanup, async, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The box is reserved from width and height as an aspect ratio, so the caption under a photo sits in its final position before a single byte arrives, and the frame keeps that space when the URL is dead instead of collapsing the page.
- An image that is already in the browser cache is detected in a layout effect before paint and revealed with a zero-duration transition, so a cached photo never flashes its own placeholder or plays a fade nobody asked for.
- The reveal waits on decode(), not on the load event, because a load event only promises the bytes arrived — swapping there can hand the compositor an undecoded bitmap and drop the frame the swap happens on.
- The blur is a constant on a static placeholder; only opacity and scale animate, because an animated filter repaints the full image every frame and cannot be composited.
- A failed load lands on a drawn glyph in the same frame at the same size, so a broken URL degrades to a state rather than to a browser default and a reflow.
- Under prefers-reduced-motion the photo replaces the placeholder immediately; nothing is hidden, only the crossfade is skipped, and the alt text is on the real element the whole time so it is available before the image is.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| src | string \| undefined | not specified | The full image. Undefined is a legal state — the placeholder holds while the URL is still being resolved, and it is not treated as an error. |
| alt | string | not specified | Required. Lives on the real <img> for the whole lifecycle, so the description is available before the bytes are. |
| width | number | not specified | Intrinsic width. Used with height to reserve the box before anything loads. |
| height | number | not specified | Intrinsic height. Used with width to reserve the box before anything loads. |
| placeholder | string | undefined | A tiny LQIP data URI. Blurred statically and never animated; only its opacity and scale move. |
| color | string | undefined | Dominant colour painted under everything, for the frames before even the placeholder decodes. |
| blur | number | 14 | Placeholder blur radius in pixels. A constant, applied once, so no frame repaints the filter. |
| radius | 5 \| 6 \| 9 \| 11 \| 14 | 11 | Corner radius, applied inline so a caller's radius always wins and the value stays on the ramp. |
| srcSet | string | undefined | Passed through. A change to it restarts load tracking alongside src. |
| sizes | string | undefined | Passed through to the <img>. |
| loading | "lazy" \| "eager" | "lazy" | Native lazy loading. An off-screen image simply stays on its placeholder. |
| fetchPriority | "high" \| "low" \| "auto" | undefined | Passed through for the one image that is the LCP candidate. |
| onReady | () => void | undefined | Fired once the bitmap is decoded, not when the load event lands. |
| onError | () => void | undefined | Fired when the image fails or decodes to nothing. |
| className | string | "" | Appended last on the frame. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
