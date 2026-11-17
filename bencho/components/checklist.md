# Checklist

Public reference: https://bencho.dev/blocks/checklist

[Original API and usage guide](../upstream-free/blocks/checklist/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Checklist.css](../upstream-free/blocks/checklist/Checklist.css): 233 lines; SHA-256 `f9ab279aebc94ea87a98dd8713990149a2fae2fa8a9768eabae216fae87c7cc5`.
- [Checklist.tsx](../upstream-free/blocks/checklist/Checklist.tsx): 799 lines; SHA-256 `b08f350894eb392a165070704e52a2569f76164203b485ad631eb7b325c60eed`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Checklist.css:15](../upstream-free/blocks/checklist/Checklist.css#L15): `transition: height 420ms cubic-bezier(0.22, 1, 0.36, 1);`
- [Checklist.css:84](../upstream-free/blocks/checklist/Checklist.css#L84): `transition: opacity 220ms ease;}`
- [Checklist.css:113](../upstream-free/blocks/checklist/Checklist.css#L113): `transition: opacity 160ms ease;}`
- [Checklist.tsx:8](../upstream-free/blocks/checklist/Checklist.tsx#L8): `ONE SPRING PER ROW, AND EVERYTHING IS READ OFF IT. The box`
- [Checklist.tsx:16](../upstream-free/blocks/checklist/Checklist.tsx#L16): `stylesheet carries a transition of its own.`
- [Checklist.tsx:19](../upstream-free/blocks/checklist/Checklist.tsx#L19): `spring goes past its target and comes back, which is what`
- [Checklist.tsx:25](../upstream-free/blocks/checklist/Checklist.tsx#L25): `glitch rather than a bounce, and a rule that overshoots`
- [Checklist.tsx:28](../upstream-free/blocks/checklist/Checklist.tsx#L28): `One spring, two readings of it, and the difference is one`
- [Checklist.tsx:31](../upstream-free/blocks/checklist/Checklist.tsx#L31): `/* ── inlined from lab/spring ──────────────────────── */`
- [Checklist.tsx:32](../upstream-free/blocks/checklist/Checklist.tsx#L32): `/* ── one spring, for everything that settles ───────────────`
- [Checklist.tsx:47](../upstream-free/blocks/checklist/Checklist.tsx#L47): `a second and the damping is RAISED to it rather than`
- [Checklist.tsx:50](../upstream-free/blocks/checklist/Checklist.tsx#L50): `version that makes a spring behave differently on a busy`
- [Checklist.tsx:58](../upstream-free/blocks/checklist/Checklist.tsx#L58): `/* 0..100 into the two numbers a spring actually has.`
- [Checklist.tsx:69](../upstream-free/blocks/checklist/Checklist.tsx#L69): `/* The pair is chosen by DAMPING RATIO and then written back`
- [Checklist.tsx:70](../upstream-free/blocks/checklist/Checklist.tsx#L70): `as stiffness and decay, because the ratio is the thing a`
- [Checklist.tsx:76](../upstream-free/blocks/checklist/Checklist.tsx#L76): `The first version of this ran 0.06..0.26 stiffness against`
- [Checklist.tsx:91](../upstream-free/blocks/checklist/Checklist.tsx#L91): `/* stiffness: how hard it is pulled toward the target */`
- [Checklist.tsx:97](../upstream-free/blocks/checklist/Checklist.tsx#L97): `/* Units matter. The snap threshold is absolute, so a caller`
- [Checklist.tsx:98](../upstream-free/blocks/checklist/Checklist.tsx#L98): `works in pixels or in 0..100 — a spring driven over 0..1`
- [Checklist.tsx:174](../upstream-free/blocks/checklist/Checklist.tsx#L174): `const BOUNCE = 50;`
- [Checklist.tsx:177](../upstream-free/blocks/checklist/Checklist.tsx#L177): `Both are read off the same spring, but the rule starts a`
- [Checklist.tsx:255](../upstream-free/blocks/checklist/Checklist.tsx#L255): `with no bounce at all reads as a card being placed — but a`
- [Checklist.tsx:362](../upstream-free/blocks/checklist/Checklist.tsx#L362): `0..100 — 0 is a spring that arrives dead, which is a`
- [Checklist.tsx:364](../upstream-free/blocks/checklist/Checklist.tsx#L364): `bounce = BOUNCE,`
- [Checklist.tsx:369](../upstream-free/blocks/checklist/Checklist.tsx#L369): `bounce?: number;`
- [Checklist.tsx:435](../upstream-free/blocks/checklist/Checklist.tsx#L435): `animation for free — the same height transition that`
- [Checklist.tsx:520](../upstream-free/blocks/checklist/Checklist.tsx#L520): `between — see the transition on .chk. Adding a task`
- [Checklist.tsx:543](../upstream-free/blocks/checklist/Checklist.tsx#L543): `bounce={bounce}`
- [Checklist.tsx:629](../upstream-free/blocks/checklist/Checklist.tsx#L629): `bounce,`
- [Checklist.tsx:645](../upstream-free/blocks/checklist/Checklist.tsx#L645): `bounce: number;`
- [Checklist.tsx:662](../upstream-free/blocks/checklist/Checklist.tsx#L662): `parent. It costs nothing at rest: a spring sitting on its`
- [Checklist.tsx:678](../upstream-free/blocks/checklist/Checklist.tsx#L678): `const t = useSpring(on ? 1 : 0, clamp(bounce, 0, 100), still);`
- [Checklist.tsx:684](../upstream-free/blocks/checklist/Checklist.tsx#L684): `Down is a duration with gravity's shape in it: it starts`
- [Checklist.tsx:687](../upstream-free/blocks/checklist/Checklist.tsx#L687): `and being placed. Up is a spring, because coming back is`
- [Checklist.tsx:689](../upstream-free/blocks/checklist/Checklist.tsx#L689): `dropped — and a spring interrupts cleanly, so unticking a`
- [Checklist.tsx:702](../upstream-free/blocks/checklist/Checklist.tsx#L702): `duration: run,`
- [Checklist.tsx:704](../upstream-free/blocks/checklist/Checklist.tsx#L704): `ease: [...FALL_EASE],`
- [Checklist.tsx:707](../upstream-free/blocks/checklist/Checklist.tsx#L707): `and do not bounce */`
- [Checklist.tsx:708](../upstream-free/blocks/checklist/Checklist.tsx#L708): `const lean = { duration: run, ease: "easeIn" as const };`
- [Checklist.tsx:723](../upstream-free/blocks/checklist/Checklist.tsx#L723): `exit={{ opacity: 0, transition: { duration: 0.16 } }}`
- [Checklist.tsx:729](../upstream-free/blocks/checklist/Checklist.tsx#L729): `transition={`
- [Checklist.tsx:732](../upstream-free/blocks/checklist/Checklist.tsx#L732): `: { type: "spring", stiffness: 380, damping: 34, mass: 0.9 }`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
