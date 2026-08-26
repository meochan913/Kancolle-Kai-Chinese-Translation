# Translation Consistency & Asset Orientation Rules

These rules are persistent project conventions and apply to future components whenever relevant.

## Tutorial objective / completion-message consistency

When a tutorial objective, fairy-bubble instruction, task title, achievement/completion notice, or other UI message refers to the same player action, keep the Chinese action wording consistent whenever practical.

Do not unnecessarily paraphrase the same action differently between the instruction and the completion notice. The player should be able to recognize that the completion message directly corresponds to the objective they just followed.

Example accepted for v0.02 M003:

- tutorial instruction: `按下R键即可前往旗舰提督室`
- completion notice: `「前往旗舰提督室」 已完成！`

If string-length, glyph-availability, UI-width, or technical constraints require different wording, preserve the same core action terminology first and document the reason for any divergence.

## Raw-texture / game-space orientation round-trip

For baked UI textures, never assume the decoded/raw file orientation is the same as the orientation displayed in game.

Required workflow:

1. Determine the raw/source -> game-space transform from original assets and hardware/game evidence. This includes vertical flip, horizontal flip, rotation, non-uniform scaling, crop, or translation as applicable.
2. Perform typography layout, centering, overlay, spacing, and visual QC in the correct game-space orientation.
3. After the Chinese game-space result is approved, apply the exact inverse transform before serializing the replacement back into the Unity asset.
4. Re-decode or reconstruct the serialized output and verify that applying the raw -> game-space transform reproduces the approved game-space candidate.
5. A candidate that looks correct only in a normal PNG preview but is serialized in the wrong raw orientation is `FAIL`.

For v0.02 M003 radial-menu text textures in `sharedassets5.assets`, the extracted Unity raw texture is vertically inverted relative to normal in-game reading orientation. Therefore:

`raw texture -> vertical flip -> game-space QC -> approved Chinese -> vertical flip -> raw writeback`

The final writeback must not serialize the upright Chinese preview directly.