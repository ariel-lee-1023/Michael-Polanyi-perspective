# Think with Michael Polanyi

I am Michael Polanyi (March 1891; exact day disputed). Consider what happens
when you drive a nail. You attend to the nail while relying on the feel of the
hammer in your hand; turn your whole attention to those sensations, and the
movement which they served may become clumsy. You have not merely collected
information about a tool. You have learned to use it in attending to something else.

I approach an apparently impersonal achievement with that dependence in view.
A scientist recognizes a promising problem, a musician finds a phrase, a judge
discerns the bearing of a precedent. Their rules matter, but someone must
understand and apply them. To acknowledge that personal contribution is to
accept responsibility for a judgment which may be mistaken and nevertheless
claims to be true.

If you ask me to remove all trust before inquiry can begin, I shall ask what
you are already trusting in order to make the demand. Bring a procedure which
is supposed to replace judgment, or a discovery whose value cannot yet be
demonstrated to everyone. We can examine the commitments that make either
intelligible, and the freedom needed to pursue them responsibly.

*This introduction is a newly written, source-grounded persona reconstruction,
not a historical quotation. [Editorial and birth-date notes](fidelity-ledger/provenance.md#readme-editorial-review-2026-10-30).*

This perspective draws on Polanyi's writings about knowledge, science, freedom,
and meaning. It offers a documented philosophical position, including contested
commitments; it does not turn tacit knowledge into a reason to exempt expertise
from examination.


Follow the personal judgment within an apparently impersonal achievement, and the commitments and institutions that let that judgment answer to truth.

[Uses](#what-to-bring) · [Getting started](#getting-started) · [Files and loading](#files-and-loading) · [Sources](#sources-and-contributions) · [Scope and status](#scope-and-current-status) · [License](#license)

## What to bring

**Suggested first prompt:**

> Our laboratory has a detailed procedure, but new researchers still cannot
> distinguish a promising result from an artifact as experienced colleagues do.
> Here are two examples and the training process. What are the rules conveying,
> and what must be learned through guided practice and judgment?

The inquiry follows what the practitioner attends from and attends to, how
examples train discrimination, and which standards make judgment responsible.
A useful account must explain why a novice's difficulty does not disappear
merely by adding more sentences to the manual.

Other questions connect this dependence to different concerns:

- **A research program whose value cannot yet be demonstrated to every funder:**
  Bring the proposed work, the community's standards and the form of oversight.
  Examine how independent inquiry coordinates and what central direction would replace.
- **An organization that works without one director:** Identify how participants
  adjust to one another and which tasks do require a common command. Distinguish
  spontaneous from corporate order instead of treating every institution alike.
- **A claim that all belief is arbitrary:** State the claim and the grounds offered
  for accepting it. Test whether it can account for its own claim to truth and for
  the difference between personal responsibility and private preference.
- **A metaphor or work of art whose meaning disappears in a literal inventory:**
  Bring the passage or description. Examine how particulars are integrated and what
  an account of meaning must preserve, with the collaborative authorship of *Meaning*
  kept in view.

These contemporary uses extend the writings; they are not recorded Polanyi
conversations or demonstrated outcomes.

## Getting started

```sh
git clone https://github.com/ariel-lee-1023/Michael-Polanyi-perspective.git polanyi-perspective
```

Install the cloned root in your file-based skill host under `polanyi-perspective`, keeping
[SKILL.md](SKILL.md) and the complete [references](references/) together.
Invoke `polanyi-perspective` through your host's skill selector, or ask it to use this perspective with one of the situations above.

Responses default to **English**. Explicitly request another language, for example
“Answer in Chinese for this conversation,” to change it for that scope. A message
written in another language alone does not change the default.

### Loading and manual configuration

Before the first substantive response, including a short answer, read the complete
[core](SKILL.md), [voice](references/voice.md) and [frameworks](references/frameworks.md).
The core alone is incomplete. Keep complete texts already in context and reload any
lost after compaction. Add relevant topic or work modules as the question requires.
For a chat without file access, supply those three complete texts and the relevant
module yourself. Maintenance and assessment records are not ordinary conversation inputs.

For a client that accepts a `.skill` archive, the included packager can create one:

```sh
python3 scripts/package_skill.py . -o polanyi-perspective.skill
```

The repository name differs from the skill name: the installed entry is `polanyi-perspective`.

## Files and loading

These are file responsibilities and loading relationships, not a fixed sequence of thought.

| File or entry | What it provides | When it is used |
| --- | --- | --- |
| [Core](SKILL.md) | Perspective, language and operating instructions | Read in full at setup |
| [Voice](references/voice.md) | Expression, register and interaction | Read in full at setup |
| [Frameworks](references/frameworks.md) | Concepts, methods and conditional judgments | Read in full at setup |
| [Topic and source modules](references/clusters/) | Evidence, examples and work-specific distinctions | Load when relevant to the question |
| [Maintenance records](fidelity-ledger/) | Provenance, editorial history and assessment evidence | Outside the ordinary conversation prompt |

## Sources and contributions

The source sequence runs from Polanyi's wartime lectures and essays to the late
collaboration *Meaning*. The nine modules separate contributions within books as well
as between them; nine clusters do not imply nine independently distinguishable voices.

| Question or concern | Work, authorship and period | Contribution and reference |
| --- | --- | --- |
| How is scientific judgment learned? | Michael Polanyi, *Science, Faith and Society* (1946; retrospective addition 1964) | Tradition, apprenticeship and the authority of a scientific community. [Lectures](references/clusters/sfs-lectures.md) |
| How can inquiry coordinate without a director? | Polanyi, *The Logic of Liberty*: essays of 1941–1951 | Scientific autonomy and the distinction between spontaneous and corporate order. [Science](references/clusters/lol-example-science.md); [other institutions](references/clusters/lol-other-examples.md) |
| What is personal in skill and discovery? | Polanyi, *Personal Knowledge* (1958), Parts One and Two | The art of knowing, tacit participation and intellectual passions. [Knowing](references/clusters/pk1-art-of-knowing.md); [tacit component](references/clusters/pk2-tacit-component.md) |
| How can a fallible judgment claim truth? | *Personal Knowledge*, Part Three | Belief, doubt, responsibility and universal intent. [Justification](references/clusters/pk3-justification.md) |
| What do levels of explanation leave to one another? | *Personal Knowledge*, Part Four | Mind, emergence and operational principles. [Knowing and being](references/clusters/pk4-knowing-being.md) |
| How do particulars become instruments of understanding? | Polanyi, *The Tacit Dimension*: Terry Lectures (1962; published 1966) | From-to knowing and the discovery of problems. [Tacit dimension](references/clusters/td-terry-lectures.md) |
| How do art, myth and religion carry meaning? | Michael Polanyi with Harry Prosch, *Meaning* (1975) | Late extensions of integration; the prose is collaborative, not unmediated evidence of Polanyi's individual style. [Meaning](references/clusters/meaning-late.md) |

The [provenance ledger](fidelity-ledger/provenance.md) gives the edition inventory,
OCR issues and attestation work. Cross-source synthesis and modern applications remain
distinct from each source's own claims.

## Scope and current status

**Historical, limited checks; broad conversational fidelity remains unestablished.**
The source classification check met its threshold for three registers but not for all
nine clusters. One short generated polemical sample passed its recorded style comparison.
Those are scoped diagnostics, not an independent demonstration of a complete persona.
Later loading changes have not been reassessed, and this README adds no recognition result.

The available voices include spoken lectures, polemical writing and sustained
philosophical argument. *Meaning* carries Harry Prosch's contribution. Short quotations
need the relevant edition before scholarly reuse. Modern applications require current
facts, and tacit knowledge does not exempt expertise from examination.

See [provenance](fidelity-ledger/provenance.md) for source boundaries, measurements
and historical results. File checks verify organization; source-based editorial review
addresses attribution; diagnostics and recognition answer different questions. The core
retains an older optional route to [historical episodes](fidelity-ledger/episodic.md)
for particular historical queries; the setup above does not preload that record or any
assessment data. This README leaves that runtime route and assessment inputs unchanged.

## License

[MIT](LICENSE) © 2026 Ariel Lee covers the original repository material,
not the source books. The full corpus is not distributed. See [NOTICE](NOTICE.md).
