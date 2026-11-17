# hero-static-radial-gradient

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/hero-static-radial-gradient.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/hero-static-radial-gradient.tsx); SHA-256 `1a5f2574381bd46c7bc6e60dbab951552f2b846c2ca379f46a041dea83e31437`; 715 lines.

Imports: `react`, `react`, `@paper-design/shaders-react`, `@/lib/utils`, `@/components/ui/badge`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 19 |
| version | string | True | 20 |
| icon | StaticRadialGradientIcon | True | 21 |
| label | React.ReactNode | False | 25 |
| href | string | False | 26 |
| target | React.HTMLAttributeAnchorTarget | True | 27 |
| rel | string | True | 28 |
| onClick | React.MouseEventHandler<HTMLAnchorElement> | True | 29 |
| className | string | True | 30 |
| buttonClassName | string | True | 31 |
| srTitle | string | True | 36 |
| title | React.ReactNode | True | 37 |
| subtitle | React.ReactNode | True | 38 |
| description | React.ReactNode | True | 39 |
| showCta | boolean | True | 40 |
| ctaProps | Partial<HeroStaticRadialGradientCTAProps> | True | 41 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 42 |
| showBadges | boolean | True | 43 |
| techStack | HeroStaticRadialGradientTechItem[] | True | 44 |
| renderBadge | (     tech: HeroStaticRadialGradientTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 45 |
| desktopShaderProps | Partial<StaticRadialGradientProps> | True | 50 |
| mobileShaderProps | Partial<StaticRadialGradientProps> | True | 51 |
| title | React.ReactNode | True | 56 |
| subtitle | React.ReactNode | True | 57 |
| headingClassName | string | True | 58 |
| description | React.ReactNode | True | 63 |
| descriptionClassName | string | True | 64 |
| showCta | boolean | True | 69 |
| ctaProps | Partial<HeroStaticRadialGradientCTAProps> | True | 70 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 71 |
| showBadges | boolean | True | 76 |
| techStack | HeroStaticRadialGradientTechItem[] | True | 77 |
| renderBadge | (     tech: HeroStaticRadialGradientTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 78 |
| desktopShaderProps | Partial<StaticRadialGradientProps> | True | 87 |
| desktopClassName | string | True | 88 |
| mobileShaderProps | Partial<StaticRadialGradientProps> | True | 93 |
| containerClassName | string | True | 98 |
| contentClassName | string | True | 99 |
| headingWrapClassName | string | True | 100 |
| headingClassName | string | True | 101 |
| descriptionWrapClassName | string | True | 102 |
| descriptionClassName | string | True | 103 |
| ctaWrapClassName | string | True | 104 |
| badgesWrapClassName | string | True | 105 |
| visualClassName | string | True | 106 |
| mobileVisualClassName | string | True | 107 |
| srTitle | string | False | 111 |
| title | React.ReactNode | False | 112 |
| subtitle | React.ReactNode | False | 113 |
| description | React.ReactNode | False | 114 |
| showCta | boolean | False | 115 |
| mergedCtaProps | HeroStaticRadialGradientCTAProps | False | 116 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 117 |
| showBadges | boolean | False | 118 |
| techStack | HeroStaticRadialGradientTechItem[] | False | 119 |
| renderBadge | HeroStaticRadialGradientBadgesProps["renderBadge"] | True | 120 |
| mergedDesktopShaderProps | Partial<StaticRadialGradientProps> | False | 121 |
| mergedMobileShaderProps | Partial<StaticRadialGradientProps> | False | 122 |

### Defaults and motion

- Default `srTitle` = `"AI SDK Agents"` (line 209).
- Default `subtitle` = `"Copy and Paste"` (line 211).
- Default `showCta` = `true` (line 211).
- Default `showBadges` = `true` (line 211).

### Input, style and lifecycle

Events: onClick (line 438).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
