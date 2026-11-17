# progress-bar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/progress-bar.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/progress-bar.tsx); SHA-256 `ef57be7f15465ea3d84644c65a13987ef82fae52849980ac5ecca77ff05899ea`; 117 lines.

Imports: `react`, `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | number \| null | False | 12 |
| max | number | True | 13 |
| label | string | True | 14 |
| pendingLabel | string | True | 15 |
| completeLabel | string | True | 16 |
| className | string | True | 17 |

### Defaults and motion

- Default `max` = `100` (line 22).
- Default `label` = `"Progress"` (line 23).
- Default `pendingLabel` = `"Working"` (line 24).
- Default `completeLabel` = `"Complete"` (line 25).
- Default `className` = `""` (line 26).
- `stiffness`: 210 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.9 (line 7).
- `stiffness`: 260 (line 8).
- `damping`: 34 (line 8).
- `mass`: 0.8 (line 8).
- `duration`: 0 (line 9).
- `duration`: 1.25 (line 103).
- `ease`: "easeInOut" (line 103).
- `duration`: 0.18 (line 104).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The bar is monotone: the position reached while the total was unknown becomes the floor, so the handover from indeterminate to determinate can never snap backwards or restart at zero.
- The indeterminate phase is not an idle loop. It is an exponential crawl toward a low ceiling that converges, cancels its own frame loop, and leaves nothing running once it has flattened.
- Progress is quantized to whole cells before anything is drawn, so React re-renders once per lit cell rather than once per frame, and the percentage in the readout is always the exact quantity the bar is showing.
- The percentage and the pending label occupy the same grid cell and every cell of the track is present from the first paint, so nothing on the row moves as the state changes.
- Under `prefers-reduced-motion` the crawl is skipped rather than faked: the bar stays honest at its last known amount, the label still says work is happening, and real values land without a spring.
- While the total is unknown the element carries `role="progressbar"` with no `aria-valuenow`, which is the ARIA spelling of indeterminate; the completion message reaches a screen reader once, not on every step.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| value | number \| null | not specified | The measured amount. `null` means the total is not known yet and the bar runs its indeterminate crawl. |
| max | number | 100 | Upper bound for `value`. Also the reported `aria-valuemax`. |
| segments | number | 24 | How many cells the bar is divided into. Progress is quantized to these, so the bar and the readout can never disagree. |
| ceiling | number | 0.35 | The fraction the indeterminate crawl converges on, clamped to 0.05–0.95. Keep it low so the real value rarely lands behind it. |
| crawl | number | 2200 | Time constant of the crawl in milliseconds. It reaches ~63% of `ceiling` after this long, then flattens. |
| label | string | "Progress" | Names the bar for sighted users and, through `aria-labelledby`, for screen readers. |
| pendingLabel | string | "Working" | Readout shown while `value` is `null`, in the same grid cell as the percentage. |
| completeLabel | string | "Complete" | Announced once through a polite live region when the bar fills. |
| className | string | "" | Appended last, so any layout or width class from the caller wins. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
