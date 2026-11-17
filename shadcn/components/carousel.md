# carousel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `968d8cb9dc42ae5d52e8fd356cf84596ec832a26`.

## apps/v4/registry/bases/aria/ui/carousel.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/aria/ui/carousel.tsx); SHA-256 `74bb60e0fa7276307b0c7a9948cedd9db3e2780776b55c5438a095dd179dbe0e`; 257 lines.

Imports: `react`, `cn`, `embla-carousel-react`, `@/registry/bases/aria/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| opts | CarouselOptions | True | 18 |
| plugins | CarouselPlugin | True | 19 |
| orientation | "horizontal" \| "vertical" | True | 20 |
| setApi | (api: CarouselApi) => void | True | 21 |
| carouselRef | ReturnType<typeof useEmblaCarousel>[0] | False | 25 |
| api | ReturnType<typeof useEmblaCarousel>[1] | False | 26 |
| scrollPrev | () => void | False | 27 |
| scrollNext | () => void | False | 28 |
| canScrollPrev | boolean | False | 29 |
| canScrollNext | boolean | False | 30 |

### Defaults and motion

- Default `orientation` = `"horizontal"` (line 46).
- Default `variant` = `"outline"` (line 176).
- Default `size` = `"icon-sm"` (line 177).
- Default `variant` = `"outline"` (line 213).
- Default `size` = `"icon-sm"` (line 214).

### Input, style and lifecycle

Events: onKeyDownCapture (line 122); onPress (line 195); onPress (line 232).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, aria.

## apps/v4/registry/bases/base/ui/carousel.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/base/ui/carousel.tsx); SHA-256 `612fd55fe73c5f358b4970179f0a32d170a32e598a3c981f91a619795cbf62e3`; 257 lines.

Imports: `react`, `cn`, `embla-carousel-react`, `@/registry/bases/base/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| opts | CarouselOptions | True | 18 |
| plugins | CarouselPlugin | True | 19 |
| orientation | "horizontal" \| "vertical" | True | 20 |
| setApi | (api: CarouselApi) => void | True | 21 |
| carouselRef | ReturnType<typeof useEmblaCarousel>[0] | False | 25 |
| api | ReturnType<typeof useEmblaCarousel>[1] | False | 26 |
| scrollPrev | () => void | False | 27 |
| scrollNext | () => void | False | 28 |
| canScrollPrev | boolean | False | 29 |
| canScrollNext | boolean | False | 30 |

### Defaults and motion

- Default `orientation` = `"horizontal"` (line 46).
- Default `variant` = `"outline"` (line 176).
- Default `size` = `"icon-sm"` (line 177).
- Default `variant` = `"outline"` (line 213).
- Default `size` = `"icon-sm"` (line 214).

### Input, style and lifecycle

Events: onKeyDownCapture (line 122); onClick (line 195); onClick (line 232).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, aria.

## apps/v4/registry/bases/radix/ui/carousel.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/bases/radix/ui/carousel.tsx); SHA-256 `a6c2f89195135f7950f4b0737bf4bf4562cf4a5ac54b232077334c9e3089c28d`; 257 lines.

Imports: `react`, `cn`, `embla-carousel-react`, `@/registry/bases/radix/ui/button`, `@/app/(create)/components/icon-placeholder`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| opts | CarouselOptions | True | 18 |
| plugins | CarouselPlugin | True | 19 |
| orientation | "horizontal" \| "vertical" | True | 20 |
| setApi | (api: CarouselApi) => void | True | 21 |
| carouselRef | ReturnType<typeof useEmblaCarousel>[0] | False | 25 |
| api | ReturnType<typeof useEmblaCarousel>[1] | False | 26 |
| scrollPrev | () => void | False | 27 |
| scrollNext | () => void | False | 28 |
| canScrollPrev | boolean | False | 29 |
| canScrollNext | boolean | False | 30 |

### Defaults and motion

- Default `orientation` = `"horizontal"` (line 46).
- Default `variant` = `"outline"` (line 176).
- Default `size` = `"icon-sm"` (line 177).
- Default `variant` = `"outline"` (line 213).
- Default `size` = `"icon-sm"` (line 214).

### Input, style and lifecycle

Events: onKeyDownCapture (line 122); onClick (line 195); onClick (line 232).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, aria.

## apps/v4/registry/new-york-v4/ui/carousel.tsx

[Original source](https://github.com/shadcn-ui/ui/blob/968d8cb9dc42ae5d52e8fd356cf84596ec832a26/apps/v4/registry/new-york-v4/ui/carousel.tsx); SHA-256 `38d896d2c4d057783cd02b287ca961283ea39579ce9c0f96af51f332563ad75a`; 242 lines.

Imports: `react`, `cn`, `embla-carousel-react`, `lucide-react`, `@/registry/new-york-v4/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| opts | CarouselOptions | True | 18 |
| plugins | CarouselPlugin | True | 19 |
| orientation | "horizontal" \| "vertical" | True | 20 |
| setApi | (api: CarouselApi) => void | True | 21 |
| carouselRef | ReturnType<typeof useEmblaCarousel>[0] | False | 25 |
| api | ReturnType<typeof useEmblaCarousel>[1] | False | 26 |
| scrollPrev | () => void | False | 27 |
| scrollNext | () => void | False | 28 |
| canScrollPrev | boolean | False | 29 |
| canScrollNext | boolean | False | 30 |

### Defaults and motion

- Default `orientation` = `"horizontal"` (line 46).
- Default `variant` = `"outline"` (line 176).
- Default `size` = `"icon"` (line 177).
- Default `variant` = `"outline"` (line 206).
- Default `size` = `"icon"` (line 207).

### Input, style and lifecycle

Events: onKeyDownCapture (line 122); onClick (line 195); onClick (line 225).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: keyboard, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
