# ai-instructions

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/ai-instructions.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/ai-instructions.tsx); SHA-256 `7c64cf8d5336c659585f5453caac7d4cb7aadbc48abcf09429a6810b6a295ed4`; 912 lines.

Imports: `react`, `@hugeicons/core-free-icons`, `@hugeicons/react`, `@/lib/utils`, `@/components/ui/button`, `@/components/ui/command`, `@/components/ui/dialog`, `@/components/ui/hover-card`, `@/components/ui/input`, `@/components/ui/popover`, `@/components/ui/textarea`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 61 |
| title | string | False | 63 |
| description | string | False | 65 |
| content | string | True | 67 |
| isCustom | boolean | True | 69 |
| activeIds | string[] | False | 74 |
| toggle | (id: string) => void | False | 76 |
| isActive | (id: string) => boolean | False | 78 |
| instructions | Instruction[] | False | 80 |
| addCustom | (instruction: Omit<Instruction, "id" \| "isCustom">) => void | False | 82 |
| removeCustom | (id: string) => void | False | 84 |
| open | boolean | False | 86 |
| setOpen | (open: boolean) => void | False | 88 |
| createDialogOpen | boolean | False | 90 |
| setCreateDialogOpen | (open: boolean) => void | False | 92 |
| value | string[] | True | 152 |
| onValueChange | (value: string[]) => void | True | 154 |
| defaultValue | string[] | True | 156 |
| instructions | Instruction[] | True | 158 |
| onInstructionsChange | (instructions: Instruction[]) => void | True | 160 |
| open | boolean | True | 162 |
| onOpenChange | (open: boolean) => void | True | 164 |
| label | ReactNode | True | 288 |
| instruction | Instruction | False | 505 |
| disablePreview | boolean | True | 507 |
| instruction | Instruction | False | 632 |
| children | ReactNode | False | 634 |
| label | ReactNode | True | 714 |
| title | DialogTitleProps["children"] | True | 767 |
| description | DialogDescriptionProps["children"] | True | 769 |
| children | ReactNode | True | 771 |

### Defaults and motion

- Default `placeholder` = `"Search instructions..."` (line 379).
- Default `children` = `"No instructions found."` (line 428).
- Default `disablePreview` = `false` (line 515).
- Default `label` = `"New Instruction"` (line 721).
- Default `title` = `"Create Instruction"` (line 778).
- Default `description` = `"Create a custom instruction to guide the AI's behavior."` (line 779).

### Input, style and lifecycle

Events: onOpenChange (line 275); onSelect (line 537); onSelect (line 740); onOpenChange (line 821); onSubmit (line 831); onChange (line 841); onChange (line 856); onChange (line 872).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
