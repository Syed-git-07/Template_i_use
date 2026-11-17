# Stepper

Category: Components. Public entry: [Stepper](https://reactbits.dev/components/stepper).

Source pinned to `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`. Full implementation stays in the excluded local snapshot; links below open the original source.

## Variants

- [content](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx)
- [tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tailwind/Components/Stepper/Stepper.jsx)
- [ts-default](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-default/Components/Stepper/Stepper.tsx)
- [ts-tailwind](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/ts-tailwind/Components/Stepper/Stepper.tsx)

## API facts

| Prop | Type | Documented default | Source scalar default |
| --- | --- | --- | --- |
| children | ReactNode | - | — |
| Step title | ReactNode | - | — |
| Step description | ReactNode | - | — |
| Step icon | ReactNode | - | — |
| step | number | - | — |
| initialStep | number | 1 | 1 |
| onStepChange | (step: number) => void | () => {} | — |
| onFinalStepCompleted | () => void | () => {} | — |
| indicator | 'numbers' \| 'dots' \| 'bars' | 'numbers' | numbers |
| orientation | 'horizontal' \| 'vertical' | 'horizontal' | horizontal |
| transition | 'slide' \| 'fade' \| 'none' | 'slide' | slide |
| linear | boolean | false | false |
| disableStepIndicators | boolean | false | false |
| renderStepIndicator | ({ step, currentStep, onStepClick }) => ReactNode | - | — |
| showFooter | boolean | true | true |
| backButtonText | string | 'Back' | Back |
| nextButtonText | string | 'Continue' | Continue |
| completeButtonText | string | 'Complete' | Complete |
| backButtonProps | ButtonHTMLAttributes | {} | — |
| nextButtonProps | ButtonHTMLAttributes | {} | — |
| completedContent | ReactNode | - | — |
| theme | 'dark' \| 'light' | 'dark' | dark |
| accentColor | string | - | — |
| frame | boolean | true | true |
| radius | number | 24 | 24 |
| width | number \| string | 440 | 440 |
| className | string | '' |  |
| stepContainerClassName | string | '' |  |
| contentClassName | string | '' |  |
| footerClassName | string | '' |  |
| style | CSSProperties | - | — |

Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.

Dependencies: react, @hugeicons/react, @hugeicons/core-free-icons

## Interaction locations

- [onClick, line 337](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L337)
- [onClick, line 361](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L361)
- [onClick, line 416](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L416)
- [onClick, line 475](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L475)
- [onClick, line 488](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L488)

## Motion locations

- [duration, line 92](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L92): 360
- [duration, line 249](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L249): computed; read the linked expression
- [duration, line 258](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L258): 560
- [duration, line 263](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L263): 420
- [duration, line 269](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L269): 140
- [duration, line 275](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.jsx#L275): 200

[Stylesheet](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/content/Components/Stepper/Stepper.css); motion-related lines: 86, 106, 145, 202, 247, 293, 334, 353, 421, 424, 428.

## Observed source structure

Literal state assignments: none captured by the structural index.

Signals present: reduced_motion, resize.

These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.
