# Like

Public reference: https://bencho.dev/blocks/like

[Original API and usage guide](../upstream-free/blocks/like/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Like.css](../upstream-free/blocks/like/Like.css): 172 lines; SHA-256 `c994dd4e5b9f605bd5dd13692a6f2254bff2223d70c11ef03a8bd05ad3001290`.
- [Like.tsx](../upstream-free/blocks/like/Like.tsx): 174 lines; SHA-256 `2e082704093525e214a87775905df7eacb5a077a23863c78a2a014e5e53f3960`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Like.css:25](../upstream-free/blocks/like/Like.css#L25): `transition: scale 220ms cubic-bezier(0.22, 1, 0.36, 1);`
- [Like.tsx:53](../upstream-free/blocks/like/Like.tsx#L53): `transition={{ duration: 0.42, ease: [0.22, 1, 0.36, 1], delay: place * 0.04 }}`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
