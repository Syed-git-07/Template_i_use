# Todo tower

Public reference: https://bencho.dev/blocks/todo-tower

[Original API and usage guide](../upstream-free/blocks/todo-tower/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Tower.css](../upstream-free/blocks/todo-tower/Tower.css): 205 lines; SHA-256 `cf62f82d487c262cffe72bd1a401dc11a35471e9d2cc38a0338e8d6dc944342e`.
- [Tower.tsx](../upstream-free/blocks/todo-tower/Tower.tsx): 1248 lines; SHA-256 `91dd93b695c0f822b760a4b3426c0b0c67776e1d0bbc7159f18c5e1a90171cbf`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Tower.css:108](../upstream-free/blocks/todo-tower/Tower.css#L108): `transition:`
- [Tower.css:111](../upstream-free/blocks/todo-tower/Tower.css#L111): `opacity 220ms ease 160ms;}`
- [Tower.css:122](../upstream-free/blocks/todo-tower/Tower.css#L122): `transition-delay: 90ms, 90ms, 150ms;}`
- [Tower.css:163](../upstream-free/blocks/todo-tower/Tower.css#L163): `transition:`
- [Tower.css:164](../upstream-free/blocks/todo-tower/Tower.css#L164): `background-color 160ms ease,`
- [Tower.css:165](../upstream-free/blocks/todo-tower/Tower.css#L165): `box-shadow 160ms ease;}`
- [Tower.css:169](../upstream-free/blocks/todo-tower/Tower.css#L169): `transition: opacity 160ms ease;}`
- [Tower.css:200](../upstream-free/blocks/todo-tower/Tower.css#L200): `.twr-card { transition-duration: 160ms, 160ms, 160ms; }`
- [Tower.css:204](../upstream-free/blocks/todo-tower/Tower.css#L204): `.twr-check, .twr-check svg { transition-duration: 160ms; }`
- [Tower.tsx:21](../upstream-free/blocks/todo-tower/Tower.tsx#L21): `clipped to the faces that are actually touching, friction,`
- [Tower.tsx:24](../upstream-free/blocks/todo-tower/Tower.tsx#L24): `centre of mass is past the edge of its support and gravity`
- [Tower.tsx:39](../upstream-free/blocks/todo-tower/Tower.tsx#L39): `/* ── inlined from lab/spring ──────────────────────── */`
- [Tower.tsx:40](../upstream-free/blocks/todo-tower/Tower.tsx#L40): `/* ── one spring, for everything that settles ───────────────`
- [Tower.tsx:55](../upstream-free/blocks/todo-tower/Tower.tsx#L55): `a second and the damping is RAISED to it rather than`
- [Tower.tsx:58](../upstream-free/blocks/todo-tower/Tower.tsx#L58): `version that makes a spring behave differently on a busy`
- [Tower.tsx:76](../upstream-free/blocks/todo-tower/Tower.tsx#L76): `contact points, then sequential impulses with friction and`
- [Tower.tsx:100](../upstream-free/blocks/todo-tower/Tower.tsx#L100): `friction: number;`
- [Tower.tsx:118](../upstream-free/blocks/todo-tower/Tower.tsx#L118): `type Arbiter = { a: Body; b: Body; cs: Contact[]; friction: number };`
- [Tower.tsx:120](../upstream-free/blocks/todo-tower/Tower.tsx#L120): `function box(id: number, x: number, y: number, hw: number, hh: number, friction: number, mass = 1): Body {`
- [Tower.tsx:121](../upstream-free/blocks/todo-tower/Tower.tsx#L121): `const still = mass === 0;`
- [Tower.tsx:123](../upstream-free/blocks/todo-tower/Tower.tsx#L123): `id, x, y, a: 0, vx: 0, vy: 0, w: 0, hw, hh, friction,`
- [Tower.tsx:124](../upstream-free/blocks/todo-tower/Tower.tsx#L124): `invM: still ? 0 : 1 / mass,`
- [Tower.tsx:125](../upstream-free/blocks/todo-tower/Tower.tsx#L125): `invI: still ? 0 : 12 / (mass * (4 * hw * hw + 4 * hh * hh)),`
- [Tower.tsx:129](../upstream-free/blocks/todo-tower/Tower.tsx#L129): `/* the mass a held card had, so letting go can give it back */`
- [Tower.tsx:284](../upstream-free/blocks/todo-tower/Tower.tsx#L284): `Both are multiples of the cards' own friction, so Slip still`
- [Tower.tsx:289](../upstream-free/blocks/todo-tower/Tower.tsx#L289): `a rider directly, as μ·g. CARRY is the friction of the real`
- [Tower.tsx:331](../upstream-free/blocks/todo-tower/Tower.tsx#L331): `the map, still solved every step — with no mass on`
- [Tower.tsx:356](../upstream-free/blocks/todo-tower/Tower.tsx#L356): `W.arbiters.set(key, { a, b, cs, friction: Math.sqrt(a.friction * b.friction) });`
- [Tower.tsx:360](../upstream-free/blocks/todo-tower/Tower.tsx#L360): `/* ── friction while something is carried ──────────────────`
- [Tower.tsx:372](../upstream-free/blocks/todo-tower/Tower.tsx#L372): `if (carried.has(arb.a) && carried.has(arb.b)) arb.friction = CARRY * Math.sqrt(arb.a.friction * arb.b.friction);`
- [Tower.tsx:373](../upstream-free/blocks/todo-tower/Tower.tsx#L373): `else if (arb.a === held || arb.b === held) arb.friction = 0;`
- [Tower.tsx:416](../upstream-free/blocks/todo-tower/Tower.tsx#L416): `for (const { a, b, cs, friction } of W.arbiters.values()) {`
- [Tower.tsx:437](../upstream-free/blocks/todo-tower/Tower.tsx#L437): `const max = friction * c.pn;`
- [Tower.tsx:554](../upstream-free/blocks/todo-tower/Tower.tsx#L554): `the hand does not have to drag them along by friction, so it`
- [Tower.tsx:558](../upstream-free/blocks/todo-tower/Tower.tsx#L558): `whenever anything sat on the card, so friction could keep up.`
- [Tower.tsx:578](../upstream-free/blocks/todo-tower/Tower.tsx#L578): `that was exact, but the moment a rider lagged, its friction`
- [Tower.tsx:583](../upstream-free/blocks/todo-tower/Tower.tsx#L583): `Sideways is friction: μ·g, times GRIP because a pointer`
- [Tower.tsx:597](../upstream-free/blocks/todo-tower/Tower.tsx#L597): `const side = r.friction * GRIP * W.gravity * dt;`
- [Tower.tsx:659](../upstream-free/blocks/todo-tower/Tower.tsx#L659): `/* ── no bounce, and no knob for it ─────────────────────────`
- [Tower.tsx:666](../upstream-free/blocks/todo-tower/Tower.tsx#L666): `/* Slip is friction, turned over — 0 is a grippy card that`
- [Tower.tsx:833](../upstream-free/blocks/todo-tower/Tower.tsx#L833): `Object.assign(b, { x, y, hw, hh, friction: fr });`
- [Tower.tsx:949](../upstream-free/blocks/todo-tower/Tower.tsx#L949): `fresh one up. Gravity and Bounce are properties of the`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
