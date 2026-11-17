# animated-testimonials

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/animated-testimonials/components/ui/animated-testimonials.tsx

[Original source](https://ui.aceternity.com/registry/animated-testimonials.json); SHA-256 `0ebd8145a884493cc52f27b9fc73aaa35102fc4d12fb31b4e33d55818e330627`; 166 lines.

Imports: `@tabler/icons-react`, `motion/react`, `react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| quote | string | False | 9 |
| name | string | False | 10 |
| designation | string | False | 11 |
| src | string | False | 12 |
| testimonials | Testimonial[] | False | 18 |
| autoplay | boolean | True | 19 |

### Defaults and motion

- Default `autoplay` = `false` (line 16).
- `duration`: 0.4 (line 77).
- `ease`: "easeInOut" (line 78).
- `duration`: 0.2 (line 111).
- `ease`: "easeInOut" (line 112).
- `duration`: 0.2 (line 136).
- `ease`: "easeInOut" (line 137).
- `delay`: computed; inspect expression (line 138).

### Input, style and lifecycle

Events: onClick (line 149); onClick (line 155).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
