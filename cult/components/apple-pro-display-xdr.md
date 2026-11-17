# apple-pro-display-xdr

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/apple-pro-display-xdr.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/apple-pro-display-xdr.tsx); SHA-256 `ef9fa7b9596400fcec23430e331dfb8ce294ae397310c51efec29cf313933b1c`; 1129 lines.

Imports: `react`, `react`, `next/image`, `@tabler/icons-react`, `motion/react`, `@/lib/utils`, `@/registry/default/ui/base-tooltip`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| mouseX | MotionValue<number> | False | 411 |
| reduceMotion | boolean | False | 412 |
| children | ReactNode | False | 433 |
| className | string | True | 434 |
| style | CSSProperties | True | 435 |
| ariaLabel | string | False | 436 |
| reduceMotion | boolean | False | 437 |
| label | string | False | 466 |
| children | ReactNode | False | 467 |
| showRunningDot | boolean | True | 468 |
| className | string | True | 536 |
| screenContent | ReactNode | True | 538 |
| initialMode | StudioScreenMode | True | 540 |
| mode | StudioScreenMode | False | 697 |

### Defaults and motion

- Default `initialMode` = `"wallpaper"` (line 717).
- `mass`: 0.12 (line 487).
- `stiffness`: computed; inspect expression (line 488).
- `damping`: computed; inspect expression (line 489).
- `duration`: 0.15 (line 769).
- `stiffness`: 520 (line 770).
- `damping`: 28 (line 770).

### Input, style and lifecycle

Events: onMouseLeave (line 450); onMouseMove (line 451); onClick (line 503); onKeyDown (line 504); onPointerDown (line 505); onMouseEnter (line 797); onMouseLeave (line 798); onMouseEnter (line 856); onMouseLeave (line 857); onClick (line 891); onKeyDown (line 892).

Typography/style anchors: 548, 655, 800.

Source signals: reduced_motion, keyboard, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
