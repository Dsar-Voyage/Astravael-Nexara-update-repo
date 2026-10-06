# Nexara release notes

Each release lists the sections that changed, so you can paste only those from
`sections/` into your save. Section names are the keys of the world JSON and match the
file names under `sections/`. The full machine-generated change table is in
[`SECTIONS.md`](SECTIONS.md).

Rule of thumb: paste **content** and **settings** sections; never paste **state** or
**meta** sections (see the category column in `SECTIONS.md`).

---

## 2026-10-05b — current release (batches 81–82 and the music fallback)

Published 2026-10-05, Creator API revision `wbwaTvZgEk5ZuORTMkkO3-8hqdV7UWXnrzYACc_ky6g`.

### Sections updated in this release

| Section | Why it changed |
|---|---|
| `abilities` | **Batch 82.** The ability curve was compressed into a small-steps ladder: a new technique every five skill points, so techniques arrive while they still matter. 840 of 841 abilities had their unlock thresholds rewritten. |
| `progressionSettings` | **Batch 82.** `abilityPointEveryLevels` and `traitPickEveryLevels` retuned to match the new ladder. |
| `worldLore` | **Batch 82.** The entry *Progression — How abilities grow on Nexara* rewritten for the new ladder. |
| `quests` | **Batch 81.** Eight quests turned into deliberate office jobs. Six quests replaced (new names below), two edited. |
| `questTriggers` | **Batch 81.** Generated progress triggers regenerated for the six replaced quests; two edited. |
| `triggers` | **Batch 81.** 19 triggers updated: quest unlock/done triggers for the replaced quests, three city chain triggers, two work offers and two quest-special triggers. |
| `locations` | **Batch 81.** Five locations reference the office-job quests: The Grand Waypoint, The Gray Rings, Relstaris City, Open Contract Hall, Orvessa Welfare District. |
| `factions` | **Batch 81.** House Orvessa, House Varriko and House Kathvar updated as the givers of the office jobs. |
| `aiInstructions` | **Batch 81.** Four blocks touched: `generateStory`, `generateInitialStart`, `generateNPCIntents`, `generateEncounters`. |
| `gameplayMusicSettings` | **Music fallback.** Slots whose songs were never re-uploaded to Voyage point to their original catbox URLs again, now that the host is back. |

Quests replaced in batch 81:

| Removed | Added |
|---|---|
| Relstaris — Across the Capitol Before Noon | Relstaris — A Shift at the Civic Desk |
| Relstaris — Before the Crews Split | Relstaris — The Signed Shift |
| Quilrath — Quiet Work Under Watch | Quilrath — A Day at the Permit Counter |
| Quilrath — Dalan's Mistake | Quilrath — The Corrected File |
| Solvraxis — Where the Reserves Went | Solvraxis — The Reserve Count |
| Helvyra — One Cargo, Three Routes | Helvyra — Three Signed Records |

Edited: *Solvraxis — The Misfiled Box*, *Study — The Agreement Nobody Can Find*.

### Minimum paste set

If your save is on the first 2026-10-05 publish, paste these ten files:
`abilities`, `progressionSettings`, `worldLore`, `quests`, `questTriggers`, `triggers`,
`locations`, `factions`, `aiInstructions`, `gameplayMusicSettings`.

---

## 2026-10-05a — first publish of 2026-10-05 (batches 75–80 and music day 2)

Published 2026-10-05, Creator API ETag `LziWh-SBzxyJJXOVJMUcVu-3-jTFTr4G1b_MKnlHpXw`.

| Section | Why it changed |
|---|---|
| `combatSettings` | **Batch 75.** Firearms made lethal: new damage types (plasma, energy, ballistic calibers) and damage-type presentation. |
| `itemTypes` | **Batch 75 / 78.** Firearm damage bonuses raised to +15..+30 and typed; Nexaran Credit described as plain Credits. 15 items. |
| `npcTypes` | **Batch 75.** 31 Starian NPC types immune to small-caliber ballistic rounds; species descriptions updated. |
| `resourceSettings` | **Batch 75.** Health rules adjusted for lethal firearms. |
| `traits` | **Batch 75.** *Starian* and *Starian aerial engagement* updated. |
| `npcs` | **Batch 75 / 77.** Every NPC: relationship moved to `initialRelationship` (new Voyage validator rule); courtship culture and orientation added. |
| `worldLore` | **Batch 76 / 77.** Starian wing references removed; species courtship cultures added. |
| `aiInstructions` | **Batches 75–80.** Direct party invitations, firearm impact rule, adventure-first rule with one paying giver, plain Credits, trimmed transaction tracking. |
| `quests` | **Batch 78 / 79.** All 58 quests rewritten to end on action with one paying giver; 22 renamed. |
| `questTriggers` | **Batch 79.** Regenerated for the renamed quests. |
| `triggers` | **Batch 79.** Quest and work-offer triggers updated for the renamed quests. |
| `storyStarts` | **Batch 80.** Bookkeeping compressed and hooks reopened in every start; the 19 most paperwork-heavy starts rewritten around people and stakes. |
| `locations` | **Batch 79 / 80.** 15 locations updated where quests and starts changed. |
| `factions` | **Batch 79.** All 36 factions updated as quest givers. |
| `gameplayMusicSettings` | **Music day 2.** More gameplay tracks re-hosted on Voyage. |

### Minimum paste set

If your save is on the 2026-10-03 publish, paste these seventeen files (this covers both
2026-10-05 releases): `abilities`, `aiInstructions`, `combatSettings`, `factions`,
`gameplayMusicSettings`, `itemTypes`, `locations`, `npcTypes`, `npcs`,
`progressionSettings`, `questTriggers`, `quests`, `resourceSettings`, `storyStarts`,
`traits`, `triggers`, `worldLore`.

---

## 2026-10-03 — first publication (through batch 74)

First time the world was published. Includes the character-creation and first 14
gameplay music tracks re-hosted on Voyage (batches 73–74) and everything before it.
No earlier published version exists, so there is no paste set for this release: import
the whole world.
