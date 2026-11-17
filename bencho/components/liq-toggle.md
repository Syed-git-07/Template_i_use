# Liquid toggle

Public reference: https://bencho.dev/blocks/liq-toggle

[Original API and usage guide](../upstream-free/blocks/liq-toggle/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Toggle.css](../upstream-free/blocks/liq-toggle/Toggle.css): 165 lines; SHA-256 `a5d4eb8414b76c163ba815f6ac1be75e6f898197a23d74f08289bb278d841976`.
- [Toggle.tsx](../upstream-free/blocks/liq-toggle/Toggle.tsx): 341 lines; SHA-256 `57f1422bd66c977b036bbd7c8a2aa61b6ca84d3b140b2c5d4e4c69ae2d970831`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Toggle.css:110](../upstream-free/blocks/liq-toggle/Toggle.css#L110): `transition: background 420ms ease;}`
- [Toggle.css:126](../upstream-free/blocks/liq-toggle/Toggle.css#L126): `lagging spring; the goo between them necked into a thread,`
- [Toggle.css:150](../upstream-free/blocks/liq-toggle/Toggle.css#L150): `/* transform is Framer's — a CSS transition on the same`
- [Toggle.css:151](../upstream-free/blocks/liq-toggle/Toggle.css#L151): `property re-interpolates every frame the spring writes,`
- [Toggle.css:152](../upstream-free/blocks/liq-toggle/Toggle.css#L152): `and what you see is the easing, not the spring. The colour`
- [Toggle.css:156](../upstream-free/blocks/liq-toggle/Toggle.css#L156): `transition: background 420ms ease;}`
- [Toggle.css:164](../upstream-free/blocks/liq-toggle/Toggle.css#L164): `.liq-thumb, .liq-pill, .liq-bead { transition-duration: 160ms; }`
- [Toggle.tsx:38](../upstream-free/blocks/liq-toggle/Toggle.tsx#L38): `be eaten by the same threshold. */`
- [Toggle.tsx:87](../upstream-free/blocks/liq-toggle/Toggle.tsx#L87): `/* held, so the settling spring knows to keep out of the way`
- [Toggle.tsx:91](../upstream-free/blocks/liq-toggle/Toggle.tsx#L91): `because what it drives is a spring in the same transform`
- [Toggle.tsx:96](../upstream-free/blocks/liq-toggle/Toggle.tsx#L96): `running behind it: blur everything, then threshold the`
- [Toggle.tsx:99](../upstream-free/blocks/liq-toggle/Toggle.tsx#L99): `work on, and a blur-then-threshold pass over a single`
- [Toggle.tsx:116](../upstream-free/blocks/liq-toggle/Toggle.tsx#L116): `is what lets a finger and a spring both drive it without`
- [Toggle.tsx:121](../upstream-free/blocks/liq-toggle/Toggle.tsx#L121): `The straggler is a SPRING FOLLOWING that value. It used to`
- [Toggle.tsx:122](../upstream-free/blocks/liq-toggle/Toggle.tsx#L122): `be the same target with a delay on it, which is a good`
- [Toggle.tsx:123](../upstream-free/blocks/liq-toggle/Toggle.tsx#L123): `description of a click and a poor one of a drag — a delay`
- [Toggle.tsx:125](../upstream-free/blocks/liq-toggle/Toggle.tsx#L125): `thumb left; a spring means it is always chasing wherever`
- [Toggle.tsx:133](../upstream-free/blocks/liq-toggle/Toggle.tsx#L133): `on a lagging spring, and the goo between them necked into`
- [Toggle.tsx:149](../upstream-free/blocks/liq-toggle/Toggle.tsx#L149): `const eased = useSpring(vel, { stiffness: 380, damping: 34, mass: 0.6 });`
- [Toggle.tsx:181](../upstream-free/blocks/liq-toggle/Toggle.tsx#L181): `stiffness: 380,`
- [Toggle.tsx:182](../upstream-free/blocks/liq-toggle/Toggle.tsx#L182): `damping: 34,`
- [Toggle.tsx:183](../upstream-free/blocks/liq-toggle/Toggle.tsx#L183): `mass: 0.6,`
- [Toggle.tsx:189](../upstream-free/blocks/liq-toggle/Toggle.tsx#L189): `Bounce is the damping and Speed is the stiffness, so both`
- [Toggle.tsx:190](../upstream-free/blocks/liq-toggle/Toggle.tsx#L190): `knobs are properties of one spring rather than of a curve.`
- [Toggle.tsx:198](../upstream-free/blocks/liq-toggle/Toggle.tsx#L198): `slow spring but the absence of a hard stop; the same`
- [Toggle.tsx:202](../upstream-free/blocks/liq-toggle/Toggle.tsx#L202): `Damping is a constant now. It was the Bounce knob, and a`
- [Toggle.tsx:203](../upstream-free/blocks/liq-toggle/Toggle.tsx#L203): `switch is not a thing anybody wants a bounce dial on: the`
- [Toggle.tsx:210](../upstream-free/blocks/liq-toggle/Toggle.tsx#L210): `type: "spring" as const,`
- [Toggle.tsx:211](../upstream-free/blocks/liq-toggle/Toggle.tsx#L211): `stiffness: 170 - (50 - speed) * 1.1,`
- [Toggle.tsx:212](../upstream-free/blocks/liq-toggle/Toggle.tsx#L212): `damping: 21.5,`
- [Toggle.tsx:213](../upstream-free/blocks/liq-toggle/Toggle.tsx#L213): `mass: 0.9,`
- [Toggle.tsx:222](../upstream-free/blocks/liq-toggle/Toggle.tsx#L222): `value exactly where the spring had got to. */`
- [Toggle.tsx:246](../upstream-free/blocks/liq-toggle/Toggle.tsx#L246): `it TELEPORTED. 'x.set()' is a hard write with no spring`
- [Toggle.tsx:300](../upstream-free/blocks/liq-toggle/Toggle.tsx#L300): `'held' never settles: the rest spring is torn down while`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
