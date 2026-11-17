# Interior behavior notes

All 54 component contracts are preserved in [contracts.json](catalogue/contracts.json), with original API notes and design invariants under the author's MIT license. These are upstream claims to consult, not independent proof that every device/state has passed. [Source guides](components/) expose defaults, motion anchors and lifecycle signals.

Interior groups components by the user's moment: Action Feedback, Input, Async, Notification, Overlay, Navigation, Scroll, Data, Gesture and Content. Its central priorities are stable dimensions across label/state changes, interruptible transitions that continue from the current position, and information that remains available when motion is reduced.

## Differences worth preserving

- Hold to Confirm has idle, holding, releasing and committed phases. Default hold duration is 1,800 ms, 20 progress steps, release rate 2.5 and movement tolerance 10 pixels. Re-pressing during release can continue from remaining progress. Completion and early abort are distinct callbacks. Its face spring uses stiffness 260, damping 34 and mass 0.8. This differs from React Bits' Hold Button; do not blend their rules accidentally.
- Long Press has a separate default duration of 550 ms, 12 progress steps and movement tolerance 8 pixels. Its contract includes cancelling on pointer drift, Escape, blur, hidden tab and pointer cancellation, and swallowing the click after a completed hold. Verify these with the actual device and integration.
- Tag Input distinguishes drafting, adding, selecting a previous tag and removing it. Empty Backspace selects before a second press removes. Stable tag identity and keyboard recovery are part of the interaction.
- Loading Button and Skeleton Swap reserve geometry across states. Async completion should not move the pointer target or reflow the surrounding form unexpectedly.
- Tooltip Group shares timing across related targets. A warm group is behaviorally different from several unrelated tooltip delays.
- New Items Pill preserves the reader's position instead of automatically pulling them to newly arrived content. Message/notification presence is separate from scroll ownership.
- Reorder List's neighboring items open a gap for the intended drop target. Dragging a visual item is not evidence that the reordered data was saved.
- Poll Results, Value Flash and Sortable Table communicate change through position or emphasis. Values must come from actual application state; animation is not a source of truth.

Use the contracts for every component, including the ones not named here. Most expose a headless hook as well as a styled example; Progress Bar and Segmented Control are documented as component-only. Check the selected file rather than assuming a uniform API.

Source-host typography uses Geist Sans and Geist Mono variables. Styled examples use Tailwind CSS and Motion; the host application's tokens can change their appearance. Keep dependency versions and chosen theme with the consuming implementation. No library-wide production, screen-reader or mobile certification is implied by this research.
