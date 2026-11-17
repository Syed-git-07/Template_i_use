# Bencho reference study

Research date: 17 November 2026. Scope: all public Bencho entries, reusable across all projects.

| Material | Location |
| --- | --- |
| 168 Blocks | [Block catalogue](catalogue/blocks.md) |
| 261 Finds and creator links | [Finds catalogue](catalogue/finds.md) |
| 145 Sounds | [Sound catalogue](catalogue/sounds.md) |
| 13 supporting pages | [Page catalogue](catalogue/pages.md) |
| All entries, short attributed descriptions, tags and original-post credits | [Full catalogue](catalogue/index.json) |
| Browser-observed Block settings and access | [Panel survey](catalogue/browser-blocks.json) |
| All 47 free components, CSS and props | [Free source index](catalogue/free-source.md) |
| Motion/event locations in the pinned source | [Detailed source index](catalogue/source-index.json) |
| All 24 free synthesised sounds | [Sounds source](upstream-free/sounds/README.md) |
| Cross-project guidance | [Interaction notes](INTERACTIONS.md) |
| Evidence and unfinished checks | [Coverage](COVERAGE.md) |
| Source origin and reuse boundaries | [Provenance](PROVENANCE.md) |

## Using a reference

Find the canonical entry, check its evidence/access status, then read its README, TSX and CSS together. For free blocks, retain the actual formulas and state transitions rather than recreating them from a screenshot. Copy only the selected component into the consuming project, with its licence and dependencies; map theme tokens and replace sample imagery. Connect actual application behavior and verify interruptions, cancellation, failure, touch, keyboard and reduced motion.

The unchanged free source is the fidelity baseline. A shared spring preset cannot replace all of its different physics, thresholds, paint order and easing.

## Local upstream playground

From `bencho/upstream-free`:

```powershell
npm ci --ignore-scripts
npm run build
npm run dev -- --host 127.0.0.1
```

TypeScript and production build passed. This is build verification, not full behavior/security/accessibility verification. Some files still name `/lab/...` images absent from the snapshot; replace those with owned assets when adapting. The combined playground bundle is large because it imports the collection; applications should select only what they use.

## Account boundary

The user confirmed a free Gmail-based sign-in without Pro. Research used an anonymous browser, not the user's signed-in Chrome profile. All 47 free blocks are live; 121 Pro blocks show static previews. Their setting labels do not prove their motion. No restricted source or account data was extracted.
