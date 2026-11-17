# hero-dithering

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/hero-dithering.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/hero-dithering.tsx); SHA-256 `e44577960247dd9c3c2f2eeabd71bf90606bb22d71227ef6ecfa692ddb564fd6`; 725 lines.

Imports: `react`, `react`, `@paper-design/shaders-react`, `@/lib/utils`, `@/components/ui/badge`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 17 |
| version | string | True | 18 |
| icon | DitheringIcon | True | 19 |
| label | React.ReactNode | False | 23 |
| href | string | False | 24 |
| target | React.HTMLAttributeAnchorTarget | True | 25 |
| rel | string | True | 26 |
| onClick | React.MouseEventHandler<HTMLAnchorElement> | True | 27 |
| className | string | True | 28 |
| buttonClassName | string | True | 29 |
| srTitle | string | True | 34 |
| title | React.ReactNode | True | 35 |
| subtitle | React.ReactNode | True | 36 |
| description | React.ReactNode | True | 37 |
| showCta | boolean | True | 38 |
| ctaProps | Partial<HeroDitheringCTAProps> | True | 39 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 40 |
| showBadges | boolean | True | 41 |
| techStack | HeroDitheringTechItem[] | True | 42 |
| renderBadge | (     tech: HeroDitheringTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 43 |
| desktopShaderProps | Partial<DitheringProps> | True | 48 |
| mobileShaderProps | Partial<DitheringProps> | True | 49 |
| title | React.ReactNode | True | 54 |
| subtitle | React.ReactNode | True | 55 |
| headingClassName | string | True | 56 |
| description | React.ReactNode | True | 61 |
| descriptionClassName | string | True | 62 |
| showCta | boolean | True | 67 |
| ctaProps | Partial<HeroDitheringCTAProps> | True | 68 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 69 |
| showBadges | boolean | True | 74 |
| techStack | HeroDitheringTechItem[] | True | 75 |
| renderBadge | (     tech: HeroDitheringTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 76 |
| desktopShaderProps | Partial<DitheringProps> | True | 85 |
| desktopClassName | string | True | 86 |
| mobileShaderProps | Partial<DitheringProps> | True | 91 |
| containerClassName | string | True | 95 |
| contentClassName | string | True | 96 |
| headingWrapClassName | string | True | 97 |
| headingClassName | string | True | 98 |
| descriptionWrapClassName | string | True | 99 |
| descriptionClassName | string | True | 100 |
| ctaWrapClassName | string | True | 101 |
| badgesWrapClassName | string | True | 102 |
| visualClassName | string | True | 103 |
| mobileVisualClassName | string | True | 104 |
| srTitle | string | False | 108 |
| title | React.ReactNode | False | 109 |
| subtitle | React.ReactNode | False | 110 |
| description | React.ReactNode | False | 111 |
| showCta | boolean | False | 112 |
| mergedCtaProps | HeroDitheringCTAProps | False | 113 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 114 |
| showBadges | boolean | False | 115 |
| techStack | HeroDitheringTechItem[] | False | 116 |
| renderBadge | HeroDitheringBadgesProps["renderBadge"] | True | 117 |
| mergedDesktopShaderProps | Partial<DitheringProps> | False | 118 |
| mergedMobileShaderProps | Partial<DitheringProps> | False | 119 |

### Defaults and motion

- Default `srTitle` = `"AI SDK Agents"` (line 201).
- Default `subtitle` = `"Copy and Paste"` (line 203).
- Default `showCta` = `true` (line 205).
- Default `showBadges` = `true` (line 208).

### Input, style and lifecycle

Events: onClick (line 448).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
