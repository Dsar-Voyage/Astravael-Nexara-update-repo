# Nexara sections — release 2026-10-05b

One file per section of the world JSON, under `sections/`. Each file holds exactly the
value of that section, so it can be pasted straight into the matching section of the
Studio editor. Sizes are for the pretty-printed file.

**Category** tells you whether a section is safe to paste over an existing save:

- **content** — authored world content. Paste to update.
- **settings** — rules and instructions. Paste to update.
- **state** — the save's own runtime state. **Never paste these into a save you want to keep.**
- **meta** — platform bookkeeping. Leave alone.

| Section | Category | Entries | Size | Changed in last update (2026-10-05a → 2026-10-05b) | Changed since 2026-10-03 | What it is |
|---|---|---|---|---|---|---|
| `abilities` | content | 841 | 699 KB | yes (840 of 841 modified) | yes | Every ability and technique, with unlock levels and effects |
| `arcs` | content | 1 | 1 KB |  |  | Long narrative arcs the engine can run |
| `authorSeeds` | content | 19 | 6 KB |  |  | Writing-style seeds the narrator can draw on |
| `characterArchetypes` | content | 22 | 10 KB |  |  | Archetype templates for generated characters |
| `encounterElements` | content | 48 | 15 KB |  |  | Building blocks for generated encounters |
| `factions` | content | 36 | 95 KB | yes (3 of 36 modified) | yes | Houses, companies and groups with standing and secrets |
| `gameModes` | content | 14 | 97 KB |  |  | Selectable play modes and their narrator instructions |
| `itemTypes` | content | 343 | 251 KB |  | yes | Every item: weapons, armor, tools, consumables, currency |
| `locationArchetypes` | content | 18 | 9 KB |  |  | Archetype templates for generated locations |
| `locations` | content | 164 | 2.3 MB | yes (5 of 164 modified) | yes | Every authored location with descriptions and hidden info |
| `narrativeEvents` | content | 36 | 69 KB |  |  | Scheduled and milestone narrative events |
| `npcTypes` | content | 61 | 215 KB |  | yes | Species and role types used for generated NPCs |
| `npcs` | content | 379 | 2.0 MB |  | yes | Every authored NPC, with personality, relationships and hidden info |
| `premadeCharacters` | content | 20 | 33 KB |  |  | The premade player characters |
| `questTriggers` | content | 57 | 35 KB | yes (6 added, 6 removed, 2 of 57 modified) | yes | Progress triggers generated for each quest |
| `quests` | content | 58 | 97 KB | yes (6 added, 6 removed, 2 of 58 modified) | yes | Every quest with giver, stakes and payment |
| `randomNames` | content | 2 | 10 KB |  |  | Random name pools by species and culture |
| `realms` | content | 1 | 8 KB |  |  | Realm definitions (one realm: Nexara) |
| `regionArchetypes` | content | 23 | 16 KB |  |  | Archetype templates for generated regions |
| `regions` | content | 400 | 572 KB |  |  | The map regions and their areas |
| `skills` | content | 186 | 67 KB |  |  | Every skill |
| `storyStarts` | content | 94 | 395 KB |  | yes | Every story start |
| `traits` | content | 1826 | 1.8 MB |  | yes | Every trait |
| `triggers` | content | 2030 | 2.1 MB | yes (19 of 2030 modified) | yes | Every scripted trigger |
| `worldLore` | content | 629 | 890 KB | yes (1 of 629 modified) | yes | Every lore entry |
| `aiInstructions` | settings | 18 | 367 KB | yes (4 of 18 modified) | yes | Narrator and engine instruction blocks (story, dialogue, NPC behaviour, starts) |
| `attributeSettings` | settings | 10 | 1 KB |  |  | Attribute definitions and modifiers |
| `characterCreationMusic` | settings | 1 | 0 KB |  |  | Music family used during character creation |
| `characterCreationSettings` | settings | 1 | 0 KB |  |  | Character creation steps, options and dependencies |
| `combatSettings` | settings | 7 | 1 KB |  | yes | Damage types, combat rules and presentation |
| `death` | settings | 2 | 4 KB |  |  | What happens when a character is downed or dies |
| `endGame` | settings | 3 | 1 KB |  |  | Ending narration for win, loss and neutral endings |
| `gameSettings` | settings | 5 | 0 KB |  |  | Difficulty, turn timer, PvP and sync options |
| `gameplayMusicSettings` | settings | 2 | 21 KB | yes (1 of 2 modified) | yes | Gameplay music tracks and variants |
| `imageModelSource` | settings | 1 | 0 KB |  |  | Image model used for generated art |
| `imagePromptConfiguration` | settings | 4 | 15 KB |  |  | Prompt routing rules for portraits and scenes |
| `itemSettings` | settings | 4 | 1 KB |  |  | Item categories, equipment slots and rules |
| `locationSettings` | settings | 9 | 0 KB |  |  | Location behaviour rules |
| `nameFilterSettings` | settings | 366 | 77 KB |  |  | Name filtering rules |
| `narratorStyle` | settings | 1 | 2 KB |  |  | Narrator voice and style |
| `otherSettings` | settings | 2 | 0 KB |  |  | Miscellaneous numeric settings (NPC health) |
| `progressionSettings` | settings | 13 | 2 KB | yes (2 of 13 modified) | yes | Levelling cadence: ability points, trait picks |
| `relationshipStages` | settings | 7 | 0 KB |  |  | The seven relationship stages |
| `resourceSettings` | settings | 5 | 6 KB |  | yes | Health and other resource rules |
| `skillSettings` | settings | 14 | 1 KB |  |  | Skill system rules |
| `storySettings` | settings | 2 | 6 KB |  |  | World background text the narrator reads |
| `successLevelSettings` | settings | 2 | 7 KB |  |  | Success tiers and their prompts |
| `tipSettings` | settings | 5 | 6 KB |  |  | Loading and gameplay tips |
| `traitCategories` | settings | 14 | 44 KB |  |  | Trait category definitions |
| `embeddingDimension` | meta | 1 | 0 KB |  |  | Vector size for retrieval embeddings |
| `gameConfig` | meta | 21 | 1 KB |  |  | Platform identifiers for the world and save slot |
| `heroesVersion` | meta | 1 | 0 KB |  |  | World schema version (36) |
| `mods` | meta | 1 | 0 KB |  |  | Installed mods (one: oDe5ickqJRiH) |
| `characters` | state | 0 | 0 KB |  |  | The player characters in this save |
| `chatLog` | state | 0 | 0 KB |  |  | The save's conversation log |
| `embeddings` | state | 2003 | 35 KB |  |  | Retrieval embeddings the engine rebuilds itself |
| `engineState` | state | 6 | 0 KB |  |  | Tick counter, phase and seed of the running save |
| `memoryBank` | state | 1 | 0 KB |  |  | The save's accumulated memories |
| `partyState` | state | 18 | 0 KB |  |  | Where the party is and who is in it |
| `stateEdited` | state | 1 | 0 KB |  |  | Flag that the save state was edited |
| `summaryState` | state | 2 | 0 KB |  |  | The save's summary streams |
| `systemResults` | state | 8 | 0 KB |  |  | Last engine task results |
| `triggerWritable` | state | 0 | 0 KB |  |  | Trigger storage written during play |
| `turnData` | state | 0 | 0 KB |  |  | Per-turn data for the save |
| `uiState` | state | 2 | 6 KB |  |  | Remaining tips and other UI state |

## Sections changed in the last update (2026-10-05a → 2026-10-05b)

- `abilities`
- `factions`
- `locations`
- `questTriggers`
- `quests`
- `triggers`
- `worldLore`
- `aiInstructions`
- `gameplayMusicSettings`
- `progressionSettings`

## Sections changed since 2026-10-03

- `abilities`
- `factions`
- `itemTypes`
- `locations`
- `npcTypes`
- `npcs`
- `questTriggers`
- `quests`
- `storyStarts`
- `traits`
- `triggers`
- `worldLore`
- `aiInstructions`
- `combatSettings`
- `gameplayMusicSettings`
- `progressionSettings`
- `resourceSettings`
