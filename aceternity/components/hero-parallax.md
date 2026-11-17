# hero-parallax

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/hero-parallax/components/ui/hero-parallax.tsx

[Original source](https://ui.aceternity.com/registry/hero-parallax.json); SHA-256 `3e700ea48e38831f35fa7b3c7e61cc438af3ae8a6de585314a12291b4312e142`; 160 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| products | {     title: string;     link: string;     thumbnail: string;   }[] | False | 16 |
| title | string | False | 17 |
| link | string | False | 18 |
| thumbnail | string | False | 19 |
| product | {     title: string;     link: string;     thumbnail: string;   } | False | 123 |
| title | string | False | 124 |
| link | string | False | 125 |
| thumbnail | string | False | 126 |
| translate | MotionValue<number> | False | 128 |

### Defaults and motion

- `stiffness`: 300 (line 31).
- `damping`: 30 (line 31).
- `bounce`: 100 (line 31).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
