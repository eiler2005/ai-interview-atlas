# Changelog

[English](CHANGELOG.md) · [Русский](docs/ru/CHANGELOG.md)

## Unreleased — 2026-10-05: content expansion and source-aligned Leadership

### Added

- 18 EN/RU answer pairs, taking the priority set to 82 Engineering and 76 Leadership questions. Twelve answers deepen existing Engineering coverage; six support Leadership, including five new generated questions on portfolio allocation, vendor exit, management through managers, stopping investment and an incident without rollback.
- Reading for all 60 questions previously without it and primary reading for the five additions. The bank now contains 299 questions across 17 themes, all with EN/RU checklists and reading; 158 have written answers. The source registry grows from 207 to 247, with dates and scope limits.
- EN/RU coverage audits, a learning roadmap, specialised guides and a content expansion plan. The eight-week baseline tables remain intact; specialised routes focus on questions, explanations, checklists and reading. No Python exercise package, labs or automated evaluator was added.
- Official general TPM stages on Amazon's company page, kept separate from the secondary AI-PM path. General Director process research is documented with its scope limits; no new company is inferred from same-publisher material alone.

### Changed

- Three Google EM prompts now preserve their source's hypothetical versus actual-experience distinction; the Stripe strategic-hiring prompt now asks about a real past hire. Stable IDs and evidence kinds remain unchanged; tests, outlines and EN/RU answers were revised together.
- The existing generated hiring-redesign question gains priority L76 and an answer with stage-specific AI-tool policies, comparable conditions and calibration limits. Existing priorities retain their order.
- Audits distinguish their 294-question baseline from current additions. The 155-question Leadership semantic review and 20 source checks do not claim full factual verification of the current bank. The unavailable Meta EM report remains unverified on the new access attempt.
- New and revised public content was authored by actual GPT-6 Astra. Independent review is a separate step for these exact versions; historical review statements below apply to their dated content. Local PDF evidence still refers to the October 2 builds and does not establish publication of this expansion.

## Unreleased — 2026-10-02 checklists for every question, a third batch of answers and deeper answers

### Added
- Every question now has a three-point checklist of what a strong answer covers, in English and Russian. Until now only the priority questions and ten others had one; the 174 new checklists span all 17 themes, and behavioural ones coach how to choose and close your own example rather than suggesting a story.
- 30 written answers in English and Russian for a third batch of priority questions, raising the priority set from 55 to 70 per track. On the engineering track they cover latency metrics, FlashAttention, text-to-SQL over a large warehouse, a reported regression after a model upgrade, reversible agent actions, training memory and distributed training, GRPO, reward hacking, Constitutional AI, HyDE, accountability for AI-assisted code and three reasoning-model exercises. On the leadership track, chosen by the demand the radar shows, they cover initiative retrospectives, a delay caused by a misjudgement, a slipped upstream dependency, team scale, resolving a disagreement without discarding either side, chartering shared AI infrastructure, protected health data, refactoring, agent writes into an ERP, an MVP that is too expensive, enterprise discovery, moderation, the interpretability trade-off, shared data access and triaging a customer's hallucination complaint.
- 45 primary sources: papers behind the new checklists and answers, such as GPTQ, SmoothQuant, ALiBi, YaRN, RMSNorm, SwiGLU, CLIP, prefix and prompt tuning, DistServe and Sarathi-Serve, plus standards and guides such as NIST SP 800-226, the Standard Webhooks specification and PostgreSQL's transaction isolation.

### Changed
- 52 existing answers were reviewed for depth and accuracy, then deepened or corrected. Among the corrections: grouped-query attention pays off at large batch and long context, because small-batch decode is bound by reading the weights; a pure causal mask never fully masks a row; a model ten times the price wins only where review and error costs dominate; and a shared prefix cache is a timing side channel rather than a direct content leak.
- Answers may now run to 180 words, so that a deeper answer can still be said aloud in about a minute.
- Every answer written or revised since 2026-09-28, including the second batch, passed an independent review in a separate session.
- Russian checklists use the infinitive throughout, and «кеш» is spelled one way.
- The English text of two questions was corrected: the date-range prompt now lists all three phrasings from its source, and the speech-quality question no longer reads as if synthesised speech were a recognition metric.
- The roadmap, the learning path and the methodology reflect the new counts; the learning path places priorities 41–70 in its weekly plans.

## Unreleased — 2026-09-30 Russian numeral agreement in generated counts

### Changed
- The Russian home pages now inflect the noun after a count instead of always printing the genitive plural, so they read "294 вопроса" and "162 источника" rather than "294 вопросов" and "162 источников". The forms are chosen from the numeral, including the 11–14 exception, and a test pins them; the counts change on every build, so the wrong form would have returned.

## Unreleased — 2026-09-30 verified machine-learning loops at Spotify and GigaChat

### Added
- Spotify gains a machine-learning path, from a candidate's first-hand account of a loop that ended in an offer: a one-hour machine-learning screen, then an assessment day of data, values, system design and depth interviews. That author deliberately publishes no questions, so the company page still records none.
- SberDevices gains the generative-AI section of the senior NLP loop on GigaChat, from Sber's own preparation page: transformer architecture, supervised finetuning, pretraining, retrieval-augmented generation and RLHF. The page lists topics rather than questions and shows no date, which its source note states.

