# halo-dropzone

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/halo-dropzone.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/halo-dropzone.tsx); SHA-256 `c01b594f02747c3e42fdf458f5d41c00330b9f14273df254801615c2c45850f9`; 2041 lines.

Imports: `react`, `lucide-react`, `motion/react`, `@/lib/utils`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| gradientIdPrefix | string | True | 36 |
| gradientIdPrefix | string | True | 233 |
| gradientIdPrefix | string | True | 393 |
| primaryBg | string | False | 820 |
| secondaryBg | string | False | 820 |
| tertiaryBg | string | False | 820 |
| ambientGradient | string | False | 842 |
| ambientGlow | string | False | 843 |
| coreGradient | string | False | 844 |
| coreGlow | string | False | 845 |
| active | boolean | False | 885 |
| rimVariant | RimVariant | True | 886 |
| borderGlow | DropzoneBorderGlowState | False | 998 |
| reduceMotion | boolean | False | 999 |
| file | File | False | 1103 |
| cf | ReturnType<typeof crossfade> | False | 1196 |
| cfTransition | ReturnType<typeof crossfadeTransition> | False | 1197 |
| disabled | boolean | False | 1198 |
| emptyLabel | string | False | 1199 |
| formatHint | string \| null | False | 1200 |
| idleIcon | ReactNode | True | 1201 |
| imageObjectUrls | Record<string, string> | False | 1202 |
| reduceMotion | boolean | False | 1203 |
| showSuccess | boolean | False | 1204 |
| showSuccessThumbnails | boolean | False | 1205 |
| successLabel | string | False | 1206 |
| uploadedFiles | File[] | False | 1207 |
| className | string | True | 1346 |
| accept | string | True | 1347 |
| multiple | boolean | True | 1348 |
| disabled | boolean | True | 1349 |
| translucent | boolean | True | 1351 |
| onFiles | (files: File[]) => void | True | 1353 |
| successResetMs | number | True | 1358 |
| emptyLabel | string | True | 1360 |
| successLabel | string | True | 1362 |
| idleIcon | ReactNode | True | 1364 |
| formatHint | string \| null | True | 1366 |
| showSuccessThumbnails | boolean | True | 1371 |
| file | File | False | 1682 |
| progress | number | False | 1684 |
| complete | boolean | True | 1686 |
| onRemove | () => void | True | 1687 |
| className | string | True | 1688 |
| id | string | False | 1794 |
| file | File | False | 1795 |
| progress | number | False | 1796 |
| done | boolean | False | 1797 |
| items | QueuedFile[] | False | 1801 |
| onRemove | (id: string) => void | False | 1802 |
| className | string | True | 1803 |
| label | string | False | 1848 |
| className | string | False | 1848 |
| className | string | True | 1902 |
| kind | FilePlaceholderKind | False | 1916 |
| kind | FilePlaceholderKind | False | 2003 |
| className | string | True | 2004 |

### Defaults and motion

- Default `gradientIdPrefix` = `""` (line 34).
- Default `gradientIdPrefix` = `""` (line 231).
- Default `gradientIdPrefix` = `""` (line 391).
- Default `rimVariant` = `"default"` (line 883).
- Default `multiple` = `false` (line 1377).
- Default `disabled` = `false` (line 1378).
- Default `translucent` = `true` (line 1379).
- Default `successResetMs` = `2400` (line 1381).
- Default `emptyLabel` = `"Drop files here or browse"` (line 1382).
- Default `successLabel` = `"Upload complete"` (line 1383).
- Default `formatHint` = `"PNG, JPG, PDF up to 10MB"` (line 1385).
- Default `showSuccessThumbnails` = `true` (line 1386).
- Default `complete` = `false` (line 1694).
- `duration`: 0.25 (line 1010).
- `ease`: "easeOut" (line 1010).
- `duration`: computed; inspect expression (line 1021).
- `ease`: "easeInOut" (line 1023).
- `duration`: computed; inspect expression (line 1035).
- `ease`: "easeInOut" (line 1037).
- `duration`: computed; inspect expression (line 1049).
- `ease`: "easeInOut" (line 1051).
- `duration`: computed; inspect expression (line 1092).
- `ease`: computed; inspect expression (line 1093).
- `duration`: 0.3 (line 1270).
- `bounce`: 0 (line 1271).
- `delay`: computed; inspect expression (line 1272).
- `duration`: 4.5 (line 1326).
- `ease`: "easeInOut" (line 1327).

### Input, style and lifecycle

Events: onChange (line 1545); onBlur (line 1565); onDragEnter (line 1566); onDragLeave (line 1567); onDragOver (line 1568); onDrop (line 1569); onFocus (line 1570); onKeyDown (line 1571); onMouseEnter (line 1580); onMouseLeave (line 1581); onClick (line 1756); onRemove (line 1823).

Typography/style anchors: 681, 709, 740.

Source signals: reduced_motion, keyboard, focus, cleanup, async, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
