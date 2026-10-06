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

## Per-section files (copy and paste)

The world is also split into **one file per section** under
[`nexara/sections/`](nexara/sections/). Each file holds exactly the value of that
section, so you can open it, copy everything, and paste it into the matching section of
the Studio editor without touching the rest of your save.

- [`nexara/SECTIONS.md`](nexara/SECTIONS.md) — every section with its category, size,
  and whether it changed in the last update or since the previous release. **Only paste
  `content` and `settings` sections. Never paste `state` or `meta` sections**, those are
  your save's own runtime data.
- [`nexara/CHANGES.md`](nexara/CHANGES.md) — release notes naming the sections each
  release changed, why, and the minimum set of files to paste.
- `nexara/releases/*.hashes.json` — per-section SHA-256 for each release, so a future
  release can list exactly what changed.

Sections updated in the current release (2026-10-05b): `abilities`,
`progressionSettings`, `worldLore`, `quests`, `questTriggers`, `triggers`, `locations`,
`factions`, `aiInstructions`, `gameplayMusicSettings`.

Raw URL pattern for a single section:

```
https://raw.githubusercontent.com/Dsar-Voyage/Astravael-Nexara-update-repo/ccr-33d24ab8-74agcd/nexara/sections/<section>.json
```

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

1. Copy the new production `Astravael_Nexara.json` over `nexara/Astravael_Nexara.json`.
2. Run the build script with the new label and the previous release's hash file:

   ```sh
   python3 tools/build_release.py --label <YYYY-MM-DD> \
       --previous nexara/releases/<previous-label>.hashes.json \
       --previous-doc /path/to/previous/Astravael_Nexara.json
   ```

   It rewrites the Studio variant, every `sections/*.json`, `SECTIONS.md` and the new
   `releases/<label>.hashes.json`, and prints which sections and entries changed.
3. Add a release entry to `nexara/CHANGES.md` and update `nexara/MANIFEST.json`.
4. Commit everything in one commit.

## Notes

- The world document contains NPC hidden information, faction secrets and plot facts.
  Anything in this repository is readable by anyone.
- The document references one installed mod (`oDe5ickqJRiH`, version 1) and Voyage-hosted
  image and music URLs. Those assets are not mirrored here.
