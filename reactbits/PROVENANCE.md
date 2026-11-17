# Provenance and reproducibility

Official repository: https://github.com/DavidHDev/react-bits

Pinned revision: `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c`.

Read the [license at that revision](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/LICENSE.md) before reuse. It is MIT with Commons Clause, not unrestricted MIT. Product use and redistribution of a standalone component collection are different permissions. Do not add the implementation, tools, sounds or exported asset packs to this shared published library. Preserve attribution and applicable notices when integrating permitted code into an application.

## Local snapshot

The local source is at `UI_REFERENCES/.local/react-bits/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/`. It includes `src`, `scripts` and root metadata. Large public media and Git history were not copied. This is an inspectable source snapshot, not a complete runnable media archive. Its `node_modules` junction supplies TypeScript for the source auditor only.

[local-source-sha256.json](catalogue/local-source-sha256.json) records hashes for 2,788 source/script files. The manifest contains paths and hashes, not source bodies. Do not silently alter this snapshot to implement project changes.

For another machine, clone the official repository into an ignored local directory, check out the pinned revision, and select `src` and `scripts` with Git sparse checkout if desired. Fetch from the original author, not from a republished copy. Review the license again if updating the revision. Public observations can change independently of this pinned source.

## Reproduce the research

1. Run `python reactbits/scripts/catalogue.py` to reconcile the public index and sitemap.
2. Install TypeScript 5.7.3 under `.local/tooling` with scripts disabled. Run `node reactbits/scripts/source-index.mjs <absolute-local-snapshot-path>` to regenerate factual API guides and the upstream prop-default audit. The script imports the official auditor; review that local script before running on a new revision.
3. Run `python reactbits/scripts/browser-survey.py <ignored-output-directory>`. Add `--retry` to revisit unsuccessful entries. This needs Python Playwright and Chromium; the catalogue also uses requests and BeautifulSoup.
4. Run `python reactbits/scripts/gesture-checks.py` for the selected public-demo assertions. Optional slug arguments rerun specific checks and merge their records.
5. Read errors and inspect screenshots before updating coverage. Do not equate a rendered panel or pointer sweep with complete interaction verification.

All code variants are linked: JavaScript + CSS, JavaScript + Tailwind, TypeScript + CSS and TypeScript + Tailwind. API extraction records names, types and scalar defaults, excluding copied explanatory paragraphs and implementation bodies. Object/function defaults retain original-source links. Structural motion/event indexes identify places to read; they do not execute every state branch.

No account cookies, credentials, Pro exports, third-party videos, screenshots or sound packs are published. Local browser captures are observation aids only. React Bits Pro is a separate offering; this inventory covers the public React Bits catalogue and its official source, not paid Pro internals.
