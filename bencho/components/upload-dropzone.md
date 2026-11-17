# Upload dropzone

Public reference: https://bencho.dev/blocks/upload-dropzone

[Original API and usage guide](../upstream-free/blocks/upload-dropzone/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [Upload.css](../upstream-free/blocks/upload-dropzone/Upload.css): 253 lines; SHA-256 `d5dd6f30f22fcd649cfbb12d4099eb971f5d962077bf1f146b01190254ab9534`.
- [Upload.tsx](../upstream-free/blocks/upload-dropzone/Upload.tsx): 395 lines; SHA-256 `9ea31fc3528cf35ca14e665bbc84b0ae2084d7597bdaa51a17533cb1edce52bf`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [Upload.css:36](../upstream-free/blocks/upload-dropzone/Upload.css#L36): `/* a file over it and it grows, with a bounce; an upload and it`
- [Upload.css:38](../upstream-free/blocks/upload-dropzone/Upload.css#L38): `transition:`
- [Upload.css:42](../upstream-free/blocks/upload-dropzone/Upload.css#L42): `background-color 220ms ease;}`
- [Upload.css:65](../upstream-free/blocks/upload-dropzone/Upload.css#L65): `transition: translate 420ms cubic-bezier(0.24, 1.34, 0.38, 1), background-color 220ms ease, color 220ms ease;}`
- [Upload.css:98](../upstream-free/blocks/upload-dropzone/Upload.css#L98): `animation: upl-land 420ms var(--upl-spring) both;}`
- [Upload.css:146](../upstream-free/blocks/upload-dropzone/Upload.css#L146): `transition: transform 220ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [Upload.css:190](../upstream-free/blocks/upload-dropzone/Upload.css#L190): `/* home is a spring; the Bounce knob sets its overshoot */`
- [Upload.css:191](../upstream-free/blocks/upload-dropzone/Upload.css#L191): `transition: transform 420ms var(--upl-spring), opacity 220ms ease;}`
- [Upload.css:196](../upstream-free/blocks/upload-dropzone/Upload.css#L196): `transition: none;}`
- [Upload.css:198](../upstream-free/blocks/upload-dropzone/Upload.css#L198): `.upl-file[data-gone] { opacity: 0; pointer-events: none; transition: none; }`
- [Upload.css:200](../upstream-free/blocks/upload-dropzone/Upload.css#L200): `.upl-file:not([data-gone]) { animation: upl-back 360ms var(--upl-spring) both; }`
- [Upload.tsx:20](../upstream-free/blocks/upload-dropzone/Upload.tsx#L20): `bounce and the arrow lifts toward the hand. Let go and the`
- [Upload.tsx:31](../upstream-free/blocks/upload-dropzone/Upload.tsx#L31): `/* ── inlined from lab/spring ──────────────────────── */`
- [Upload.tsx:32](../upstream-free/blocks/upload-dropzone/Upload.tsx#L32): `/* ── one spring, for everything that settles ───────────────`
- [Upload.tsx:47](../upstream-free/blocks/upload-dropzone/Upload.tsx#L47): `a second and the damping is RAISED to it rather than`
- [Upload.tsx:50](../upstream-free/blocks/upload-dropzone/Upload.tsx#L50): `version that makes a spring behave differently on a busy`
- [Upload.tsx:128](../upstream-free/blocks/upload-dropzone/Upload.tsx#L128): `bounce = 40,`
- [Upload.tsx:132](../upstream-free/blocks/upload-dropzone/Upload.tsx#L132): `bounce?: number;`
- [Upload.tsx:197](../upstream-free/blocks/upload-dropzone/Upload.tsx#L197): `shake.start({ x: [0, -7, 6, -4, 2, 0], transition: { duration: 0.42 } });`
- [Upload.tsx:258](../upstream-free/blocks/upload-dropzone/Upload.tsx#L258): `From where it was let go to the box's middle, on an ease-IN:`
- [Upload.tsx:278](../upstream-free/blocks/upload-dropzone/Upload.tsx#L278): `el.style.transition = "transform 380ms cubic-bezier(0.55, 0, 0.85, 0.3), opacity 300ms ease-in 80ms";`
- [Upload.tsx:288](../upstream-free/blocks/upload-dropzone/Upload.tsx#L288): `el.style.transition = "none";`
- [Upload.tsx:322](../upstream-free/blocks/upload-dropzone/Upload.tsx#L322): `style={{ "--upl-r": '${r}px', "--upl-spring": 'cubic-bezier(0.3, ${1 + (bounce / 100) * 0.9}, 0.4, 1)' } as React.CSSProperties}`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
