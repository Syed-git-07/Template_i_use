# apple-cards-carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/apple-cards-carousel/components/ui/apple-cards-carousel.tsx

[Original source](https://ui.aceternity.com/registry/apple-cards-carousel.json); SHA-256 `fa1b1a602acc90e231a6aa5aacbecbe27592a18363d84d1a7df0a2feb76e9a68`; 297 lines.

Imports: `react`, `@tabler/icons-react`, `@/lib/utils`, `motion/react`, `next/image`, `@/hooks/use-outside-click`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| items | JSX.Element[] | False | 20 |
| initialScroll | number | True | 21 |
| src | string | False | 25 |
| title | string | False | 26 |
| category | string | False | 27 |
| content | React.ReactNode | False | 28 |
| onCardClose | (index: number) => void | False | 32 |
| currentIndex | number | False | 33 |
| card | Card | False | 160 |
| index | number | False | 161 |
| layout | boolean | True | 162 |

### Defaults and motion

- Default `initialScroll` = `0` (line 39).
- Default `layout` = `false` (line 158).
- `duration`: 0.5 (line 121).
- `delay`: computed; inspect expression (line 122).
- `ease`: "easeOut" (line 123).

### Input, style and lifecycle

Events: onScroll (line 97); onClick (line 137); onClick (line 144); keydown (line 181); onClick (line 217); onClick (line 240); onLoad (line 285).

Typography/style anchors: 120.

Source signals: keyboard, cleanup, async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
