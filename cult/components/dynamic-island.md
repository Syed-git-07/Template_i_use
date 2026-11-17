# dynamic-island

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/dynamic-island.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/dynamic-island.tsx); SHA-256 `3870201c948329438c42807415e2dfc09e2d5bf9e7dc68e8424c198927107a01`; 542 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| width | number | False | 57 |
| height | number | True | 58 |
| aspectRatio | number | False | 59 |
| borderRadius | number | False | 60 |
| size | SizePresets | False | 138 |
| previousSize | SizePresets \| undefined | False | 139 |
| animationQueue | Array<{ size: SizePresets; delay: number }> | False | 140 |
| size | SizePresets | False | 140 |
| delay | number | False | 140 |
| isAnimating | boolean | False | 141 |
| type | "SET_SIZE" | False | 145 |
| newSize | SizePresets | False | 145 |
| type | "INITIALIZE" | False | 146 |
| firstState | SizePresets | False | 146 |
| type | "SCHEDULE_ANIMATION" | False | 148 |
| animationSteps | Array<{ size: SizePresets; delay: number }> | False | 149 |
| size | SizePresets | False | 149 |
| delay | number | False | 149 |
| type | "ANIMATION_END" | False | 151 |
| state | BlobStateType | False | 154 |
| dispatch | React.Dispatch<BlobAction> | False | 155 |
| setSize | (size: SizePresets) => void | False | 156 |
| scheduleAnimation | (     animationSteps: Array<{ size: SizePresets; delay: number }>   ) => void | False | 157 |
| size | SizePresets | False | 158 |
| delay | number | False | 158 |
| presets | Record<SizePresets, Preset> | False | 160 |
| children | React.ReactNode | False | 201 |
| initialSize | SizePresets | True | 202 |
| initialAnimation | Array<{ size: SizePresets; delay: number }> | True | 203 |
| size | SizePresets | False | 203 |
| delay | number | False | 203 |
| size | SizePresets | False | 246 |
| delay | number | False | 246 |
| size | SizePresets | False | 276 |
| delay | number | False | 276 |
| children | ReactNode | False | 286 |
| children | ReactNode | False | 299 |
| id | string | False | 300 |
| width | string | False | 339 |
| height | number | False | 339 |
| children | React.ReactNode | False | 362 |
| id | string | False | 363 |
| willChange | any | False | 364 |
| screenSize | string | False | 365 |
| className | string | True | 400 |
| children | React.ReactNode | True | 401 |
| className | string | True | 445 |
| children | React.ReactNode | True | 446 |
| className | string | False | 479 |
| children | React.ReactNode | False | 480 |

### Defaults and motion

- `duration`: computed; inspect expression (line 427).

### Input, style and lifecycle

Events: resize (line 317).

Typography/style anchors: 381, 463, 495, 516.

Source signals: cleanup, async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
