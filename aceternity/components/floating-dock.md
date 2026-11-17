# floating-dock

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/floating-dock/components/ui/floating-dock.tsx

[Original source](https://ui.aceternity.com/registry/floating-dock.json); SHA-256 `e6e4d163f11dd13135cf7ce08f3801ee91a81dbb75ccc9e0df51154cdd602919`; 201 lines.

Imports: `@/lib/utils`, `@tabler/icons-react`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| items | { title: string; icon: React.ReactNode; href: string }[] | False | 26 |
| title | string | False | 26 |
| icon | React.ReactNode | False | 26 |
| href | string | False | 26 |
| desktopClassName | string | True | 27 |
| mobileClassName | string | True | 28 |
| items | { title: string; icon: React.ReactNode; href: string }[] | False | 42 |
| title | string | False | 42 |
| icon | React.ReactNode | False | 42 |
| href | string | False | 42 |
| className | string | True | 43 |
| items | { title: string; icon: React.ReactNode; href: string }[] | False | 97 |
| title | string | False | 97 |
| icon | React.ReactNode | False | 97 |
| href | string | False | 97 |
| className | string | True | 98 |
| mouseX | MotionValue | False | 123 |
| title | string | False | 124 |
| icon | React.ReactNode | False | 125 |
| href | string | False | 126 |

### Defaults and motion

- `delay`: computed; inspect expression (line 66).
- `delay`: computed; inspect expression (line 69).
- `mass`: 0.1 (line 147).
- `stiffness`: 150 (line 148).
- `damping`: 12 (line 149).
- `mass`: 0.1 (line 152).
- `stiffness`: 150 (line 153).
- `damping`: 12 (line 154).
- `mass`: 0.1 (line 158).
- `stiffness`: 150 (line 159).
- `damping`: 12 (line 160).
- `mass`: 0.1 (line 163).
- `stiffness`: 150 (line 164).
- `damping`: 12 (line 165).

### Input, style and lifecycle

Events: onClick (line 84); onMouseMove (line 103); onMouseLeave (line 104); onMouseEnter (line 175); onMouseLeave (line 176).

Typography/style anchors: 65.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
