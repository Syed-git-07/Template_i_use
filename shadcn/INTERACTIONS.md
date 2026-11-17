# shadcn/ui baseline and behavior notes

shadcn/ui is the user's baseline for clean, restrained, complete interfaces. Reference its spacing, typography, surfaces, hierarchy and states even when adding a richer interaction from another source. Minimal does not mean empty, unfinished or missing validation.

## Source organization

The pinned official repository includes Base UI, Radix and React Aria registry branches, plus the New York v4 registry, styles, blocks, examples and registry tooling. They are different primitive APIs, not interchangeable import paths. The live catalogue contains separate documentation routes for all three bases. Keep the chosen base consistent within a composed component and consult its dependency's original API for inherited props and semantics.

Every source-defined UI filename has a component guide grouping its available variants. Documentation-only compositions such as data tables and date pickers may combine several files rather than correspond to a single UI file. Use the full page catalogue and source index for those compositions. Code Block and Trace are included; so are the AI-element docs, charts, forms, installation, theming, RTL and registry documentation from the public sitemap.

## Interaction contracts to retain

| Family | Important behavior |
| --- | --- |
| Dialog, Alert Dialog, Sheet, Drawer, Popover | Trigger/content relationship, focus entry and return, dismissal semantics, scroll containment, modal versus nonmodal behavior; alert cancellation must remain clear |
| Menu, Menubar, Context Menu, Navigation Menu, Command, Combobox | Keyboard navigation, typeahead/filtering, selection versus activation, focus movement, disabled items, nested menus and Escape recovery |
| Input, Field, Input Group, Textarea, OTP, Checkbox, Radio, Switch, Select | Label/control association, controlled values, validation, disabled/read-only distinction, grouping, paste and keyboard behavior; real verification is external |
| Accordion, Collapsible, Tabs, Toggle Group, Sidebar | Stable item identity, controlled/uncontrolled state, expansion/selection semantics, orientation and compact/mobile presentation |
| Table, Data Table, Chart, Calendar, Date Picker | Real data semantics, sorting/filtering/selection, date/locale boundaries, keyboard use, loading/empty/error states and responsive containment |
| Toast, Alert, Progress, Skeleton, Spinner | Honest task state, accessible announcement, determinate versus indeterminate progress, stable dimensions and failure recovery |
| Code Block, Trace, Message, Bubble, Message Scroller | Readability, overflow, copy state, stream/task status, user-controlled scrolling and safe rendering of untrusted content |

These are integration requirements to inspect in the selected original implementation and test in the host app. The existence of a primitive dependency does not certify the final composition's accessibility or security. Do not treat a documentation demo as a working backend, login, payment or persistent data table.

## Typography, tokens and formation

The pinned font definitions enumerate supported families and their import/provider metadata. Geist Variable, Inter Variable, Noto Sans Variable, Nunito Sans Variable and others are choices in that system; do not assert that every component uses one universal font. Body and heading font roles are separate. The registry's style files include luma, lyra, maia, mira, nova, rhea, sera and vega. Preserve the selected theme's tokens, sizes, radius, borders, focus rings and density as a coherent set.

For exact values, read `apps/v4/lib/font-definitions.ts`, `apps/v4/registry/fonts.ts`, `apps/v4/registry/styles/` and the selected variant in the pinned [source index](catalogue/source-index.json). Browser font observations describe the documentation page; they are not automatically the font contract for a component copied into another app.

Small transitions should support state change rather than overwhelm ordinary tasks. Preserve useful motion and reduced-motion handling, but use the user's request and project context to decide whether an expressive reference belongs in the flow. Keep internal explanations in documentation, not in the product interface.
