# Provenance, fidelity, and caveats

What this skill is built from, how much weight each part carries, and where it must not be trusted.

## 1. Source works

Nine clusters, 401,072 words. `firsthand_ratio` = 0.79 (313,427 firsthand words in c01–c08;
*Meaning* excluded as mixed attribution). Word counts are post-cleaning — see §5.

| Cluster | Module | Work | Published | Words | Attribution | What it grounds |
| --- | --- | --- | --- | --- | --- | --- |
| `c01` | `sfs-lectures` | *Science, Faith and Society* (Riddell Memorial Lectures), with "Background and Prospect" added 1964 | 1946 / 1964 | 33,768 | firsthand | Origin narrative; discovery and verification; premisses of science; tradition and apprenticeship; General vs Specific Authority |
| `c02` | `lol-example-science` | *The Logic of Liberty*, Part I: The Example of Science (essays 1–6) | 1941–1948 | 36,183 | firsthand | Pure vs applied science; autonomy and self-government of science; the case against planning inquiry; the polemical register |
| `c03` | `lol-other-examples` | *The Logic of Liberty*, Part II: Other Examples (essays 7–10) | 1948–1951 | 44,066 | firsthand | Perils of inconsistency; span of central direction; profits and polycentricity; manageability of social tasks |
| `c04` | `pk1-art-of-knowing` | *Personal Knowledge*, Part One: The Art of Knowing | 1958 | 28,688 | firsthand | Objectivity; probability; order; skills and the tacit component |
| `c05` | `pk2-tacit-component` | *Personal Knowledge*, Part Two: The Tacit Component | 1958 | 80,512 | firsthand | Articulation; intellectual passions; conviviality; ideology critique |
| `c06` | `pk3-justification` | *Personal Knowledge*, Part Three: The Justification of Personal Knowledge | 1958 | 35,104 | firsthand | The fiduciary programme; critique of doubt; commitment |
| `c07` | `pk4-knowing-being` | *Personal Knowledge*, Part Four: Knowing and Being | 1958 | 34,838 | firsthand | Operational principles; knowing life; emergence and the rise of man |
| `c08` | `td-terry-lectures` | *The Tacit Dimension* (Terry Lectures 1962) | 1966 | 21,747 | firsthand | From-to knowing named; the four aspects of tacit knowing; the Meno paradox; emergence; a society of explorers |
| `c09` | `meaning-late` | *Meaning*, with Harry Prosch | 1975 | 86,166 | **mixed** | Late restatement; metaphor, art, myth, religion; late social register |

**Why *The Logic of Liberty* is two clusters.** Parts I and II are two domains — the defence of
scientific autonomy against the planners, and the general theory of social ordering — and they
measure differently: Part II runs a higher hedge:booster ratio (2.45 vs 2.01) and four times the
second-person share (4.1% vs 2.6%). The 0.1.0 release covered both in one 847-word module.

**Not yet covered.** The posthumous *Knowing and Being* (1969) essay collection, including "The
Republic of Science" (1962). Its doctrine is largely represented through the clusters above, but a
question turning on its specific formulations is outside this skill's attested range.

## 2. Fidelity tiers

Weight claims by tier. When the skill is uncertain, it should say which tier it is standing on.

**Tier A — doctrine attested across multiple works.** From-to structure of tacit knowing;
subsidiary/focal exclusion; indwelling; the fiduciary prefix; personal-not-subjective via universal
intent; symmetry-then-dedication; General vs Specific Authority; corporate vs spontaneous order and
polycentricity; opposition to the planning of science; moral inversion; transcendent ideals as
operative forces; freedom grounded in dedication rather than in doing as one pleases. Assert
without hedging.

**Tier B — attested in one work, stated in his own terms.** The three regions of the
tacit–articulate spectrum; the three functions of the intellectual passions; operational principles
and the levels argument; natural vs transnatural integration; frame-and-story in art; the
morphogenetic and quantum-automaton arguments; span-of-control arithmetic. Assert, with the source
available on request.

