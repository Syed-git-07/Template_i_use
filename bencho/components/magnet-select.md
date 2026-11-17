# Magnetic select

Public reference: https://bencho.dev/blocks/magnet-select

[Original API and usage guide](../upstream-free/blocks/magnet-select/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [MagneticSelect.css](../upstream-free/blocks/magnet-select/MagneticSelect.css): 142 lines; SHA-256 `1930c4b570863750aa2b1848cb475032aaf450601f95f08dafcc16e0164567d9`.
- [MagneticSelect.tsx](../upstream-free/blocks/magnet-select/MagneticSelect.tsx): 534 lines; SHA-256 `e6af6fe24deb918bf79ef5aea8365d63ce7caded24492c09e9994ed33fb139f1`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [MagneticSelect.css:8](../upstream-free/blocks/magnet-select/MagneticSelect.css#L8): `folded into it, so a rule here and a spring there do not`
- [MagneticSelect.css:10](../upstream-free/blocks/magnet-select/MagneticSelect.css#L10): `may set or transition a transform on .mag-chip, and the`
- [MagneticSelect.css:12](../upstream-free/blocks/magnet-select/MagneticSelect.css#L12): `a 'transition: all' would sweep the transform up with the`
- [MagneticSelect.css:63](../upstream-free/blocks/magnet-select/MagneticSelect.css#L63): `Deliberately not a spring. The field springs; this does`
- [MagneticSelect.css:71](../upstream-free/blocks/magnet-select/MagneticSelect.css#L71): `as damping rather than as tracking. Same curve and same`
- [MagneticSelect.css:72](../upstream-free/blocks/magnet-select/MagneticSelect.css#L72): `duration as the search field, because it is the same`
- [MagneticSelect.css:75](../upstream-free/blocks/magnet-select/MagneticSelect.css#L75): `transition:`
- [MagneticSelect.css:77](../upstream-free/blocks/magnet-select/MagneticSelect.css#L77): `background-color 220ms ease,`
- [MagneticSelect.css:78](../upstream-free/blocks/magnet-select/MagneticSelect.css#L78): `color 220ms ease;}`
- [MagneticSelect.css:117](../upstream-free/blocks/magnet-select/MagneticSelect.css#L117): `transition: opacity 220ms ease;}`
- [MagneticSelect.css:141](../upstream-free/blocks/magnet-select/MagneticSelect.css#L141): `.mag-skin { transition-duration: 160ms; }`
- [MagneticSelect.tsx:4](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L4): `/* ── inlined from lab/spring ──────────────────────── */`
- [MagneticSelect.tsx:5](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L5): `/* ── one spring, for everything that settles ───────────────`
- [MagneticSelect.tsx:20](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L20): `a second and the damping is RAISED to it rather than`
- [MagneticSelect.tsx:23](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L23): `version that makes a spring behave differently on a busy`
- [MagneticSelect.tsx:185](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L185): `bounce = 55,`
- [MagneticSelect.tsx:191](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L191): `bounce?: number;`
- [MagneticSelect.tsx:233](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L233): `the magnet takes the mass as well as the space, and the`
- [MagneticSelect.tsx:304](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L304): `Bounce is a DAMPING RATIO, not a damping value: tie it to`
- [MagneticSelect.tsx:307](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L307): `different stiffness. As a ratio it means the same thing`
- [MagneticSelect.tsx:309](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L309): `rings — and stiffness is then free to vary. */`
- [MagneticSelect.tsx:310](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L310): `const zeta = 0.9 - 0.48 * (clamp(bounce, 0, 100) / 100);`
- [MagneticSelect.tsx:311](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L311): `const swing = (k: number, mass: number) => ({`
- [MagneticSelect.tsx:312](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L312): `type: "spring" as const,`
- [MagneticSelect.tsx:313](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L313): `stiffness: k,`
- [MagneticSelect.tsx:314](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L314): `damping: 2 * Math.sqrt(k * mass) * zeta,`
- [MagneticSelect.tsx:315](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L315): `mass,`
- [MagneticSelect.tsx:476](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L476): `the same squash at every Bounce setting and`
- [MagneticSelect.tsx:477](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L477): `this one is not there at all when the spring`
- [MagneticSelect.tsx:488](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L488): `transition={{`
- [MagneticSelect.tsx:494](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L494): `x: { ...swing(k, 0.9), delay: wait },`
- [MagneticSelect.tsx:495](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L495): `y: { ...swing(k, 0.9), delay: wait },`
- [MagneticSelect.tsx:496](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L496): `scaleX: { ...swing(k * 1.24, 0.8), delay: wait },`
- [MagneticSelect.tsx:497](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L497): `scaleY: { ...swing(k * 0.86, 0.95), delay: wait },`
- [MagneticSelect.tsx:498](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L498): `rotate: { ...swing(k * 0.8, 1), delay: wait },`
- [MagneticSelect.tsx:506](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L506): `here and a spring there fight every frame. Two`
- [MagneticSelect.tsx:509](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L509): `since the spring that moves the field would`
- [MagneticSelect.tsx:514](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L514): `shove, the swell and the tilt, all on one spring`
- [MagneticSelect.tsx:515](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L515): `with a delay on it. A cursor-follow on that`
- [MagneticSelect.tsx:516](../upstream-free/blocks/magnet-select/MagneticSelect.tsx#L516): `spring would arrive late and keep arriving after`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
