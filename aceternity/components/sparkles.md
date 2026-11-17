# sparkles

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/cover/components/ui/sparkles.tsx

[Original source](https://ui.aceternity.com/registry/cover.json); SHA-256 `4b37534984e393929bc7af6ef292affc9a5b416fd3549fc4c4941ca568a7e03e`; 435 lines.

Imports: `react`, `react`, `@tsparticles/react`, `@tsparticles/engine`, `@tsparticles/slim`, `@/lib/utils`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | True | 11 |
| className | string | True | 12 |
| background | string | True | 13 |
| particleSize | number | True | 14 |
| minSize | number | True | 15 |
| maxSize | number | True | 16 |
| speed | number | True | 17 |
| particleColor | string | True | 18 |
| particleDensity | number | True | 19 |

### Defaults and motion

- `duration`: 1 (line 47).
- `duration`: 0.4 (line 91).
- `bounce`: computed; inspect expression (line 96).
- `bounce`: computed; inspect expression (line 108).
- `delay`: 0 (line 132).
- `delay`: 0 (line 141).
- `delay`: 0 (line 150).
- `delay`: computed; inspect expression (line 195).
- `delay`: 0 (line 245).
- `delay`: 0 (line 280).
- `delay`: computed; inspect expression (line 359).
- `duration`: computed; inspect expression (line 363).
- `delay`: 0 (line 385).
- `duration`: 1 (line 423).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 46, 126, 240, 275, 328, 370, 380.

Source signals: async.

## components/sparkles/components/ui/sparkles.tsx

[Original source](https://ui.aceternity.com/registry/sparkles.json); SHA-256 `4b37534984e393929bc7af6ef292affc9a5b416fd3549fc4c4941ca568a7e03e`; 435 lines.

Imports: `react`, `react`, `@tsparticles/react`, `@tsparticles/engine`, `@tsparticles/slim`, `@/lib/utils`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | True | 11 |
| className | string | True | 12 |
| background | string | True | 13 |
| particleSize | number | True | 14 |
| minSize | number | True | 15 |
| maxSize | number | True | 16 |
| speed | number | True | 17 |
| particleColor | string | True | 18 |
| particleDensity | number | True | 19 |

### Defaults and motion

- `duration`: 1 (line 47).
- `duration`: 0.4 (line 91).
- `bounce`: computed; inspect expression (line 96).
- `bounce`: computed; inspect expression (line 108).
- `delay`: 0 (line 132).
- `delay`: 0 (line 141).
- `delay`: 0 (line 150).
- `delay`: computed; inspect expression (line 195).
- `delay`: 0 (line 245).
- `delay`: 0 (line 280).
- `delay`: computed; inspect expression (line 359).
- `duration`: computed; inspect expression (line 363).
- `delay`: 0 (line 385).
- `duration`: 1 (line 423).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: 46, 126, 240, 275, 328, 370, 380.

Source signals: async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
