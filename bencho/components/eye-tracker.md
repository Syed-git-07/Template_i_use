# Eye tracker

Public reference: https://bencho.dev/blocks/eye-tracker

[Original API and usage guide](../upstream-free/blocks/eye-tracker/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Watcher.css](../upstream-free/blocks/eye-tracker/Watcher.css): 87 lines; SHA-256 `49304fc9d31035aa41ca381165f2380f5455585bf251f8bdb04eec1d710fba58`.
- [Watcher.tsx](../upstream-free/blocks/eye-tracker/Watcher.tsx): 513 lines; SHA-256 `2fca7968d9272446648fc7a7a4549d309d4baec2a7e6e2d012092c84d4c341ba`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Watcher.css:30](../upstream-free/blocks/eye-tracker/Watcher.css#L30): `transition: scale 420ms cubic-bezier(0.24, 1.34, 0.38, 1);`
- [Watcher.css:33](../upstream-free/blocks/eye-tracker/Watcher.css#L33): `.eyt-ball[data-poke]:active { scale: 0.96; transition-duration: 160ms; transition-timing-function: ease; }`
- [Watcher.css:56](../upstream-free/blocks/eye-tracker/Watcher.css#L56): `transition: opacity 160ms ease, scale 220ms cubic-bezier(0.24, 1.34, 0.38, 1), background-color 220ms ease;`
- [Watcher.tsx:24](../upstream-free/blocks/eye-tracker/Watcher.tsx#L24): `/* ── inlined from lab/spring ──────────────────────── */`
- [Watcher.tsx:25](../upstream-free/blocks/eye-tracker/Watcher.tsx#L25): `/* ── one spring, for everything that settles ───────────────`
- [Watcher.tsx:40](../upstream-free/blocks/eye-tracker/Watcher.tsx#L40): `a second and the damping is RAISED to it rather than`
- [Watcher.tsx:43](../upstream-free/blocks/eye-tracker/Watcher.tsx#L43): `version that makes a spring behave differently on a busy`
- [Watcher.tsx:178](../upstream-free/blocks/eye-tracker/Watcher.tsx#L178): `bounce = 30,`
- [Watcher.tsx:201](../upstream-free/blocks/eye-tracker/Watcher.tsx#L201): `bounce?: number;`
- [Watcher.tsx:241](../upstream-free/blocks/eye-tracker/Watcher.tsx#L241): `const knobs = useRef({ follow, bounce, eyeScale });`
- [Watcher.tsx:242](../upstream-free/blocks/eye-tracker/Watcher.tsx#L242): `knobs.current = { follow, bounce, eyeScale };`
- [Watcher.tsx:256](../upstream-free/blocks/eye-tracker/Watcher.tsx#L256): `its speed, and where it is heading — one spring on a point,`
- [Watcher.tsx:340](../upstream-free/blocks/eye-tracker/Watcher.tsx#L340): `/* one spring for both axes; Bounce loosens the damping */`
- [Watcher.tsx:342](../upstream-free/blocks/eye-tracker/Watcher.tsx#L342): `const d = 0.34 - (clamp(knobs.current.bounce, 0, 100) / 100) * 0.22;`
- [Watcher.tsx:452](../upstream-free/blocks/eye-tracker/Watcher.tsx#L452): `/* ease out with a touch of overshoot */`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
