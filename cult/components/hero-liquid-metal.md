# hero-liquid-metal

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/hero-liquid-metal.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/hero-liquid-metal.tsx); SHA-256 `a7d3fb34e405cf90482eb3f1e70c5f29f0b40802b3f9b4bcb1e4965f38be3732`; 816 lines.

Imports: `react`, `react`, `@paper-design/shaders-react`, `@/lib/utils`, `@/components/ui/badge`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 17 |
| version | string | True | 18 |
| icon | LiquidMetalIcon | True | 19 |
| label | React.ReactNode | False | 23 |
| href | string | False | 24 |
| target | React.HTMLAttributeAnchorTarget | True | 25 |
| rel | string | True | 26 |
| onClick | React.MouseEventHandler<HTMLAnchorElement> | True | 27 |
| className | string | True | 28 |
| buttonClassName | string | True | 29 |
| srTitle | string | True | 66 |
| title | React.ReactNode | True | 67 |
| subtitle | React.ReactNode | True | 68 |
| description | React.ReactNode | True | 69 |
| showCta | boolean | True | 70 |
| ctaProps | Partial<HeroLiquidMetalCTAProps> | True | 71 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 72 |
| showBadges | boolean | True | 73 |
| techStack | HeroLiquidMetalTechItem[] | True | 74 |
| renderBadge | (     tech: HeroLiquidMetalTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 75 |
| desktopShaderProps | Partial<LiquidMetalProps> | True | 80 |
| mobileShaderProps | Partial<LiquidMetalProps> | True | 81 |
| title | React.ReactNode | True | 86 |
| subtitle | React.ReactNode | True | 87 |
| headingClassName | string | True | 88 |
| description | React.ReactNode | True | 93 |
| descriptionClassName | string | True | 94 |
| showCta | boolean | True | 99 |
| ctaProps | Partial<HeroLiquidMetalCTAProps> | True | 100 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 101 |
| showBadges | boolean | True | 106 |
| techStack | HeroLiquidMetalTechItem[] | True | 107 |
| renderBadge | (     tech: HeroLiquidMetalTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 108 |
| desktopShaderProps | Partial<LiquidMetalProps> | True | 117 |
| desktopClassName | string | True | 118 |
| mobileShaderProps | Partial<LiquidMetalProps> | True | 123 |
| containerClassName | string | True | 127 |
| contentClassName | string | True | 128 |
| headingWrapClassName | string | True | 129 |
| headingClassName | string | True | 130 |
| descriptionWrapClassName | string | True | 131 |
| descriptionClassName | string | True | 132 |
| ctaWrapClassName | string | True | 133 |
| badgesWrapClassName | string | True | 134 |
| visualClassName | string | True | 135 |
| mobileVisualClassName | string | True | 136 |
| srTitle | string | False | 140 |
| title | React.ReactNode | False | 141 |
| subtitle | React.ReactNode | False | 142 |
| description | React.ReactNode | False | 143 |
| showCta | boolean | False | 144 |
| mergedCtaProps | HeroLiquidMetalCTAProps | False | 145 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 146 |
| showBadges | boolean | False | 147 |
| techStack | HeroLiquidMetalTechItem[] | False | 148 |
| renderBadge | HeroLiquidMetalBadgesProps["renderBadge"] | True | 149 |
| mergedDesktopShaderProps | Partial<LiquidMetalProps> | False | 150 |
| mergedMobileShaderProps | Partial<LiquidMetalProps> | False | 151 |

### Defaults and motion

- Default `srTitle` = `"AI SDK Agents"` (line 242).
- Default `subtitle` = `"Copy and Paste"` (line 244).
- Default `showCta` = `true` (line 244).
- Default `showBadges` = `true` (line 244).

### Input, style and lifecycle

Events: onClick (line 527).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
