# Generate

Public reference: https://bencho.dev/blocks/generate

[Original API and usage guide](../upstream-free/blocks/generate/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Generate.css](../upstream-free/blocks/generate/Generate.css): 170 lines; SHA-256 `9fe4e6662e6970bcf3c7f23a004849427a645e5407ad68f110a9e50a05e65c1e`.
- [Generate.tsx](../upstream-free/blocks/generate/Generate.tsx): 265 lines; SHA-256 `e8964a178e0bce24eab2e009e652d2ebf7c9476d1ace49f48c53e164a5400634`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Generate.css:86](../upstream-free/blocks/generate/Generate.css#L86): `transition: opacity 220ms ease, scale 220ms cubic-bezier(0.22, 1, 0.36, 1);`
- [Generate.css:91](../upstream-free/blocks/generate/Generate.css#L91): `.gen-go:active:not(:disabled) { scale: 0.96; transition-duration: 160ms; }`
- [Generate.css:137](../upstream-free/blocks/generate/Generate.css#L137): `transition: opacity 220ms ease, translate 220ms ease;`
- [Generate.css:147](../upstream-free/blocks/generate/Generate.css#L147): `.gen-pct { transition-duration: 160ms; }`
- [Generate.tsx:3](../upstream-free/blocks/generate/Generate.tsx#L3): `/* ── inlined from lab/spring ──────────────────────── */`
- [Generate.tsx:4](../upstream-free/blocks/generate/Generate.tsx#L4): `/* ── one spring, for everything that settles ───────────────`
- [Generate.tsx:19](../upstream-free/blocks/generate/Generate.tsx#L19): `a second and the damping is RAISED to it rather than`
- [Generate.tsx:22](../upstream-free/blocks/generate/Generate.tsx#L22): `version that makes a spring behave differently on a busy`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
