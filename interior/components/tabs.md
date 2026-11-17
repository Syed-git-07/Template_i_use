# tabs

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/tabs.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/tabs.tsx); SHA-256 `53542b1779cab5f70cc74b7eb1e77835372f9465ae8ae54fd40d667c5f34f72e`; 299 lines.

Imports: `react`, `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| value | string | False | 15 |
| label | string | False | 16 |
| disabled | boolean | True | 17 |
| items | TabItem[] | False | 22 |
| value | string | True | 23 |
| defaultValue | string | True | 24 |
| onValueChange | (value: string) => void | True | 25 |
| activation | TabsActivation | True | 26 |
| items | TabItem[] | False | 164 |
| value | string | True | 165 |
| defaultValue | string | True | 166 |
| onValueChange | (value: string) => void | True | 167 |
| activation | TabsActivation | True | 168 |
| renderPanel | (value: string) => ReactNode | True | 169 |
| label | string | True | 170 |
| panelClassName | string | True | 171 |
| className | string | True | 172 |

### Defaults and motion

- Default `activation` = `"automatic"` (line 34).
- Default `activation` = `"automatic"` (line 180).
- Default `label` = `"Tabs"` (line 182).
- Default `panelClassName` = `""` (line 183).
- Default `className` = `""` (line 184).
- `stiffness`: 620 (line 7).
- `damping`: 42 (line 7).
- `mass`: 0.35 (line 7).
- `stiffness`: 460 (line 12).
- `damping`: 38 (line 12).
- `mass`: 0.8 (line 12).
- `duration`: 0 (line 240).
- `duration`: 0 (line 246).
- `duration`: 0 (line 290).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, keyboard, focus, resize, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- The indicator is a single element carried between tabs by a shared layout id, so a fast switch cannot leave two bars crossfading past each other or restart a bar from zero width, and interrupting the move resumes the spring from where the bar currently is.
- The selected label changes weight without changing geometry: an invisible copy at the target weight holds the cell width, so the row never reflows on selection and the indicator never lands on stale measurements.
- Arrow keys walk the row, Home and End jump to the ends, and disabled tabs are stepped over rather than focused; only the selected tab sits in the page tab order, so Tab leaves the row instead of visiting every item in it.
- Only the selected panel is mounted, wired with role tabpanel and aria-labelledby, so a screen reader is handed one section of content rather than all of them stacked.
- Under prefers-reduced-motion the indicator's travel and the panel's 3px slide collapse to zero duration; the bar still ends up under the right label and the panel still appears.
- Selection is optional state: pass value and onValueChange to own it, or defaultValue to let the component own it, and take useTabs alone when you want the roving focus, ids and ARIA wiring under your own chrome.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| items | TabItem[] | not specified | Each tab is { value, label, disabled? }. Labels are strings so the row can reserve their selected width. |
| value | string | not specified | Controlled selection. Omit it and the component keeps its own. |
| defaultValue | string | first enabled item | Uncontrolled starting tab. |
| onValueChange | (value: string) => void | not specified | Fires on click, on Enter or Space, and on arrow keys when activation is automatic. |
| activation | "automatic" \| "manual" | "automatic" | Manual separates focus from selection: arrows move focus, Enter or Space commits. Use it when a panel is expensive. |
| variant | "underline" \| "segmented" | "underline" | Two dressings of the same single indicator: a 2px bar on the hairline, or a lifted block inside a track. |
| renderPanel | (value: string) => React.ReactNode | not specified | Called only for the selected tab. Omit it to render the tab row alone and wire panels yourself. |
| label | string | "Tabs" | aria-label on the tablist. Name the thing being sectioned, not the widget. |
| panelClassName | string | "" | Applied to the panel. Reserve a min height here when panel contents differ in length. |
| className | string | "" | Appended last on the root so callers win. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