### Changed
- Spotify's summary no longer claims that its sources establish no dedicated loop, because the machine-learning path is now sourced.
- Four candidate reports on a preparation site, which would have upgraded four product questions to first-hand evidence, were examined and left out: those pages assemble their content in the browser, so the questions attributed to them could not be read and confirmed.

## Unreleased — 2026-09-30 second batch of answers

### Added
- 30 written answers, in English and Russian, for the next 15 priority questions on each track. On the engineering track they cover sparse expert routing and latent attention, prefix and paged KV caching, allocating a reasoning budget under a deadline, reranking and claim-level citations, MCP, agent memory and when to split work between agents, measuring unsupported claims and the faithfulness of a reasoning trace, a model-access API, a voice-agent latency budget and a minimal agent runner. On the leadership track they cover model choice, agent use cases, enterprise pricing, answer engines against search, evaluating an assistant without access to customer data, reviewing AI-written code, hiring and quality standards, the research-to-production boundary, research milestones, launch-readiness disputes, a voice contact-centre engagement, exceptions to a safety control, stakeholder conflict and difficult feedback. Each of those questions also gained a three-point checklist and primary reading, so priority questions per track rise from 40 to 55.
- Canva's interview policy as a company page, from two dated posts on its engineering blog, and two questions: staying accountable for code the model wrote, and redesigning a loop so that AI assistance still produces a hiring signal. The second is marked as generated, because no source shows it being asked.

### Changed
- Every source defined in the atlas is now referenced by content. The 18 sources that were defined but unused are wired into the reading of the questions they belong to, among them the EU AI Act, the supervisory letter on model risk management, the Model Context Protocol specification, the prompt-injection and lethal-trifecta write-ups, and the RoPE, Switch Transformer and DeepSeek-V2 papers.

## Unreleased — 2026-09-29 role pages with interview evidence

### Added
- The AI roles guide is generated from `src/content/roles.yaml`. Each of the six role families has its own page with what the role involves, how it is interviewed and the questions for it. Stages and questions count as reported for a role only when their source names the role; everything else is listed as practice.
- New taxonomy roles: forward deployed engineer, AI solutions architect, deployment strategist, AI evaluation engineer, and ML engineer or data scientist. The applied AI role no longer doubles as the forward deployed one.
- 32 questions from newly verified sources. They cover the AI-assisted build and review rounds Sierra introduced in 2026, Cursor's rounds in its own repository, and Anthropic's historical performance take-home and Research Fellowship brainstorm. They also cover Palantir's decomposition, learning and SQL rounds, forward deployed interviews at OpenAI, Anthropic and Cognition, and Russian ML and prompt-engineering interviews at Yandex, T-Bank and Tochka. Company pages separately describe interview stages and preparation guidance from Avito, SberDevices and MegaFon.
- Company pages for Sierra, Cursor, Ramp, Cognition, LangChain, MegaFon, SberDevices and Tochka. Palantir, Anthropic, OpenAI, Yandex, T-Bank and Avito gain role-specific stages. 33 sources added.

### Changed
- Job postings are a separate source kind, `posting`: they describe a role and can no longer be cited as evidence of an interview question or stage.
- The README names the largest compilation but links to its attribution on the sources page instead of the external repository.
- The methodology covers hiring-side accounts, archived official pages and generated "interview guide" sites. The Russian translation of the reasoning-models guide was corrected.

## Unreleased — 2026-09-29 reasoning, roles and source transparency

### Added
- Bilingual guides to reasoning models and six AI role families, with preparation priorities and links into the atlas.
- Five reasoning-model practice questions, explicitly marked as generated rather than reported interview questions.
- Primary reading and bilingual answer checklists for nine existing questions on post-training, retrieval, attention and multi-agent systems. Their secondary interview-evidence markers are unchanged.

### Changed
- The home pages disclose reliance on secondary guides and the concentration of questions in one compilation. Technical reading is distinguished from evidence that an employer asked a question.
- Contribution rules and validation reject repeated source URLs and identical question text, while preserving existing question IDs and combining evidence in one entry.
- Released PDF books are described as dated snapshots; they are not regenerated for this update.

## Unreleased — 2026-09-29 navigation, site and repository

### Added
- Every question has a stable anchor on its theme page. Start pages, answers, company pages and *Asked across companies* link each question to that entry, and a priority question also to its written answer.
- A generated map of the atlas (`docs/README.md`, `docs/ru/README.md`): tracks, themes, companies by segment and reference pages in one place. The README opens with a one-line menu.
- Answers pages open with contents grouped by theme; each answer links back to its checklist and to the contents. Theme and company pages have a breadcrumb to their section of the map and links to the previous and next page; company pages, and theme pages with more than one track section, have an *On this page* line.
- A searchable site built with MkDocs Material from the same pages, with an English menu and a Russian tab. The menu is built from the content, and the strict build fails if a page is missing from it. Deployment to GitHub Pages stays off until the maintainer enables it.
- Issue forms for proposing a question, reporting a correction and reporting an outdated source; every question on a theme page links to the correction form with its id filled in. A pull request template, code owners, a security policy and a code of conduct.
- A weekly source-freshness job that checks that cited URLs still resolve (sites that block automated checks are skipped) and keeps one issue listing the failures, and a release workflow that builds the PDF books into a draft release for the maintainer to inspect and publish.

