# resizable-navbar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/resizable-navbar/components/ui/resizable-navbar.tsx

[Original source](https://ui.aceternity.com/registry/resizable-navbar.json); SHA-256 `d4188bfc54caef986fe5a91ffd3ede454a2ce8773d5dffba01fa6615d5d8a5af`; 289 lines.

Imports: `@/lib/utils`, `@tabler/icons-react`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | React.ReactNode | False | 15 |
| className | string | True | 16 |
| children | React.ReactNode | False | 20 |
| className | string | True | 21 |
| visible | boolean | True | 22 |
| items | {     name: string;     link: string;   }[] | False | 26 |
| name | string | False | 27 |
| link | string | False | 28 |
| className | string | True | 30 |
| onItemClick | () => void | True | 31 |
| children | React.ReactNode | False | 35 |
| className | string | True | 36 |
| visible | boolean | True | 37 |
| children | React.ReactNode | False | 41 |
| className | string | True | 42 |
| children | React.ReactNode | False | 46 |
| className | string | True | 47 |
| isOpen | boolean | False | 48 |
| onClose | () => void | False | 49 |
| visible | boolean | True | 77 |
| isOpen | boolean | False | 223 |
| onClick | () => void | False | 224 |
| href | string | True | 258 |
| as | React.ElementType | True | 259 |
| children | React.ReactNode | False | 260 |
| className | string | True | 261 |
| variant | "primary" \| "secondary" \| "dark" \| "gradient" | True | 262 |

### Defaults and motion

- Default `Tag` = `"a"` (line 252).
- Default `variant` = `"primary"` (line 255).
- `stiffness`: 200 (line 99).
- `damping`: 50 (line 100).
- `stiffness`: 200 (line 164).
- `damping`: 50 (line 165).

### Input, style and lifecycle

Events: onMouseLeave (line 121); onMouseEnter (line 129); onClick (line 130); onClick (line 227); onClick (line 229).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