**Tier C — personal-belief provenance, left visible by Polanyi himself.** The late social claims in
*Meaning* carry his own note that they rest on his personal belief that the modes of intercourse he
observed in his part of science extend through all sciences. Keep that qualification visible when
reproducing them.

**Tier D — extrapolation.** Anything applied to a case Polanyi did not address, and everything
after 1976. The skill may extrapolate — that is what a perspective is for — but it must mark the
move: this is where the frame leads, not something he said.

## 3. Caveats

**Co-authorship confound (*Meaning*, 1975).** The book was edited and assembled with Harry Prosch,
whose hand is in the prose. Style features unique to it carry a confound. Trust the doctrine, which
is continuous with *Personal Knowledge*; do not treat its sentence rhythms as evidence of Polanyi's
own late style. The Prosch collaboration was later contested in the secondary literature over how
far the religious material represents Polanyi's own position — a further reason to keep chs. 9–10
at Tier B/C rather than Tier A.

**Quotations are inherited, not verified here.** The short phrases carried in the reference modules
were drawn from the published works, but page references have not been checked against print
editions in this release. Anyone quoting them in scholarship must verify them independently. The
skill should never manufacture a quotation to fill a gap; when the exact wording is not in the
modules, it paraphrases from the doctrine the frame supports, in character (see `SKILL.md`'s
retrieval-failure handling) — it does not narrate the gap or its own retrieval state. This row is a
record for the human reader, not a runtime instruction: the phrasing the persona actually uses when
a passage is not attested is specified once, in voice, in `SKILL.md`.

**Style statistics are descriptive, not normative.** The sentence-length and hedge-to-booster
figures in the cluster files and in `voice.md` characterize a register; they are not a target for
generation, and outputs should not be tuned to hit them. The measured block in `voice.md` is
calibration data for the host agent and is never spoken by the persona.

**The persona is a lens, not an oracle.** Polanyi held sharply contested positions — against the
planning of science, against the individualist formula of liberty, against reductive accounts of
mind and life. The skill's job is to state them at full strength in his terms. It is not evidence
that they are correct, and a user asking for a balanced survey should be given one rather than the
lens.

**No forgery.** The skill must not produce fabricated quotations, invented biography, or positions
attributed to Polanyi on matters he never addressed. Where the frame is being extended, the output
says it is being extended.

## 4. Reproducibility

Each cluster file follows a fixed shape, so new modules can be added without disturbing the
routing: **Register** (how this work sounds and why) → **chapter-by-chapter substance** →
**Apparatus this cluster owns** → **Moves to reproduce** → **Not this cluster** (the fence against
the eight siblings) → **Load for**. A contribution that keeps this shape and cites its source
edition can be merged without re-tuning `SKILL.md`.

## 5. Corpus preparation

Run with `persona-distiller/scripts/corpus_clean.py`, `persona-distiller/scripts/segment.py`, `persona-distiller/scripts/style_metrics.py`,
`persona-distiller/scripts/kwic.py`, `persona-distiller/scripts/cluster_budget.py` and `persona-distiller/scripts/discrimination_test.py` from the
`persona-distiller` toolkit. Two defects were found and repaired before any figure was measured;
had they gone unnoticed every number in this file would have been wrong.

- **Double-column scan merge in *The Logic of Liberty*.** Every word and phrase appeared twice
  ("it it used to be commonly assumed used to be commonly assumed"), which would have halved the
  measured lexical diversity and roughly doubled measured sentence length. Collapsed by a
  longest-run token-doubling pass: 154,946 → 84,802 words, ratio 0.547. The other four works were
  checked and needed no such pass (ratios 0.999–1.000). **Residual duplication survives in
  places** — the collapse is greedy, not exhaustive, and short doubled spans remain
  (`old· old-fashioned bourgeois reactionary' fashioned bourgeois reactionary'`).
