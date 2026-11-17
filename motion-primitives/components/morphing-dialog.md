# morphing-dialog

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/morphing-dialog.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/morphing-dialog.tsx); SHA-256 `b6536d4643d20edd1d667120775ce507f23f97d36b9b91d63bf92546517a2ea6`; 423 lines.

Imports: `react`, `motion/react`, `react-dom`, `@/lib/utils`, `lucide-react`, `@/hooks/useClickOutside`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isOpen | boolean | False | 25 |
| setIsOpen | React.Dispatch<React.SetStateAction<boolean>> | False | 26 |
| uniqueId | string | False | 27 |
| triggerRef | React.RefObject<HTMLButtonElement \| null> | False | 28 |
| children | React.ReactNode | False | 45 |
| transition | Transition | True | 46 |
| children | React.ReactNode | False | 75 |
| transition | Transition | True | 76 |
| children | React.ReactNode | False | 88 |
| className | string | True | 89 |
| style | React.CSSProperties | True | 90 |
| triggerRef | React.RefObject<HTMLButtonElement> | True | 91 |
| children | React.ReactNode | False | 135 |
| className | string | True | 136 |
| style | React.CSSProperties | True | 137 |
| children | React.ReactNode | False | 223 |
| className | string | True | 224 |
| style | React.CSSProperties | True | 225 |
| children | React.ReactNode | False | 261 |
| className | string | True | 262 |
| style | React.CSSProperties | True | 263 |
| children | React.ReactNode | False | 286 |
| className | string | True | 287 |
| style | React.CSSProperties | True | 288 |
| children | React.ReactNode | False | 310 |
| className | string | True | 311 |
| disableLayoutAnimation | boolean | True | 312 |
| variants | {     initial: Variant;     animate: Variant;     exit: Variant;   } | True | 313 |
| initial | Variant | False | 314 |
| animate | Variant | False | 315 |
| exit | Variant | False | 316 |
| src | string | False | 349 |
| alt | string | False | 350 |
| className | string | True | 351 |
| style | React.CSSProperties | True | 352 |
| children | React.ReactNode | True | 375 |
| className | string | True | 376 |
| variants | {     initial: Variant;     animate: Variant;     exit: Variant;   } | True | 377 |
| initial | Variant | False | 378 |
| animate | Variant | False | 379 |
| exit | Variant | False | 380 |

### Defaults and motion


### Input, style and lifecycle

Events: onClick (line 121); onKeyDown (line 122); keydown (line 174); onClick (line 397).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, focus, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
