# One-time code

Public reference: https://bencho.dev/blocks/one-time-code

[Original API and usage guide](../upstream-free/blocks/one-time-code/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Otp.css](../upstream-free/blocks/one-time-code/Otp.css): 136 lines; SHA-256 `8184c38a7b519562572e7465cf1f7059f6202b5ca1dcb0a8233818db1dc39002`.
- [Otp.tsx](../upstream-free/blocks/one-time-code/Otp.tsx): 431 lines; SHA-256 `a0e748ef1d45e9b947623154e6a669d6292ea84fef9ada4d223a7c9478b19b61`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Otp.css:46](../upstream-free/blocks/one-time-code/Otp.css#L46): `/* one colour under the filter, or the threshold smears two */`
- [Otp.css:71](../upstream-free/blocks/one-time-code/Otp.css#L71): `transition: color 160ms ease;}`
- [Otp.css:86](../upstream-free/blocks/one-time-code/Otp.css#L86): `transition: opacity 160ms ease;}`
- [Otp.css:90](../upstream-free/blocks/one-time-code/Otp.css#L90): `animation: otp-breathe 1.1s ease-in-out infinite alternate;}`
- [Otp.tsx:17](../upstream-free/blocks/one-time-code/Otp.tsx#L17): `The cells sit under a blur-and-threshold filter, far enough`
- [Otp.tsx:31](../upstream-free/blocks/one-time-code/Otp.tsx#L31): `Shared parts for the Framer Motion layer: one spring, one`
- [Otp.tsx:79](../upstream-free/blocks/one-time-code/Otp.tsx#L79): `/* ── inlined from lab/spring ──────────────────────── */`
- [Otp.tsx:80](../upstream-free/blocks/one-time-code/Otp.tsx#L80): `/* ── one spring, for everything that settles ───────────────`
- [Otp.tsx:95](../upstream-free/blocks/one-time-code/Otp.tsx#L95): `a second and the damping is RAISED to it rather than`
- [Otp.tsx:98](../upstream-free/blocks/one-time-code/Otp.tsx#L98): `version that makes a spring behave differently on a busy`
- [Otp.tsx:127](../upstream-free/blocks/one-time-code/Otp.tsx#L127): `/* ── the merge is a SPRING, not a tween ─────────────────`
- [Otp.tsx:128](../upstream-free/blocks/one-time-code/Otp.tsx#L128): `It was a 560ms ease-in-out, which arrived and stopped. A`
- [Otp.tsx:129](../upstream-free/blocks/one-time-code/Otp.tsx#L129): `spring a little under critical lets the capsule run past its`
- [Otp.tsx:133](../upstream-free/blocks/one-time-code/Otp.tsx#L133): `a stiffness and a damping ratio, as spring.ts does. */`
- [Otp.tsx:193](../upstream-free/blocks/one-time-code/Otp.tsx#L193): `/* the caret, on a spring with a little give */`
- [Otp.tsx:289](../upstream-free/blocks/one-time-code/Otp.tsx#L289): `/* the raw spring runs past 0 and 1; the cells' travel is`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
