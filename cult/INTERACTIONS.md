# Cult UI behavior notes

The official source snapshot includes 141 source-defined component guides, alongside examples, blocks, docs and shared styles. The website's published documentation is a separate inventory: source entries without a current public page must remain labelled source-only, not silently treated as live examples.

Retain the full collection: AI inputs and generated UI, app/workspace components, form controls, status/feedback, navigation/overlays, display/content and visual treatments. External AI SDK Agents links are related products; their entire separate catalogues are not part of the Cult source snapshot.

For Dynamic Island, Floating Panel, Popover and Popover Form, study the compact and expanded geometry, shared layout identities, opening origin, content reveal and close/reset path. A changing container shape must remain coupled to actual state and focus. Do not wire a decorative submit animation as proof that a request succeeded.

For Direction Aware Tabs, preserve the previous and next index when determining motion direction. For Timer, distinguish displayed transitions from authoritative elapsed time and background-tab behavior. For Kanban, Sortable List and voting/poll components, preserve stable keys, input alternatives and persistence boundaries.

For AI inputs, instructions, prompt libraries, streaming/code and agent-facing cards, separate editable user data from display/demo content. Implement real cancellation, errors and permissions in the consuming app. Never expose provider credentials in frontend settings or treat model-generated text as trusted executable markup.

Halo inputs, fields, selects, switches, segmented controls, progress and notification components provide distinct styling/state treatments; use their source guides rather than flattening them into one generic effect. Inspect contrast, focus, validation and disabled/read-only states with the actual theme.

The host stylesheet maps Geist Sans/Mono and several Geist Pixel variants. This records source-host typography, not a universal typeface requirement. Component utility classes, CSS variables, radius, shadows and selected theme jointly establish the visual structure. Exact source, imports, APIs, defaults and event/motion anchors remain local and linked from the guides.
