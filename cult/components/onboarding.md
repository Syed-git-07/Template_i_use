# onboarding

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/onboarding.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/onboarding.tsx); SHA-256 `1a9cd5c7b56a138f392595e68638e7db5a9afab693ce1224e873675eba047645`; 886 lines.

Imports: `react`, `react`, `@radix-ui/react-use-controllable-state`, `class-variance-authority`, `@/lib/utils`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| currentStep | number | False | 49 |
| totalSteps | number | False | 51 |
| dotClassName | string | True | 53 |
| currentStep | number | False | 110 |
| totalSteps | number | False | 112 |
| stepValue | number | False | 114 |
| setStep | (step: number \| ((prev: number) => number)) => void | False | 116 |
| setStepValue | (value: number \| ((prev: number) => number)) => void | False | 118 |
| maxStepValue | number | False | 120 |
| canGoNext | boolean | False | 122 |
| canGoBack | boolean | False | 124 |
| handleBack | () => void | False | 126 |
| handleNext | () => void | False | 128 |
| handleComplete | () => void | False | 130 |
| onComplete | () => void | True | 132 |
| value | number | True | 157 |
| defaultValue | number | True | 159 |
| onValueChange | (step: number) => void | True | 161 |
| stepValue | number | True | 163 |
| defaultStepValue | number | True | 165 |
| onStepValueChange | (value: number) => void | True | 167 |
| totalSteps | number | False | 169 |
| maxStepValue | number | True | 171 |
| onComplete | () => void | True | 173 |
| canGoNext | (step: number, stepValue: number) => boolean | True | 175 |
| step | number | False | 297 |
| title | string | True | 353 |
| description | string | True | 355 |
| children | React.ReactNode | True | 357 |
| backLabel | string | True | 403 |
| nextLabel | string | True | 405 |
| completeLabel | string | True | 407 |
| canGoNext | boolean | True | 409 |
| children | React.ReactNode | True | 411 |
| value | string \| null | False | 496 |
| setValue | (value: string) => void | False | 497 |
| name | string | False | 498 |
| orientation | Orientation | False | 499 |
| value | string \| null | True | 523 |
| defaultValue | string \| null | True | 525 |
| onValueChange | (value: string) => void | True | 527 |
| name | string | False | 529 |
| orientation | Orientation | True | 531 |
| value | string | False | 590 |
| value | number | False | 646 |
| setValue | (value: number \| ((prev: number) => number)) => void | False | 647 |
| totalItems | number | False | 648 |
| isActive | (index: number) => boolean | False | 649 |
| value | number | True | 674 |
| defaultValue | number | True | 676 |
| onValueChange | (index: number) => void | True | 678 |
| totalItems | number | True | 680 |
| index | number | False | 734 |
| title | string | True | 805 |
| number | number | True | 840 |

### Defaults and motion

- Default `variant` = `"dots"` (line 64).
- Default `defaultValue` = `1` (line 180).
- Default `defaultStepValue` = `0` (line 183).
- Default `controlledMaxStepValue` = `0` (line 186).
- Default `backLabel` = `"Back"` (line 415).
- Default `nextLabel` = `"Next"` (line 416).
- Default `completeLabel` = `"Start Creating"` (line 417).
- Default `defaultValue` = `null` (line 536).
- Default `orientation` = `"grid"` (line 539).
- Default `defaultValue` = `0` (line 685).

### Input, style and lifecycle

Events: onClick (line 460); onClick (line 470); onClick (line 480); onChange (line 622); onClick (line 777); onKeyDown (line 778).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
