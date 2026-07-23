# polanyi-perspective

A Claude [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
that lets a model analyze questions of knowledge, science, society, art, and freedom through
**Michael Polanyi's** documented frame — locating the tacit, personal contribution inside every
impersonal-seeming achievement; testing doctrines for self-referential consistency; distinguishing
spontaneous from corporate order; and grounding freedom in dedication rather than in doing as one
pleases.

It is a *thinking lens*, not an impersonation service. See [Scope and limits](#scope-and-limits).

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
  concrete description before thesis; concepts named as they are minted.

## Repository layout

```
polanyi-perspective/
├── SKILL.md                        # the skill itself (YAML frontmatter + body)
├── references/
│   ├── frameworks.md               # the named frameworks, defined in Polanyi's terms
│   ├── episodic.md                 # attested but lower-priority material
│   ├── provenance.md               # sources, fidelity notes, caveats
│   └── clusters/                   # work-specific depth modules
│       ├── pk1-art-of-knowing.md   # Personal Knowledge, Part One   (chs. 1–4)
│       ├── pk2-tacit-component.md  # Personal Knowledge, Part Two   (chs. 5–7)
│       ├── pk3-justification.md    # Personal Knowledge, Part Three (chs. 8–10)
│       ├── pk4-knowing-being.md    # Personal Knowledge, Part Four  (chs. 11–13)
│       ├── sfs-lectures.md         # Science, Faith and Society (1946/1964)
│       ├── lol-essays.md           # The Logic of Liberty (1951)
│       └── meaning-late.md         # Meaning (1975, with Harry Prosch)
├── scripts/package_skill.py        # zips the folder into an installable .skill bundle
├── CHANGELOG.md
├── LICENSE
└── .github/workflows/validate.yml  # CI: checks structure and internal links
```

### Progressive disclosure

`SKILL.md` is what the agent always reads. Everything under `references/` is loaded **only when
the question calls for it** — that is the whole point of the split. Rough routing:

| If the question is about… | Load |
| --- | --- |
| Objectivity, probability, skill and craft, design vs randomness | `clusters/pk1-art-of-knowing.md` |
| Language, AI, incommensurability, ideology critique, academic culture | `clusters/pk2-tacit-component.md` |
| Justification, relativism, "isn't that just your belief?", professional independence | `clusters/pk3-justification.md` |
| Emergence, reductionism, mind–body, teleology, human dignity | `clusters/pk4-knowing-being.md` |
| Origin narrative, discovery, tradition and apprenticeship, master–pupil ethics | `clusters/sfs-lectures.md` |
| Institutional design, planning vs markets, academic freedom, coordination | `clusters/lol-essays.md` |
| Aesthetics, metaphor, myth, religion, meaning and nihilism | `clusters/meaning-late.md` |
| A term used precisely (from-to, indwelling, General Authority, polycentricity) | `references/frameworks.md` |
| Where a claim comes from and how much weight it bears | `references/provenance.md` |

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

**As a plain system prompt** — paste the body of `SKILL.md` (everything below the frontmatter)
into whatever prompt field you have, and paste in a cluster file when the topic warrants it.

## Usage

Invoke it by asking for the lens, not for the man:

- "Analyze the peer-review crisis through the Polanyi perspective."
- "What would a Polanyian read of LLM capability evaluations look like?"
- "Apply the corporate/spontaneous order distinction to this org chart."
- "Is 'alignment by explicit specification' vulnerable to the tacit-knowledge objection?"

The skill is deliberately *unhelpful* in one direction: it will not hand back a comfortable
half-way position, and it will often concede more than the objector expected before rebuilding on
the conceded ground.

## Scope and limits

- **This is a perspective, not a person.** The skill reconstructs a documented way of reasoning.
  It must not be used to forge quotations, to fabricate positions on questions Polanyi never
  addressed while presenting them as his, or to pass invented statements off as his real words.
- **Quotations are inherited, not verified here.** Short phrases carried in the reference modules
  come from the published works; anyone quoting them in scholarship should check them against a
  print edition. See `references/provenance.md`.
- **One book has a co-authorship confound.** *Meaning* (1975) was edited and assembled with Harry
  Prosch. Trust its doctrine (continuous with *Personal Knowledge*) more than its fine stylistic
  detail.
- **Polanyi died in 1976.** Anything he is made to say about events after that is extrapolation,
  and the skill should say so when it extrapolates.

## Contributing

Issues and pull requests are welcome, particularly:

- corrections to attributed phrasing, with a page reference to a print edition;
- new cluster modules for works not yet covered (e.g. *The Tacit Dimension*, *Knowing and Being*);
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
