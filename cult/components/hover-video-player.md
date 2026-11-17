# hover-video-player

Source reference guide for all projects. These are structural facts, not a claim that every gesture has been exercised.

Pinned revision: `d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`.

## apps/www/registry/default/ui/hover-video-player.tsx

[Original source](https://github.com/nolly-studio/cult-ui/blob/d71b1428b811c2779d46ea41b7ef8c9f9c9991c2/apps/www/registry/default/ui/hover-video-player.tsx); SHA-256 `1c3b6fd6a72a774badc0534a4694f84107388a779882d0f42751a8b3697215cd`; 1211 lines.

Imports: `react`, `next/image`, `lucide-react`, `motion/react`, `@/lib/utils`, `@/components/ui/button`, `@/components/ui/slider`

### API structure

| Name | Type | Optional | Source line |
| --- | --- | --- | --- |
| isHovering | boolean | False | 56 |
| isPlaying | boolean | False | 57 |
| isLoading | boolean | False | 58 |
| progress | number | False | 59 |
| muted | boolean | False | 60 |
| volume | number | False | 61 |
| isPiP | boolean | False | 62 |
| isMobile | boolean | False | 63 |
| controlsVisible | boolean | False | 64 |
| showThumbnail | boolean | False | 65 |
| isInView | boolean | False | 66 |
| videoSrc | string | False | 70 |
| thumbnailSrc | string | True | 71 |
| hoverOverlay | React.ReactNode | True | 72 |
| pausedOverlay | React.ReactNode | True | 73 |
| loadingOverlay | React.ReactNode | True | 74 |
| playbackStartDelay | number | True | 75 |
| restartOnPaused | boolean | True | 76 |
| unloadVideoOnPaused | boolean | True | 77 |
| playbackRangeStart | number | True | 78 |
| playbackRangeEnd | number | True | 79 |
| muted | boolean | True | 80 |
| loop | boolean | True | 81 |
| preload | "auto" \| "metadata" \| "none" | True | 82 |
| className | string | True | 83 |
| style | React.CSSProperties | True | 84 |
| onHoverStart | () => void | True | 85 |
| onHoverEnd | () => void | True | 86 |
| enableControls | boolean | True | 87 |
| cropTop | number | True | 88 |
| cropBottom | number | True | 89 |
| isVimeo | boolean | True | 90 |
| isPlaying | boolean | False | 94 |
| isHovering | boolean | False | 95 |
| isLoading | boolean | False | 96 |
| progress | number | False | 97 |
| volume | number | False | 98 |
| muted | boolean | False | 99 |
| isPiP | boolean | False | 100 |
| isMobile | boolean | False | 101 |
| controlsVisible | boolean | False | 102 |
| videoRef | React.RefObject<HTMLVideoElement \| null> | False | 103 |
| togglePlay | () => void | False | 104 |
| toggleMute | () => void | False | 105 |
| togglePiP | () => void | False | 106 |
| setVolume | (value: number) => void | False | 107 |
| setProgress | (value: number) => void | False | 108 |
| seekProgress | (value: number) => void | False | 109 |
| setSeekProgressHandler | (     handler: ((value: number) => void \| Promise<void>) \| null   ) => void | False | 110 |
| setVideoLoading | (isLoading: boolean) => void | False | 113 |
| setVideoPlaying | (isPlaying: boolean) => void | False | 114 |
| cropTop | number | False | 115 |
| cropBottom | number | False | 116 |
| thumbnailSrc | string | True | 117 |
| destroy | () => void | False | 121 |
| ready | () => Promise<void> | False | 122 |
| setVolume | (volume: number) => Promise<void> | False | 123 |
| getDuration | () => Promise<number> | False | 124 |
| setCurrentTime | (seconds: number) => Promise<number> | False | 125 |
| play | () => Promise<void> | False | 126 |
| pause | () => Promise<void> | False | 127 |
| on | (event: string, callback: (...args: any[]) => void) => void | False | 128 |
| off | (event: string, callback: (...args: any[]) => void) => void | False | 129 |
| Player | {     new (element: HTMLElement, options: any): VimeoPlayer   } | False | 133 |
| cancel | () => void | False | 162 |
| src | string | False | 749 |
| unloadVideoOnPaused | boolean | False | 750 |
| loop | boolean | False | 751 |
| preload | string | False | 752 |
| src | string | False | 920 |
| children | React.ReactNode | False | 957 |
| children | React.ReactNode | False | 989 |
| children | React.ReactNode | False | 1016 |
| children | React.ReactNode | False | 1042 |
| width | number | False | 1167 |
| height | number | False | 1168 |
| className | string | True | 1169 |
| children | ReactNode | True | 1170 |

### Defaults and motion

- Default `playbackStartDelay` = `0` (line 210).
- Default `restartOnPaused` = `false` (line 211).
- Default `unloadVideoOnPaused` = `false` (line 212).
- Default `initialMuted` = `false` (line 215).
- Default `loop` = `true` (line 216).
- Default `preload` = `"metadata"` (line 217).
- Default `enableControls` = `false` (line 222).
- Default `cropTop` = `0` (line 223).
- Default `cropBottom` = `0` (line 224).
- Default `isVimeo` = `false` (line 225).
- `duration`: 0.18 (line 44).
- `ease`: computed; inspect expression (line 45).
- `duration`: 0.3 (line 50).
- `bounce`: 0 (line 51).
- `threshold`: 0.1 (line 395).
- `duration`: computed; inspect expression (line 419).
- `duration`: 0 (line 940).
- `duration`: 0 (line 977).
- `duration`: 0 (line 1003).
- `duration`: 0 (line 1029).
- `duration`: 0 (line 1055).

### Input, style and lifecycle

Events: canplay (line 348); resize (line 372); computed event (line 474); onHoverStart (line 695); onHoverEnd (line 696); onTouchStart (line 697); onClick (line 1074); onClick (line 1094); onValueChange (line 1110); onValueChange (line 1130); onClick (line 1148).

Typography/style anchors: 1177, 1180.

Source signals: reduced_motion, cleanup, async, visibility, aria.

## Reuse and verification

Read source and dependencies for computed motion, state changes, inherited keyboard/focus behavior, controlled/uncontrolled data and cleanup. Verify cancellation, repeated input, reduced motion, touch, resize, loading and failure in the consuming application. Keep demo actions separate from actual data persistence. See the site coverage and licensing notes.
