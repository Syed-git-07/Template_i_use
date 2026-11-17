# hero-color-panel

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/hero-color-panel.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/hero-color-panel.tsx); SHA-256 `b68e334e8c38b238729bb165e34c7731d74fb1f0a904dc74f447ae4c485ad0b5`; 716 lines.

Imports: `react`, `react`, `@paper-design/shaders-react`, `@/lib/utils`, `@/components/ui/badge`, `@/components/ui/button`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| name | string | False | 17 |
| version | string | True | 18 |
| icon | ColorPanelsIcon | True | 19 |
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
| ctaProps | Partial<HeroColorPanelsCTAProps> | True | 39 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 40 |
| showBadges | boolean | True | 41 |
| techStack | HeroColorPanelsTechItem[] | True | 42 |
| renderBadge | (     tech: HeroColorPanelsTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 43 |
| desktopShaderProps | Partial<ColorPanelsProps> | True | 48 |
| mobileShaderProps | Partial<ColorPanelsProps> | True | 49 |
| title | React.ReactNode | True | 54 |
| subtitle | React.ReactNode | True | 55 |
| headingClassName | string | True | 56 |
| description | React.ReactNode | True | 61 |
| descriptionClassName | string | True | 62 |
| showCta | boolean | True | 67 |
| ctaProps | Partial<HeroColorPanelsCTAProps> | True | 68 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 69 |
| showBadges | boolean | True | 74 |
| techStack | HeroColorPanelsTechItem[] | True | 75 |
| renderBadge | (     tech: HeroColorPanelsTechItem,     index: number,     defaultBadge: React.ReactNode   ) => React.ReactNode | True | 76 |
| desktopShaderProps | Partial<ColorPanelsProps> | True | 85 |
| desktopClassName | string | True | 86 |
| mobileShaderProps | Partial<ColorPanelsProps> | True | 91 |
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
| mergedCtaProps | HeroColorPanelsCTAProps | False | 113 |
| renderCta | (defaultCta: React.ReactNode) => React.ReactNode | True | 114 |
| showBadges | boolean | False | 115 |
| techStack | HeroColorPanelsTechItem[] | False | 116 |
| renderBadge | HeroColorPanelsBadgesProps["renderBadge"] | True | 117 |
| mergedDesktopShaderProps | Partial<ColorPanelsProps> | False | 118 |
| mergedMobileShaderProps | Partial<ColorPanelsProps> | False | 119 |

### Defaults and motion

- Default `srTitle` = `"AI SDK Agents"` (line 210).
- Default `subtitle` = `"Copy and Paste"` (line 212).
- Default `showCta` = `true` (line 212).
- Default `showBadges` = `true` (line 212).

### Input, style and lifecycle

Events: onClick (line 439).

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: none matched.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
