# hero-heatmap

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/hero-heatmap.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/hero-heatmap.tsx); SHA-256 `91517daa6b43a4d50b4872aa6e01d2a628ba1170b3d5da01576d9d7b0d8a6795`; 788 lines.

Imports: `react`, `react`, `@paper-design/shaders-react`, `@/lib/utils`, `@/components/ui/badge`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 17 |
| version | string | True | 18 |
| icon | HeatmapIcon | True | 19 |
| label | React.ReactNode | False | 23 |
| href | string | False | 24 |
| target | React.HTMLAttributeAnchorTarget | True | 25 |
| rel | string | True | 26 |
| onClick | React.MouseEventHandler<HTMLAnchorElement> | True | 27 |
| className | string | True | 28 |
| buttonClassName | string | True | 29 |
| srTitle | string | True | 54 |
| title | React.ReactNode | True | 55 |
| subtitle | React.ReactNode | True | 56 |
| description | React.ReactNode | True | 57 |
| showCta | boolean | True | 58 |
| ctaProps | Partial<HeroHeatmapCTAProps> | True | 59 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 60 |
| showBadges | boolean | True | 61 |
| techStack | HeroHeatmapTechItem[] | True | 62 |
| renderBadge | (     tech: HeroHeatmapTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 63 |
| desktopShaderProps | Partial<HeatmapProps> | True | 68 |
| mobileShaderProps | Partial<HeatmapProps> | True | 69 |
| title | React.ReactNode | True | 74 |
| subtitle | React.ReactNode | True | 75 |
| headingClassName | string | True | 76 |
| description | React.ReactNode | True | 81 |
| descriptionClassName | string | True | 82 |
| showCta | boolean | True | 87 |
| ctaProps | Partial<HeroHeatmapCTAProps> | True | 88 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 89 |
| showBadges | boolean | True | 94 |
| techStack | HeroHeatmapTechItem[] | True | 95 |
| renderBadge | (     tech: HeroHeatmapTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 96 |
| desktopShaderProps | Partial<HeatmapProps> | True | 105 |
| desktopClassName | string | True | 106 |
| mobileShaderProps | Partial<HeatmapProps> | True | 111 |
| containerClassName | string | True | 115 |
| contentClassName | string | True | 116 |
| headingWrapClassName | string | True | 117 |
| headingClassName | string | True | 118 |
| descriptionWrapClassName | string | True | 119 |
| descriptionClassName | string | True | 120 |
| ctaWrapClassName | string | True | 121 |
| badgesWrapClassName | string | True | 122 |
| visualClassName | string | True | 123 |
| mobileVisualClassName | string | True | 124 |
| srTitle | string | False | 128 |
| title | React.ReactNode | False | 129 |
| subtitle | React.ReactNode | False | 130 |
| description | React.ReactNode | False | 131 |
| showCta | boolean | False | 132 |
| mergedCtaProps | HeroHeatmapCTAProps | False | 133 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 134 |
| showBadges | boolean | False | 135 |
| techStack | HeroHeatmapTechItem[] | False | 136 |
| renderBadge | HeroHeatmapBadgesProps["renderBadge"] | True | 137 |
| mergedDesktopShaderProps | Partial<HeatmapProps> | False | 138 |
| mergedMobileShaderProps | Partial<HeatmapProps> | False | 139 |

### Defaults and motion

- Default `srTitle` = `"AI SDK Agents"` (line 238).
- Default `subtitle` = `"Copy and Paste"` (line 240).
- Default `showCta` = `true` (line 240).
- Default `showBadges` = `true` (line 240).

### Input, style and lifecycle

Events: onClick (line 499).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
