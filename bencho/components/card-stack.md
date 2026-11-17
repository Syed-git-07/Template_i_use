# Card stack

Public reference: https://bencho.dev/blocks/card-stack

[Original API and usage guide](../upstream-free/blocks/card-stack/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Stack.css](../upstream-free/blocks/card-stack/Stack.css): 213 lines; SHA-256 `abd7b386b0484365bd9a55ba5dc02da39c51d47fc9f7ce0bda18b0af0859b5d7`.
- [Stack.tsx](../upstream-free/blocks/card-stack/Stack.tsx): 825 lines; SHA-256 `5332c8d97a714f0307697c9d19b836d8585d747f69a162fcb6dd574b8937ae94`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Stack.css:57](../upstream-free/blocks/card-stack/Stack.css#L57): `browser promotes these on its own once the spring starts`
- [Stack.css:94](../upstream-free/blocks/card-stack/Stack.css#L94): `spring every frame, and a transition on the same property`
- [Stack.css:97](../upstream-free/blocks/card-stack/Stack.css#L97): `Bounce knob so the lift and the fan settle alike. */`
- [Stack.css:100](../upstream-free/blocks/card-stack/Stack.css#L100): `transition:`
- [Stack.css:101](../upstream-free/blocks/card-stack/Stack.css#L101): `translate 480ms var(--stk-ease, ease),`
- [Stack.css:119](../upstream-free/blocks/card-stack/Stack.css#L119): `transition:`
- [Stack.css:190](../upstream-free/blocks/card-stack/Stack.css#L190): `transition: transform 420ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Stack.css:193](../upstream-free/blocks/card-stack/Stack.css#L193): `.stk-view-tilt { transition: none; }`
- [Stack.css:196](../upstream-free/blocks/card-stack/Stack.css#L196): `.stk-card { transition: opacity 360ms cubic-bezier(0.22, 1, 0.36, 1); }`
- [Stack.css:200](../upstream-free/blocks/card-stack/Stack.css#L200): `springs are at rest, so a transition here argues with nothing */`
- [Stack.css:202](../upstream-free/blocks/card-stack/Stack.css#L202): `transition:`
- [Stack.css:212](../upstream-free/blocks/card-stack/Stack.css#L212): `.stk-face, .stk-face[data-lift] { transition-duration: 1ms; transition-delay: 0ms; }`
- [Stack.tsx:45](../upstream-free/blocks/card-stack/Stack.tsx#L45): `/* ── inlined from lab/spring ──────────────────────── */`
- [Stack.tsx:46](../upstream-free/blocks/card-stack/Stack.tsx#L46): `/* ── one spring, for everything that settles ───────────────`
- [Stack.tsx:61](../upstream-free/blocks/card-stack/Stack.tsx#L61): `a second and the damping is RAISED to it rather than`
- [Stack.tsx:64](../upstream-free/blocks/card-stack/Stack.tsx#L64): `version that makes a spring behave differently on a busy`
- [Stack.tsx:72](../upstream-free/blocks/card-stack/Stack.tsx#L72): `/* 0..100 into the two numbers a spring actually has.`
- [Stack.tsx:83](../upstream-free/blocks/card-stack/Stack.tsx#L83): `/* The pair is chosen by DAMPING RATIO and then written back`
- [Stack.tsx:84](../upstream-free/blocks/card-stack/Stack.tsx#L84): `as stiffness and decay, because the ratio is the thing a`
- [Stack.tsx:90](../upstream-free/blocks/card-stack/Stack.tsx#L90): `The first version of this ran 0.06..0.26 stiffness against`
- [Stack.tsx:105](../upstream-free/blocks/card-stack/Stack.tsx#L105): `/* stiffness: how hard it is pulled toward the target */`
- [Stack.tsx:111](../upstream-free/blocks/card-stack/Stack.tsx#L111): `/* Units matter. The snap threshold is absolute, so a caller`
- [Stack.tsx:112](../upstream-free/blocks/card-stack/Stack.tsx#L112): `works in pixels or in 0..100 — a spring driven over 0..1`
- [Stack.tsx:273](../upstream-free/blocks/card-stack/Stack.tsx#L273): `own spring is than the knob says.`
- [Stack.tsx:276](../upstream-free/blocks/card-stack/Stack.tsx#L276): `springs at identical stiffness arrive together however they`
- [Stack.tsx:363](../upstream-free/blocks/card-stack/Stack.tsx#L363): `/* the spring, 0..100 — see springOf in ./spring */`
- [Stack.tsx:364](../upstream-free/blocks/card-stack/Stack.tsx#L364): `bounce = 5,`
- [Stack.tsx:373](../upstream-free/blocks/card-stack/Stack.tsx#L373): `bounce?: number;`
- [Stack.tsx:382](../upstream-free/blocks/card-stack/Stack.tsx#L382): `/* 'on' is the pointer. 'lit' is what each spring is aiming`
- [Stack.tsx:460](../upstream-free/blocks/card-stack/Stack.tsx#L460): `duration: VIEW_OUT,`
- [Stack.tsx:472](../upstream-free/blocks/card-stack/Stack.tsx#L472): `duration: still ? 1 : VIEW_IN,`
- [Stack.tsx:531](../upstream-free/blocks/card-stack/Stack.tsx#L531): `conditionally, and a spring nobody reads costs a number`
- [Stack.tsx:535](../upstream-free/blocks/card-stack/Stack.tsx#L535): `const tune = (i: number) => clamp(bounce * (1 + SEED[i].tune * sc * 0.45), 0, 100);`
- [Stack.tsx:593](../upstream-free/blocks/card-stack/Stack.tsx#L593): `/* the lift rides a CSS transition rather than a`
- [Stack.tsx:594](../upstream-free/blocks/card-stack/Stack.tsx#L594): `spring of its own, which is the pattern the`
- [Stack.tsx:596](../upstream-free/blocks/card-stack/Stack.tsx#L596): `element as a spring is two animations arguing over`
- [Stack.tsx:599](../upstream-free/blocks/card-stack/Stack.tsx#L599): `so the two cannot meet. A soft ease with no`
- [Stack.tsx:601](../upstream-free/blocks/card-stack/Stack.tsx#L601): `Bounce curve and read as a card jumping out of the`
- [Stack.tsx:603](../upstream-free/blocks/card-stack/Stack.tsx#L603): `"--stk-ease": still ? "linear" : "cubic-bezier(0.4, 0, 0.2, 1)",`
- [Stack.tsx:681](../upstream-free/blocks/card-stack/Stack.tsx#L681): `on its own spring. */`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
