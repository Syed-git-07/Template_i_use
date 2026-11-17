# intro-disclosure

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/intro-disclosure.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/intro-disclosure.tsx); SHA-256 `d9fe1e666c3af2237fd2e5fe5e8bb6a4027a654a18dc4e3f661ea778c00ba9fa`; 677 lines.

Imports: `react`, `next/image`, `lucide-react`, `motion/react`, `@/lib/utils`, `@/components/ui/aspect-ratio`, `@/components/ui/button`, `@/components/ui/checkbox`, `@/components/ui/dialog`, `@/components/ui/drawer`, `@/components/ui/progress`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| step | Step | False | 101 |
| direction | 1 \| -1 | False | 101 |
| step | Step | False | 172 |
| isActive | boolean | False | 173 |
| onClick | () => void | False | 174 |
| isCompleted | boolean | False | 175 |
| title | string | False | 207 |
| short_description | string | False | 208 |
| full_description | string | False | 209 |
| action | {     label: string     onClick?: () => void     href?: string   } | True | 210 |
| label | string | False | 211 |
| onClick | () => void | True | 212 |
| href | string | True | 213 |
| media | {     type: "image" \| "video"     src: string     alt?: string   } | True | 215 |
| type | "image" \| "video" | False | 216 |
| src | string | False | 217 |
| alt | string | True | 218 |
| steps | Step[] | False | 223 |
| featureId | string | False | 224 |
| onComplete | () => void | True | 225 |
| onSkip | () => void | True | 226 |
| showProgressBar | boolean | True | 227 |
| open | boolean | False | 228 |
| setOpen | (open: boolean) => void | False | 229 |
| forceVariant | "mobile" \| "desktop" | True | 230 |
| steps | Step[] | False | 234 |
| currentStep | number | False | 235 |
| onSkip | () => void | False | 236 |
| onNext | () => void | False | 237 |
| onPrevious | () => void | False | 238 |
| hideFeature | () => void | False | 239 |
| completedSteps | number[] | False | 240 |
| onStepSelect | (index: number) => void | False | 241 |
| direction | 1 \| -1 | False | 242 |
| isDesktop | boolean | False | 243 |
| stepRef | React.RefObject<HTMLButtonElement \| null> | False | 258 |

### Defaults and motion

- Default `showProgressBar` = `true` (line 409).
- `duration`: 0.2 (line 85).
- `ease`: computed; inspect expression (line 85).
- `duration`: 0.3 (line 92).
- `ease`: computed; inspect expression (line 92).
- `duration`: 0.2 (line 98).
- `delay`: 0.2 (line 108).
- `duration`: 0.3 (line 108).
- `duration`: 0.5 (line 296).
- `ease`: computed; inspect expression (line 296).

### Input, style and lifecycle

Events: change (line 39); onClick (line 182); onClick (line 282); onClick (line 304); onClick (line 351); onClick (line 359); onClick (line 368); onCheckedChange (line 387); onOpenChange (line 501); onKeyDown (line 504); onSkip (line 523); onNext (line 524); onPrevious (line 525); onStepSelect (line 528); onOpenChange (line 548); onDragEnd (line 553); onKeyDown (line 554); onClick (line 576); onClick (line 610); onClick (line 626); onClick (line 634); onClick (line 643); onCheckedChange (line 657).

Typography/style anchors: 85, 92, 98, 108.

Source signals: keyboard, focus, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
