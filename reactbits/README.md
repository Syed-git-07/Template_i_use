# React Bits reference library

Shared across every current and future project. Research snapshot: 17 November 2026. Creator: David Haz; official site [React Bits](https://reactbits.dev/), official [source](https://github.com/DavidHDev/react-bits).

The complete public index contains **217 components**: 33 text animations, 38 animations, 48 components, 34 micro interactions and 64 backgrounds. Two additional source components, EvilEye and FlyingButton, are retained as unlisted references. No background has been selected for the portfolio.

## Browse

- [Text animations](catalogue/text-animations.md)
- [Animations](catalogue/animations.md)
- [Components](catalogue/components.md)
- [Micro interactions](catalogue/micro.md)
- [Backgrounds](catalogue/backgrounds.md)
- [Tools and supporting pages](catalogue/tools-and-pages.md)
- [219 per-component API and motion guides](components/)
- [Favorites and spoken-name mappings](FAVORITES.md)
- [Behavior, cancellation and integration notes](INTERACTIONS.md)
- [Tools](TOOLS.md)
- [Evidence and limitations](COVERAGE.md)
- [Provenance and local source recovery](PROVENANCE.md)

## How to reuse

Start with the component guide and its pinned original source. Preserve the full interaction sequence: initial state, input tracking, threshold, release, completion, cancellation, reversal and reset. Keep the exact dependency and variant choices together. Use the recorded props as facts; a computed expression must be read at its linked source location rather than guessed from a screenshot.

Treat demos as presentation examples. Connect real authentication, storage, recording, navigation, payments and destructive actions in the consuming application. Test its actual keyboard, touch, reduced-motion and async failure behavior. Keep professional, concise product copy and avoid adding explanatory UI narration.

This repository publishes authored notes, factual API metadata and pinned links. React Bits uses **MIT + Commons Clause**, with restrictions on redistribution as a component library. The full source snapshot is available locally under ignored `.local/react-bits/`; it is intentionally absent from GitHub. See [provenance](PROVENANCE.md).