- **Hyphenation damage** in *The Logic of Liberty* (568 sites) and *The Tacit Dimension* (664),
  repaired with `corpus_clean.py --fix`.

**Scan-quality caveat, *The Tacit Dimension*.** `c08` is the roughest scan in the corpus, with
character-level corruption visible throughout (`menninehalaat`, `tre-produce`, `sho ere mistaken`,
`éxpéct`). Its quotations are lower-confidence than the other four works and its lexical figures
are the softest in the set. Anyone quoting *The Tacit Dimension* from this package should check a
print edition first.

**Line-break artifacts affect two measured punctuation figures.** The em-dash rate in `c02`/`c03`
(0.22–0.25 per 1,000 words, against 2.66–4.62 elsewhere) is the scan rendering dashes as hyphens,
not a register feature. Do not tune to it.

## 6. Module budgets

Computed with `persona-distiller/scripts/cluster_budget.py`, nine sibling modules, `words_firsthand` = 313,427.
No FLOOR and no RECUT flag was raised, so every cluster earned its own module. Estimated tokens
below are words × 1.4.

| Module | Budget | Actual | Dev |
| --- | --- | --- | --- |
| `sfs-lectures` | 3,331 | 3,656 | +9.8% |
| `lol-example-science` | 3,456 | 3,806 | +10.1% |
| `lol-other-examples` | 3,765 | 4,132 | +9.7% |
| `pk1-art-of-knowing` | 3,321 | 3,488 | +5.0% |
| `pk2-tacit-component` | 3,583 | 3,364 | −6.1% |
| `pk3-justification` | 3,424 | 3,360 | −1.9% |
| `pk4-knowing-being` | 3,333 | 3,624 | +8.7% |
| `td-terry-lectures` | 3,305 | 3,477 | +5.2% |
| `meaning-late` | 3,410 | 3,606 | +5.7% |

All nine sit far below the 6,000-token module ceiling. Runtime load, not package size, is what
matters: one module loads at a time, two when a second ranks close.

```
loaded_worst_case = core 2,991 + two largest modules 7,938 + voice.md 3,784
                  + frameworks.md 2,417  =  17,130 tokens
```

**Core floor, flagged not padded.** `SKILL.md` measures 2,991 estimated tokens against a 3,000
floor — 0.3% short, inside the noise of a words × 1.4 estimator. It was left alone rather than
padded to clear an arbitrary line. A related finding is recorded here because it is the floor
procedure working as intended: *"we can know more than we can tell"* and *"a society of
explorers"*, Polanyi's two most quotable phrases, occur in **one cluster only** (`c08`, 6 hits).
The projection gate requires ≥2 independent clusters for core placement, so they stay in
`td-terry-lectures.md` and out of the core, however tempting the core would look with them.

## 7. Fidelity results (Stage 5)

**Quotation audit — pass.** Every quoted span in all nine cluster modules was checked
programmatically against that cluster's own corpus slice, normalizing for the scan's hyphenation
and word-merge artifacts: **116/116 verified**. In `voice.md`, **28/29** attested fragments verify
against the firsthand corpus; the one exception is a residual scan duplication, not a bad
quotation. Four anti-drift fragments were found to have drifted in wording during drafting and were
corrected to exact source text, and one sentence that could not be attested at all was replaced
with an attested one. This is what the audit is for.

**Style match — pass.** A 454-word sample generated in the polemical register scores within 15% of
the firsthand baseline on all seven core features (sentence mean −4.0%, median +8.3%, stdev
−13.7%, MATTR +9.0%, hedges +2.8%, boosters +4.5%, hedge:booster −1.5%). One deviation to note:
first-person share came in at 21.4% against a 55.5% baseline and ~41% for the polemical register.
At 454 words this figure is noisy, but it points the right way — generated output drifts toward
impersonal construction and should be pulled back toward first-person procedure.

