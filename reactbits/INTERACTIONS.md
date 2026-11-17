# Interaction and implementation notes

These authored notes supplement every component's API, event, motion and stylesheet index. All numeric defaults below come from the pinned source, not estimates from video. Component guides link the exact implementation and all four variants. Runtime assertions are recorded separately in [gesture-checks.json](catalogue/gesture-checks.json).

## Folder and spatial browsing

**Folder:** flap/book modes and solid/glass presentation are different paths. The default is flap, spread layout, click activation, closed initially, draggable papers, zoom-on-click, preview peek and outside-click closing. Source limits the rendered entries to six and uses a fixed physics step of 1/240 second. Default tilt is 0.5, bounce 0.4 and speed 1. Clicking a paper can focus it; clicking again, Escape or clicking away recovers. Drag release invokes `onItemDrop` with item/index and the inside/outside result. The application decides what that drop means. It does not create files, persist moves or provide a document editor. Content can be supplied by the application; editing needs a real editor and save flow. A drag changing a transform is not proof of persisted file movement. See [Folder](components/Folder.md).

**FolderFloat:** distinct from Folder. Hover opens by default, selection closes by default, and optional physics/drift animate the papers. Defaults: spread 180, lift 26, tilt 8, flap angle 34, rest angle 16, open duration 520 ms, stagger 45 ms, bounce 0.3. Preserve the open/selection callbacks rather than replacing this with a static folder icon. See [FolderFloat](components/FolderFloat.md).

**InfiniteSpiral:** default automatic upward movement at speed 0.55, radius 170, seven cards per turn, 60 vertical spacing, 100×100 cards, perspective 1000, center scale 1.2, edge fade 0.3 and blur 6. Hover pauses by default. Parameters define a continuous depth arrangement; they are not equivalent to a generic flat carousel. See [InfiniteSpiral](components/InfiniteSpiral.md).

**InfiniteMenu:** spherical drag browsing uses 160 tiles by default, tile size 0.63, roundness 0.2, zoom 1.65, pull-back 1, stretch 0.6, inertia 0.6 and autoplay 3. Active-item change and item-click callbacks are separate. Keep GPU geometry, drag response, inertia, active-item resolution and item metadata together. Real route activation and safe external links belong to the application. See [InfiniteMenu](components/InfiniteMenu.md).

**OptionWheel:** default selected index 3, curve 1, tilt 6, blur 2, fade 0.25, smoothing 200, inset 80, drag enabled and looping off. Preserve the distinction between a transient dragged position and the selected item reported through `onChange`. See [OptionWheel](components/OptionWheel.md).

## Navigation and progression

**CardNav:** click activation, glass surface, rising effect, stagger 0.12, bounce 0.2, speed 1, card height 176 and maximum width 800 are defaults. Open state and link selection have separate callbacks. Verify focus order, Escape, actual routes and narrow-layout behavior when integrating. **BubbleMenu** defaults to a 0.5-second animation and 0.12 stagger with `back.out(1.5)` easing. **PillNav**, **LineSidebar**, **Stack** and **ScrollStack** retain their independent source guides; do not impose one navigation behavior on all of them.

**Stepper:** starts at step 1, numbered horizontal indicators, slide transition, non-linear navigation and visible footer by default. Step changes and final completion are separate callbacks. Form validation, required steps and submission failures must be wired by the consuming application. See [Stepper](components/Stepper.md).

## Numeric motion and direct manipulation

**Counter:** locale en-US, one minimum digit, automatic direction, duration 0.7, bounce 0.2, stagger 0.04, motion blur and intro enabled; tabular figures and edge fade 0.3. A counter displays supplied values. Clock accuracy, elapsed time and background-tab scheduling require application logic. See [Counter](components/Counter.md).

**ElasticSlider:** range 0–100, initial 50, step 1, horizontal, thickness 6 growing to 12 while active, maximum stretch 50 and bounce 0.5. Jump-to-click is enabled; wheel adjustment and stepped movement are off by default. `onChangeEnd` marks the end of interaction, distinct from continuous `onChange`. Clamp the committed value while preserving visual stretch outside the track. See [ElasticSlider](components/ElasticSlider.md).

**CometDial:** default 62 on a 0–100 range, sweep 320°, size 250, speed 25, tap bounce 0.2, flick bounce 0.1, momentum 1 and comet reach 180. **WakeSlider:** 32 bars, height 56, resting height 12, sensitivity 1, reach 6, skew 0.6, glide 0.3 and smoothing 100. These controls are not interchangeable; retain their geometry and release behavior. See [CometDial](components/CometDial.md), [WakeSlider](components/WakeSlider.md).

## Code input and confirmation

**CodeSlots:** six digits by default; numeric input, paste handler, one-time-code autofill, Backspace and optional masking. Default colors are near monochrome: accent/ink #f5f5f5, slot #27272a, digit #18181b; error uses #ff3b30. Slot size 44, gap 8, radius 12, bounce 0.2, settle 0.3 seconds, rise 8 and cascade 20 ms. Completion calls `onComplete`; the application sets status. The public demo waits 350 ms and chooses its configured accept/reject outcome. Success locks the input while the slots merge into the confirmation treatment. Error drains the digits and allows retry. Do not treat entering any six digits as authentication. See [CodeSlots](components/CodeSlots.md).

