# wizard-expandable

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/wizard-expandable.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/wizard-expandable.tsx); SHA-256 `7c6cd7c2dc0fbe6058af886557d8f081b41773949f14f810cc8fe819a1284059`; 1226 lines.

Imports: `react`, `@base-ui/react/scroll-area`, `@radix-ui/react-use-controllable-state`, `motion/react`, `@/lib/utils`, `@/components/ui/badge`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 53 |
| title | string | False | 54 |
| description | string | False | 55 |
| icon | \| React.ComponentType<{ className?: string }>     \| React.ReactElement<{ className?: string }> | False | 56 |
| className | string | True | 57 |
| className | string | True | 58 |
| content | React.ReactNode | False | 59 |
| fromStepId | string \| null | False | 63 |
| toStepId | string | False | 64 |
| fromIndex | number | False | 65 |
| toIndex | number | False | 66 |
| ok | true | False | 70 |
| ok | false | False | 71 |
| context | WizardNavigateContext | False | 71 |
| steps | WizardStep[] | False | 80 |
| fromId | string \| null | False | 81 |
| toId | string | False | 82 |
| canNavigateToStep | ((context: WizardNavigateContext) => boolean) \| undefined | False | 83 |
| skipValidationForBackward | boolean | False | 84 |
| activeStepId | string \| null | False | 120 |
| activeIndex | number | False | 121 |
| totalSteps | number | False | 122 |
| isLastStep | boolean | False | 123 |
| canGoBack | boolean | False | 124 |
| canGoNext | boolean | False | 126 |
| goNext | () => void | False | 127 |
| goBack | () => void | False | 128 |
| complete | () => void | False | 129 |
| steps | WizardStep[] | False | 144 |
| badgeText | string | True | 145 |
| className | string | True | 147 |
| expanded | boolean | True | 148 |
| onExpandedChange | (expanded: boolean) => void | True | 149 |
| activeStep | string \| null | True | 150 |
| onActiveStepChange | (stepId: string \| null) => void | True | 151 |
| canNavigateToStep | (context: WizardNavigateContext) => boolean | True | 158 |
| skipValidationForBackward | boolean | True | 163 |
| onNavigateBlocked | (context: WizardNavigateContext) => void | True | 165 |
| canGoNext | boolean | True | 171 |
| showNavigation | boolean | True | 173 |
| backLabel | string | True | 174 |
| nextLabel | string | True | 175 |
| completeLabel | string | True | 176 |
| onComplete | () => void | True | 178 |
| left | number | False | 824 |
| top | number | False | 825 |
| width | number | False | 826 |
| height | number | False | 827 |
| top | boolean | False | 972 |
| bottom | boolean | False | 973 |
| left | boolean | False | 974 |
| right | boolean | False | 975 |
| viewportClassName | string | True | 981 |
| maskHeight | number | True | 987 |
| maskClassName | string | True | 988 |
| showMask | ScrollFadeMask | False | 1172 |
| maskHeight | number | False | 1173 |

### Defaults and motion

- Default `skipValidationForBackward` = `true` (line 192).
- Default `showNavigation` = `true` (line 195).
- Default `backLabel` = `"Back"` (line 196).
- Default `nextLabel` = `"Next"` (line 197).
- Default `completeLabel` = `"Finish"` (line 198).
- Default `maskHeight` = `30` (line 997).
- Default `orientation` = `"vertical"` (line 1130).
- `bounce`: 0 (line 42).
- `duration`: 0.25 (line 43).
- `duration`: 0.01 (line 233).
- `duration`: computed; inspect expression (line 511).
- `ease`: computed; inspect expression (line 512).
- `duration`: 0.1 (line 518).
- `ease`: computed; inspect expression (line 518).
- `duration`: 0.16 (line 524).
- `ease`: computed; inspect expression (line 524).

### Input, style and lifecycle

Events: keydown (line 434); onClick (line 565); onClick (line 575); onClick (line 584); onClick (line 751); onKeyDown (line 752); onMouseEnter (line 753); onMouseLeave (line 754); mousedown (line 912); touchstart (line 913); change (line 955); pointerdown (line 956); scroll (line 1050); resize (line 1051).

Typography/style anchors: 492, 498, 510, 518, 524, 673, 798.

Source signals: reduced_motion, keyboard, focus, cleanup, resize, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
