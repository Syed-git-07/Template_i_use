# mock-browser-window

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/mock-browser-window.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/mock-browser-window.tsx); SHA-256 `892e8687a8f5d451310b8f251ea6645fc48e8efaf6d2880ecf286177553644c0`; 356 lines.

Imports: `react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| icon | React.ReactNode | True | 6 |
| label | string | False | 7 |
| active | boolean | True | 8 |
| badge | string \| number | True | 9 |
| variant | "macos" \| "windows" \| "chrome" \| "safari" | True | 13 |
| headerStyle | "minimal" \| "full" | True | 14 |
| url | string | True | 18 |
| secure | boolean | True | 19 |
| variant | "chrome" \| "safari" | True | 20 |
| className | string | True | 21 |
| items | SidebarItem[] | True | 25 |
| variant | "navigation" \| "bookmarks" \| "history" \| "extensions" | True | 26 |
| className | string | True | 27 |
| children | React.ReactNode | True | 31 |
| className | string | True | 32 |
| size | "sm" \| "md" \| "lg" \| "xl" | True | 33 |
| showSidebar | boolean | True | 34 |
| sidebarPosition | "left" \| "right" \| "top" \| "bottom" | True | 35 |
| headerStyle | "minimal" \| "full" | True | 36 |
| variant | "chrome" \| "safari" \| "generic" | True | 37 |
| theme | "light" \| "dark" \| "auto" | True | 38 |
| url | string | True | 39 |
| sidebarItems | Array<{     icon?: React.ReactNode     label: string     active?: boolean     badge?: string \| number   }> | True | 40 |
| icon | React.ReactNode | True | 41 |
| label | string | False | 42 |
| active | boolean | True | 43 |
| badge | string \| number | True | 44 |

### Defaults and motion

- Default `variant` = `"macos"` (line 49).
- Default `headerStyle` = `"full"` (line 50).
- Default `url` = `"https://example.com"` (line 170).
- Default `secure` = `true` (line 171).
- Default `variant` = `"chrome"` (line 172).
- Default `className` = `""` (line 173).
- Default `className` = `""` (line 213).
- Default `className` = `""` (line 243).
- Default `size` = `"md"` (line 244).
- Default `showSidebar` = `false` (line 245).
- Default `sidebarPosition` = `"left"` (line 246).
- Default `headerStyle` = `"minimal"` (line 247).
- Default `variant` = `"generic"` (line 248).
- Default `theme` = `"auto"` (line 249).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
