# sidebar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/sidebar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/sidebar.tsx); SHA-256 `885ab2803f37d84160f84bf9d53ab02b04ea493acb7a17ed45a357ce9c5a3aa3`; 714 lines.

Imports: `react`, `class-variance-authority`, `cn`, `react-aria-components`, `@/registry/bases/aria/hooks/use-mobile`, `@/registry/bases/aria/ui/button`, `@/registry/bases/aria/ui/input`, `@/registry/bases/aria/ui/separator`, `@/registry/bases/aria/ui/sheet`, `@/registry/bases/aria/ui/skeleton`, `@/registry/bases/aria/ui/tooltip`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | "expanded" \| "collapsed" | False | 35 |
| open | boolean | False | 36 |
| setOpen | (open: boolean) => void | False | 37 |
| openMobile | boolean | False | 38 |
| setOpenMobile | (open: boolean) => void | False | 39 |
| isMobile | boolean | False | 40 |
| toggleSidebar | () => void | False | 41 |
| href | string | False | 45 |
| href | never | True | 46 |
| defaultOpen | boolean | True | 68 |
| open | boolean | True | 69 |
| onOpenChange | (open: boolean) => void | True | 70 |
| side | "left" \| "right" | True | 164 |
| variant | "sidebar" \| "floating" \| "inset" | True | 165 |
| collapsible | "offcanvas" \| "icon" \| "none" | True | 166 |
| elementType | React.ElementType | True | 411 |
| isActive | boolean | True | 507 |
| tooltip | string \| React.ComponentProps<typeof Tooltip> | True | 508 |
| showOnHover | boolean | True | 555 |
| showIcon | boolean | True | 594 |
| size | "sm" \| "md" | True | 658 |
| isActive | boolean | True | 659 |

### Defaults and motion

- Default `defaultOpen` = `true` (line 60).
- Default `side` = `"left"` (line 156).
- Default `variant` = `"sidebar"` (line 157).
- Default `collapsible` = `"offcanvas"` (line 158).
- Default `Element` = `"div"` (line 409).
- Default `isActive` = `false` (line 500).
- Default `variant` = `"default"` (line 501).
- Default `size` = `"default"` (line 502).
- Default `showOnHover` = `false` (line 552).
- Default `showIcon` = `false` (line 591).
- Default `size` = `"md"` (line 653).
- Default `isActive` = `false` (line 654).

### Input, style and lifecycle

Events: keydown (line 111); onOpenChange (line 189); onPress (line 272); onClick (line 300).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, aria.

## apps/v4/registry/bases/base/ui/sidebar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/sidebar.tsx); SHA-256 `9cbd10505eda6a0d633637d92ae27a8619fbdd5c7d514792218ead06b14e6bee`; 730 lines.

Imports: `react`, `@base-ui/react/merge-props`, `@base-ui/react/use-render`, `class-variance-authority`, `cn`, `@/registry/bases/base/hooks/use-mobile`, `@/registry/bases/base/ui/button`, `@/registry/bases/base/ui/input`, `@/registry/bases/base/ui/separator`, `@/registry/bases/base/ui/sheet`, `@/registry/bases/base/ui/skeleton`, `@/registry/bases/base/ui/tooltip`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | "expanded" \| "collapsed" | False | 36 |
| open | boolean | False | 37 |
| setOpen | (open: boolean) => void | False | 38 |
| openMobile | boolean | False | 39 |
| setOpenMobile | (open: boolean) => void | False | 40 |
| isMobile | boolean | False | 41 |
| toggleSidebar | () => void | False | 42 |
| defaultOpen | boolean | True | 65 |
| open | boolean | True | 66 |
| onOpenChange | (open: boolean) => void | True | 67 |
| side | "left" \| "right" | True | 161 |
| variant | "sidebar" \| "floating" \| "inset" | True | 162 |
| collapsible | "offcanvas" \| "icon" \| "none" | True | 163 |
| isActive | boolean | True | 518 |
| tooltip | string \| React.ComponentProps<typeof TooltipContent> | True | 519 |
| showOnHover | boolean | True | 569 |
| showIcon | boolean | True | 614 |
| size | "sm" \| "md" | True | 680 |
| isActive | boolean | True | 681 |

### Defaults and motion

- Default `defaultOpen` = `true` (line 57).
- Default `side` = `"left"` (line 153).
- Default `variant` = `"sidebar"` (line 154).
- Default `collapsible` = `"offcanvas"` (line 155).
- Default `isActive` = `false` (line 510).
- Default `variant` = `"default"` (line 511).
- Default `size` = `"default"` (line 512).
- Default `showOnHover` = `false` (line 565).
- Default `showIcon` = `false` (line 611).
- Default `size` = `"md"` (line 674).
- Default `isActive` = `false` (line 675).

### Input, style and lifecycle

Events: keydown (line 108); onOpenChange (line 184); onClick (line 268); onClick (line 296).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, aria.

## apps/v4/registry/bases/radix/ui/sidebar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/sidebar.tsx); SHA-256 `41b69bf6b45cdcd6a74d2d10188a35ed6ebfd75e8b63984b95267f6f66d92ff6`; 709 lines.

