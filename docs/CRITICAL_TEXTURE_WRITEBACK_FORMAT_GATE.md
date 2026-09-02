# CRITICAL — Texture Writeback Format Gate

Status: **NON-NEGOTIABLE / FAIL-CLOSED**

Date added: 2026-09-02

## Rule

For baked UI typography or other fine-detail UI textures, visual approval of an RGBA raster does **not** imply that a DXT5/BC3 writeback is acceptable.

The exact final texture encoding used in the game asset must pass its own roundtrip QC before a writeback candidate may be called FINAL.

Mandatory order:

1. Finish and visually approve the game-space RGBA raster.
2. Encode it using the exact proposed Unity TextureFormat.
3. Decode that encoded payload back to game-space pixels.
4. Compare the encoded roundtrip on white and black backgrounds at source pixel scale and enlarged nearest-neighbor scale.
5. If thin text, 1 px bevels, halo edges, or antialiasing become blocky / soft / visibly different, the encoded candidate is **REJECTED**, regardless of whether the source raster used SS8 or higher supersampling.
6. Use a lossless/uncompressed format such as RGBA32 when required by visual fidelity, following the established SerializedFile v15 rebuild workflow.

Supersampling and texture compression are separate stages. SS8 improves the source raster, but it cannot prevent a later BC3 4x4 block compression stage from destroying fine detail.

## StrategyFrame incident — rejected DXT5 writeback

Target:

- `sharedassets5.assets`
- Texture2D PathID `461`
- `StrategyFrame`
- 512x512

Visual revision:

- R11.1 FINAL / user-approved

Rejected writeback:

- format: DXT5 / TextureFormat 12
- PathID461 DXT5 payload SHA-256: `d352140de457f5ea5d5d881fddc45259c82f490056b8fa8398d5d69fda15ae0f`
- exact cumulative input Mother SHA-256: `80e928863d532cdff580176daf8016d832e51dc21c5d88c06a5e976835c28d55`
- rejected full output SHA-256: `733edad4a0edae3b9f5a043c2edbd65c8003b8adeeb88b4502d4f53202360181`

Failure:

DXT5/BC3 roundtrip visibly reintroduced block/mosaic artifacts in the fine StrategyFrame button typography after the source text had already been rendered correctly using SS8 and a single Lanczos downsample.

Disposition:

- DXT5 StrategyFrame package: **REJECTED / SUPERSEDED**
- `733edad4...` must never become the cumulative Mother.
- Corrected writeback format: **RGBA32 / TextureFormat 4**
- R11.1 approved RGBA32 raw payload SHA-256: `b2f3c6858fa3c69988b60db0c66a81955d54db0dc847b9d18c1cdc7fbb5790c4`
- payload size: `1,048,576` bytes
- PathID461 object growth: `786,432` bytes (`0xC0000`)
- expected exact cumulative output size from the `80e928...` Mother: `59,133,448` bytes
- RGBA32 raw roundtrip pixel difference against the approved R11.1 RGBA raster: **0 pixels**

## Precedent

This follows the existing M002 PortTop RGBA32 rule: when fine baked UI text does not survive DXT5 faithfully, rebuild the target Texture2D as RGBA32 and update SerializedFile v15 object size / downstream byteStart metadata rather than accepting a visually degraded compressed texture.
