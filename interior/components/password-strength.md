# password-strength

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `b6b272307464ba79db7183cee0515846d7eb1f9c`.

## components/interior/password-strength.tsx

[Original source](https://github.com/ddoemonn/interior/blob/b6b272307464ba79db7183cee0515846d7eb1f9c/components/interior/password-strength.tsx); SHA-256 `083c8c53bb01388c4efd2b3e6201c474c0ffb8c3bb67da5934b49ce8667e966e`; 250 lines.

Imports: `react`, `motion/react`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| id | string | False | 16 |
| label | string | False | 17 |
| test | (value: string) => boolean | False | 18 |
| met | boolean | False | 21 |
| rules | readonly PasswordRule[] | True | 24 |
| labels | readonly string[] | True | 25 |
| announceDelay | number | True | 26 |
| score | number | False | 30 |
| max | number | False | 31 |
| label | string | False | 32 |
| rules | EvaluatedRule[] | False | 33 |
| guessable | boolean | False | 34 |
| announcement | string | False | 35 |
| value | string | False | 102 |
| rules | readonly PasswordRule[] | True | 103 |
| labels | readonly string[] | True | 104 |
| announceDelay | number | True | 105 |
| showRules | boolean | True | 106 |
| className | string | True | 107 |

### Defaults and motion

- Default `announceDelay` = `700` (line 56).
- Default `announceDelay` = `700` (line 129).
- Default `showRules` = `true` (line 130).
- Default `className` = `""` (line 131).
- `stiffness`: 520 (line 6).
- `damping`: 34 (line 6).
- `mass`: 0.45 (line 6).
- `stiffness`: 260 (line 7).
- `damping`: 34 (line 7).
- `mass`: 0.8 (line 7).
- `duration`: 0 (line 8).
- `delay`: computed; inspect expression (line 166).

### Input, style and lifecycle

Events: none directly declared in this file.

Typography/style anchors: none matched; utility classes or shared theme may own these.

Source signals: reduced_motion, aria.

## Original author behavior contract

The following notes and documented API are from interior.dev / ozzy under the [MIT license](../UPSTREAM-LICENSE.txt). They describe upstream design intentions, not independently tested guarantees.

- Strength is a whole number of segments, never a percentage, so the meter cannot report a change too small to name; the cells, the label and the count move together or not at all.
- The five verdict labels occupy one grid cell and the requirement list is fixed length, so nothing below the field, including the submit button, moves while a password is typed.
- A screen reader hears the verdict once, after typing stops, from a polite region that names the level and the requirements still outstanding, instead of a new announcement per keystroke.
- Meaning is never carried by color: the number of filled cells, the label, and a per-row met or not met string each state it, so the component survives greyscale and low vision.
- Segments fill with transform rather than width, and each cell springs from wherever it currently is, so deleting three characters reverses the fill mid-flight instead of restarting it.
- Common passwords, four-character repeats and keyboard walks are capped at one segment, because a meter that calls Passw0rd! strong is worse than no meter at all.

| Prop | Type | Documented default | Original note |
| --- | --- | --- | --- |
| value | string | not specified | The password being typed. The component is controlled and keeps no copy of the secret. |
| rules | readonly PasswordRule[] | defaultPasswordRules | The requirement set. Its length is the number of segments, so a five-rule policy draws five cells without touching the markup. |
| labels | readonly string[] | ["Empty", "Weak", "Fair", "Good", "Strong"] | One label per score from 0 to rules.length. All of them share a single grid cell, so the widest sets the width once. |
| announceDelay | number | 700 | Milliseconds of quiet before the live region speaks. The visible meter is never delayed by it. |
| showRules | boolean | true | Renders the requirement checklist under the meter. Turn it off when the policy is stated elsewhere on the page. |
| className | string | "" | Appended last, so a caller's spacing or width class wins. |

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
