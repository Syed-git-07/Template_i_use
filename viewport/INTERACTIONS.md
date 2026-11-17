# Viewport interaction research

Viewport is a curated reference gallery, not a single component implementation library. Its 624 posts retain creator links and kind/font/style/industry tags. A recording establishes visible movement, not the original source's spring constants, hidden error states, keyboard semantics or backend behavior. Public media remain on the original host; local observation frames are excluded from Git.

## Skeuomorphic Contact Form — portfolio priority

[Reference](https://viewportui.com/posts/598-probably-the-best-contact-form-i-ve-ever-made) · [Creator: @alimdesigner_](https://x.com/alimdesigner_/status/2107769836382331242).

The observed composition pairs a compact input card on the left with a ruled letter and envelope on the right. A black pen follows the letter-writing presentation. The page uses a blue sky and cloud imagery; the heading is a compact bold sans-serif treatment, while entered letter content is cursive. These are visual classifications, not identified font files. The original font family and asset licenses are not established by the recording.

The form's name, email and message appear in corresponding positions on the letter as typing progresses. This relationship matters: the letter is a synchronized representation of the same form state, rather than a separate typing animation that can drift from the inputs. The recording alone does not establish edit/delete selection behavior, validation rules, pasted multiline content or mobile layout.

The 16.230748-second clip was sampled across its timeline, then more densely around submission. [Frame timestamps](catalogue/contact-sequence.json) record requested and actual playback positions. These are positions within the recording, not exact animation durations or implementation constants.

| Observed recording time | Visible state |
| --- | --- |
| 0–11.5 s, sampled | Form entry and matching cursive letter content; pen near the latest writing |
| 12 s | Send control shows its in-progress state; letter content remains visible |
| 12.25 s | Pen disappears and letter rises above the open envelope |
| 12.5–12.75 s | Letter folds and descends into the envelope |
| 13 s | Open flap remains above the now-inserted letter |
| 13.25 s | Envelope is closed |
| 13.5 s | Red seal appears on the flap |
| 14 s | Sealed envelope tilts before leaving |
| 14.5 s | Confirmation replaces the envelope; a write-another action is visible |
| About 15.9 s | Empty form/letter presentation returns |

For future portfolio implementation, preserve synchronized input, paper/envelope layering, transform origins, pen removal, fold/insert/close/seal/depart order and reversible reset. Use the creator's reference for fidelity; do not guess exact easing values. The real send result must control success. On failure, preserve the typed draft and offer retry rather than letting an attractive envelope animation falsely imply delivery. That failure behavior is an integration requirement, not an observed behavior of the clip. The animation may begin while the request is pending, but confirmed delivery/acceptance must come from the configured service.

The reference is approved for later portfolio design; no portfolio code was changed in this research stage. No actual email was sent. No publicly accessible original source was established from the gallery/creator links during this pass.

## Compressing Images — processing and before/after reference

[Reference](https://viewportui.com/posts/586-compressing-images) · [Creator: @th2049](https://x.com/th2049/status/2092109898758988133).

The 16.816667-second recording shows a rounded mobile media sheet. A selection action becomes a compression panel over a media grid. Original and compressed thumbnails sit in separate positions, with changing paper/photo cards, an item counter and byte totals. A large saved-space value accumulates beneath the two columns. The main control remains visually unavailable during processing, becomes an explicit replacement action on completion, and then a system permission/deletion prompt appears.

The useful reusable structure is selection → per-item processing → aggregate result → explicit application of the result. Card movement conveys which image is being processed; numeric change communicates real output. For uploads, conversion, transcoding or import, keep those distinct states and use actual counts/bytes. Do not reuse fictional saved-space numbers, drive success from elapsed time, or hide the final replacement decision inside motion. Before/after quality, cancellation, individual failures and undo are not established by this recording.

## Shredder on the web

[Reference](https://viewportui.com/posts/626-shredder-on-the-web) · [Creator: @heydamir](https://x.com/heydamir/status/2109679416494391746).

This is the likely reference described as “shutter.” The clip shows a small dark shredder on a light surface, surrounded by notes, receipts and photo-like documents. A selected paper enters the upper slot; fragments emerge below and accumulate/scatter. The machine's small display and indicator light help communicate state. Paper shape, printed texture, shadows, clipping at the slot and fragments all contribute to the physical effect.

The reference is suitable for document disposal or playful processing feedback when the product calls for it. Real deletion, retention rules, confirmation and recovery must be separate application behavior. Exact collision geometry, particle count, gravity, material shaders and pointer thresholds are unknown without original code. Do not claim those are recovered from sampled frames.

## Reading the rest of the collection

Use the full catalogue and searchable tags for navigation, cards, mobile controls, charts, forms, typography, loaders, overlays, gestures and transitions across every industry. Keep a reference's typeface category distinct from a verified font family. Match the interaction sequence and visual hierarchy before selecting effects. A still-only post remains still-only evidence; a sampled video is not an exhaustive interaction test.

The media ledger preserves observed duration, resolution, original media URL and actual sampled positions. Early captures that failed seek verification were replaced; the original host sometimes advertises a zero-length seekable range. Current captures use an ephemeral browser buffer when needed, without publishing a video archive.
