# notch

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/notch/components/ui/notch.tsx

[Original source](https://ui.aceternity.com/registry/notch.json); SHA-256 `c61d87255e4e1658ab8f19a47524283e3428974e1f58aa20980de71bdd3af26c`; 311 lines.

Imports: `react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 9 |
| label | React.ReactNode | False | 11 |
| icon | React.ReactNode | True | 13 |
| id | string | False | 18 |
| label | React.ReactNode | False | 20 |
| icon | React.ReactNode | True | 22 |
| options | NotchOption[] | False | 24 |
| defaultValue | string | True | 26 |
| value | string | True | 28 |
| showValue | boolean | True | 30 |
| onChange | (optionId: string, option: NotchOption) => void | True | 32 |
| items | NotchItem[] | False | 37 |
| position | "top" \| "bottom" | True | 39 |
| align | "start" \| "center" \| "end" | True | 41 |
| onItemChange | (     itemId: string,     optionId: string,     option: NotchOption,   ) => void | True | 43 |
| closeOnSelect | boolean | True | 49 |
| showSelectedValue | boolean | True | 51 |
| showDividers | boolean | True | 53 |
| accentColor | string | True | 55 |
| offset | number | True | 57 |
| reveal | boolean | True | 59 |
| className | string | True | 61 |
| itemClassName | string | True | 63 |
| panelClassName | string | True | 65 |

### Defaults and motion

- Default `position` = `"bottom"` (line 102).
- Default `align` = `"center"` (line 103).
- Default `closeOnSelect` = `true` (line 105).
- Default `showSelectedValue` = `true` (line 106).
- Default `showDividers` = `true` (line 107).
- Default `accentColor` = `"var(--color-blue-500, #3b82f6)"` (line 108).
- Default `offset` = `16` (line 109).
- Default `reveal` = `true` (line 110).
- `stiffness`: 380 (line 68).
- `damping`: 34 (line 68).
- `stiffness`: 420 (line 81).
- `damping`: 30 (line 81).
- `duration`: 0.15 (line 182).
- `duration`: 0.15 (line 241).

### Input, style and lifecycle

Events: keydown (line 134); pointerdown (line 143); onClick (line 200); onClick (line 254).

Typography/style anchors: 72, 81.

Source signals: keyboard, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
