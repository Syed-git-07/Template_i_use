# Slide to confirm

Public reference: https://bencho.dev/blocks/slide-confirm

[Original API and usage guide](../upstream-free/blocks/slide-confirm/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [SlideConfirm.css](../upstream-free/blocks/slide-confirm/SlideConfirm.css): 161 lines; SHA-256 `597ca7896fe8018bd1900fdc3e0f4a0860ef53bf910a7512e4d7ddc00c58f3a0`.
- [SlideConfirm.tsx](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx): 474 lines; SHA-256 `d29b92647ff29e8832011b80c8444abe2be210b197972c0a3a98ab8c83c3ceb8`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [SlideConfirm.css:123](../upstream-free/blocks/slide-confirm/SlideConfirm.css#L123): `transition 'transform' or the two fight every frame */`
- [SlideConfirm.css:124](../upstream-free/blocks/slide-confirm/SlideConfirm.css#L124): `transition: none;`
- [SlideConfirm.css:160](../upstream-free/blocks/slide-confirm/SlideConfirm.css#L160): `.sld-done { transition-duration: 160ms; }`
- [SlideConfirm.tsx:92](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L92): `It was two: 'x' on one spring and 'width' on another with`
- [SlideConfirm.tsx:111](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L111): `Its own clock rather than the spring's. The spring is`
- [SlideConfirm.tsx:114](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L114): `rest — the note the player's bounce carries. And the peak`
- [SlideConfirm.tsx:146](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L146): `/* ── SPEED, and deliberately not Bounce ──────────────────`
- [SlideConfirm.tsx:147](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L147): `There was a Bounce knob and it had to go, for the reason`
- [SlideConfirm.tsx:153](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L153): `Bounce 50: the handle shot 42px out of its own track.`
- [SlideConfirm.tsx:157](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L157): `it takes over once you let go — and the damping is derived`
- [SlideConfirm.tsx:163](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L163): `stiffness freely and the spring stays honest. */`
- [SlideConfirm.tsx:167](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L167): `const spring = {`
- [SlideConfirm.tsx:168](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L168): `type: "spring" as const,`
- [SlideConfirm.tsx:169](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L169): `stiffness: stiff,`
- [SlideConfirm.tsx:170](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L170): `damping: 2 * Math.sqrt(stiff * 0.9),`
- [SlideConfirm.tsx:171](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L171): `mass: 0.9,`
- [SlideConfirm.tsx:179](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L179): `const home = { ...spring, damping: 2 * Math.sqrt(stiff * 0.9) * 0.62 };`
- [SlideConfirm.tsx:249](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L249): `The spring is critically damped so x should never go below`
- [SlideConfirm.tsx:259](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L259): `The return spring is under-damped now, so it wants to`
- [SlideConfirm.tsx:262](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L262): `inset is not room to bounce in. Letting it through was`
- [SlideConfirm.tsx:263](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L263): `measured at 42px outside the block when the commit spring`
- [SlideConfirm.tsx:268](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L268): `what a bounce off a wall IS, and it reads as a soft`
- [SlideConfirm.tsx:270](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L270): `spring that went past; the two scales are read off it, and`
- [SlideConfirm.tsx:331](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L331): `spring, which is what keeps them in step frame by frame`
- [SlideConfirm.tsx:334](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L334): `animate(shown, 0, { duration: 0.16 });`
- [SlideConfirm.tsx:335](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L335): `animate(x, 0, spring);`
- [SlideConfirm.tsx:337](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L337): `duration: 0.42,`
- [SlideConfirm.tsx:339](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L339): `ease: [0.33, 0.55, 0.2, 1],`
- [SlideConfirm.tsx:342](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L342): `delay: 0.1,`
- [SlideConfirm.tsx:346](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L346): `animate(shown, 1, { duration: 0.22, delay: 0.12 });`
- [SlideConfirm.tsx:352](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L352): `animate(anchor, 0, { type: "spring", stiffness: 380, damping: 34, mass: 0.9 });`
- [SlideConfirm.tsx:444](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L444): `arithmetic on the value the spring is already`
- [SlideConfirm.tsx:451](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L451): `transition={{ type: "spring", stiffness: 380, damping: 34, mass: 0.7 }}`
- [SlideConfirm.tsx:465](../upstream-free/blocks/slide-confirm/SlideConfirm.tsx#L465): `transition={{ duration: 0.16, ease: [0.33, 0.55, 0.2, 1] }}`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
