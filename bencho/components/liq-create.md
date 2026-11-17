# Create menu

Public reference: https://bencho.dev/blocks/liq-create

[Original API and usage guide](../upstream-free/blocks/liq-create/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Create.css](../upstream-free/blocks/liq-create/Create.css): 286 lines; SHA-256 `5349b1b25ebb74f65baba0a45ee62b2a26489733a5255da4ac60296e91991058`.
- [Create.tsx](../upstream-free/blocks/liq-create/Create.tsx): 302 lines; SHA-256 `cf19467dd4f58521d0126f39b6fb154d7500660fa7533ef140e3203d8f887a84`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Create.css:102](../upstream-free/blocks/liq-create/Create.css#L102): `And no overshoot. A spring past the target takes the`
- [Create.css:104](../upstream-free/blocks/liq-create/Create.css#L104): `came back, which is a wobble, not a bounce. This curve is`
- [Create.css:110](../upstream-free/blocks/liq-create/Create.css#L110): `transition: scale 420ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Create.css:122](../upstream-free/blocks/liq-create/Create.css#L122): `transition: scale 160ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Create.css:126](../upstream-free/blocks/liq-create/Create.css#L126): `transition: scale 220ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Create.css:172](../upstream-free/blocks/liq-create/Create.css#L172): `transition:`
- [Create.css:174](../upstream-free/blocks/liq-create/Create.css#L174): `opacity 160ms ease,`
- [Create.css:181](../upstream-free/blocks/liq-create/Create.css#L181): `transition: opacity 160ms ease;}`
- [Create.css:196](../upstream-free/blocks/liq-create/Create.css#L196): `transition: width 420ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Create.css:226](../upstream-free/blocks/liq-create/Create.css#L226): `transition: opacity 160ms ease, transform 220ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [Create.css:250](../upstream-free/blocks/liq-create/Create.css#L250): `transition: color 220ms ease;`
- [Create.css:267](../upstream-free/blocks/liq-create/Create.css#L267): `transition: opacity 220ms ease;`
- [Create.css:271](../upstream-free/blocks/liq-create/Create.css#L271): `.crt-item button:hover::before { opacity: 1; transition-duration: 160ms; }`
- [Create.css:280](../upstream-free/blocks/liq-create/Create.css#L280): `.crt-body, .crt-pill, .crt-item, .crt-say { transition-duration: 160ms; }`
- [Create.tsx:22](../upstream-free/blocks/liq-create/Create.tsx#L22): `be eaten by the same threshold. */`
- [Create.tsx:26](../upstream-free/blocks/liq-create/Create.tsx#L26): `Shared parts for the Framer Motion layer: one spring, one`
- [Create.tsx:48](../upstream-free/blocks/liq-create/Create.tsx#L48): `bounce, not a wobble. */`
- [Create.tsx:50](../upstream-free/blocks/liq-create/Create.tsx#L50): `type: "spring" as const,`
- [Create.tsx:51](../upstream-free/blocks/liq-create/Create.tsx#L51): `stiffness: 220,`
- [Create.tsx:52](../upstream-free/blocks/liq-create/Create.tsx#L52): `damping: 14,`
- [Create.tsx:53](../upstream-free/blocks/liq-create/Create.tsx#L53): `mass: 0.5,`
- [Create.tsx:57](../upstream-free/blocks/liq-create/Create.tsx#L57): `so a toggle does not bounce like a dragged card. */`
- [Create.tsx:59](../upstream-free/blocks/liq-create/Create.tsx#L59): `For shapes whose corner radius is animating: a spring that`
- [Create.tsx:62](../upstream-free/blocks/liq-create/Create.tsx#L62): `as a bounce.`
- [Create.tsx:64](../upstream-free/blocks/liq-create/Create.tsx#L64): `NOT just LIQUID with more damping, which is what this was.`
- [Create.tsx:65](../upstream-free/blocks/liq-create/Create.tsx#L65): `Raising damping alone to 30 against the same stiffness put`
- [Create.tsx:70](../upstream-free/blocks/liq-create/Create.tsx#L70): `Stiffness comes up with the damping instead, which holds ζ`
- [Create.tsx:72](../upstream-free/blocks/liq-create/Create.tsx#L72): `const LIQUID_STILL = { ...LIQUID, stiffness: 420, damping: 30 };`
- [Create.tsx:243](../upstream-free/blocks/liq-create/Create.tsx#L243): `{/* LIQUID_STILL, not LIQUID. A spring past the target`
- [Create.tsx:246](../upstream-free/blocks/liq-create/Create.tsx#L246): `bounce. This is the one shape here that must not`
- [Create.tsx:263](../upstream-free/blocks/liq-create/Create.tsx#L263): `transition={LIQUID_STILL}`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
