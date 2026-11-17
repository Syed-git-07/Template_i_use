# calendar

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/calendar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/calendar.tsx); SHA-256 `f49ff30dd2f29c2409b35cab53af2eac9b4a634ef00d8a74be845a6435fa7759`; 288 lines.

Imports: `react`, `class-variance-authority`, `cn`, `react-aria-components`, `@/registry/bases/aria/ui/button`, `@/registry/bases/aria/ui/select`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| buttonVariant | React.ComponentProps<typeof Button>["variant"] | True | 70 |
| captionLayout | "label" \| "dropdown" | True | 71 |
| numberOfMonths | number | True | 72 |
| showWeekNumber | boolean | True | 73 |
| headerFormat | Intl.DateTimeFormatOptions | True | 74 |
| renderCell | (       renderProps: CalendarCellRenderProps & {         defaultChildren: React.ReactNode       }     ) => React.ReactNode | True | 75 |
| defaultChildren | React.ReactNode | False | 77 |
| buttonVariant | React.ComponentProps<typeof Button>["variant"] | True | 99 |
| captionLayout | "label" \| "dropdown" | True | 100 |
| headerFormat | Intl.DateTimeFormatOptions | True | 101 |
| numberOfMonths | number | True | 102 |
| showWeekNumber | boolean | True | 103 |
| renderCell | (       renderProps: CalendarCellRenderProps & {         defaultChildren: React.ReactNode       }     ) => React.ReactNode | True | 104 |
| defaultChildren | React.ReactNode | False | 106 |
| buttonVariant | React.ComponentProps<typeof Button>["variant"] | True | 135 |
| captionLayout | "label" \| "dropdown" | True | 136 |
| numberOfMonths | number | True | 137 |
| showWeekNumber | boolean | True | 138 |
| headerFormat | Intl.DateTimeFormatOptions | True | 139 |
| renderCell | (     renderProps: CalendarCellRenderProps & { defaultChildren: React.ReactNode }   ) => React.ReactNode | True | 140 |
| defaultChildren | React.ReactNode | False | 141 |
| isRange | boolean | True | 143 |
| format | Intl.DateTimeFormatOptions | True | 243 |
| format | Intl.DateTimeFormatOptions | True | 266 |

### Defaults and motion

- Default `captionLayout` = `"label"` (line 127).
- Default `buttonVariant` = `"ghost"` (line 128).
- Default `numberOfMonths` = `1` (line 129).
- Default `showWeekNumber` = `false` (line 130).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: aria.

## apps/v4/registry/bases/base/ui/calendar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/calendar.tsx); SHA-256 `bf451423d00a4b4e75d00f54dc5257c5bacbe7d749b274f1a032b3316de8617d`; 246 lines.

Imports: `react`, `cn`, `react-day-picker`, `@/registry/bases/base/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| buttonVariant | React.ComponentProps<typeof Button>["variant"] | True | 26 |
| locale | Partial<Locale> | True | 213 |

### Defaults and motion

- Default `showOutsideDays` = `true` (line 18).
- Default `captionLayout` = `"label"` (line 19).
- Default `buttonVariant` = `"ghost"` (line 20).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: focus, aria.

## apps/v4/registry/bases/radix/ui/calendar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/calendar.tsx); SHA-256 `c9de458db596c314ba29c8d4a02d1348572a1d0a9dd2ee45334d95a91ae878bf`; 247 lines.

Imports: `react`, `cn`, `react-day-picker`, `@/registry/bases/radix/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| buttonVariant | React.ComponentProps<typeof Button>["variant"] | True | 26 |
| locale | Partial<Locale> | True | 213 |

### Defaults and motion

- Default `showOutsideDays` = `true` (line 18).
- Default `captionLayout` = `"label"` (line 19).
- Default `buttonVariant` = `"ghost"` (line 20).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: focus, aria.

## apps/v4/registry/new-york-v4/ui/calendar.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/calendar.tsx); SHA-256 `5e4ce97669da1661c11dcc2d1bcf48f3639b28a052f023e2785240a6216cc821`; 221 lines.

Imports: `react`, `cn`, `lucide-react`, `react-day-picker`, `@/registry/new-york-v4/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| buttonVariant | React.ComponentProps<typeof Button>["variant"] | True | 28 |

### Defaults and motion

- Default `showOutsideDays` = `true` (line 21).
- Default `captionLayout` = `"label"` (line 22).
- Default `buttonVariant` = `"ghost"` (line 23).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: focus, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
