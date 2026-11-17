# prompt-library

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/prompt-library.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/prompt-library.tsx); SHA-256 `91730a9348be810c415b65c5e7246f4aba1258baf6fc4cbe998759bedd1cadd8`; 890 lines.

Imports: `react`, `@hugeicons/core-free-icons`, `@hugeicons/react`, `@/lib/utils`, `@/components/ui/button`, `@/components/ui/command`, `@/components/ui/dialog`, `@/components/ui/hover-card`, `@/components/ui/input`, `@/components/ui/popover`, `@/components/ui/textarea`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 57 |
| title | string | False | 59 |
| description | string | False | 61 |
| prompt | string | False | 63 |
| category | string | True | 65 |
| isCustom | boolean | True | 67 |
| prompts | Prompt[] | False | 72 |
| addCustom | (prompt: Omit<Prompt, "id" \| "isCustom">) => void | False | 74 |
| removeCustom | (id: string) => void | False | 76 |
| selectPrompt | (prompt: Prompt) => void | False | 78 |
| lastSelectedId | string \| null | False | 80 |
| open | boolean | False | 82 |
| setOpen | (open: boolean) => void | False | 84 |
| createDialogOpen | boolean | False | 86 |
| setCreateDialogOpen | (open: boolean) => void | False | 88 |
| prompts | Prompt[] | True | 150 |
| onPromptsChange | (prompts: Prompt[]) => void | True | 152 |
| onSelect | (prompt: Prompt) => void | True | 154 |
| onInsert | (text: string) => void | True | 159 |
| open | boolean | True | 161 |
| onOpenChange | (open: boolean) => void | True | 163 |
| label | ReactNode | True | 283 |
| prompt | Prompt | False | 485 |
| disablePreview | boolean | True | 487 |
| prompt | Prompt | False | 594 |
| children | ReactNode | False | 596 |
| label | ReactNode | True | 681 |
| title | DialogTitleProps["children"] | True | 734 |
| description | DialogDescriptionProps["children"] | True | 736 |
| children | ReactNode | True | 738 |

### Defaults and motion

- Default `placeholder` = `"Search prompts..."` (line 358).
- Default `children` = `"No prompts found."` (line 407).
- Default `disablePreview` = `false` (line 495).
- Default `label` = `"New Prompt"` (line 688).
- Default `title` = `"Create Prompt"` (line 745).
- Default `description` = `"Create a custom prompt template for quick access."` (line 746).

### Input, style and lifecycle

Events: onOpenChange (line 270); onSelect (line 516); onSelect (line 707); onOpenChange (line 793); onSubmit (line 803); onChange (line 810); onChange (line 825); onChange (line 838); onChange (line 850).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: async.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
