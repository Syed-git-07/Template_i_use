# text-roll

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `120f64f6ca60348e251f929e9c81f11ccbe45eda`.

## components/core/text-roll.tsx

[Original source](https://github.com/ibelick/motion-primitives/blob/120f64f6ca60348e251f929e9c81f11ccbe45eda/components/core/text-roll.tsx); SHA-256 `61d335da143a92a10cbcd2cdc222647181bb06f706241a912bb1f0d0be9bdd5e`; 103 lines.

Imports: `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| children | string | False | 11 |
| duration | number | True | 12 |
| getEnterDelay | (index: number) => number | True | 13 |
| getExitDelay | (index: number) => number | True | 14 |
| className | string | True | 15 |
| transition | Transition | True | 16 |
| variants | {     enter: {       initial: Target \| VariantLabels \| boolean;       animate: TargetAndTransition \| VariantLabels;     };     exit: {       initial: Target \| VariantLabels \| boolean;       animate: TargetAndTransition \| VariantLabels;     };   } | True | 17 |
| enter | {       initial: Target \| VariantLabels \| boolean;       animate: TargetAndTransition \| VariantLabels;     } | False | 18 |
| initial | Target \| VariantLabels \| boolean | False | 19 |
| animate | TargetAndTransition \| VariantLabels | False | 20 |
| exit | {       initial: Target \| VariantLabels \| boolean;       animate: TargetAndTransition \| VariantLabels;     } | False | 22 |
| initial | Target \| VariantLabels \| boolean | False | 23 |
| animate | TargetAndTransition \| VariantLabels | False | 24 |
| onAnimationComplete | () => void | True | 27 |

### Defaults and motion

- Default `duration` = `0.5` (line 32).
- `ease`: "easeIn" (line 36).
- `delay`: computed; inspect expression (line 73).
- `delay`: computed; inspect expression (line 85).

### Input, style and lifecycle

Events: onAnimationComplete (line 87).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
