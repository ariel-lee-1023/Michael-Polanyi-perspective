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

### Planned
- Cluster module for *The Tacit Dimension* (1966).
- Cluster module for the posthumous *Knowing and Being* (1969) essays, incl. "The Republic of Science".
- Trigger evals for the skill description, to measure under- and over-triggering.
- Page references against print editions for every quoted phrase in `references/`.

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
- `references/clusters/lol-essays.md` — *The Logic of Liberty* (1951): academic freedom,
  self-government of science, span of control, polycentricity, moral inversion.
- `references/clusters/meaning-late.md` — *Meaning* (1975, with Harry Prosch): from-to knowing,
  metaphor, art, myth, religion, the free society.
- `references/frameworks.md` — the named frameworks defined in compact form.
- `references/episodic.md` — attested but lower-priority material.
- `references/provenance.md` — sources, fidelity notes, and caveats.
- `scripts/package_skill.py` — builds an installable `.skill` bundle.
- Repository scaffolding: README, MIT license, `.gitignore`, CI structure check.

[Unreleased]: https://github.com/ariel-lee-1023/Polanyi-perspective/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ariel-lee-1023/Polanyi-perspective/releases/tag/v0.1.0
