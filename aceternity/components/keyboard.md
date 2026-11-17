# keyboard

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/keyboard/components/ui/keyboard.tsx

[Original source](https://ui.aceternity.com/registry/keyboard.json); SHA-256 `a0ba174c681f87f53f96536ad1b584768f5a3aa89bf39ff145d4003174b08f60`; 972 lines.

Imports: `react`, `motion/react`, `@/lib/utils`, `@tabler/icons-react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| playSoundDown | (keyCode: string) => void | False | 240 |
| playSoundUp | (keyCode: string) => void | False | 241 |
| pressedKeys | Set<string> | False | 242 |
| setPressed | (keyCode: string) => void | False | 243 |
| setReleased | (keyCode: string) => void | False | 244 |
| lastPressedKey | string \| null | False | 245 |
| children | React.ReactNode | False | 263 |
| enableSound | boolean | True | 264 |
| containerRef | React.RefObject<HTMLDivElement \| null> | False | 265 |
| className | string | True | 518 |
| enableSound | boolean | True | 519 |
| showPreview | boolean | True | 520 |
| children | React.ReactNode | False | 822 |
| className | string | True | 833 |
| childrenClassName | string | True | 834 |
| containerClassName | string | True | 835 |
| children | React.ReactNode | True | 836 |
| keyCode | string | True | 837 |
| className | string | True | 896 |
| containerClassName | string | True | 897 |
| children | React.ReactNode | True | 898 |
| keyCode | string | True | 899 |
| className | string | True | 947 |

### Defaults and motion

- Default `enableSound` = `false` (line 260).
- Default `enableSound` = `false` (line 515).
- Default `showPreview` = `false` (line 516).
- `threshold`: 0.1 (line 398).
- `stiffness`: 500 (line 492).
- `damping`: 30 (line 493).
- `mass`: 0.5 (line 494).
- `duration`: 0.05 (line 501).

### Input, style and lifecycle

Events: click (line 313); keydown (line 314); keydown (line 427); keyup (line 428); onMouseDown (line 867); onMouseUp (line 868); onMouseLeave (line 869); onMouseDown (line 929); onMouseUp (line 930); onMouseLeave (line 931).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, async, visibility.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
