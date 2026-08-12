# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

For a skill, the version numbers mean:

- **MAJOR** — the persona's commitments, voice, or reading procedure change enough that outputs
  will read differently to someone who knows the previous version.
- **MINOR** — new reference modules, new example material, expanded coverage; existing behaviour
  preserved.
- **PATCH** — corrections to attributed phrasing, typos, routing-table fixes, documentation.

## [Unreleased]

### Changed
- **`provenance.md` moved out of `references/` into a new top-level `fidelity-ledger/` folder.**
  `references/` is loaded by the host agent at runtime, so the audit trail (sources, fidelity
  scores, caveats) now lives at `fidelity-ledger/provenance.md`, a sibling of `references/` rather
  than a member of it — structurally out of reach during embodiment, not just documented as
  off-limits. Content unchanged; only the path moved. `SKILL.md` and `README.md` updated to point
  at the new location.
- **`episodic.md` moved out of `references/` into `fidelity-ledger/`, alongside `provenance.md`.**
  Attested but lower-priority material is not reasoning the host agent should load
  mid-embodiment, so it belongs with the audit trail rather than the host-agent-facing package.
  Content unchanged; only the path moved, to `fidelity-ledger/episodic.md`. `SKILL.md` and
  `README.md` (including the repository-layout tree) updated to point at the new location.
- **Loading depth now states a real-world-retrieval rule, and distinguishes it from the two rules
  it could be confused with.** `references/` and `fidelity-ledger/` answer questions about
  Polanyi's own frameworks and voice — corpus-internal by design — and were never meant to stand in
  for a fact about the world he did not personally address: a quotation, a current event, the
  present state of a field. `SKILL.md` now says so explicitly, and names the distinction from
  anti-drift pair 7 in `voice.md` ("Confessing the search versus answering the case"): that rule
  bans *naming* the gap inside his sentences, it has never meant the underlying lookup should be
  skipped.

### Fixed
- **Retrieval-shaped character breaks, including borrowed-humility phrasing that still names the
  search.** A compiled instance broke character when a question quoted a passage more specific than
  the loaded clusters attest, narrating its own retrieval state ("I have my two retrievals for this
  turn... I should answer from what's genuinely supported rather than fabricate"). Root cause was
  two-fold: `provenance.md` carried an imperative line ("paraphrases and says so") that read as a
  runtime instruction rather than an audit note — fixed in `persona-distiller` and here — and this
  skill separately lacked any in-voice handling for the unattested-specific-quotation case, leaving nothing to route to
  besides the search-narrating fallback. Added a paragraph to `SKILL.md`'s "How I move in an
  exchange" and a new anti-drift pair (#7) to `voice.md` that name and ban the softer, in-character-
  sounding version of the same break — e.g. "I answer within my own frame rather than that
  quotation" — not just the blunt tool-voice version, since the softer form is the one most likely
  to pass a casual voice check.

### Planned
- Cluster module for the posthumous *Knowing and Being* (1969) essays, incl. "The Republic of Science".
- Trigger evals for the skill description, to measure under- and over-triggering.
- Page references against print editions for every quoted phrase in `references/`.

## [0.2.0] — 2026-08-12

The voice module the first release was missing, and every cluster module rebuilt to its computed
depth. Full corpus pass over all five works, cleaned and re-segmented.

### Added
- `references/voice.md` — the expressive system: sentence architecture, prohibitions derived from
  measured absence, trigger→shift register rules, a register-range routing table, the lexical
  fingerprint, opening and closing moves, a measured baseline over 313,427 words of firsthand text,
  and six generic-vs-Polanyi anti-drift sentence pairs. `SKILL.md`'s loading block now points to it
  before any sustained prose.
- `references/clusters/td-terry-lectures.md` — *The Tacit Dimension* (Terry Lectures 1962,
  published 1966): from-to knowing named, the four aspects of tacit knowing, the Meno paradox,
  emergence, a society of explorers. Its spoken-lecture register is measurably distinct from the
  written work.
- `references/clusters/lol-example-science.md` and `references/clusters/lol-other-examples.md` —
  *The Logic of Liberty* re-cut into its two Parts, which are two registers and two domains.
- An **Apparatus this cluster owns** section and a **Not this cluster** fencing section in every
  cluster module, so nine siblings no longer bleed vocabulary into each other.

### Changed
- Every cluster module rebuilt to the depth its budget asks for. The 0.1.0 modules ran 553–876
  words each, roughly a quarter of the computed budget; each now lands near its own target
  (3,305–3,765 tokens), with added attested constructs, moves and evidence rather than padding.
- `provenance.md` (then still under `references/`, later relocated to `fidelity-ledger/` — see
  [Unreleased]) — records the corpus cleaning pass, the segmentation into nine clusters, the
  per-cluster budgets, the measured style figures, and the new scan-quality caveats.
- `README.md` — layout and routing table updated for nine modules plus `voice.md`.

### Removed
- *references/clusters/lol-essays.md*, superseded by the two Part-level modules.

### Fixed
- Two corpus defects that would have corrupted every measured figure, had they gone unnoticed: a
  double-column scan of *The Logic of Liberty* in which each phrase appeared twice, and
  hyphenation damage across *The Logic of Liberty* and *The Tacit Dimension*. Both repaired before
  measurement; residual OCR corruption in *The Tacit Dimension* is now recorded as a caveat.

## [0.1.0] — 2026-07-23

Initial public release.

### Added
- `SKILL.md` — the persona core: what Polanyi will not concede, how he reads a question, how he
  moves in an exchange, how he sounds, and what he keeps returning to.
- `references/clusters/pk1-art-of-knowing.md` — *Personal Knowledge* Part One (chs. 1–4):
  objectivity, probability, order, skills.
- `references/clusters/pk2-tacit-component.md` — Part Two (chs. 5–7): articulation, intellectual
  passions, conviviality, the Marxism/Lysenko dossier.
- `references/clusters/pk3-justification.md` — Part Three (chs. 8–10): the logic of affirmation,
  the critique of doubt, commitment.
- `references/clusters/pk4-knowing-being.md` — Part Four (chs. 11–13): operational principles,
  knowing life, the rise of man.
- `references/clusters/sfs-lectures.md` — *Science, Faith and Society* (1946) with the 1964
  "Background and Prospect" retrospective.
- *references/clusters/lol-essays.md* (removed in 0.2.0) — *The Logic of Liberty* (1951): academic freedom,
  self-government of science, span of control, polycentricity, moral inversion.
- `references/clusters/meaning-late.md` — *Meaning* (1975, with Harry Prosch): from-to knowing,
  metaphor, art, myth, religion, the free society.
- `references/frameworks.md` — the named frameworks defined in compact form.
- `references/episodic.md` — attested but lower-priority material.
- `provenance.md` (then under `references/`, later relocated to `fidelity-ledger/` — see
  [Unreleased]) — sources, fidelity notes, and caveats.
- `scripts/package_skill.py` — builds an installable `.skill` bundle.
- Repository scaffolding: README, MIT license, `.gitignore`, CI structure check.

[Unreleased]: https://github.com/<your-username>/polanyi-perspective/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/<your-username>/polanyi-perspective/releases/tag/v0.2.0
[0.1.0]: https://github.com/<your-username>/polanyi-perspective/releases/tag/v0.1.0
