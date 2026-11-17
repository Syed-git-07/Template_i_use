# Typography and motion fidelity

Read this with the chosen site's source guide. A faithful result comes from structure, type, spacing, surfaces, input response and state transitions together.

## Typography evidence

| Evidence | What it establishes | What it does not establish |
| --- | --- | --- |
| Viewport font tag such as sans, cursive or mono | Curator classification | Exact font family, weight, variable axes or font license |
| Typeface visible in a recording | Visual shape and hierarchy at that recording's resolution | Original font file, line metrics or CSS |
| Browser computed font on documentation page | Host page's current font stack and heading metrics | Font used by the same component in another application's theme |
| Pinned font definitions and theme CSS | Source-backed family/provider/variable mappings and style rules | Whether the font loaded correctly on every device |
| Application visual check | Actual rendered result in that application | Unchecked browsers, locales, zoom levels or screen readers |

shadcn exposes separate body/heading font definitions and multiple registry styles. Interior uses Geist Sans/Mono variables in the host. Cult includes Geist Sans/Mono and Pixel variable mappings. Motion Primitives' host imports Inter and includes mono styles. These are source observations, not instructions to force one family onto all projects.

Preserve readable type scale, weights, tracking, line height and wrapping. Test long labels, multiline content, translated text, numerical alignment and narrow widths. Reserve dimensions when status labels change. Obtain fonts from their permitted source and retain applicable notices.

## Motion evidence

An implementation's literal duration or spring value is stronger evidence than a visual estimate. Computed values, transforms, geometry and shader uniforms need their surrounding source. A source index provides anchors; it is not a replacement for reading the selected implementation.

Record the starting state, input tracking, threshold, release, completion, interruption, reversal and reset. Distinguish duration-based motion from spring settlement and direct pointer tracking. Keep shared layout identity, transform origins, clipping layers and stacking order together. Recreating only the final appearance loses the interaction.

The gallery surveys generally use one midpoint per recording, with denser sampling for the named Viewport priorities. All verified samples store requested and actual playback times. A small overview sheet was visually inspected for each gallery; this broad inspection is not precision analysis of every frame. Native player controls or transient loading indicators can appear in captures, so inspect the original before using a screenshot as a specification.

Do not infer haptics, sound, physical frame rate, hidden cancellation paths or backend results from a silent recording. Use original source when available and selected runtime checks for concrete behavior. Reduced motion must retain information, focus and completion state even if travel, blur or bounce changes.

## Implementation choices

Use shadcn's restrained baseline for ordinary product flows. Add expressive motion when requested or when it explains orientation, change or direct manipulation. Keep the user's clean-copy preference: short labels, useful validation and essential warnings, without implementation narration or filler subtitles.

Tie success to the actual application result. Preserve drafts and recovery after errors. A contact envelope, file shredder, upload animation, OTP tick or payment slider is a presentation of state, not proof that an email arrived, data was erased, bytes were stored, identity was verified or payment completed.