**HoldButton:** idle → holding → done, or release/cancellation → idle. Default hold time 2,000 ms; incomplete release animates home over 200 ms; completion resets after 1,200 ms. Press scale 0.97, directional fill, optional wave amplitude 6 and glow. The source gates completion to the holding state, includes a completion timer fallback, cancels on keyboard Escape and pointer drift, and observes blur/visibility. `onTap` and `onHold` are different callbacks. A deletion label does not delete data. See [HoldButton](components/HoldButton.md).

**SlideCommit:** independent track motion, pending state, success and failure callbacks. Defaults: 280×56, radius 28, speed 50, return bounce 0.38, landing dip 0.026 and success hold 1,500 ms. The source sets a minimum pending display of 300 ms. Await the actual `onConfirm` result and handle rejection; do not show payment success solely because the handle reached the end. See [SlideCommit](components/SlideCommit.md).

**FuseButton:** default 4,000 ms undo window, hover pauses, commit on press and reset on settle. `onCommit`, `onUndo`, `onFuseEnd` and phase changes convey different stages. A timed visual undo affordance needs a corresponding backend policy. See [FuseButton](components/FuseButton.md).

## Swipe, menus and feedback

**SwipeRow:** left direction, 80-pixel actions, height 64, radius 16, snap bounce 0.2, resistance 0.55, collapse 200 ms, commit threshold 0.6 and full-swipe enabled. Separate reveal/close, action selection and full-commit callbacks. Keyboard action reveal and Escape are available in the demo. The demo removes/restores sample rows; persistence, undo and failures belong to the host application. See [SwipeRow](components/SwipeRow.md).

**GlideSelect:** pop duration 180 ms, glide 220 ms, remembered position enabled, width 176, radius 10, bottom/left placement. Preserve keyboard semantics and selected value independently of the sliding highlight. **SwipeToast:** default 4,000 ms duration, pause-on-hover, swipe distance 40, slide duration 400 ms, bounce 0.2 and dismissible. Do not make toast disappearance the only confirmation of data persistence. See [GlideSelect](components/GlideSelect.md), [SwipeToast](components/SwipeToast.md).

**WarmTooltip:** group defaults include cold delay 400 ms, warm window 300 ms and travel 320; individual default pop duration 160 ms, scale 0.94, blur 4 and touch long-press 500 ms. Source lean spring: stiffness 260, damping 22, mass 0.4. A warm group carries timing across neighboring targets; isolated generic tooltips lose that behavior. Touch movement/cancellation and focus semantics need application testing. See [WarmTooltip](components/WarmTooltip.md).

**CallChip:** default running status and expected duration 2,500 ms are display inputs; it does not execute the represented task. **ThoughtLine:** working by default, breath period 1.6, depth 0.45, shimmer 1.8 seconds, settle 350 ms and collapse on settle. Connect completion to the real task. See [CallChip](components/CallChip.md), [ThoughtLine](components/ThoughtLine.md).

## Material and tactile interactions

**FlipCard:** Y-axis flip, click and drag enabled, tilt up to 12°, glare opacity 0.22, hover scale 1.03, perspective 1100, spring stiffness 170/damping 20. Ensure the hidden face's interactive controls do not remain incorrectly reachable. **TearTicket:** horizontal by default, 460×250, stub 150, tear angle 30, stretch 30, resistance 0.45 and rotation 4. `onTear` reports the interaction; it does not redeem a ticket. See [FlipCard](components/FlipCard.md), [TearTicket](components/TearTicket.md).

**PaperCrumple:** default amount 0.85, crumple 0.55 seconds, restore 0.4 seconds, six folds, sharpness 0.6, wrinkle 0.65, crease 0.18, roughness 0.92, drag enabled, rotation 10, drag radius 180, return-to-origin and restore-on-release. Seed 7 and detail 64 affect reproducibility and rendering cost. Preserve state-change and error handling. See [PaperCrumple](components/PaperCrumple.md).

**SlingButton:** arm at 48, maximum pull 160, launch speed 2600, recoil 0.2, flight 120, 14 particles and spread 60; any-axis drag and tap-send are defaults. `onSend` is an application callback. **SquishSwitch:** 76×38, radius 19, speed 50, stretch 36, hover scale 1.035 and color transition 320 ms. See [SlingButton](components/SlingButton.md), [SquishSwitch](components/SquishSwitch.md).

**VoicePill:** default auto interaction mode, hold-after 300 ms, slide-to-cancel enabled with distance 64, attack 40, release 240 and open duration 200 ms. Default reactivity is simulated. The optional microphone path uses microphone input for reactivity; do not infer that an audio file is recorded, saved or uploaded. Integrate explicit recording permissions, stream cleanup, cancellation and storage as required. The research did not request microphone access. See [VoicePill](components/VoicePill.md).

## Every other component and background

The 219 component guides retain APIs, exact scalar defaults, dependency imports, event locations, literal state assignments, motion parameters and CSS motion locations across the full collection. All 64 public backgrounds are included, including GPU and shader-based implementations. Choose a background only when a project calls for it. Preserve shader uniforms, geometry, device-pixel-ratio and cleanup behavior from the selected source; a screenshot cannot recover these.

Structural signals for keyboard, reduced motion, pointer cancellation, visibility, cleanup, frame loops, microphone, network, WebGL and resizing are search aids. A present signal is not proof that all paths are correct, and an absent signal is not proof that CSS or a dependency cannot supply that behavior. Test mobile/touch, interruption, reduced motion and performance in each real integration.