**Discrimination — register claim passes, cluster claim does not.** Blind test, 24 name-masked
130-word passages, three per firsthand cluster, seed 1023.

| Distinction under test | Score | Threshold | Verdict |
| --- | --- | --- | --- |
| 3-way **register** (spoken-lecture / written-polemic / written-philosophical) | **0.83** (20/24) | 0.70 | pass |
| 9-way **cluster** | **0.58** (14/24) | 0.70 | fail |

The failure is informative rather than fatal, and it constrains how this package may describe
itself. No pair of clusters was confused twice — the error is diffuse, not a collapsed
distinction — and **6 of the 10 misses are two Parts of the same book**: Parts of *Personal
Knowledge* mistaken for each other, and Part I of *The Logic of Liberty* for Part II. Per-register
recall was 6/6 polemic, 10/12 philosophical, 4/6 spoken.

**What follows from that.** The nine modules are **topical routing inside three registers**, not
nine registers. Polanyi wrote *Personal Knowledge* as one book in one year in one voice; its four
Parts differ in subject matter and emphasis, not in separable register. The **Register** paragraph
opening each module should therefore be read as describing that Part's subject matter, emphasis and
measured drift within its register — not as a claim that a reader could identify the Part from a
blind passage. The register-level claim, which `voice.md` makes and routes on, is the one the corpus
supports at 0.83. Nothing in this package should assert nine distinguishable Polanyi voices.

**Reproduce it:**

```bash
python scripts/discrimination_test.py sample <firsthand-clusters>/ \
    --per-cluster 3 --length 130 --seed 1023 --mask-names --key key.json
python scripts/discrimination_test.py score key.json --answers c01 c02 ...
```


## README editorial review 2026-10-30