### Changed
- CI runs on pull requests and on pushes to `main` rather than on every push, so a pull-request branch is no longer checked twice; superseded pull-request runs are cancelled and every action is pinned to a commit. Dependabot proposes monthly updates for actions and Python dependencies.
- A company page no longer links to itself in *Asked at*.

## Unreleased — 2026-09-28 continuation

### Changed
- Added the project title and descriptive text to the README banner; updated its alt text and image attribution.
- Added a bilingual learning path with role-specific priorities, eight-week practice plans, diagnostic checks and evidence-based completion gates; the project roadmap remains separate.
- Added a bilingual repository roadmap, separate from a personal preparation plan, with explicit limits on company evidence and source freshness.
- Completed 80 English written answers alongside 80 Russian answers and corrected technical and translation issues. All 160 texts passed independent content review; all four local PDF books passed text and visual production checks. Local files do not establish a new release or maintainer approval.
- Added a primary Faiss reference for the comparison of exact search, HNSW and IVF-PQ; the catalogue now contains 108 sources.
- Automated checks complement factual review; worktree, index and history privacy checks have distinct scopes.

## 2026-09-28 — A README that explains itself

### Changed
- The README is a landing page: what this is, who it is for, what is inside, why it differs from the usual question lists, and how to start in three steps. It is 103 lines instead of 322.
- The priority questions of each track moved to `docs/{lang}/start/{track}.md`, and the questions asked at two or more companies to `docs/{lang}/common.md`. Both are linked from the README, and a track's start page links its answers.
- Both PDF books open with the same summary as the README.

## 2026-09-28 — Written answers, in Russian first

### Added
- Written answers for 80 priority questions, 40 per track: one paragraph of 100-150 words that a candidate could say aloud — the point, the mechanism and its trade-off, what to do or measure, and where the answer stops holding. Each answer is presented as one good answer, not the reference answer.
- For `behavioral` and `self_presentation` questions an answer describes how to build your own account and what the interviewer is listening for; no invented stories, companies or numbers.
- Answers live in the `answer` field of the same content files and are rendered to separate pages (`docs/ru/answers/`) and a separate PDF edition, so the question pages and the main book stay unchanged for a first pass at answering yourself. PDF pagination depends on the build; local editions are not necessarily released assets.
- Answers start in one language: pages and the answers book for a language appear only once that language has answers. English answers follow in a later wave.

## 2026-09-28 — Printable PDF books

### Added
- `scripts/build_pdf.py` builds one PDF book per language from the same content with the Career Copilot document renderer: A4 pages, 12 pt body text, a contents page whose page numbers are checked against the rendered bookmarks, and clickable source links. The parts are the *Start here* questions for each track, every theme, company loops, the requirements radar with its chart, the methodology, attribution and sources.
- Answer checklists are printed once, in *Start here*; theme parts point to them by number. Emoji markers are printed as font glyphs (● confirmed by the company, ○ candidate report, † secondary, ‡ generated, ? assumption), and the build stops if the font lacks any character. Books, their Markdown sources and hash manifests are written to the ignored `dist/pdf/`.

## 2026-09-27 — First edition

### Added
- 255 bilingual questions across 17 themes: 191 in AI Engineering and 146 in AI Leadership, with overlap between tracks. Each track has 40 starting questions with answer outlines and reading.
- 20 company pages with sourced interview-loop claims, coding requirements and clearly labelled general-role baselines where specialist AI evidence is unavailable.
- 107 source records: 21 official sources, 9 participant reports, 17 preparation guides, 1 secondary compilation and 59 references. Of the questions, 245 cite interview sources and 10 are labelled as practice generated from published radar themes. References support reading, not claims that a question was asked.
- An aggregate requirements radar from 79 postings collected in September 2026: 62 leadership and 17 engineering. Only leadership theme counts are published; engineering is below the minimum track size of 20, and cells below five postings are suppressed.
- Content schema for tracks, roles, themes, sources, companies, questions and the requirements radar, with provenance rules enforced at build time.
- Generator for bilingual README, theme, company, radar and source pages plus a static radar SVG; `--check` fails on stale pages, broken local links and missing Russian pages.
- Methodology, attribution and contribution guides in English and Russian; privacy hooks and CI that reuse the Career Copilot checker and Gitleaks.

### Limits
- Preparation guides and compilation tags remain secondary evidence, not first-hand confirmation. General software or product interview guides do not establish an AI-specific loop; source-check dates do not guarantee a current process for every team.
- The radar is a small, nonrepresentative sample weighted towards international fintech and business software. It measures requirements in retained postings, not current hiring availability or the whole market. Only anonymised aggregates are published.
