# Step player

Public reference: https://bencho.dev/blocks/step-player

[Original API and usage guide](../upstream-free/blocks/step-player/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [StepPlayer.css](../upstream-free/blocks/step-player/StepPlayer.css): 96 lines; SHA-256 `9744c80d25c2c1dd3a9f833e72b12870acd4a9c820dae2c3a7f5a09d585ba6e3`.
- [StepPlayer.tsx](../upstream-free/blocks/step-player/StepPlayer.tsx): 530 lines; SHA-256 `1ae9509be559a4be6f4028ec5a7db9cb33472a4404e03ac361d943033595d3c8`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [StepPlayer.css:6](../upstream-free/blocks/step-player/StepPlayer.css#L6): `transition on a thing that moves. */`
- [StepPlayer.css:74](../upstream-free/blocks/step-player/StepPlayer.css#L74): `transition: scale 160ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [StepPlayer.css:89](../upstream-free/blocks/step-player/StepPlayer.css#L89): `transition: color 160ms ease;}`
- [StepPlayer.tsx:31](../upstream-free/blocks/step-player/StepPlayer.tsx#L31): `/* ── inlined from lab/spring ──────────────────────── */`
- [StepPlayer.tsx:32](../upstream-free/blocks/step-player/StepPlayer.tsx#L32): `/* ── one spring, for everything that settles ───────────────`
- [StepPlayer.tsx:47](../upstream-free/blocks/step-player/StepPlayer.tsx#L47): `a second and the damping is RAISED to it rather than`
- [StepPlayer.tsx:50](../upstream-free/blocks/step-player/StepPlayer.tsx#L50): `version that makes a spring behave differently on a busy`
- [StepPlayer.tsx:68](../upstream-free/blocks/step-player/StepPlayer.tsx#L68): `ONE NUMBER IS THE STATE. There is a single spring running`
- [StepPlayer.tsx:70](../upstream-free/blocks/step-player/StepPlayer.tsx#L70): `below is read off it. Nothing has a transition of its own`
- [StepPlayer.tsx:75](../upstream-free/blocks/step-player/StepPlayer.tsx#L75): `of them to arrive early; with one spring there are none.`
- [StepPlayer.tsx:98](../upstream-free/blocks/step-player/StepPlayer.tsx#L98): `function useTween(to: number, ms: number, instant = false, ease = QUART) {`
- [StepPlayer.tsx:114](../upstream-free/blocks/step-player/StepPlayer.tsx#L114): `cur.current = from + (to - from) * ease(t);`
- [StepPlayer.tsx:123](../upstream-free/blocks/step-player/StepPlayer.tsx#L123): `}, [to, ms, instant, ease]);`
- [StepPlayer.tsx:229](../upstream-free/blocks/step-player/StepPlayer.tsx#L229): `The fill arrives at a steady speed, and an ease-in-out`
- [StepPlayer.tsx:233](../upstream-free/blocks/step-player/StepPlayer.tsx#L233): `ease-out leaves at speed and does its slowing on arrival. */`
- [StepPlayer.tsx:251](../upstream-free/blocks/step-player/StepPlayer.tsx#L251): `than it was, because an ease-out spends its time landing */`
- [StepPlayer.tsx:255](../upstream-free/blocks/step-player/StepPlayer.tsx#L255): `to follow an ease-out that covers most of its ground early. */`
- [StepPlayer.tsx:286](../upstream-free/blocks/step-player/StepPlayer.tsx#L286): `/* a spring for the rare edge with no timed move to follow —`
- [StepPlayer.tsx:462](../upstream-free/blocks/step-player/StepPlayer.tsx#L462): `let delay = -1;`
- [StepPlayer.tsx:465](../upstream-free/blocks/step-player/StepPlayer.tsx#L465): `delay = Math.min(span, wk.reach) * wk.stagger;`
- [StepPlayer.tsx:471](../upstream-free/blocks/step-player/StepPlayer.tsx#L471): `if (span - k <= wk.reach) delay = (k - skip) * wk.stagger;`
- [StepPlayer.tsx:473](../upstream-free/blocks/step-player/StepPlayer.tsx#L473): `if (delay >= 0) {`
- [StepPlayer.tsx:474](../upstream-free/blocks/step-player/StepPlayer.tsx#L474): `const u = (now - w.t0 - LEAD - delay) / RISE;`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