Imports: `react`, `class-variance-authority`, `cn`, `radix-ui`, `@/registry/bases/radix/hooks/use-mobile`, `@/registry/bases/radix/ui/button`, `@/registry/bases/radix/ui/input`, `@/registry/bases/radix/ui/separator`, `@/registry/bases/radix/ui/sheet`, `@/registry/bases/radix/ui/skeleton`, `@/registry/bases/radix/ui/tooltip`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | "expanded" \| "collapsed" | False | 35 |
| open | boolean | False | 36 |
| setOpen | (open: boolean) => void | False | 37 |
| openMobile | boolean | False | 38 |
| setOpenMobile | (open: boolean) => void | False | 39 |
| isMobile | boolean | False | 40 |
| toggleSidebar | () => void | False | 41 |
| defaultOpen | boolean | True | 64 |
| open | boolean | True | 65 |
| onOpenChange | (open: boolean) => void | True | 66 |
| side | "left" \| "right" | True | 160 |
| variant | "sidebar" \| "floating" \| "inset" | True | 161 |
| collapsible | "offcanvas" \| "icon" \| "none" | True | 162 |
| asChild | boolean | True | 406 |
| asChild | boolean | True | 426 |
| asChild | boolean | True | 508 |
| isActive | boolean | True | 509 |
| tooltip | string \| React.ComponentProps<typeof TooltipContent> | True | 510 |
| asChild | boolean | True | 555 |
| showOnHover | boolean | True | 556 |
| showIcon | boolean | True | 597 |
| asChild | boolean | True | 662 |
| size | "sm" \| "md" | True | 663 |
| isActive | boolean | True | 664 |

### Defaults and motion

- Default `defaultOpen` = `true` (line 56).
- Default `side` = `"left"` (line 152).
- Default `variant` = `"sidebar"` (line 153).
- Default `collapsible` = `"offcanvas"` (line 154).
- Default `asChild` = `false` (line 404).
- Default `asChild` = `false` (line 424).
- Default `asChild` = `false` (line 500).
- Default `isActive` = `false` (line 501).
- Default `variant` = `"default"` (line 502).
- Default `size` = `"default"` (line 503).
- Default `asChild` = `false` (line 551).
- Default `showOnHover` = `false` (line 552).
- Default `showIcon` = `false` (line 594).
- Default `asChild` = `false` (line 656).
- Default `size` = `"md"` (line 657).
- Default `isActive` = `false` (line 658).

### Input, style and lifecycle

Events: keydown (line 107); onOpenChange (line 183); onClick (line 267); onClick (line 295).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, aria.

## apps/v4/registry/new-york-v4/ui/sidebar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/sidebar.tsx); SHA-256 `4b474046db825fd20659f7d93759e71fd8016681dd715c1e7721842c3e4df4ee`; 727 lines.

Imports: `react`, `class-variance-authority`, `cn`, `lucide-react`, `radix-ui`, `@/registry/new-york-v4/hooks/use-mobile`, `@/registry/new-york-v4/ui/button`, `@/registry/new-york-v4/ui/input`, `@/registry/new-york-v4/ui/separator`, `@/registry/new-york-v4/ui/sheet`, `@/registry/new-york-v4/ui/skeleton`, `@/registry/new-york-v4/ui/tooltip`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| state | "expanded" \| "collapsed" | False | 36 |
| open | boolean | False | 37 |
| setOpen | (open: boolean) => void | False | 38 |
| openMobile | boolean | False | 39 |
| setOpenMobile | (open: boolean) => void | False | 40 |
| isMobile | boolean | False | 41 |
| toggleSidebar | () => void | False | 42 |
| defaultOpen | boolean | True | 65 |
| open | boolean | True | 66 |
| onOpenChange | (open: boolean) => void | True | 67 |
| side | "left" \| "right" | True | 162 |
| variant | "sidebar" \| "floating" \| "inset" | True | 163 |
| collapsible | "offcanvas" \| "icon" \| "none" | True | 164 |
| asChild | boolean | True | 400 |
| asChild | boolean | True | 421 |
| asChild | boolean | True | 507 |
| isActive | boolean | True | 508 |
| tooltip | string \| React.ComponentProps<typeof TooltipContent> | True | 509 |
| asChild | boolean | True | 554 |
| showOnHover | boolean | True | 555 |
| showIcon | boolean | True | 607 |
| asChild | boolean | True | 676 |
| size | "sm" \| "md" | True | 677 |
| isActive | boolean | True | 678 |

### Defaults and motion

- Default `defaultOpen` = `true` (line 57).
- Default `side` = `"left"` (line 155).
- Default `variant` = `"sidebar"` (line 156).
- Default `collapsible` = `"offcanvas"` (line 157).
- Default `asChild` = `false` (line 398).
- Default `asChild` = `false` (line 419).
- Default `asChild` = `false` (line 499).
- Default `isActive` = `false` (line 500).
- Default `variant` = `"default"` (line 501).
- Default `size` = `"default"` (line 502).
- Default `asChild` = `false` (line 550).
- Default `showOnHover` = `false` (line 551).
- Default `showIcon` = `false` (line 604).
- Default `asChild` = `false` (line 670).
- Default `size` = `"md"` (line 671).
- Default `isActive` = `false` (line 672).

### Input, style and lifecycle

Events: keydown (line 108); onOpenChange (line 185); onClick (line 270); onClick (line 291).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, cleanup, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
