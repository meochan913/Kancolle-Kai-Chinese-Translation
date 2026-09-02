# CRITICAL — Normal/Selected Overlay Must Use Final Atlas Placement

Status: **NON-NEGOTIABLE / FAIL-CLOSED**

This rule supplements:

- `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md`
- `docs/CRITICAL_BAKED_TEXT_DUAL_COMPARISON_GATE.md`

It was added after the StrategyFrame R8 QC regression on 2026-09-01.

## Failure that triggered this rule

The R8 QC sheet reported `differing alpha-geometry pixels = 0` for Normal vs Selected button labels, but the actual rendered atlas was visibly misaligned.

Root cause: the comparison was performed on the isolated local text layers **before final atlas placement**. Normal and Selected were generated from identical local masks, so the local comparison necessarily returned zero differences. Their final X placements were nevertheless different because the Selected placement used the wrong button-center delta.

Therefore **local-layer equality does not prove final-state alignment**.

## Mandatory state-alignment gate

For every Normal/Selected text pair:

1. Measure the actual containing button/sprite bounds in the exact source atlas.
2. Record left edge, right edge, width, and center for both Normal and Selected button states.
3. Choose one state as canonical geometry. For StrategyFrame buttons, Normal is canonical unless the user explicitly reopens that decision.
4. Render Normal and Selected from the same base Chinese glyph/effect geometry.
5. Place Normal in the final atlas.
6. Place Selected using the **measured button-bound delta**, not a guessed or independently fitted X/Y.
7. Construct the QC overlay from the **final atlas-space placements**.
8. Translate the final Selected atlas-space geometry back into the Normal button coordinate frame using the measured button-bound delta.
9. Compare those final-position masks. Only this comparison may report the Normal↔Selected geometry difference count.
10. Also report left/right margins from the text bbox to the actual containing button bounds.

A pre-placement local-layer overlay may be shown as a secondary diagnostic, but it MUST NOT be labeled or treated as proof of final alignment.

## StrategyFrame PathID 461 measured button bounds

From the accepted clean plate / original atlas:

- Row 1 Normal button: `x=151..280`, center `215.5`, width `130`
- Row 1 Selected button: `x=282..411`, center `346.5`, width `130`
- Row 1 Normal→Selected X delta: `+131`

- Row 2 Normal button: `x=151..280`, center `215.5`, width `130`
- Row 2 Selected button: `x=282..411`, center `346.5`, width `130`
- Row 2 Normal→Selected X delta: `+131`

- Row 3 Normal button: `x=151..290`, center `220.5`, width `140`
- Row 3 Selected button: `x=292..431`, center `361.5`, width `140`
- Row 3 Normal→Selected X delta: `+141`

The rejected R8 used Selected centers one pixel too far right for these rows. Any future StrategyFrame candidate must use the measured `+131 / +131 / +141` state deltas unless new source evidence supersedes them.

## Horizontal centering rule when translation width differs

When Chinese and Japanese strings have different natural widths, do not compare left edges as though the strings should have equal width.

Instead:

- measure the containing button bounds;
- compare left/right margins of the Chinese text/effect bbox to that button;
- use the button center as the horizontal anchor when the source design is centered;
- if the original Japanese source has an intentional small offset, preserve that offset only when source evidence is clear;
- never horizontally stretch Chinese to make both margins numerically identical.

## StrategyFrame R8 status

R8 state-alignment QC is **REJECTED** as proof of alignment because it compared pre-placement local masks. Its visual/material experiments may still be referenced, but final Normal↔Selected placement must be re-solved with this gate.