Scope: README and this appended editorial record only, following Persona-Distiller
revision `b515337` and its [README writing standard](https://github.com/ariel-lee-1023/persona-distiller/blob/b51533728bca2ac1e60303859378eec14e5dacfa/references/readme-experience.md). This is an editorial
update, not a persona rebuild or a new acceptance assessment. Biographical checks
below supply the introduction date only; the persona source corpus was not expanded.

- **Passage decisions:** Replace the capability-list opening with a concrete knowing act. Preserve source routing, co-authorship and quotation limits, and historical test distinctions. Replace the placeholder clone URL with the actual remote and retain the verified polanyi-perspective slug.
- **Runtime/evidence basis:** Frameworks §1 on subsidiary/focal awareness and §4 on personal versus subjective judgment, voice’s concrete-case movement, and Personal Knowledge modules pk1–pk3 support the hammer and laboratory inquiry.
- **Particularity:** The hammer’s subsidiary sensations lead to the personal responsibility in an apparently impersonal achievement; acknowledging trust does not make judgment arbitrary.
- **Encounter:** The laboratory prompt distinguishes explicit procedure from acquired discrimination and asks for actual examples.
- **Entry and language:** The clone command, complete activation texts, and inspected packager command are usable; source and maintainer routes are separated. English matches the declared default. Birth precision is deliberately limited to the undisputed month and year; the recorded 11/12 March conflict is visible.
- **Honesty:** The visible first-person opening is locally labeled as newly written
  reconstruction, not an authentic quotation or observed package output. Suggested
  prompts are labeled. Source gaps, historical test limitations, and existing Candidate
  status where applicable remain in the README; no assessment result is promoted.
- **Birth-date verification:** March 1891; exact day disputed. Source/locator: [Oxford Dictionary of National Biography, “Polanyi, Michael,” opening biographical paragraph](https://academic.oup.com/oxford-dictionary-of-national-biography/reference/63486/reference-article-abstract/581767242); compare [Royal Society record: 12 March](https://makingscience.royalsociety.org/people/na8008/michael-polanyi) and [Scott and Moleski, Early Years: 11 March](https://academic.oup.com/book/36398/chapter-abstract/320036558). Checked
  2026-10-30. No death date or lifespan range appears in the title or opening.

Runtime files, source/evidence packets, assessment inputs, saved outputs, and existing
validation records are preserved. New recognition calls: **0**. Package and README
checks for this pass are recorded below separately from historical assessments.

### Checks completed in this editorial pass

README opening placement, birth-date form, example labels, installation entry,
and 8 local links/anchors passed inspection; `git diff --check` passed.
Every other existing file remains byte-identical to the baseline, including the
core, references, evidence, assessment inputs, and saved results. Pre-existing
working-tree changes were preserved. The latest package validator reported
10 errors/1 warnings before and 10 errors/1 warnings after;
there are no new failure codes and no missing README-local paths. This is a
documentation pass, not a current package pass. Existing layout/runtime-route
issues remain outside this README task. Historical whole-package hashes that
included documentation continue to describe their original trees. Recognition
calls remain **0**.

## CI reference correction — 2026-10-31

The October README editorial record named an authoring-tool path in inline code,
which the repository link checker interpreted as a local runtime file. The record
now links to the exact external tool revision. No runtime, assessment, or validator
rule changed. Validation uses all four existing workflow steps, including packaging.

The exact workflow frontmatter, local-reference and required-file checks pass; the skill bundle builds successfully.


## README reading-order review — 2026-10-31

This is a documentation-only review under Persona Distiller's complete README
authoring rules. The existing first-person opening, birth-date precision,
attribution note and material opening qualifications are preserved. Existing situations were
retained or reorganized; navigation, a short installation entry, a file/loading table
and sources organized by contribution were added. Build statistics are linked here
instead of repeated in the reader's path. No conversation excerpts or sample answers
were added. The review used retained package materials, not new primary-source research.

Particularity continues through the orientation, concrete uses and source table;
uses cover distinct supported concerns without claiming observed outcomes. Entry
checks cover installation names, language, file links and navigation. Honesty checks
preserve source attribution, material limitations and actual assessment scope.

The runtime and historical assessments are unchanged; zero recognition calls were
made. The core retains a conditional route to fidelity-ledger/episodic.md for historical
queries. This pre-existing routing difference is recorded separately, not silently
repaired or presented as full compliance with the current runtime-separation standard.


### Completed checks for this README revision

The nail-driving opening is continued through laboratory apprenticeship, scientific autonomy, institutional coordination and artistic meaning. The source table traces personal judgment and responsibility while retaining Harry Prosch’s contribution to Meaning.

The review used a prepared tree based on committed baseline c5487ad1, excluding unrelated working-directory changes. All 31 README local links, including six navigation anchors in body order, resolve. The invocation name agrees with the existing frontmatter. Byte comparisons preserve the full opening and nearby qualifications, all earlier provenance text, and every other tracked file.

Local rendering with marked and Chrome in a GitHub-style layout was inspected at 1100 px and 390 px widths, including visual review of the opening, hierarchy, tables and source section. Body content does not overflow horizontally; wide tables and code blocks scroll within their own bounds. All six rendered navigation targets exist. This is a local compatible-renderer check, not a screenshot audit of the published GitHub page.

The current generic Persona Distiller package check reports FAIL both before and after, with existing findings C1, C1b, C2, C6, L2, S1, S2, S3, S4, S9. A comparison of individual findings adds no failure. These pre-existing runtime/layout issues are outside this documentation edit; this is not a claim that the whole package meets the newer structure standard. The generic validator is from Persona Distiller commit 3774ccc. Source/editorial review used retained materials and attribution records; it did not reread the original corpus. No recognition assessment ran, and the new recognition-call count is zero.

The repository workflow’s frontmatter, internal-reference and required-file checks also pass. Its package_skill.py builds the installable archive successfully in temporary storage; the archive is not added to the repository.
