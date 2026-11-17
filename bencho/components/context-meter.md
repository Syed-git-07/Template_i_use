# Context meter

Public reference: https://bencho.dev/blocks/context-meter

[Original API and usage guide](../upstream-free/blocks/context-meter/README.md). The upstream files remain unchanged and retain their MIT notices.

## Implementation and formation

- [ContextMeter.css](../upstream-free/blocks/context-meter/ContextMeter.css): 242 lines; SHA-256 `b351f07fb2889388c9375ca8e22743ffc816fb36990c4adebe9eb23433848a10`.
- [ContextMeter.tsx](../upstream-free/blocks/context-meter/ContextMeter.tsx): 266 lines; SHA-256 `063ea2137c634677fc379f02a4944c048edb0b13ab29eabce39e25163f6e0451`.

## Motion and transition locations

These search anchors include comments and computed formulas; read the surrounding implementation. They are not independent runtime measurements.

- [ContextMeter.css:61](../upstream-free/blocks/context-meter/ContextMeter.css#L61): `transition: background-color 260ms ease, opacity 220ms ease, scale 260ms cubic-bezier(0.22, 1, 0.36, 1);}`
- [ContextMeter.css:76](../upstream-free/blocks/context-meter/ContextMeter.css#L76): `animation-delay: inherit;}`
- [ContextMeter.css:82](../upstream-free/blocks/context-meter/ContextMeter.css#L82): `.ctx-dot[data-swap="drain"]::after { background: var(--was); animation-name: ctx-shrink; animation-timing-function: cubic-bezier(0.55, 0, 0.75, 0.4); animation-duration: 240ms; }`
- [ContextMeter.css:110](../upstream-free/blocks/context-meter/ContextMeter.css#L110): `left as a faint tail; widths ease, so Compact slides the chat down */`
- [ContextMeter.css:118](../upstream-free/blocks/context-meter/ContextMeter.css#L118): `/* the width is a real flex-grow transition, so the corners stay`
- [ContextMeter.css:120](../upstream-free/blocks/context-meter/ContextMeter.css#L120): `transition:`
- [ContextMeter.css:122](../upstream-free/blocks/context-meter/ContextMeter.css#L122): `opacity 220ms ease;}`
- [ContextMeter.css:131](../upstream-free/blocks/context-meter/ContextMeter.css#L131): `.ctx-seg { transition-duration: 1ms; }`
- [ContextMeter.css:172](../upstream-free/blocks/context-meter/ContextMeter.css#L172): `transition: background-color 160ms ease, scale 260ms cubic-bezier(0.34, 1.56, 0.64, 1);}`
- [ContextMeter.css:206](../upstream-free/blocks/context-meter/ContextMeter.css#L206): `transition: scale 240ms cubic-bezier(0.22, 1, 0.36, 1), background-color 220ms ease, color 220ms ease;}`
- [ContextMeter.css:225](../upstream-free/blocks/context-meter/ContextMeter.css#L225): `.ctx-dot { transition-duration: 1ms; transition-delay: 0ms !important; }`
- [ContextMeter.tsx:16](../upstream-free/blocks/context-meter/ContextMeter.tsx#L16): `belongs to, and the colour change is the animation. A delay that`
- [ContextMeter.tsx:65](../upstream-free/blocks/context-meter/ContextMeter.tsx#L65): `exit={{ opacity: 0, filter: "blur(2px)", transition: { duration: 0.16 } }}`
- [ContextMeter.tsx:66](../upstream-free/blocks/context-meter/ContextMeter.tsx#L66): `transition={{ duration: 0.5, ease: [0.34, 1.45, 0.64, 1], delay: i * 0.07 }}`
- [ContextMeter.tsx:105](../upstream-free/blocks/context-meter/ContextMeter.tsx#L105): `const DELAY = OWNERS[0].map((o, i) => (o !== OWNERS[1][i] ? 1 + Math.round(((i - FIRST) / (LAST - FIRST || 1)) * RIPPLE) : 0));`
- [ContextMeter.tsx:232](../upstream-free/blocks/context-meter/ContextMeter.tsx#L232): `key={moved && DELAY[i] ? '${i}${compact ? "+" : "-"}' : i}`
- [ContextMeter.tsx:235](../upstream-free/blocks/context-meter/ContextMeter.tsx#L235): `data-swap={moved && DELAY[i] ? (o === null ? "drain" : "fill") : undefined}`
- [ContextMeter.tsx:237](../upstream-free/blocks/context-meter/ContextMeter.tsx#L237): `style={DELAY[i] ? ({`
- [ContextMeter.tsx:238](../upstream-free/blocks/context-meter/ContextMeter.tsx#L238): `transitionDelay: '${DELAY[i]}ms',`
- [ContextMeter.tsx:239](../upstream-free/blocks/context-meter/ContextMeter.tsx#L239): `animationDelay: '${DELAY[i]}ms',`

## Verification

[Coverage](../COVERAGE.md) distinguishes public previews, guided replay samples and directly exercised gestures. Source availability does not establish touch, accessibility or production-service correctness.
