# Voice note

Public reference: https://bencho.dev/blocks/voice-note

[Original API and usage guide](../upstream-free/blocks/voice-note/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [VoiceNote.css](../upstream-free/blocks/voice-note/VoiceNote.css): 195 lines; SHA-256 `bd7892aa097d2c77c9b8d6b41199366497efa41674e28ffb8ccb356ada5d0308`.
- [VoiceNote.tsx](../upstream-free/blocks/voice-note/VoiceNote.tsx): 411 lines; SHA-256 `1cb25d99b8c8da18203a3d990758d48d25c3f628dabf634a6e9470bcb00bd0e0`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [VoiceNote.css:27](../upstream-free/blocks/voice-note/VoiceNote.css#L27): `/* y1 past 1 is the overshoot; Bounce sets it */`
- [VoiceNote.css:28](../upstream-free/blocks/voice-note/VoiceNote.css#L28): `transition:`
- [VoiceNote.css:47](../upstream-free/blocks/voice-note/VoiceNote.css#L47): `animation: vn-in 240ms ease 80ms both;}`
- [VoiceNote.css:68](../upstream-free/blocks/voice-note/VoiceNote.css#L68): `animation: vn-blink 1s ease-in-out infinite;}`
- [VoiceNote.css:85](../upstream-free/blocks/voice-note/VoiceNote.css#L85): `transition: height 160ms linear;}`
- [VoiceNote.css:94](../upstream-free/blocks/voice-note/VoiceNote.css#L94): `transition: none;`
- [VoiceNote.css:103](../upstream-free/blocks/voice-note/VoiceNote.css#L103): `transition: scale 220ms ease, opacity 220ms ease;}`
- [VoiceNote.css:107](../upstream-free/blocks/voice-note/VoiceNote.css#L107): `.vn[data-phase="cancel"] button { opacity: 0; transition: opacity 160ms ease; }`
- [VoiceNote.css:118](../upstream-free/blocks/voice-note/VoiceNote.css#L118): `transition: scale 160ms cubic-bezier(0.22, 1, 0.36, 1), color 160ms ease;}`
- [VoiceNote.css:153](../upstream-free/blocks/voice-note/VoiceNote.css#L153): `transition: opacity 220ms ease;`
- [VoiceNote.css:182](../upstream-free/blocks/voice-note/VoiceNote.css#L182): `transition: opacity 160ms ease, scale 160ms ease;}`
- [VoiceNote.css:187](../upstream-free/blocks/voice-note/VoiceNote.css#L187): `transition: opacity 160ms ease, scale 420ms cubic-bezier(0.24, 1.34, 0.38, 1);}`
- [VoiceNote.css:189](../upstream-free/blocks/voice-note/VoiceNote.css#L189): `.vn[data-phase="cancel"] .vn-cancel { opacity: 0; scale: 0.6; transition: opacity 220ms ease, scale 220ms ease; }`
- [VoiceNote.tsx:116](../upstream-free/blocks/voice-note/VoiceNote.tsx#L116): `bounce = 40,`
- [VoiceNote.tsx:121](../upstream-free/blocks/voice-note/VoiceNote.tsx#L121): `bounce?: number;`
- [VoiceNote.tsx:300](../upstream-free/blocks/voice-note/VoiceNote.tsx#L300): `"--ov": (1 + (clamp(bounce, 0, 100) / 100) * 0.7).toFixed(3),`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
