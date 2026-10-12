# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring it.

This repo is **single-context**: one `GLOSSARY.md` at the root, and ADRs in `docs/adr/` once the first one is written.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root.
- **`docs/adr/`**, once it exists.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill creates them lazily when terms or decisions actually get resolved.

## File structure

```
/
├── GLOSSARY.md
├── docs/adr/
│   ├── 0001-...md
│   └── 0002-...md
└── .scratch/
```

## Use the glossary's vocabulary

When your output names a domain concept (SOP, LOR, POI, qualifying exam, etc.) in an issue title, a draft, or a note, use the term as defined in `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language this repo doesn't use (reconsider), or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0003 (target only US programs), but worth reopening because…_
