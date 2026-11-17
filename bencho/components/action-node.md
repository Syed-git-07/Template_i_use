# Action node

Public reference: https://bencho.dev/blocks/action-node

[Original API and usage guide](../upstream-free/blocks/action-node/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [ActionNode.css](../upstream-free/blocks/action-node/ActionNode.css): 326 lines; SHA-256 `162ffaadb92f807e933a244d1f5cf9ae1eb9eeb1a6a74fefefe542e1c53d354c`.
- [ActionNode.tsx](../upstream-free/blocks/action-node/ActionNode.tsx): 776 lines; SHA-256 `0e01b33bec11f82c1b6ed0e6053d7911e492bb07b6439d7f2bc7b27b92851470`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [ActionNode.css:111](../upstream-free/blocks/action-node/ActionNode.css#L111): `transition: translate 220ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [ActionNode.css:301](../upstream-free/blocks/action-node/ActionNode.css#L301): `The spring owns how far out of the corner a button is and`
- [ActionNode.css:308](../upstream-free/blocks/action-node/ActionNode.css#L308): `for the split. A transition on 'scale' itself would smooth`
- [ActionNode.css:309](../upstream-free/blocks/action-node/ActionNode.css#L309): `the spring's own frames — two animations arguing over one`
- [ActionNode.css:314](../upstream-free/blocks/action-node/ActionNode.css#L314): `transition: --zoom 160ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [ActionNode.css:325](../upstream-free/blocks/action-node/ActionNode.css#L325): `has no background transition left to run. */`
- [ActionNode.tsx:4](../upstream-free/blocks/action-node/ActionNode.tsx#L4): `/* ── inlined from lab/spring ──────────────────────── */`
- [ActionNode.tsx:5](../upstream-free/blocks/action-node/ActionNode.tsx#L5): `/* ── one spring, for everything that settles ───────────────`
- [ActionNode.tsx:20](../upstream-free/blocks/action-node/ActionNode.tsx#L20): `a second and the damping is RAISED to it rather than`
- [ActionNode.tsx:23](../upstream-free/blocks/action-node/ActionNode.tsx#L23): `version that makes a spring behave differently on a busy`
- [ActionNode.tsx:31](../upstream-free/blocks/action-node/ActionNode.tsx#L31): `/* 0..100 into the two numbers a spring actually has.`
- [ActionNode.tsx:42](../upstream-free/blocks/action-node/ActionNode.tsx#L42): `/* The pair is chosen by DAMPING RATIO and then written back`
- [ActionNode.tsx:43](../upstream-free/blocks/action-node/ActionNode.tsx#L43): `as stiffness and decay, because the ratio is the thing a`
- [ActionNode.tsx:49](../upstream-free/blocks/action-node/ActionNode.tsx#L49): `The first version of this ran 0.06..0.26 stiffness against`
- [ActionNode.tsx:64](../upstream-free/blocks/action-node/ActionNode.tsx#L64): `/* stiffness: how hard it is pulled toward the target */`
- [ActionNode.tsx:70](../upstream-free/blocks/action-node/ActionNode.tsx#L70): `/* Units matter. The snap threshold is absolute, so a caller`
- [ActionNode.tsx:71](../upstream-free/blocks/action-node/ActionNode.tsx#L71): `works in pixels or in 0..100 — a spring driven over 0..1`
- [ActionNode.tsx:161](../upstream-free/blocks/action-node/ActionNode.tsx#L161): `── ONE SPRING EACH, AND THE STAGGER IS A DELAY ON THE`
- [ActionNode.tsx:162](../upstream-free/blocks/action-node/ActionNode.tsx#L162): `TARGET, NOT AN EASE ─────────────────────────────────`
- [ActionNode.tsx:166](../upstream-free/blocks/action-node/ActionNode.tsx#L166): `the one before it, and the spring does the rest: the`
- [ActionNode.tsx:388](../upstream-free/blocks/action-node/ActionNode.tsx#L388): `/* the spring, 0..100 — see springOf in ./spring */`
- [ActionNode.tsx:389](../upstream-free/blocks/action-node/ActionNode.tsx#L389): `bounce = 20,`
- [ActionNode.tsx:398](../upstream-free/blocks/action-node/ActionNode.tsx#L398): `bounce?: number;`
- [ActionNode.tsx:407](../upstream-free/blocks/action-node/ActionNode.tsx#L407): `'on' is the pointer. 'lit' is what each spring is aiming`
- [ActionNode.tsx:443](../upstream-free/blocks/action-node/ActionNode.tsx#L443): `drawn conditionally and a spring nobody reads costs a`
- [ActionNode.tsx:445](../upstream-free/blocks/action-node/ActionNode.tsx#L445): `const p0 = useSpring(lit[0] ? 100 : 0, bounce, still);`
- [ActionNode.tsx:446](../upstream-free/blocks/action-node/ActionNode.tsx#L446): `const p1 = useSpring(lit[1] ? 100 : 0, bounce, still);`
- [ActionNode.tsx:447](../upstream-free/blocks/action-node/ActionNode.tsx#L447): `const p2 = useSpring(lit[2] ? 100 : 0, bounce, still);`
- [ActionNode.tsx:448](../upstream-free/blocks/action-node/ActionNode.tsx#L448): `const p3 = useSpring(lit[3] ? 100 : 0, bounce, still);`
- [ActionNode.tsx:711](../upstream-free/blocks/action-node/ActionNode.tsx#L711): `'u' is not clamped, so the spring's overshoot`
- [ActionNode.tsx:750](../upstream-free/blocks/action-node/ActionNode.tsx#L750): `arrives at its place, and the spring's own`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
