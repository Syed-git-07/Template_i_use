# ripple

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/ripple.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/ripple.tsx); SHA-256 `474c6080703baf70115da11c18b27ea00cf1c6711e3c5be3bae977a7ee635692`; 248 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | number | False | 11 |
| x | number | False | 12 |
| y | number | False | 13 |
| scale | number | False | 14 |
| released | boolean | False | 15 |
| disabled | boolean | True | 19 |
| max | number | True | 20 |
| minVisible | number | True | 21 |
| fade | number | True | 22 |
| children | React.ReactNode | False | 188 |
| onPress | () => void | True | 189 |
| disabled | boolean | True | 190 |
| max | number | True | 191 |
| tintClassName | string | True | 192 |
| className | string | True | 193 |

### Defaults and motion

- Default `disabled` = `false` (line 26).
- Default `max` = `4` (line 27).
- Default `minVisible` = `220` (line 28).
- Default `fade` = `320` (line 29).
- Default `disabled` = `false` (line 199).
- Default `max` = `4` (line 200).
- Default `tintClassName` = `"bg-stone-800/15 dark:bg-white/20"` (line 201).
- Default `className` = `""` (line 202).
- `duration`: 0.5 (line 7).
- `ease`: "linear" (line 7).
- `duration`: 0 (line 234).
- `duration`: computed; inspect expression (line 236).
- `ease`: computed; inspect expression (line 237).

### Input, style and lifecycle

Events: blur (line 138); visibilitychange (line 139); onClick (line 211).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, pointer_cancel, focus, cleanup, visibility, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- A tap released in forty milliseconds still gets a whole bloom: the fade cannot begin until the ripple has been visible for its minimum window, so the fastest presses are the ones most implementations swallow and this one does not.
- The bloom is spawned at the pointer's coordinates inside the element rect and scaled to the distance of the farthest corner, so a press on an edge fills the surface instead of stopping short of the opposite side.
- Nothing that moves is a layout property: the ripple is a fixed 40px patch, absolutely positioned inside an aria-hidden overlay, driven only by transform and opacity, so no press can shift the content sitting above it.
- Pointer capture, lost capture, pointer cancel, blur, and tab hide all release through one path, so dragging off the control, scrolling the list out from under a finger, or switching tabs mid-press never strands a ripple on screen.
- Space and Enter spawn from the element's centre and release on key up, so keyboard activation is acknowledged exactly like a finger, while the overlay stays aria-hidden and the button announces itself once rather than once per bloom.
- Under prefers-reduced-motion the patch arrives already at full size and only fades, so the press is still confirmed and only the travel is skipped.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| children | React.ReactNode | not specified | The label of the pressable surface. It is painted above the ripple layer, so the bloom never washes it out. |
| onPress | () => void | undefined | Fired on click, which means pointer and keyboard activation both route through the same native path. |
| disabled | boolean | false | Disables the button and refuses to spawn ripples, so a dead control never gives live feedback. |
| max | number | 4 | Ceiling on simultaneous blooms. A hammered key evicts the oldest instead of growing the DOM without limit. |
| tintClassName | string | "bg-stone-800/15 dark:bg-white/20" | The bloom fill. Swap it when the surface is dark, inverted, or tinted with a brand color. |
| className | string | "" | Appended last, so the caller's radius, height and padding win. The clip layer reads border-radius with rounded-[inherit], so overriding the radius still clips correctly. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
