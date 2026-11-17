# CurvedInput

Category: Components. Public entry: [CurvedInput](https://reactbits.dev/components/curved-input).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/CurvedInput/CurvedInput.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/CurvedInput/CurvedInput.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/CurvedInput/CurvedInput.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| value | string | undefined | — |
| defaultValue | string | "" |  |
| onChange | (value) => void | - | — |
| onSubmit | (value) => void | - | — |
| placeholder | string | "Enter your email" | Enter your email |
| buttonText | string | "Get Started" | Get Started |
| type | string | "email" | email |
| name | string | undefined | — |
| ariaLabel | string | undefined | — |
| theme | "dark" \| "light" | "dark" | dark |
| width | number \| string | 450 | 450 |
| bend | number | 28 | 28 |
| height | number | 64 | 64 |
| cornerRadius | number | 18 | 18 |
| borderWidth | number | 1.5 | 1.5 |
| fontSize | number | 16 | 16 |
| backgroundColor | string | undefined | — |
| textColor | string | undefined | — |
| placeholderColor | string | undefined | — |
| borderColor | string | undefined | — |
| buttonColor | string | undefined | — |
| buttonTextColor | string | undefined | — |
| iconColor | string | undefined | — |
| shadowSize | "none" \| "sm" \| "md" \| "lg" | "md" | md |
| shadowColor | string | undefined | — |
| showButton | boolean | true | true |
| showIcon | boolean | true | true |
| icon | React.ReactNode | undefined | — |
| className | string | "" |  |
| style | React.CSSProperties | undefined | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react

## Interaction locations

- [onPointerDown, line 371](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L371)
- [onClick, line 372](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L372)
- [onClick, line 441](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L441)
- [onPointerDown, line 445](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L445)
- [onKeyDown, line 446](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L446)
- [onSubmit, line 486](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L486)
- [onChange, line 497](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L497)
- [onSelect, line 498](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L498)
- [onKeyUp, line 499](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L499)
- [onFocus, line 500](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L500)
- [onBlur, line 501](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.jsx#L501)

## Motion locations


[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/CurvedInput/CurvedInput.css); motion-related lines: 26, 39.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: keyboard, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
