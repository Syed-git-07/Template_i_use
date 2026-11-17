# placeholders-and-vanish-input

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/placeholders-and-vanish-input/components/ui/placeholders-and-vanish-input.tsx

[Original source](https://ui.aceternity.com/registry/placeholders-and-vanish-input.json); SHA-256 `0decb6b2f53e2896b784c0e3fedeaf8fdec60aa5cd3d4bcdea72a6d6d6d27e3d`; 277 lines.

Imports: `motion/react`, `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| placeholders | string[] | False | 12 |
| onChange | (e: React.ChangeEvent<HTMLInputElement>) => void | False | 13 |
| onSubmit | (e: React.FormEvent<HTMLFormElement>) => void | False | 14 |

### Defaults and motion

- `duration`: 0.3 (line 237).
- `ease`: "linear" (line 238).
- `duration`: 0.3 (line 264).
- `ease`: "linear" (line 265).

### Input, style and lifecycle

Events: visibilitychange (line 35); onSubmit (line 183); onChange (line 193); onKeyDown (line 199).

Typography/style anchors: 64.

Source signals: keyboard, cleanup, visibility.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
