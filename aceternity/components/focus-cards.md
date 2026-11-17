# focus-cards

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/focus-cards/components/ui/focus-cards.tsx

[Original source](https://ui.aceternity.com/registry/focus-cards.json); SHA-256 `545e481dfd448b33508770ab661878382f45636cb1e0fe77e623d408bc35ebec`; 69 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| card | any | False | 13 |
| index | number | False | 14 |
| hovered | number \| null | False | 15 |
| setHovered | React.Dispatch<React.SetStateAction<number \| null>> | False | 16 |
| title | string | False | 48 |
| src | string | False | 49 |
| cards | Card[] | False | 52 |

### Defaults and motion


### Input, style and lifecycle

Events: onMouseEnter (line 19); onMouseLeave (line 20).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
