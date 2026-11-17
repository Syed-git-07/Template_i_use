# Glass bubble

Public reference: https://bencho.dev/blocks/glass-bubble

[Original API and usage guide](../upstream-free/blocks/glass-bubble/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [LiquidGlass.css](../upstream-free/blocks/glass-bubble/LiquidGlass.css): 18 lines; SHA-256 `e373cec692b4a52e52d87e1c20ae3ebda66e8b863f61319794e0c1d7522623f5`.
- [LiquidGlass.tsx](../upstream-free/blocks/glass-bubble/LiquidGlass.tsx): 396 lines; SHA-256 `0af8c4f1ed75ce708ca0755fbd772fffde075949c26b30b0a2025ed4b4787cc1`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [LiquidGlass.tsx:3](../upstream-free/blocks/glass-bubble/LiquidGlass.tsx#L3): `/* ── inlined from lab/spring ──────────────────────── */`
- [LiquidGlass.tsx:4](../upstream-free/blocks/glass-bubble/LiquidGlass.tsx#L4): `/* ── one spring, for everything that settles ───────────────`
- [LiquidGlass.tsx:19](../upstream-free/blocks/glass-bubble/LiquidGlass.tsx#L19): `a second and the damping is RAISED to it rather than`
- [LiquidGlass.tsx:22](../upstream-free/blocks/glass-bubble/LiquidGlass.tsx#L22): `version that makes a spring behave differently on a busy`
- [LiquidGlass.tsx:249](../upstream-free/blocks/glass-bubble/LiquidGlass.tsx#L249): `/* ── the loop: a spring toward the hand, then stop ─────── */`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
