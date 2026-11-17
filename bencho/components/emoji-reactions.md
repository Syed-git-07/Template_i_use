# Emoji reactions

Public reference: https://bencho.dev/blocks/emoji-reactions

[Original API and usage guide](../upstream-free/blocks/emoji-reactions/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Reactions.css](../upstream-free/blocks/emoji-reactions/Reactions.css): 317 lines; SHA-256 `e4383bd1d9bfa68cab87ed6761cee582ed8bebc24791aae4a99abe5e6d07dde5`.
- [Reactions.tsx](../upstream-free/blocks/emoji-reactions/Reactions.tsx): 461 lines; SHA-256 `a1cd870a85513e61db043e26fd5a453a2559e7c44d9332d32ed2a281a2ac2086`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Reactions.css:44](../upstream-free/blocks/emoji-reactions/Reactions.css#L44): `spring is at, so a measuring pixel can never pile up on one side */`
- [Reactions.css:86](../upstream-free/blocks/emoji-reactions/Reactions.css#L86): `transition: background-color 160ms ease, box-shadow 160ms ease;`
- [Reactions.css:106](../upstream-free/blocks/emoji-reactions/Reactions.css#L106): `.rxn-chip-e { font-size: 20px; line-height: 1; transition: opacity 160ms ease; letter-spacing: -0.02em; }`
- [Reactions.css:129](../upstream-free/blocks/emoji-reactions/Reactions.css#L129): `animation: rxn-puff 520ms ease-out forwards;}`
- [Reactions.css:131](../upstream-free/blocks/emoji-reactions/Reactions.css#L131): `.rxn-p[data-play][data-k="flicker"] { animation: rxn-flicker 620ms ease-out; }`
- [Reactions.css:146](../upstream-free/blocks/emoji-reactions/Reactions.css#L146): `.rxn-p[data-play][data-k="glance"] { animation: rxn-glance 700ms ease-in-out; }`
- [Reactions.css:150](../upstream-free/blocks/emoji-reactions/Reactions.css#L150): `.rxn-p[data-play][data-k="beat"] { animation: rxn-beat 620ms ease-in-out; }`
- [Reactions.css:154](../upstream-free/blocks/emoji-reactions/Reactions.css#L154): `.rxn-p[data-play][data-k="laugh"] { animation: rxn-laugh 560ms ease-in-out; }`
- [Reactions.css:158](../upstream-free/blocks/emoji-reactions/Reactions.css#L158): `.rxn-p[data-play][data-k="droop"] { animation: rxn-droop 700ms ease-in-out; transform-origin: 50% 100%; }`
- [Reactions.css:160](../upstream-free/blocks/emoji-reactions/Reactions.css#L160): `.rxn-p[data-play][data-k="bow"] { animation: rxn-bow 620ms ease-in-out; transform-origin: 50% 100%; }`
- [Reactions.css:173](../upstream-free/blocks/emoji-reactions/Reactions.css#L173): `transition: transform 220ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [Reactions.css:196](../upstream-free/blocks/emoji-reactions/Reactions.css#L196): `transition: color 160ms ease, scale 160ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [Reactions.css:234](../upstream-free/blocks/emoji-reactions/Reactions.css#L234): `transition: transform 220ms cubic-bezier(0.24, 1.34, 0.38, 1);`
- [Reactions.tsx:37](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L37): `/* ── inlined from lab/spring ──────────────────────── */`
- [Reactions.tsx:38](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L38): `/* ── one spring, for everything that settles ───────────────`
- [Reactions.tsx:53](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L53): `a second and the damping is RAISED to it rather than`
- [Reactions.tsx:56](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L56): `version that makes a spring behave differently on a busy`
- [Reactions.tsx:88](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L88): `Not one generic bounce for all of them: the rocket launches,`
- [Reactions.tsx:144](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L144): `bounce = 45,`
- [Reactions.tsx:149](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L149): `bounce?: number;`
- [Reactions.tsx:166](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L166): `const spring = { type: "spring" as const, bounce: (bounce / 100) * 0.55, duration: 0.42 };`
- [Reactions.tsx:169](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L169): `const quick = { type: "spring" as const, bounce: (bounce / 100) * 0.45, duration: 0.22 };`
- [Reactions.tsx:188](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L188): `/* the message's own width, so the pill can spring to and from it */`
- [Reactions.tsx:323](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L323): `width and corner spring between the two */}`
- [Reactions.tsx:333](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L333): `transition={quick}`
- [Reactions.tsx:340](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L340): `transition={{ duration: open ? 0.09 : 0.22, delay: open ? 0 : 0.08 }}`
- [Reactions.tsx:351](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L351): `exit={{ opacity: 0, transition: { duration: 0.16 } }}`
- [Reactions.tsx:367](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L367): `animate={{ opacity: 1, y: 0, scale: 1, filter: "blur(0px)", transition: { ...quick, delay: 0.02 + i * 0.018 } }}`
- [Reactions.tsx:382](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L382): `transition={{ duration: 0.16 }}`
- [Reactions.tsx:395](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L395): `<motion.div className="rxn-row" layout transition={spring}>`
- [Reactions.tsx:408](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L408): `animate={{ opacity: 1, scale: 1, transition: spring }}`
- [Reactions.tsx:409](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L409): `exit={{ opacity: 0, scale: 0.5, transition: { duration: 0.16 } }}`
- [Reactions.tsx:453](../upstream-free/blocks/emoji-reactions/Reactions.tsx#L453): `transition={{ duration: 0.6, ease: [0.35, 0, 0.3, 1], times: [0, 0.45, 1] }}`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
