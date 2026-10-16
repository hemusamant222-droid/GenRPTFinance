# Current screenshot sequence — four-image journey

This map supersedes the original 13-image map. The previous inventory is retained in `screenshot-inventory-initial.json`. The four latest screenshots define the product state order.

## Source availability

All four screenshots are visible in chat, but no original image files are available in the workspace or download directory. Import is pending. Planned asset filenames are recorded in `screenshot-inventory.json`; no files have been substituted or fabricated. The existing test composition remains unchanged until actual assets can be used and checked.

## 33-second storyboard (990 frames at 30 FPS)

| Time | Source / action | Camera and continuity |
| --- | --- | --- |
| 0–6s | SS1: focus existing company input; type `abc.com` character by character; cursor moves to Next and clicks | Begin with product context, gently zoom into the actual input. Remove browser chrome by framing. Replace input placeholder only inside its existing bounds. |
| 6–10s | SS2: report appears with primary company relabeled ABC Inc. (ABC) | Gentle fade between entry and report states. Establish the actual report, fixed toolbar and sidebar; do not fabricate a loading screen or authentication transition. |
| 10–16s | SS2 → SS3: scroll only the main report content | Keep report header, page toolbar and sidebar stationary. Mask content to the real report viewport and animate its upward movement. Preserve the source endpoints; do not generate missing research paragraphs between them. |
| 16–23s | SS3: focus Tax Risk Exposure / EV-EBITDA Impact Ranges chart | Smooth camera push, restrained spotlight on existing range bars and current markers. Keep visible labels, values and geometry unchanged; no fabricated tooltip. |
| 23–29s | SS3 → SS4: scroll only the left navigation | Keep the main chart at its existing scroll position. Animate only the navigation viewport and scrollbar to the supplied sections 6–10 endpoint. The selected report remains section 4.5; scrolling navigation does not open another section. |
| 29–33s | SS4: pull back toward Download Report; move cursor and click | End on original download control and brand. No invented save dialog or download-completion notification. |

## Anonymization

The user explicitly authorizes anonymization of company identities while retaining the actual product interface.

- Type exactly `abc.com` in SS1's company input; retain the actual product address if any browser chrome is kept. Prefer cropping that chrome out.
- Replace Apple Inc. / AAPL with ABC Inc. / ABC throughout report headings and body copy. Replace possessive Apple references and both chart titles consistently.
- Replace featured sample identities with ABC Inc., XYZ Ltd, XYZ Platforms, Inc., and ABC Corporation, plus corresponding fictional tickers.
- Preserve GenRPT Finance branding, navigation labels, button labels, chart data, and original styling.
- Use localized background masks and matching typography for text replacement. Do not paint over chart data, restructure paragraphs, or redraw the interface. Inspect masks at rendered resolution once originals are available.
- Because the original financial data belongs to a real company, any relabeled output should carry a discreet editorial note such as “Illustrative demo · company names anonymized”; do not present it as actual ABC/XYZ research.

## Implementation constraints

- Align SS2–SS4 to common anchors before compositing; their dimensions and offsets differ slightly.
- Use independently clipped layers for the main report, sidebar content, and fixed chrome. A full-image crossfade alone does not satisfy the requested scroll effect.
- The screenshots show endpoints rather than the full scrollable document. Bridge unobserved content with a short masked motion transition, without inventing intermediate research text or navigation entries.
- Keep the product UI dominant in the 1920×1080 frame. Camera moves, cursor, and highlights are editorial overlays, not new product functionality.
- No final animation or anonymized export has been produced yet. Original image files are the remaining prerequisite.
