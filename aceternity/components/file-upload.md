# file-upload

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `dated public registry; file hashes recorded`.

## components/file-upload/components/ui/file-upload.tsx

[Original source](https://ui.aceternity.com/registry/file-upload.json); SHA-256 `04c24106950be495496e801ef5093529c935c5fa12d03d30f9a009f0d8adc622`; 195 lines.

Imports: `@/lib/utils`, `react`, `motion/react`, `@tabler/icons-react`, `react-dropzone`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| onChange | (files: File[]) => void | True | 32 |

### Defaults and motion

- `stiffness`: 300 (line 136).
- `damping`: 20 (line 137).

### Input, style and lifecycle

Events: onClick (line 58); onChange (line 66).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
