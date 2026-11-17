# Time scrubber

Public reference: https://bencho.dev/blocks/time-scrubber

[Original API and usage guide](../upstream-free/blocks/time-scrubber/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Scrub.css](../upstream-free/blocks/time-scrubber/Scrub.css): 114 lines; SHA-256 `2f4070de23ee5cd76aa0a0b4b922bcb0a62781753a6d54e3cf09fa6ad35694c3`.
- [Scrub.tsx](../upstream-free/blocks/time-scrubber/Scrub.tsx): 312 lines; SHA-256 `15caf70200e9411647e821fa69b4cf80d60cef9854dda2d3818213018ecda8f6`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Scrub.css:44](../upstream-free/blocks/time-scrubber/Scrub.css#L44): `transition: transform 220ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [Scrub.css:49](../upstream-free/blocks/time-scrubber/Scrub.css#L49): `.tms-strip[data-flip="a"] { animation: tms-blur-a 260ms ease-out; }`
- [Scrub.css:51](../upstream-free/blocks/time-scrubber/Scrub.css#L51): `.tms-strip[data-flip="b"] { animation: tms-blur-b 260ms ease-out; }`
- [Scrub.tsx:8](../upstream-free/blocks/time-scrubber/Scrub.tsx#L8): `── ONE SPRING FOR THE THROW AND THE SNAP ───────────────`
- [Scrub.tsx:11](../upstream-free/blocks/time-scrubber/Scrub.tsx#L11): `nearest step. Then one spring carries it there, starting with`
- [Scrub.tsx:22](../upstream-free/blocks/time-scrubber/Scrub.tsx#L22): `/* ── inlined from lab/spring ──────────────────────── */`
- [Scrub.tsx:23](../upstream-free/blocks/time-scrubber/Scrub.tsx#L23): `/* ── one spring, for everything that settles ───────────────`
- [Scrub.tsx:38](../upstream-free/blocks/time-scrubber/Scrub.tsx#L38): `a second and the damping is RAISED to it rather than`
- [Scrub.tsx:41](../upstream-free/blocks/time-scrubber/Scrub.tsx#L41): `version that makes a spring behave differently on a busy`
- [Scrub.tsx:165](../upstream-free/blocks/time-scrubber/Scrub.tsx#L165): `/* go to a time, by the spring */`
- [Scrub.tsx:209](../upstream-free/blocks/time-scrubber/Scrub.tsx#L209): `/* the landing already includes the throw, so the spring starts`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
