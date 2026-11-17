# Motion Primitives behavior notes

The 33 core source components are indexed individually, together with documentation, examples and dependency imports. The library supplies composable animated pieces. A visually correct animation still needs the final application's interaction and data semantics.

Accordion supports internal state or an externally supplied expanded value and change callback. Keep the controlled state contract consistent; do not pass a change callback that leaves the displayed value stale. Its trigger uses a button and expansion state, while content transitions use Motion. Record the selected transition and variants with the composition.

Animated Background shares an active background across children identified by `data-id`. It can activate by click or hover, and its change callback can receive null. Stable identity and a shared layout are central to the effect. A shared moving highlight alone does not implement tabs, navigation or selection semantics.

For Morphing Dialog, Popover, Disclosure and related overlays, preserve the trigger-to-content relationship, layout identity and exit path. Test focus return, Escape, click-outside behavior and nested interaction in the composed application. Do not assume that every primitive implements the same focus model as shadcn's chosen base.

For Text Effect, Text Morph, Text Scramble, Text Shimmer, Text Loop, Sliding Number and animated number/text treatments, preserve segmentation, stable keys, transition order and repeated updates. Changing text while an exit animation is running is a distinct case from a single entrance. Actual counts and async completion come from the app.

For scroll, cursor, magnetic, tilt and visibility-triggered components, distinguish pointer coordinates from viewport coordinates, preserve cleanup and verify mobile alternatives. Reduced motion should retain content and state information.

Exact defaults, event locations and motion parameters are in [component guides](components/) and the pinned [source index](catalogue/source-index.json). Computed expressions are linked rather than guessed. The source-host layout imports Inter and defines mono font styles; this is documentation typography, not a required font for every component.
