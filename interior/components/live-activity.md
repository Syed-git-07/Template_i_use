# live-activity

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/live-activity.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/live-activity.tsx); SHA-256 `1c61c694e69c67076977e13816f42b14b817f5cdc4907727463a062c339c7305`; 469 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 33 |
| title | string | False | 34 |
| detail | string | True | 35 |
| progress | number \| null | True | 36 |
| phase | ActivityPhase | False | 37 |
| action | { label: string; onClick: () => void } | True | 38 |
| label | string | False | 38 |
| onClick | () => void | False | 38 |
| title | string | False | 42 |
| detail | string | True | 43 |
| progress | number \| null | True | 44 |
| linger | number | True | 48 |
| activity | Activity \| null | False | 113 |
| onDismiss | () => void | True | 114 |
| width | number | True | 115 |
| dismissLabel | string | True | 116 |
| label | string | True | 117 |
| className | string | True | 118 |
| w | number | False | 139 |
| h | number | False | 139 |
| phase | ActivityPhase | False | 398 |
| reduced | boolean | False | 398 |

### Defaults and motion

- Default `linger` = `2000` (line 51).
- Default `width` = `300` (line 124).
- Default `dismissLabel` = `"Dismiss activity"` (line 125).
- Default `label` = `"Activity"` (line 126).
- Default `className` = `""` (line 127).
- `stiffness`: 420 (line 12).
- `damping`: 36 (line 12).
- `mass`: 0.9 (line 12).
- `stiffness`: 260 (line 13).
- `damping`: 34 (line 13).
- `mass`: 0.8 (line 13).
- `stiffness`: 700 (line 14).
- `damping`: 46 (line 14).
- `mass`: 0.5 (line 14).
- `stiffness`: 210 (line 15).
- `damping`: 34 (line 15).
- `mass`: 0.9 (line 15).
- `duration`: 0.3 (line 18).
- `ease`: computed; inspect expression (line 18).
- `duration`: 0 (line 19).
- `duration`: 0.85 (line 20).
- `ease`: "linear" (line 20).
- `duration`: 0.16 (line 267).
- `ease`: computed; inspect expression (line 267).
- `duration`: 0.2 (line 275).
- `ease`: computed; inspect expression (line 275).
- `duration`: 0.2 (line 276).
- `ease`: computed; inspect expression (line 276).

### Input, style and lifecycle

Events: onPointerEnter (line 280); onPointerLeave (line 281); onFocusCapture (line 282); onBlurCapture (line 283); onKeyDown (line 288); onClick (line 336); onClick (line 347).

Typography/style anchors: 261, 267.

Source signals: reduced_motion, keyboard, focus, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- One pod, not a stack. The latest work replaces the last, because a system genuinely doing four things deserves a page, not a pile of chips — this is the honest difference from a toast.
- The surface itself morphs: both faces are always mounted, measured with a ResizeObserver behind an epsilon, and the pod springs its width and height between them — nothing is re-laid-out, nothing pops.
- It peeks on every phase change, holds long enough to read, then folds back to a glyph; hover, focus or a failure keep it open, and Escape folds or dismisses depending on whether the work is done.
- Progress is worn quietly in the compact face as a tabular percentage and fully in the expanded face as the 4/2 track; an indeterminate wait is a spinner, never a guessed meter.
- Success draws its tick and leaves on its own; failure stays, states the reason, and keeps a live Retry — the pod never auto-dismisses bad news.
- One announcement per phase per activity, deduplicated the same way the reference toast did it; screen readers hear started, finished, failed — never a progress stream.
- Under prefers-reduced-motion the morph lands instantly, the spinner becomes a still ring and the tick appears whole; the pod still tells the same story.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| activity | Activity \| null | not specified | The one thing the system is doing, from useLiveActivity. Null means the pod is gone, not hidden. |
| onDismiss | () => void | not specified | Wired to the close affordance and Escape once the work has resolved. |
| width | number | 300 | Expanded width in pixels. The pod stays a small object over the page; it never spans it. |
| dismissLabel | string | "Dismiss activity" | Accessible name of the close button. |
| label | string | "Activity" | Accessible name of the region. |
| useLiveActivity.linger | number | 2000 | How long a finished activity stays before the pod leaves on its own. |
| className | string | "" | Appended to the anchoring wrapper. Position it fixed at the top of your app. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
