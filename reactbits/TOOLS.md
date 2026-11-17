# Creative tools and supporting documentation

The five public tools are included in the shared reference scope. Their source is retained in the ignored local snapshot and covered by the source hash manifest. This page records their purpose and integration boundaries; [tools-browser.json](catalogue/tools-browser.json) records observed controls. It does not claim that every preset or export was exercised.

| Tool | Reference scope | Boundaries to preserve |
| --- | --- | --- |
| [Background Studio](https://reactbits.dev/tools/background-studio) | Background discovery, presets, live parameters and output choices | Keep selected component/uniforms and source attribution; check actual video/image export and looping before delivery |
| [Center Stage](https://reactbits.dev/tools/center-stage) | Screens within device/browser scenes, camera framing, depth, shadows and typography | Use authorized input media; preview aspect ratio, cropping, readability and export resolution |
| [Shape Magic](https://reactbits.dev/tools/shape-magic) | Shapes, patterns, text/SVG and material treatments | Preserve editable geometry separately from raster appearance; check font/SVG rights and output format |
| [Texture Lab](https://reactbits.dev/tools/texture-lab) | Image/video effects, presets and stacked processing | Keep effect order and parameter values; verify animation, GPU support and export fidelity; camera access is optional |
| [Sound Lab](https://reactbits.dev/tools/sound-lab) | Interface/video sound discovery and sound parameters | Compare actual playback and levels before use; do not republish the collection as an asset pack |

Pinned implementation entry locations: [tools](https://github.com/DavidHDev/react-bits/tree/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/tools), [sounds](https://github.com/DavidHDev/react-bits/tree/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/sounds), [tool catalogue](https://github.com/DavidHDev/react-bits/blob/d01aa914dcbe76da8b2923ebf872b5c8b1066e4c/src/constants/Tools.js).

The [supporting-page index](catalogue/tools-and-pages.md) also retains installation, introduction, MCP, changelog, showcase, sponsors, category pages and the Pro landing page. Treat installation/MCP instructions as documentation to review, not authorization to install or run arbitrary tools. No MCP server was installed during this study. The separate paid Pro catalogue and its implementation are outside the available public-source snapshot.

No uploaded user media, camera/microphone permission, sound listening comparison, export artifact or signed-in account workflow was tested. Read the original license before distributing tool outputs or sound assets; commercial application use does not authorize publishing standalone reference packs.
