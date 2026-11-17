# Pull to refresh

Public reference: https://bencho.dev/blocks/pull

[Original API and usage guide](../upstream-free/blocks/pull/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Balance.css](../upstream-free/blocks/pull/Balance.css): 523 lines; SHA-256 `2f99bf281cd996f7ff2fa97e0e226d2bda58759555adb897a84e6194c44b8922`.
- [Balance.tsx](../upstream-free/blocks/pull/Balance.tsx): 1054 lines; SHA-256 `7dda9ab003eaddf482e8eddf8fc68ad635ebaeaea430e51630e83b53f533d11f`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Balance.css:104](../upstream-free/blocks/pull/Balance.css#L104): `the rebound can spend it — the spring goes past zero on`
- [Balance.css:106](../upstream-free/blocks/pull/Balance.css#L106): `its resting height. That is the bounce.`
- [Balance.css:406](../upstream-free/blocks/pull/Balance.css#L406): `transition: opacity 160ms ease;}`
- [Balance.css:414](../upstream-free/blocks/pull/Balance.css#L414): `It does NOT transition its position. A dot that eases toward`
- [Balance.css:441](../upstream-free/blocks/pull/Balance.css#L441): `transition: scale 160ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [Balance.css:476](../upstream-free/blocks/pull/Balance.css#L476): `/* A bounce you feel rather than watch. The overshoot is`
- [Balance.css:482](../upstream-free/blocks/pull/Balance.css#L482): `the shorter duration keeps the whole move under the time`
- [Balance.css:484](../upstream-free/blocks/pull/Balance.css#L484): `transition: transform 420ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [Balance.css:506](../upstream-free/blocks/pull/Balance.css#L506): `transition: color 220ms ease, transform 220ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [Balance.css:516](../upstream-free/blocks/pull/Balance.css#L516): `.bal[data-phase="work"] .bal-goo { animation-duration: 3s; }`
- [Balance.css:520](../upstream-free/blocks/pull/Balance.css#L520): `.bal-tip, .bal-guide, .bal-win-pill { transition-duration: 160ms; }`
- [Balance.tsx:14](../upstream-free/blocks/pull/Balance.tsx#L14): `when the droplet stops wobbling. A spring that gates a`
- [Balance.tsx:17](../upstream-free/blocks/pull/Balance.tsx#L17): `/* ── inlined from lab/spring ──────────────────────── */`
- [Balance.tsx:18](../upstream-free/blocks/pull/Balance.tsx#L18): `/* ── one spring, for everything that settles ───────────────`
- [Balance.tsx:33](../upstream-free/blocks/pull/Balance.tsx#L33): `a second and the damping is RAISED to it rather than`
- [Balance.tsx:36](../upstream-free/blocks/pull/Balance.tsx#L36): `version that makes a spring behave differently on a busy`
- [Balance.tsx:44](../upstream-free/blocks/pull/Balance.tsx#L44): `/* 0..100 into the two numbers a spring actually has.`
- [Balance.tsx:55](../upstream-free/blocks/pull/Balance.tsx#L55): `/* The pair is chosen by DAMPING RATIO and then written back`
- [Balance.tsx:56](../upstream-free/blocks/pull/Balance.tsx#L56): `as stiffness and decay, because the ratio is the thing a`
- [Balance.tsx:62](../upstream-free/blocks/pull/Balance.tsx#L62): `The first version of this ran 0.06..0.26 stiffness against`
- [Balance.tsx:77](../upstream-free/blocks/pull/Balance.tsx#L77): `/* stiffness: how hard it is pulled toward the target */`
- [Balance.tsx:83](../upstream-free/blocks/pull/Balance.tsx#L83): `/* Units matter. The snap threshold is absolute, so a caller`
- [Balance.tsx:84](../upstream-free/blocks/pull/Balance.tsx#L84): `works in pixels or in 0..100 — a spring driven over 0..1`
- [Balance.tsx:156](../upstream-free/blocks/pull/Balance.tsx#L156): `our own filter needs, since text under an alpha threshold`
- [Balance.tsx:231](../upstream-free/blocks/pull/Balance.tsx#L231): `at a DISTANCE, not on release. Crossing the threshold is`
- [Balance.tsx:246](../upstream-free/blocks/pull/Balance.tsx#L246): `crossing the threshold is the moment they touch and fuse`
- [Balance.tsx:444](../upstream-free/blocks/pull/Balance.tsx#L444): `much at rest and the bounce spends it. Twelve is enough to`
- [Balance.tsx:470](../upstream-free/blocks/pull/Balance.tsx#L470): `bends near the top: 68 at the 80px threshold, and 104 at a`
- [Balance.tsx:483](../upstream-free/blocks/pull/Balance.tsx#L483): `threshold = 58,`
- [Balance.tsx:493](../upstream-free/blocks/pull/Balance.tsx#L493): `threshold?: number;`
- [Balance.tsx:535](../upstream-free/blocks/pull/Balance.tsx#L535): `/* Rubber, not a rail. A linear pull reaches the threshold at`
- [Balance.tsx:536](../upstream-free/blocks/pull/Balance.tsx#L536): `exactly the threshold and tells you nothing on the way;`
- [Balance.tsx:542](../upstream-free/blocks/pull/Balance.tsx#L542): `the threshold's ceiling or the top of the Resistance range`
- [Balance.tsx:547](../upstream-free/blocks/pull/Balance.tsx#L547): `const target = phase === "work" ? threshold : phase === "hold" ? drawn : 0;`
- [Balance.tsx:549](../upstream-free/blocks/pull/Balance.tsx#L549): `The spring is only ever the journey home. */`
- [Balance.tsx:565](../upstream-free/blocks/pull/Balance.tsx#L565): `and that unclamped tail is the bounce. The spring at tune`
- [Balance.tsx:591](../upstream-free/blocks/pull/Balance.tsx#L591): `const p = clamp(at / threshold, 0, 1);`
- [Balance.tsx:752](../upstream-free/blocks/pull/Balance.tsx#L752): `/* the new figure lands WITH the spring back, not before`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
