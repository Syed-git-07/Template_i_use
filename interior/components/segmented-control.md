# segmented-control

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/segmented-control.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/segmented-control.tsx); SHA-256 `b44fd3a988b76a30c7100faf98dbca58eaefc7781639ae268c11d7f54c2bf43f`; 198 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string | False | 18 |
| label | string | False | 19 |
| disabled | boolean | True | 20 |
| options | SegmentedOption[] | False | 24 |
| label | string | False | 25 |
| value | string | True | 26 |
| defaultValue | string | True | 27 |
| onValueChange | (value: string) => void | True | 28 |
| className | string | True | 29 |

### Defaults and motion

- Default `className` = `""` (line 38).
- `stiffness`: 520 (line 12).
- `damping`: 34 (line 12).
- `mass`: 0.45 (line 12).

### Input, style and lifecycle

Events: onPointerLeave (line 172); onClick (line 185); onKeyDown (line 186); onPointerEnter (line 187).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, focus, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The label does not change color when the click lands; it inverts where the thumb's edge crosses it, because the inverted copy is a second grid clipped to the thumb and translated by the negative of the thumb's own transform, so the two halves of a glyph can be two colors at once.
- Segments never resize on selection: labels keep one weight in every state, both label layers share the same padding and type, and the track is a grid of equal fr columns, so the widest option fixes the geometry before anything moves.
- The thumb spring is driven by a motion value written straight to the DOM, so a selection changed mid-flight resumes from where the thumb currently is instead of restarting from the old segment, and React never re-renders during the slide.
- Under prefers-reduced-motion the thumb is placed on the new segment in one frame; the inversion still happens and no label is hidden.
- It is a real radiogroup with roving tabindex: arrow keys move and select, Home and End jump to the first and last enabled option, disabled segments are skipped rather than focused, and a screen reader is given one label per segment instead of the three visual copies on screen.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| options | SegmentedOption[] | not specified | Each is { value, label, disabled? }. Segments are equal width, sized to the widest label. |
| label | string | not specified | Accessible name for the radiogroup. Required, because an unlabelled group of radios announces nothing about what it switches. |
| value | string \| undefined | undefined | Controlled selection. Pass it with onValueChange to own the state. |
| defaultValue | string \| undefined | options[0].value | Uncontrolled starting selection. Falls back to the first option. |
| onValueChange | (value: string) => void | undefined | Fires only when the selection actually changes, never on a click that re-selects the current segment. |
| className | string | "" | Appended last to the track, so callers can override radius, border and surface. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
