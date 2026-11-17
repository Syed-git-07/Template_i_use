# Interaction notes for all projects

These are reusable design ideas and integration requirements. Exact defaults and implementations live in the component READMEs, TSX and CSS. Adaptation suggestions are not claims that complete product workflows have been tested.

## Preserve the sequence

For a faithful adaptation, track rest, approach, hover/focus, press, movement, threshold, release, settle, dismissal and re-entry. Preserve the originating object's location and corner relationships through morphs. Test reversals and repeated input before the current animation finishes. A generic CSS transition loses the defining behavior when the reference uses a spring, inertia or a simulation.

The free collection mixes CSS transforms, Framer Motion, custom frame-loop integrators, SVG/filter effects and Three.js. Read CSS and TSX together. Do not infer an engine or exact timing from a still image.

## Priority references and source-backed detail

### Folding bill

[Live](https://bencho.dev/blocks/folding-bill) · [Source and props](upstream-free/blocks/folding-bill/README.md)

This is a deformable surface using Three.js, not a flat card rotating on a hinge. Defaults are Plain print, stiffness 40 and settle 0; the latter controls independently range from 0 to 100. Preserve grab location, distributed deformation, shading and release behavior. A CSS fold alone would not reproduce it.

Possible uses: document cover, receipt, ticket, certificate or task sheet. Keep the underlying document readable and independently accessible; PDF opening/export and real actions stay normal controls. Site banknote artwork is not bundled for reuse.

### Eye tracker

[Live](https://bencho.dev/blocks/eye-tracker) · [Source and props](upstream-free/blocks/eye-tracker/README.md)

Pointer-following eyes sit on a turning body. Defaults: follow 60, bounce 30, Cube, Slant, size 100. Shape, eye style and response are separate controls; the source includes idle and visibility handling. It follows the pointer, not a camera, so it does not require webcam permission.

Possible uses: a small optional character, empty-state detail or landing-page accent. Keep it secondary to the task and calm without a pointer.

### Dragging ball

[Live](https://bencho.dev/blocks/drag-ball) · [Source and props](upstream-free/blocks/drag-ball/README.md)

Approach, grip and travel produce different deformation. Source facts: `liquid-gooey`, one stretching body, `trail: 0`, `wobble: 0.35`, boundary elasticity `0.14`, and `dragMomentum={false}`. Grip/hover use stiffness 500, damping 18, mass 0.6. A trailing duplicate or release fling would change the requested interaction. If adapted into an input, supply a real value and keyboard semantics; the original is an object demonstration.

### Cards

[Card stack](upstream-free/blocks/card-stack/README.md) separates fan, hover lift, selected-card view and return. Spread, bounce, scatter, count and corners are independent. Good candidates include documents, achievements and media; keep a reliable open/close path.

[Card swap](upstream-free/blocks/card-swap/README.md) depends on slot transforms and immediate z-index changes. Source thresholds: a press under 6 px, drag over 70 px, or movement over 24 px at over 0.6 px/ms advances the front card. Other releases return it; pointer cancellation does not advance. Auto defaults off and pauses during hover, dragging and hidden-document state. Keep those rules before changing visuals.

### Meters and bars

[Context meter](upstream-free/blocks/context-meter/README.md) links category emphasis across Bar/Field and Colour/Mono views. Compact changes the demo distribution. Adapt it to capacity, composition, storage or budget only when values have a defensible meaning; do not invent skill percentages.

[Stacked bars](upstream-free/blocks/stacked-bars/README.md) coordinates highlighted bars, moving tooltip and Day/Week transition. Default count is 20. Real analytics need units, real values, empty states and accessible details.

### Morphing controls

[Create menu](upstream-free/blocks/liq-create/README.md) preserves the trigger pill as it becomes the options surface. [Search](upstream-free/blocks/seek/README.md) turns the icon into the field. Keep the originating geometry, focus, dismissal and re-entry coherent.

[Liquid toggle](upstream-free/blocks/liq-toggle/README.md) separates speed (50) and stretch (36). Actual checked state must remain authoritative during animation. [Dynamic island](upstream-free/blocks/dynamic-island/README.md) uses stiffness 380, mass 0.9 and damping `34 - b * 16`, with normalized bounce `b`. Adapt it to a real task/timer, not decorative fake activity.

## All 47 free blocks: application map

| Block | Possible use | Preserve or verify |
| --- | --- | --- |
| Action node | Workflow editor | Corner action sequence; keyboard access. |
| ASCII wake | Interactive accent | Cooling trail, character pull and press wave. |
| Aspect ratio | Crop picker | Shape morph and actual radio/crop state. |
| Asset swap | Source/target selector | Reversal, arrow and picker state stay consistent. |
| Assignees | Collaboration form | Avatar stacking; replace sample identities and permissions. |
| Card stack | Documents/media | Fan, lift, preview, return ordering. |
| Card swap | Projects/products | Front-only drag, thresholds, cancellation, paint order. |
| Carousel | Media browser | Orbit depth, tilt, settlement, navigation. |
| Checklist | Tasks | Box fill, drawn check and strike-through; persist real state. |
| Context meter | Capacity/composition | Linked category emphasis; meaningful values. |
| Create menu | Action launcher | Trigger-to-panel continuity and real actions. |
| Dragging ball | Object demo | Single-body stretch, grip, boundary, no release fling. |
| Dynamic island | Running task | Compact/expanded silhouette and real status. |
| Emoji reactions | Reference unless requested | Retain mechanism without adding unsolicited emoji. |
| Escape button | Optional novelty | Never use evasion for required submit/dismiss/consent. |
| Eye tracker | Optional character | Pointer, eye/body response, idle and visibility. |
| Folding bill | Document presentation | Distributed deformation and material response. |
| Generate | Result presentation | Timed demo needs real job status/failure. |
| Glass bubble | Visual/media demo | Refraction, edge fringe, drag, rendering cost. |
| Heat map | Reactive artwork | Heat field/decay; not statistical data. |
| Image accordion | Gallery | Neighbor displacement; touch selection and labels. |
| Image compare | Before/after view | Divider, inertia, edges and keyboard. |
| Label input | Form | Floating label, populated states and validation. |
| Like | Save/appreciation | Burst/digit roll follow real state without duplicate writes. |
| Liquid toggle | Preference | Droplet deformation follows checked state. |
| Magnetic select | Mode/filter | Neighbor displacement and radio semantics. |
| Magnifying dock | Navigation | Distance falloff, lift, stable touch targets. |
| Now playing | Media UI | Expand/collapse; connect actual audio and pause. |
| One-time code | Verification | Paste/autofill, check/reject/success; server validation. |
| Palette | Colour exploration | Swatch morph; contrast before applying. |
| Particles | Accent | Repulsion, home spring and shockwave. |
| Pull to refresh | Refreshable list | Threshold, loading and return tied to real fetch. |
| Rolling counter | Stepper/statistic | Digit carry, hold acceleration, drag and bounds. |
| Search | Compact search | Icon-to-field, focus, query, real results. |
| Signature pad | Drawing | Speed-sensitive stroke, clear rewind; export separately. |
| Slide to confirm | Deliberate action | Reset/commit threshold; keyboard alternative. |
| Slingshot | Physics/play | Tension, release, collision, home return. |
| Slosh slider | Value control | Fill inertia versus actual handle/value. |
| Stacked bars | Analytics | Tooltip/period transition; real data. |
| Step player | Process demo | Step fill, pause/resume, direct selection. |
| Tilt card | Preview | Sinking surface, not generic upward hover. |
| Time scrubber | Time input | Inertial snap; precise accessible entry. |
| Toast stack | Feedback | Peeks, expansion, usable actions and dismissal. |
| Todo tower | Task visualization | Falling stack; real persistence/undo. |
| Upload dropzone | Upload UI | Accept/reject/progress; implement actual upload. |
| Voice note | Recording UI | Hold/cancel/clip/scrub; implement real audio capture. |
| Wake slider | Parameter input | Bar wake/settle; expose readable value. |

## Finds and ambiguous spoken names

All 261 entries retain source/creator links. Tags are not exclusive: Reveal 91, Morph 91, Press 73, Hover 51, Drag 39, Elastic 28, Select 23, Type 14, Refract 9, Scroll 8, Slide 7, Swipe 6, Magnetic 3, Parallax 3. Some entries have no listed tag.

| Reference | Canonical entry | What needs detailed verification |
| --- | --- | --- |
| Button anatomy | [Altin](https://bencho.dev/finds/altinsmaili-button-anatomy) | Layer order, labels, tilt and recomposition; tags are Reveal/Morph, not proof of scroll triggering. |
| Trip cards | [Stella Peng](https://bencho.dev/finds/abtste11a-trip-cards) | Row-to-card continuity, coordinated close/open and content reveal. |
| Genie menu | [Harsh Sharma](https://bencho.dev/finds/imharshin-genie-menu) | Trigger attachment, stretch, option reveal, reverse and interruption. |
| Liquid menus | [kev](https://bencho.dev/finds/koppkev-liquid-menus) | Tooltip, swatches and avatar menu have distinct morphs. |
| Download progress | [Ramin Nasibov](https://bencho.dev/finds/raminnasibov-download-progress) | Dot-matrix value, ring synchronization and completion. |
| Tool stack | No exact Block title | Candidates: [Folders of tools](https://bencho.dev/finds/raul-tool-folders), [Tools fill a grid](https://bencho.dev/finds/adi-tool-grid). Confirm at implementation time. |
| Slingshot button | [Slingshot](https://bencho.dev/blocks/slingshot) | Current reference is a draggable object. |
| ASCII wake-up | [ASCII wake](https://bencho.dev/blocks/ascii-wake) | Separate from [Wake slider](https://bencho.dev/blocks/wake-slider). |
| Slash/slide bar | Ambiguous | Retain [Slosh slider](https://bencho.dev/blocks/slosh), [Slide to confirm](https://bencho.dev/blocks/slide-confirm), and [Time scrubber](https://bencho.dev/blocks/time-scrubber) candidates. |

Sampled frames establish visual observations only. They do not reveal creator source, exact springs, hidden states or input behavior outside the recording. Do not promise an exact reproduction on that basis.

## Source-established production boundaries

- `Upload.tsx` advances local progress in a frame loop and returns a demo file to its tray. It is not a real server upload.
- `VoiceNote.tsx` generates waveform samples with `standIn(...)`. Real microphone capture, consent, actual audio and cleanup must be added.
- `Otp.tsx` selects success/rejection from its `answer` prop after a local delay. Real code verification, expiry and attempt limits belong on the server.
- Generate resolves a sample image on a timeline; real completion must follow actual job status.
- Like, tasks, charts, timers and players use demonstration data/state. Connect the application's own data and permissions.
- Card swap includes `/lab/...` image paths absent from this archive. Build success does not validate imagery. Replace site-specific images explicitly.

## Acceptance when adopting a block

Record the source commit, props and any changed formula. Verify rest/hover/press/drag/release, cancellation, repeated input, close/reopen, keyboard/touch, reduced motion, resize/zoom, light/dark contrast and actual success/failure. Test physics-heavy effects on target devices. A build and a few sampled frames do not complete this acceptance record.
