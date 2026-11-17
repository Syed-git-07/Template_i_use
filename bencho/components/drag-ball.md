# Dragging ball

Public reference: https://bencho.dev/blocks/drag-ball

[Original API and usage guide](../upstream-free/blocks/drag-ball/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Ball.css](../upstream-free/blocks/drag-ball/Ball.css): 36 lines; SHA-256 `2ad98f927f967695b9abc2f2e1db7bd02c4aeb3b3b9550eefbbc220b78a4950b`.
- [Ball.tsx](../upstream-free/blocks/drag-ball/Ball.tsx): 309 lines; SHA-256 `67f3d2ef79ceab034a51ae9c11ba05899a704164fe522d78ca0fc884b29163e8`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Ball.tsx:14](../upstream-free/blocks/drag-ball/Ball.tsx#L14): `straggler, with the drag standing in for the spring: there`
- [Ball.tsx:43](../upstream-free/blocks/drag-ball/Ball.tsx#L43): `our own filter needs, since text under an alpha threshold`
- [Ball.tsx:114](../upstream-free/blocks/drag-ball/Ball.tsx#L114): `let go  it rounds back out on a spring`
- [Ball.tsx:244](../upstream-free/blocks/drag-ball/Ball.tsx#L244): `dead ease, and springiness is what decides how`
- [Ball.tsx:271](../upstream-free/blocks/drag-ball/Ball.tsx#L271): `dragElastic={0.14}`
- [Ball.tsx:272](../upstream-free/blocks/drag-ball/Ball.tsx#L272): `dragMomentum={false}`
- [Ball.tsx:281](../upstream-free/blocks/drag-ball/Ball.tsx#L281): `A spring rather than an ease: a squeeze that`
- [Ball.tsx:287](../upstream-free/blocks/drag-ball/Ball.tsx#L287): `transition={{ type: "spring", stiffness: 500, damping: 18, mass: 0.6 }}`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
