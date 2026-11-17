# carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/carousel/components/ui/carousel.tsx

[Original source](https://ui.aceternity.com/registry/carousel.json); SHA-256 `04759858e8dc938b453c77e152658fc6cb07d7f04eaabf7a49673d9f9a434c4e`; 215 lines.

Imports: `@tabler/icons-react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| title | string | False | 6 |
| button | string | False | 7 |
| src | string | False | 8 |
| slide | SlideData | False | 12 |
| index | number | False | 13 |
| current | number | False | 14 |
| handleSlideClick | (index: number) => void | False | 15 |
| type | string | False | 129 |
| title | string | False | 130 |
| handleClick | () => void | False | 131 |
| slides | SlideData[] | False | 153 |

### Defaults and motion


### Input, style and lifecycle

Events: onClick (line 72); onMouseMove (line 73); onMouseLeave (line 74); onLoad (line 100); onClick (line 145).

Typography/style anchors: 80.

Source signals: cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
