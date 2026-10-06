#!/usr/bin/env python3
"""Build the per-section release files for the Nexara update repository.

Reads the full Creator API world document, writes:
  nexara/Astravael_Nexara.studio.json      initialGameState only (Studio editor JSON)
  nexara/sections/<section>.json           one file per top-level initialGameState section
  nexara/releases/<label>.hashes.json      SHA-256 of every section for this release
  nexara/SECTIONS.md                       section guide with change flags

Usage:
  python3 tools/build_release.py --label 2026-10-05b \
      [--previous nexara/releases/2026-10-05a.hashes.json] \
      [--previous-doc /path/to/previous/Astravael_Nexara.json] \
      [--older nexara/releases/2026-10-03.hashes.json]

--previous is the immediately preceding release (drives the "changed in last
update" column). --previous-doc, when given, is that release's full document and
adds entry-level counts (added / removed / modified). --older may be repeated for
earlier releases and adds one extra "changed since <label>" column each.
"""
import argparse, hashlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "nexara", "Astravael_Nexara.json")
STUDIO = os.path.join(ROOT, "nexara", "Astravael_Nexara.studio.json")
SECTIONS_DIR = os.path.join(ROOT, "nexara", "sections")
RELEASES_DIR = os.path.join(ROOT, "nexara", "releases")
GUIDE = os.path.join(ROOT, "nexara", "SECTIONS.md")

# category, one-line description. Categories:
#   content   authored world content; safe to paste into a save to update it
#   settings  rules and instructions the engine reads; safe to paste
#   state     per-save runtime state; NEVER paste over an existing save
#   meta      platform bookkeeping; leave alone
SECTIONS = {
    "abilities": ("content", "Every ability and technique, with unlock levels and effects"),
    "aiInstructions": ("settings", "Narrator and engine instruction blocks (story, dialogue, NPC behaviour, starts)"),
    "arcs": ("content", "Long narrative arcs the engine can run"),
    "attributeSettings": ("settings", "Attribute definitions and modifiers"),
    "authorSeeds": ("content", "Writing-style seeds the narrator can draw on"),
    "characterArchetypes": ("content", "Archetype templates for generated characters"),
    "characterCreationMusic": ("settings", "Music family used during character creation"),
    "characterCreationSettings": ("settings", "Character creation steps, options and dependencies"),
    "characters": ("state", "The player characters in this save"),
    "chatLog": ("state", "The save's conversation log"),
    "combatSettings": ("settings", "Damage types, combat rules and presentation"),
    "death": ("settings", "What happens when a character is downed or dies"),
    "embeddingDimension": ("meta", "Vector size for retrieval embeddings"),
    "embeddings": ("state", "Retrieval embeddings the engine rebuilds itself"),
    "encounterElements": ("content", "Building blocks for generated encounters"),
    "endGame": ("settings", "Ending narration for win, loss and neutral endings"),
    "engineState": ("state", "Tick counter, phase and seed of the running save"),
    "factions": ("content", "Houses, companies and groups with standing and secrets"),
    "gameConfig": ("meta", "Platform identifiers for the world and save slot"),
    "gameModes": ("content", "Selectable play modes and their narrator instructions"),
    "gameSettings": ("settings", "Difficulty, turn timer, PvP and sync options"),
    "gameplayMusicSettings": ("settings", "Gameplay music tracks and variants"),
    "heroesVersion": ("meta", "World schema version (36)"),
    "imageModelSource": ("settings", "Image model used for generated art"),
    "imagePromptConfiguration": ("settings", "Prompt routing rules for portraits and scenes"),
    "itemSettings": ("settings", "Item categories, equipment slots and rules"),
    "itemTypes": ("content", "Every item: weapons, armor, tools, consumables, currency"),
    "locationArchetypes": ("content", "Archetype templates for generated locations"),
    "locationSettings": ("settings", "Location behaviour rules"),
    "locations": ("content", "Every authored location with descriptions and hidden info"),
    "memoryBank": ("state", "The save's accumulated memories"),
    "mods": ("meta", "Installed mods (one: oDe5ickqJRiH)"),
    "nameFilterSettings": ("settings", "Name filtering rules"),
    "narrativeEvents": ("content", "Scheduled and milestone narrative events"),
    "narratorStyle": ("settings", "Narrator voice and style"),
    "npcTypes": ("content", "Species and role types used for generated NPCs"),
    "npcs": ("content", "Every authored NPC, with personality, relationships and hidden info"),
    "otherSettings": ("settings", "Miscellaneous numeric settings (NPC health)"),
    "partyState": ("state", "Where the party is and who is in it"),
    "premadeCharacters": ("content", "The premade player characters"),
    "progressionSettings": ("settings", "Levelling cadence: ability points, trait picks"),
    "questTriggers": ("content", "Progress triggers generated for each quest"),
    "quests": ("content", "Every quest with giver, stakes and payment"),
    "randomNames": ("content", "Random name pools by species and culture"),
    "realms": ("content", "Realm definitions (one realm: Nexara)"),
    "regionArchetypes": ("content", "Archetype templates for generated regions"),
    "regions": ("content", "The map regions and their areas"),
    "relationshipStages": ("settings", "The seven relationship stages"),
    "resourceSettings": ("settings", "Health and other resource rules"),
    "skillSettings": ("settings", "Skill system rules"),
    "skills": ("content", "Every skill"),
    "stateEdited": ("state", "Flag that the save state was edited"),
    "storySettings": ("settings", "World background text the narrator reads"),
    "storyStarts": ("content", "Every story start"),
    "successLevelSettings": ("settings", "Success tiers and their prompts"),
    "summaryState": ("state", "The save's summary streams"),
    "systemResults": ("state", "Last engine task results"),
    "tipSettings": ("settings", "Loading and gameplay tips"),
    "traitCategories": ("settings", "Trait category definitions"),
    "traits": ("content", "Every trait"),
    "triggerWritable": ("state", "Trigger storage written during play"),
    "triggers": ("content", "Every scripted trigger"),
    "turnData": ("state", "Per-turn data for the save"),
    "uiState": ("state", "Remaining tips and other UI state"),
    "worldLore": ("content", "Every lore entry"),
}

