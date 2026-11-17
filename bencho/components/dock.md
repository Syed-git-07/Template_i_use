# Magnifying dock

Public reference: https://bencho.dev/blocks/dock

[Original API and usage guide](../upstream-free/blocks/dock/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [GlassDock.css](../upstream-free/blocks/dock/GlassDock.css): 267 lines; SHA-256 `e7dfada8266278e033745d93a67cbf51b12119798f2e3e8aa291046d65c41bd5`.
- [GlassDock.tsx](../upstream-free/blocks/dock/GlassDock.tsx): 249 lines; SHA-256 `054adc7b2077466f66dbfbe538d6dd47755e2451c1d54d3dfeacfbcfc99983f2`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [GlassDock.css:55](../upstream-free/blocks/dock/GlassDock.css#L55): `transition: opacity 220ms ease;}`
- [GlassDock.css:62](../upstream-free/blocks/dock/GlassDock.css#L62): `transition: transform 420ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [GlassDock.css:85](../upstream-free/blocks/dock/GlassDock.css#L85): `transition: opacity 220ms ease, transform 420ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [GlassDock.css:115](../upstream-free/blocks/dock/GlassDock.css#L115): `transition:`
- [GlassDock.css:123](../upstream-free/blocks/dock/GlassDock.css#L123): `.gdock-tip:not([data-ready]) { transition: opacity 160ms cubic-bezier(0.22, 1, 0.36, 1); }`
- [GlassDock.tsx:219](../upstream-free/blocks/dock/GlassDock.tsx#L219): `until it has been placed once it moves without a transition */`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
