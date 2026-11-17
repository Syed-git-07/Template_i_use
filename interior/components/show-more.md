# show-more

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/show-more.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/show-more.tsx); SHA-256 `30fbf9a18c78fa81399148a8f404a1d1be6eb52105c175561c7bb4a53b4cc37d`; 254 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| line | number | False | 26 |
| full | number | False | 26 |
| lines | number | True | 29 |
| maxHeight | number | True | 30 |
| defaultExpanded | boolean | True | 31 |
| expanded | boolean | True | 32 |
| onExpandedChange | (expanded: boolean) => void | True | 33 |
| contentRef | React.RefObject<HTMLDivElement \| null> | False | 37 |
| expanded | boolean | False | 38 |
| open | boolean | False | 39 |
| toggle | () => void | False | 40 |
| setExpanded | (next: boolean) => void | False | 41 |
| height | number \| null | False | 42 |
| collapsedHeight | number \| null | False | 43 |
| fullHeight | number \| null | False | 44 |
| expandable | boolean | False | 45 |
| capped | boolean | False | 46 |
| scrollable | boolean | False | 47 |
| children | React.ReactNode | False | 128 |
| moreLabel | string | True | 129 |
| lessLabel | string | True | 130 |
| label | string | True | 131 |
| className | string | True | 132 |

### Defaults and motion

- Default `lines` = `3` (line 51).
- Default `maxHeight` = `320` (line 52).
- Default `defaultExpanded` = `false` (line 53).
- Default `moreLabel` = `"Show more"` (line 137).
- Default `lessLabel` = `"Show less"` (line 138).
- Default `label` = `"Details"` (line 139).
- Default `lines` = `3` (line 140).
- Default `maxHeight` = `320` (line 141).
- Default `className` = `""` (line 145).
- `stiffness`: 190 (line 12).
- `damping`: 30 (line 13).
- `mass`: 1 (line 14).
- `stiffness`: 700 (line 19).
- `damping`: 46 (line 20).
- `mass`: 0.5 (line 21).
- `duration`: 0 (line 24).

### Input, style and lifecycle

Events: onClick (line 203).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The collapsed state is a measured pixel height, never `-webkit-line-clamp`, so no ellipsis is added to or removed from the last visible line and the paragraph breaks in exactly the same places open or shut.
- The animated height is a number read from a ResizeObserver rather than `auto`, so a toggle interrupted mid-flight springs from the height the box currently has instead of snapping to a freshly measured one.
- Content taller than `maxHeight` scrolls instead of expanding without bound, and the scrollbar gutter is reserved from the first paint whenever the content overflows, so the scrollbar's arrival cannot narrow the column and re-wrap the text.
- Before hydration the box is clamped in CSS at `lines × 1lh`, so server-rendered markup already shows the collapsed height rather than painting the whole paragraph and collapsing it once JavaScript lands.
- The trigger's two labels occupy one grid cell and its row keeps its height even when the content is short enough that no trigger is offered, so nothing below the block ever moves.
- Under `prefers-reduced-motion` the height, the edge fade and the chevron all settle instantly, and the clipped text stays in the accessibility tree while collapsed, so the information arrives either way.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| children | React.ReactNode | not specified | The content to clamp. It is laid out once at full width and never re-flowed. |
| lines | number | 3 | Collapsed height, in lines of the content's own computed line-height. |
| maxHeight | number | 320 | Ceiling in px for the expanded height. Anything past it scrolls inside. |
| expanded | boolean | not specified | Controlled open state. Omit to let the component hold its own. |
| defaultExpanded | boolean | false | Initial open state when uncontrolled. |
| onExpandedChange | (expanded: boolean) => void | not specified | Fires on every toggle, controlled or not. |
| moreLabel | string | "Show more" | Trigger label while collapsed. |
| lessLabel | string | "Show less" | Trigger label while expanded. Shares a grid cell with moreLabel. |
| label | string | "Details" | Accessible name for the region once it becomes a scroll container. |
| className | string | "" | Appended last to the outer element. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
