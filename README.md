# Astravael: Nexara — Update Repository

Public distribution point for the **latest production version** of the Voyage world
**Astravael: Nexara** (world `W1KX_CXxd4JS`).

Purpose of this repository: test whether Voyage Studio can pull the current production
world from a public URL into a player's private save, so a playthrough can be fully
updated without losing the save.

This repository holds **released world data only**. Canon, lore sources, tooling and
work in progress stay in the private `Dsar-Voyage/Astravael` repository.

## Current release

| Field | Value |
|---|---|
| World | Astravael: Nexara (`W1KX_CXxd4JS`) |
| Schema | Voyage V36 (`heroesVersion` 36) |
| Released | 2026-10-05 |
| Contents | Batches 81–82 (small-steps ability ladder) and the music fallback |
| Creator API revision | `wbwaTvZgEk5ZuORTMkkO3-8hqdV7UWXnrzYACc_ky6g` |

Full provenance, byte counts and SHA-256 hashes are in [`nexara/MANIFEST.json`](nexara/MANIFEST.json).

## Files

| File | What it is | Raw URL |
|---|---|---|
| `nexara/Astravael_Nexara.json` | The complete Creator API world document (`data.world`, including `initialGameState`). Byte-identical to the private production source. | [raw](https://raw.githubusercontent.com/Dsar-Voyage/Astravael-Nexara-update-repo/ccr-33d24ab8-74agcd/nexara/Astravael_Nexara.json) |
| `nexara/Astravael_Nexara.studio.json` | `initialGameState` only: the V36 world JSON exactly as the Studio editor presents a world. Use this for a paste-import into Studio. | [raw](https://raw.githubusercontent.com/Dsar-Voyage/Astravael-Nexara-update-repo/ccr-33d24ab8-74agcd/nexara/Astravael_Nexara.studio.json) |
| `nexara/MANIFEST.json` | Release metadata, source commit and SHA-256 hashes. | [raw](https://raw.githubusercontent.com/Dsar-Voyage/Astravael-Nexara-update-repo/ccr-33d24ab8-74agcd/nexara/MANIFEST.json) |

## Test procedure: pull the update into a private save

1. Open the save (or the private copy of the world) in Voyage Studio.
2. Fetch the world JSON from the raw URL above. Use `Astravael_Nexara.studio.json`
   when Studio expects the editor's world JSON; use `Astravael_Nexara.json` when the
   import path expects the Creator API document.
3. Import or paste it over the existing world content and let Studio validate.
4. Confirm the save still loads and the new content is present. Quick checks for this
   release:
   - the ability ladder grants a technique every five skill points;
   - music slots that were not re-hosted fall back to their original songs.
5. Record the result (works / fails, and the exact error if any) so the update path can
   be adopted or fixed.

Verify a download before importing it:

```sh
sha256sum Astravael_Nexara.json
# expected: see nexara/MANIFEST.json
```

## Updating this repository

Each new production release replaces the two JSON files and `MANIFEST.json` in one
commit. The manifest records the private source commit so every public release can be
traced back to the exact state that was published to Voyage.

## Notes

- The world document contains NPC hidden information, faction secrets and plot facts.
  Anything in this repository is readable by anyone.
- The document references one installed mod (`oDe5ickqJRiH`, version 1) and Voyage-hosted
  image and music URLs. Those assets are not mirrored here.
