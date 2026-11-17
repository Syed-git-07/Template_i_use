# Recover local original source on another machine

The published reference repository contains notes, API facts, source hashes and pinned links. The ignored `.local` directory is deliberately not transported through GitHub. Obtain original implementations from their official authors when moving this research to another machine.

| Source | Official repository | Pinned revision | Local directory |
| --- | --- | --- | --- |
| shadcn/ui | https://github.com/shadcn-ui/ui | `968d8cb9dc42ae5d52e8fd356cf84596ec832a26` | `.local/upstream/shadcn` |
| Interior | https://github.com/ddoemonn/interior | `b6b272307464ba79db7183cee0515846d7eb1f9c` | `.local/upstream/interior` |
| Motion Primitives | https://github.com/ibelick/motion-primitives | `120f64f6ca60348e251f929e9c81f11ccbe45eda` | `.local/upstream/motion-primitives` |
| Cult UI | https://github.com/nolly-studio/cult-ui | `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2` | `.local/upstream/cult` |
| React Bits | https://github.com/DavidHDev/react-bits | `d01aa914dcbe76da8b2923ebf872b5c8b1066e4c` | `.local/react-bits/<revision>` |

Clone from the official repository, fetch the pinned revision if it is not in a shallow clone, and check it out before verifying hashes. Do not reset or overwrite an existing project checkout. The shadcn snapshot used sparse checkout for `apps/v4/registry`, `apps/v4/content`, `apps/v4/lib`, `apps/v4/hooks`, `apps/v4/styles`, `apps/v4/components` and `packages`. The React Bits snapshot is described in its provenance guide.

Aceternity is a dated public-registry snapshot, not a Git revision. Its per-item endpoint and content hashes are recorded in `aceternity/catalogue/registry-source.json`. Public availability can change; do not substitute newly fetched bytes while claiming they match the earlier observation. HTTP 401 entries remain restricted. Review the item license before using or distributing code.

60fps snippets are cached from their public pages and linked individually. Viewport and 60fps recordings remain on their original hosts; local frame captures are evidence aids rather than a republished media archive. Revisit the original entry if a capture is absent or stale.

For scripts using TypeScript parsing, install TypeScript 5.7.3 into ignored `.local/tooling` with installation scripts disabled. Python scripts require requests, BeautifulSoup, Playwright and its Chromium browser. The research scripts never install a project's dependencies, publish a website or configure an MCP server. Read the selected script before refreshing a new upstream revision.

After recovery, run the relevant source-index generator and compare pinned revisions/hashes. Re-indexing source is not a substitute for browser or integration testing. Preserve original license notices and review third-party assets separately.