def sha(b): return hashlib.sha256(b).hexdigest()

def dumps(v):
    return json.dumps(v, ensure_ascii=False, indent=2) + "\n"

def entry_key(e):
    if isinstance(e, dict):
        for k in ("id", "shortId", "name", "title", "key"):
            if k in e: return str(e[k])
    return json.dumps(e, sort_keys=True)

def detail(a, b):
    """Entry-level change summary between two versions of one section."""
    if a is None: return "new section"
    if a == b: return ""
    if isinstance(a, list) and isinstance(b, list):
        A = {entry_key(x): x for x in a}; B = {entry_key(x): x for x in b}
    elif isinstance(a, dict) and isinstance(b, dict):
        A, B = a, b
    else:
        return "value changed"
    add = [k for k in B if k not in A]; rem = [k for k in A if k not in B]
    mod = [k for k in A if k in B and A[k] != B[k]]
    parts = []
    if add: parts.append(f"{len(add)} added")
    if rem: parts.append(f"{len(rem)} removed")
    if mod: parts.append(f"{len(mod)} of {len(A)} modified")
    return ", ".join(parts), add, rem, mod

def count(v):
    return len(v) if isinstance(v, (list, dict)) else 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True, help="release label, e.g. 2026-10-05b")
    ap.add_argument("--previous", help="hashes.json of the immediately preceding release")
    ap.add_argument("--previous-doc", help="full world document of the preceding release (adds entry counts)")
    ap.add_argument("--older", action="append", default=[], help="hashes.json of an earlier release (repeatable)")
    args = ap.parse_args()

    doc = json.load(open(FULL, encoding="utf-8"))
    igs = doc["data"]["world"]["initialGameState"]
    unknown = sorted(set(igs) - set(SECTIONS))
    if unknown:
        print("WARNING: sections without a description, add them to SECTIONS:", unknown, file=sys.stderr)

    with open(STUDIO, "w", encoding="utf-8") as f: f.write(dumps(igs))

    os.makedirs(SECTIONS_DIR, exist_ok=True); os.makedirs(RELEASES_DIR, exist_ok=True)
    for stale in os.listdir(SECTIONS_DIR):
        if stale.endswith(".json") and stale[:-5] not in igs: os.remove(os.path.join(SECTIONS_DIR, stale))
    hashes = {}
    for k, v in igs.items():
        body = dumps(v).encode("utf-8")
        with open(os.path.join(SECTIONS_DIR, f"{k}.json"), "wb") as f: f.write(body)
        hashes[k] = {"sha256": sha(body), "bytes": len(body), "entries": count(v)}
    rel = {"label": args.label, "worldShortId": doc["data"]["world"].get("shortId"),
           "creatorApiRevision": doc["data"].get("revision"), "sections": hashes}
    with open(os.path.join(RELEASES_DIR, f"{args.label}.hashes.json"), "w", encoding="utf-8") as f: f.write(dumps(rel))

    prev = json.load(open(args.previous))["sections"] if args.previous else None
    prev_label = json.load(open(args.previous))["label"] if args.previous else None
    prev_doc = json.load(open(args.previous_doc, encoding="utf-8"))["data"]["world"]["initialGameState"] if args.previous_doc else None
    olders = [json.load(open(p)) for p in args.older]

    def changed(h, k): return h is None or k not in h or h[k]["sha256"] != hashes[k]["sha256"]

    lines = [f"# Nexara sections — release {args.label}", "",
             "One file per section of the world JSON, under `sections/`. Each file holds exactly the",
             "value of that section, so it can be pasted straight into the matching section of the",
             "Studio editor. Sizes are for the pretty-printed file.", "",
             "**Category** tells you whether a section is safe to paste over an existing save:", "",
             "- **content** — authored world content. Paste to update.",
             "- **settings** — rules and instructions. Paste to update.",
             "- **state** — the save's own runtime state. **Never paste these into a save you want to keep.**",
             "- **meta** — platform bookkeeping. Leave alone.", ""]
    cols = ["Section", "Category", "Entries", "Size", f"Changed in last update ({prev_label or 'n/a'} → {args.label})"]
    cols += [f"Changed since {o['label']}" for o in olders]
    cols.append("What it is")
    lines.append("| " + " | ".join(cols) + " |"); lines.append("|" + "---|" * len(cols))
    def size(n): return f"{n/1024:.0f} KB" if n < 1024*1024 else f"{n/1024/1024:.1f} MB"
    order = sorted(igs, key=lambda k: ({"content":0,"settings":1,"meta":2,"state":3}[SECTIONS.get(k,("content",""))[0]], k))
    last_changed = []
    for k in order:
        cat, desc = SECTIONS.get(k, ("content", ""))
        flag = "yes" if (prev is not None and changed(prev, k)) else ("—" if prev is None else "")
        if prev is not None and changed(prev, k):
            last_changed.append(k)
            if prev_doc is not None:
                d = detail(prev_doc.get(k), igs[k])
                if isinstance(d, tuple) and d[0]: flag = f"yes ({d[0]})"
        row = [f"`{k}`", cat, str(hashes[k]["entries"]), size(hashes[k]["bytes"]), flag]
        row += [("yes" if changed(o["sections"], k) else "") for o in olders]
        row.append(desc)
        lines.append("| " + " | ".join(row) + " |")
    lines += ["", f"## Sections changed in the last update ({prev_label} → {args.label})", ""]
    lines += [f"- `{k}`" for k in last_changed] or ["- none"]
    for o in olders:
        lines += ["", f"## Sections changed since {o['label']}", ""]
        lines += [f"- `{k}`" for k in order if changed(o["sections"], k)] or ["- none"]
    with open(GUIDE, "w", encoding="utf-8") as f: f.write("\n".join(lines) + "\n")

    if prev_doc is not None:
        print("Entry-level detail for the last update:")
        for k in last_changed:
            d = detail(prev_doc.get(k), igs[k])
            if isinstance(d, tuple):
                s, add, rem, mod = d
                print(f"  {k}: {s}")
                if add: print("    added:", add[:30])
                if rem: print("    removed:", rem[:30])
                if mod and len(mod) <= 40: print("    modified:", mod)
    print(f"wrote {len(igs)} sections, {GUIDE}, {args.label}.hashes.json; last update changed: {last_changed}")

if __name__ == "__main__":
    main()
