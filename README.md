# polanyi-perspective

A [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
that lets a model analyze questions of knowledge, science, society, art, and freedom through
**Michael Polanyi's** documented frame — locating the tacit, personal contribution inside every
impersonal-seeming achievement; testing doctrines for self-referential consistency; distinguishing
spontaneous from corporate order; and grounding freedom in dedication rather than in doing as one
pleases.

---

## What it does

Loaded into a compatible agent, the skill supplies:

- **A stable point of view** — the commitments Polanyi refused to concede, stated in his own terms.
- **A reading procedure** — look for the tacit coefficient first; test every doctrine on itself;
  concede the symmetry, then locate the difference; convert order questions into
  ordering-principle questions.
- **An example bank** — the hammer, the pianist, the cyclist, the map, the judge, Columbus,
  the jigsaw puzzle, the Azande poison-oracle, Lysenko 1948, Bukharin at Easter 1935.
- **A voice** — long periodic sentences gathering qualifications and landing on a short verdict;
  concrete description before thesis; concepts named as they are minted. `references/voice.md`
  carries the full expressive system, including the register shifts between the polemical,
  philosophical and spoken-lecture settings, and a measured baseline computed over 313,000 words
  of firsthand text.

## Repository layout

```
polanyi-perspective/
├── SKILL.md                        # the skill itself (YAML frontmatter + body)
├── references/                          # host-agent-facing, loaded at runtime, never contains
│   │                                    #   provenance or episodic material
│   ├── voice.md                    # the expressive system + measured baseline
│   ├── frameworks.md               # the named frameworks, defined in Polanyi's terms
│   └── clusters/                        # work-specific depth modules
│       ├── sfs-lectures.md              # Science, Faith and Society (1946/1964)
│       ├── lol-example-science.md       # Logic of Liberty, Part I  (essays 1–6, 1941–48)
│       ├── lol-other-examples.md        # Logic of Liberty, Part II (essays 7–10, 1948–51)
│       ├── pk1-art-of-knowing.md        # Personal Knowledge, Part One   (chs. 1–4)
│       ├── pk2-tacit-component.md       # Personal Knowledge, Part Two   (chs. 5–7)
│       ├── pk3-justification.md         # Personal Knowledge, Part Three (chs. 8–10)
│       ├── pk4-knowing-being.md         # Personal Knowledge, Part Four  (chs. 11–13)
│       ├── td-terry-lectures.md         # The Tacit Dimension (Terry Lectures 1962/1966)
│       └── meaning-late.md              # Meaning (1975, with Harry Prosch)
├── fidelity-ledger/                     # human-facing, never loaded by the host agent
│   ├── provenance.md               # sources, fidelity notes, caveats
│   └── episodic.md                 # attested but lower-priority material
├── scripts/package_skill.py        # zips the folder into an installable .skill bundle
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md                       # what is distilled here, and what is not
├── .gitignore
└── .github/workflows/validate.yml  # CI: checks structure and internal links
```

### Progressive disclosure

Before the first substantive reply, the agent reads `SKILL.md`, `references/voice.md`
and `references/frameworks.md` in full, including for short answers. Additional work
modules are loaded when the question calls for them. Rough routing:

| If the question is about… | Load |
| --- | --- |
| Objectivity, probability, skill and craft, design vs randomness | `clusters/pk1-art-of-knowing.md` |
| Language, AI, incommensurability, ideology critique, academic culture | `clusters/pk2-tacit-component.md` |
| Justification, relativism, "isn't that just your belief?", professional independence | `clusters/pk3-justification.md` |
| Emergence, reductionism, mind–body, teleology, human dignity | `clusters/pk4-knowing-being.md` |
| Origin narrative, discovery, tradition and apprenticeship, master–pupil ethics | `clusters/sfs-lectures.md` |
| Autonomy of science, planned research, the 1930s–40s attack on pure inquiry | `clusters/lol-example-science.md` |
| Institutional design, planning vs markets, span of control, polycentricity | `clusters/lol-other-examples.md` |
| From-to knowing named, the Meno paradox, emergence, a society of explorers | `clusters/td-terry-lectures.md` |
| Aesthetics, metaphor, myth, religion, meaning and nihilism | `clusters/meaning-late.md` |
| Every activation; expression, register, prohibitions, cadence | `references/voice.md` |
| Every activation; precise concepts (from-to, indwelling, General Authority, polycentricity) | `references/frameworks.md` |
| Where a claim comes from and how much weight it bears | `fidelity-ledger/provenance.md` |

## Activation

Before the first substantive answer, read the complete [SKILL.md](SKILL.md),
[voice](references/voice.md) and [frameworks](references/frameworks.md), including for
short replies. The core supplies the perspective, voice supplies its expressive
system, and frameworks supplies its conceptual and reasoning distinctions. Reuse files
already fully retained in context; reload missing files after compaction. Add topic,
work or mode modules when relevant. For a chat without file access, supply all three
complete texts at the start.

This loading-only update has not been reassessed. Existing assessment results remain
attached to the runtime inputs and scope originally tested.

## Installation

**Claude Code / agents that read a skills directory** — clone into your skills folder:

```bash
git clone https://github.com/<your-username>/polanyi-perspective.git ~/.claude/skills/polanyi-perspective
```

**As a bundled `.skill` file** — build one and upload it wherever your client accepts skills:

```bash
python scripts/package_skill.py .
# → polanyi-perspective.skill
```

**As a plain system prompt:** supply the body of `SKILL.md` (everything below the frontmatter)
together with the complete `references/voice.md` and `references/frameworks.md`. Add a cluster
file when the topic warrants it.


## Scope and limits

- **Quotations are inherited, not verified here.** Short phrases carried in the reference modules
  come from the published works; anyone quoting them in scholarship should check them against a
  print edition. See `fidelity-ledger/provenance.md`.
- **One book has a co-authorship confound.** *Meaning* (1975) was edited and assembled with Harry
  Prosch. Trust its doctrine (continuous with *Personal Knowledge*) more than its fine stylistic
  detail.


## Contributing

Issues and pull requests are welcome, particularly:

- corrections to attributed phrasing, with a page reference to a print edition;
- new cluster modules for works not yet covered (e.g. the posthumous *Knowing and Being*, 1969);
- eval prompts that expose places where the lens drifts into generic philosophizing.

Please keep every claim traceable to a source. A pull request that improves fluency at the cost of
provenance will be declined.

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. It does not extend to any referenced source books, which remain the property of their respective copyright holders.

## Acknowledgements

Built on the work of Michael Polanyi (1891–1976): *Science, Faith and Society* (1946),
*The Logic of Liberty* (1951), *Personal Knowledge* (1958), *The Tacit Dimension* (1966),
and *Meaning* (1975, with Harry Prosch).
