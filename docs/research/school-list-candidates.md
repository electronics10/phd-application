# Candidate PhD program list — draft for issue #2

Research note for GitHub issue #2 ("School list: compile ~10-12 candidate programs"), a child of the wayfinder map (#1). Access dates below are **2026-10-15** unless stated otherwise. This file verifies the named-person hypothesis list from the earlier advisory conversation against each person's current, official university page, and proposes a final candidate list.

Legend: **[FACT]** = directly sourced from a primary/official page, with citation. **[INFER]** = my synthesis across sources, not stated verbatim anywhere. **[REC]** = a recommendation/judgment call, not a fact.

Variant A = USCT wave inversion / FWI SOP (issue #3). Variant B = photonic inverse design SOP (issue #4).

---

## 0. Headline result

Of the 14 named people in the original hypothesis list, **all but two resolved to a current, verifiable, PhD-admitting university affiliation** — but three of them had moved institutions since the list was first drawn up, and two (both at Los Alamos National Laboratory) could not be tied to any PhD-admitting university appointment at all, consistent with the brief's own caveat about LANL. One named person (Christian Böhm/Boehm at ETH) could not be confirmed as currently active in any faculty role. One named person ("Marty") turned out to be a graduate student in the ETH group, not a PI.

**Final list: 10 program entries across 8 institutions.** Distribution: **4 Europe-based entries (Imperial x2 departments, ETH, DTU) / 6 US-based entries** (WashU, UT Austin, UNC, Stanford, Princeton, MIT). **This diverges from the applicant's own 5-6/5-6 Europe/US target** — see §4 for why, and §5 for what it would take to close the gap honestly rather than by padding.

**Correction log (2026-10-15, user review):** (1) University of Rochester/Duric dropped per the applicant's own fit judgment — too medical-oriented for the methodological framing wanted, not a factual error in the original entry. (2) The original Villa (UT Austin) entry's "POI contact norm: unconfirmed" was wrong — the user found Villa's own lab page stating the opposite directly. See §1.4 and §7 for what that miss was and what a targeted re-check of the remaining entries did and didn't turn up.

---

## 1. Variant A — USCT wave inversion / FWI

### 1.1 Imperial College London

Two separate departments are active in ultrasound tomography via the joint **TRUST (Transmission and Reflection Ultrasound Tomography)** group, which spans Earth Science & Engineering and Bioengineering ([Imperial TRUST group page](https://www.imperial.ac.uk/earth-science/research/research-groups/transmission-and-reflection-ultrasound-tomography-trust/), accessed 2026-10-15). Because UK PhD admission in STEM is department-specific (separate admissions page, separate POI-contact norms even within one university), I list these as two program entries.

**(a) Dept. of Earth Science & Engineering**
- **[FACT]** PIs: **Mike Warner** — Professor of Geophysics since 2000, research interests list full-waveform seismic inversion and "medical FWI" explicitly ([Imperial profile, profiles.imperial.ac.uk/9951-mike-warner](https://profiles.imperial.ac.uk/9951-mike-warner), accessed 2026-10-15). **Lluís Guasch** — now **Associate Professor in Seismic and Medical Imaging** (title confirmed current via the TRUST people page, not stale as the brief's caveat suggested might be the case). **Óscar Calderón Agudo** — Advanced Research Fellow, PI of the EU QUSTom breast-imaging project ([Imperial news item](https://imperial.ac.uk/news/237156/new-project-revolutionise-detection-breast-cancer), accessed 2026-10-15; TRUST people page).
- Variant A.
- **[FACT]** Deadline: Imperial PhD applications are rolling year-round (4 intakes/year), but scholarship deadlines cluster Nov–Mar; President's PhD Scholarship Round 1 for the 2025/26 cycle closed 4 Nov 2024 ([Imperial scholarships search results], accessed 2026-10-15). **[INFER]** Proxy for Fall 2027: expect an early-November 2026 scholarship round, though the general application itself has no hard deadline.
- **[FACT]** POI contact: explicitly **required** — ESE's own PhD guidance tells applicants to contact a potential supervisor and confirm willingness/project fit *before* submitting the formal application; the online application should only be submitted "after the potential academic supervisor has expressed sufficient interest" (Imperial ESE PhD opportunities/apply pages, accessed 2026-10-15; consistent with the UK-norms finding already in `docs/research/phd-application-procedure.md` §5).

**(b) Dept. of Bioengineering**
- **[FACT]** PI: **Meng-Xing Tang** — Professor of Biomedical Imaging, joined 2006, professor since 2018, founder of the Ultrasound Laboratory for Imaging and Sensing (ULIS) ([Imperial faculty page, imperial.ac.uk/people/mengxing.tang](https://www.imperial.ac.uk/people/mengxing.tang/research.html); tanglab.bg.ic.ac.uk, accessed 2026-10-15). **[FACT, bonus]** A fourth TRUST PI not in the original hypothesis list, **Carlos Cueto Mondéjar** (Assistant Professor in AI and Fluid Flow Imaging), also surfaced during verification — worth adding to any direct-contact shortlist.
- Variant A.
- Deadline/POI-contact norms: same rolling-admission, POI-contact-expected pattern as (a) — Imperial's Bioengineering doctoral "apply" page gives the same instruction (cited already in `phd-application-procedure.md` §5).

**Tooling note:** Imperial's TRUST group is also the origin of **Stride**, the open-source USCT platform built on Devito — confirming this is the live center of gravity for the sub-community ([Stride paper, Computer Methods and Programs in Biomedicine, 2022], via arXiv:2110.03345, accessed 2026-10-15).

### 1.2 ETH Zürich — Dept. of Earth Sciences

- **[FACT]** PI: **Andreas Fichtner** — Professor of Seismology and Wave Physics, on the Earth Sciences faculty since 2013, leads the Computational Seismology Group; research centers on wave-propagation tools and full-waveform inversion; co-founder of the ETH spin-off Mondaic, which commercializes FWI software (multiple third-party academic sources corroborate the title and group; the official ethz.ch/erdw page did not load directly in this research — **flagged as needing a direct re-check** before relying on it).
- **[INFER/FLAG]** **Christian Böhm (Boehm)**, named in the original hypothesis list, could **not** be confirmed as currently active anywhere. The most recent trace found was as an examiner on a 2022 ETH doctoral thesis in Fichtner's group; no current faculty page, no current LinkedIn/company bio, nothing tying him to Mondaic or another institution was found. **Treat as stale/unconfirmed — do not list as a current contact** without direct re-verification (e.g., his own ORCID or a current ETH group page).
- **[INFER/FLAG]** "**Marty**" from the original list is most likely **Patrick Marty**, who appears in a Fichtner talk slide as a member of the "Seismology & Wave Physics Group" alongside Fichtner, Böhm, and Ines Ulrich — this reads as a **PhD student or postdoc, not a PI**. Reclassified: not a contact target, but useful circumstantial evidence the group has (or had) active PhD students.
- Variant A.
- **[FACT]** Deadline: none in the US sense — ETH's own doctorate brochure states the first step is finding an ETH professor willing to supervise; the applicant only applies to the Doctoral Administration once that agreement exists, and the supervisor must endorse the application (ETH doctorate brochure; cited already in `phd-application-procedure.md` §2.2/§5).
- **[FACT]** POI contact: **structurally required** — this is not a courtesy, it is a gating admission step (same source).

### 1.3 Washington University in St. Louis — Mallinckrodt Institute of Radiology (Imaging Sciences) / McKelvey School of Engineering, Dept. of Electrical & Systems Engineering

- **[FACT — STALE ORIGINAL, UPDATED]** The brief named "Anastasio (UIUC)." **Mark Anastasio is no longer at UIUC.** A 2025 WashU McKelvey Engineering announcement states he returns **effective Feb 1, 2026** as the **Mallinckrodt Endowed Professor in Imaging Sciences** at the Mallinckrodt Institute of Radiology, **and** a Professor of Electrical & Systems Engineering in McKelvey Engineering, serving as Vice Chair of Imaging Science & AI Research in MIR ([WashU McKelvey Engineering news, "New faculty to join McKelvey Engineering for 2025-26 academic year"], accessed 2026-10-15). Since today's date (2026-10-15) is after the stated Feb 1, 2026 effective date, this move should already be in effect.
- **[REC]** Apply via whichever route the lab's PhD students actually come through — likely the Electrical & Systems Engineering PhD (McKelvey) rather than a clinical radiology-sciences track, but this needs direct confirmation with the department before treating it as settled, since dual appointments like this often have one "home" department for admissions purposes.
- Variant A.
- **[INFER/FLAG]** Deadline not independently confirmed for this specific PhD track; WashU engineering PhD cycles commonly run Dec–Jan for Fall entry, consistent with the general US pattern in `phd-application-procedure.md` §2.1, but this is an inference, not a verified date — check the ESE department's own page directly.
- POI contact norm: not independently confirmed; **[INFER]** likely optional/committee-based per the general US pattern.

### 1.4 University of Texas at Austin — Oden Institute for Computational Engineering and Sciences (CSEM graduate program)

- **[FACT]** PI: **Umberto Villa** — Research Associate Professor and Core Faculty at the Oden Institute, joined 2022 from a research-assistant-professor post at WashU (Electrical & Systems Engineering); co-developer of **hIPPYlib**, a toolkit for large-scale PDE-constrained deterministic and Bayesian inverse problems (Oden Institute directory listing; JOSS paper on hIPPYlib with Noemi Petra and Omar Ghattas, accessed 2026-10-15). This confirms the original hypothesis as current.
- **[INFER]** Fit note: Villa's work (adjoint-based PDE-constrained inversion, uncertainty quantification) is a strong **methodological** match to the applicant's MS-thesis identity, even though CSEM is not itself USCT-specific — it's the most "pure methods" program on this list and could anchor either SOP variant depending on framing.
- **[FACT]** Deadline: CSEM's own page lists a **December 10, 2026** deadline for **Fall 2027 entry**, and states the GRE is not required ([Oden/CSEM application page, oden.utexas.edu], accessed 2026-10-15) — this is an actual current-cycle date, not a proxy.
- **[FACT — CORRECTED 2026-10-15]** POI-contact norm: **direct email contact is explicitly invited**, not unconfirmed/committee-based as originally written here. Villa's own page ([uvilla.github.io/available_positions.html](https://uvilla.github.io/available_positions.html), accessed 2026-10-15) asks prospective PhD students interested in either the **BME or CSEM** PhD programs to email him directly with a CV, transcripts, a brief statement of research interests, and their linear algebra/numerical methods/optimization/programming background. The page does not say this is required before applying, but it is a clear, direct, standing invitation — the opposite of "committee-based, no named-advisor contact." **[FACT]** The page also surfaces a second admissions route not in the original entry: **BME (Biomedical Engineering) PhD**, not only CSEM — worth checking which department's requirements (GRE, prerequisites) fit better. **Root cause of the original miss:** the first research pass checked the Oden Institute/CSEM program page and a JOSS co-authorship paper, but not Villa's own personal site, which is where PI-level contact norms actually live when a PI states one explicitly.

### 1.5 University of North Carolina at Chapel Hill — School of Data Science and Society (undergoing a 2026 reorganization into a "Division of Data Science and Society" within a School of Data and Information Sciences, per a July 2026 job posting — name is in flux)

- **[FACT — RESOLVES THE LANL CAVEAT]** The brief's own instruction was to check whether LANL-affiliated names "have PhD-student-supervising affiliations via a partner university." **Youzuo Lin** is the answer: after 12+ years as a staff scientist in LANL's Geophysics group, he joined UNC's School of Data Science and Society as an **Associate Professor in July 2024** ([UNC Data Science faculty page, datascience.unc.edu/person/youzuo-lin](https://datascience.unc.edu/person/youzuo-lin/), accessed 2026-10-15). His research is physics-informed/deep learning for computational wave imaging, explicitly including breast-cancer ultrasound.
- Variant A.
- **[INFER/FLAG]** Deadline not independently confirmed; the department's recent renaming may also have changed or be changing its admissions pages — check directly before relying on any date found elsewhere.
- POI-contact norm: not confirmed; **[INFER]** likely optional/committee-based, US norm.

---

## 2. Variant B — Photonic inverse design

### 2.1 Stanford University — Dept. of Electrical Engineering (courtesy appointment in Applied Physics)

- **[FACT]** PI: **Jelena Vučković** — Jensen Huang Professor of Global Leadership; primary appointment **Professor of Electrical Engineering**, courtesy appointment in Applied Physics; leads the Nanoscale and Quantum Photonics Lab ([Stanford profile, profiles.stanford.edu/jelena-vuckovic], accessed 2026-10-15). Confirms the original hypothesis as current.
- **[INFER]** Department-precision note: because her primary appointment is EE, PhD applicants should apply through **Electrical Engineering**, not Applied Physics, to have a direct path to her group — the courtesy appointment alone would not normally carry admissions rights.
- Variant B.
- **[FACT]** Deadline: the Fall 2026 cycle deadline was **Dec 2, 2025** (EE) — already closed; Stanford's own FAQ states Fall 2027 dates are "not yet determined" as of this research (ee.stanford.edu/admissions/phd/faq, accessed 2026-10-15). **[INFER]** Proxy: expect an early-December 2026 deadline for Fall 2027 entry.
- POI-contact norm: not confirmed directly; **[INFER]** US committee-based norm, likely optional.

### 2.2 Princeton University — Dept. of Electrical and Computer Engineering

- **[FACT]** PI: **Alejandro Rodriguez** — now **Associate Professor** of Electrical and Computer Engineering (promoted from Assistant Professor since joining in 2013); also Director of the Program in Materials Science and Engineering and co-founder/CTO of Maxwell Labs; leads the Nanophotonics Design and Computation Group ([Princeton ECE department page; arodriguez.princeton.edu], accessed 2026-10-15). Confirms and updates the original hypothesis (title had changed since the list was drawn up).
- Variant B.
- **[FACT]** Deadline: Fall 2026 PhD deadline was **Dec 15, 2025** (closed); Princeton's Graduate School states the Fall 2027 application **opens September 2026** ([gradschool.princeton.edu application-deadlines page], accessed 2026-10-15). **[INFER]** Proxy: expect a mid-December 2026 deadline.
- POI-contact norm: not confirmed directly; **[INFER]** US committee-based norm.

### 2.3 MIT — Dept. of Mathematics (Applied Mathematics)

- **[FACT]** PI: **Steven G. Johnson** — Professor of Applied Mathematics, confirmed current via the MIT Mathematics directory, which also notes he is "on sabbatical leave" this fall semester ([math.mit.edu directory], accessed 2026-10-15) — relevant for responsiveness to outreach emails in the near term, not for PhD admission itself (which is committee-based). Co-maintains **Meep**, the open-source FDTD electromagnetics/adjoint-method simulation tool — directly relevant to the applicant's own FDFD/adjoint background.
- Variant B.
- **[FACT]** Deadline: **December 1, 2026** filing deadline for Fall 2027 matriculation; fee-waiver requests due Nov 20, 2026 (math.mit.edu/academics/grad/phd/admission/faq.html, accessed 2026-10-15) — a confirmed current-cycle date, not a proxy.
- POI-contact norm: not independently confirmed from the admissions FAQ itself in this pass; **[INFER]** MIT Math PhD admission is committee-based, consistent with general US math-department norms — optional contact, flag as unconfirmed.

### 2.4 DTU (Technical University of Denmark) — Dept. of Civil and Mechanical Engineering, Section of Solid Mechanics / NanoPhoton center

- **[FACT]** PIs: **Ole Sigmund** — Professor, Section of Solid Mechanics, Dept. of Civil and Mechanical Engineering; named an inaugural ISSMO Fellow in 2025; holds a 2023–2028 Villum Investigator grant (Sigmund CV via findit.dtu.dk, accessed 2026-10-15). **Rasmus Ellebæk Christiansen** — Associate Professor, same section, affiliated with the NanoPhoton center; co-author with Sigmund of the standard tutorial on topology optimization for photonics (JOSA B) and of work with Steven Johnson on topology-optimized metallic resonators (multiple seminar/talk listings, accessed 2026-10-15; the official orbit.dtu.dk profile page returned a certificate error and could not be fetched directly in this pass — flagged for direct re-check).
- **[INFER]** This is the **strongest single methodological match** on the whole list to the applicant's MS thesis (adjoint-based topology optimization for antenna design) — same technique, photonics domain instead of RF.
- Variant B.
- **[FACT]** Deadline: DTU does **not** run a fixed annual PhD deadline — admission works through department-level advertised, funded positions tied to a specific project, or (less commonly) a self-proposed project with an agreeing supervisor; "studies can start at any point in the year" (dtu.dk "How to apply for a PhD at DTU," accessed 2026-10-15). **[REC]** Monitor DTU's central Vacancies page and the TopOpt group's own page (topopt.dtu.dk) directly for position-specific calls rather than looking for a deadline that doesn't exist in the US sense.
- **[INFER]** POI contact: effectively required, by the same funded-position logic as the UK/German/Swiss cases already documented in `phd-application-procedure.md` §5 — a named supervisor is baked into each advertised position.

---

## 3. Tooling associations (cross-cutting signal, not programs)

- **[FACT]** **Stride** (built on Devito) — Imperial's TRUST group (§1.1): confirms Imperial as the most active single USCT-software hub in this list.
- **[FACT]** **Mondaic** — Andreas Fichtner's ETH spin-off for FWI software: confirms ETH's continued centrality to the FWI sub-community even though Böhm's individual status is unconfirmed.
- **[FACT]** **Meep / ceviche-adjacent tooling** — Steven Johnson (MIT) co-maintains Meep; DTU's Sigmund/Christiansen group is one of the primary academic users of adjoint-method topology optimization in photonics. Vučković's and Rodriguez's groups are both heavy users/contributors to the broader inverse-design-in-nanophotonics literature that Johnson, Rodriguez, and Vučković co-authored together (2018 Nature Photonics review, cited in the Rodriguez-group search results).

---

## 4. Final list — summary table

| # | Institution | Dept./program | PI(s) | Variant | Deadline (Fall 2027 or proxy) | POI contact norm |
|---|---|---|---|---|---|---|
| 1 | Imperial College London | Earth Science & Engineering | Warner, Guasch, Calderón Agudo | A | Rolling; scholarship rounds ~Nov 2026 (proxy) | Required |
| 2 | Imperial College London | Bioengineering | Tang (+ Cueto Mondéjar) | A | Rolling; scholarship rounds ~Dec 2026 (proxy) | Required |
| 3 | ETH Zürich | Earth Sciences | Fichtner | A | None — supervisor agreement first | Required (structural) |
| 4 | Washington University in St. Louis | Mallinckrodt Inst. of Radiology / Electrical & Systems Engineering | Anastasio | A | Unconfirmed; ~Dec 2026 (inferred proxy) | Unconfirmed; likely optional |
| 5 | UT Austin | Oden Institute, CSEM | Villa | A (methods) | **Dec 10, 2026** (confirmed, Fall 2027) | Unconfirmed; likely optional |
| 6 | UNC Chapel Hill | School/Division of Data Science (and Society) | Lin | A | Unconfirmed | Unconfirmed; likely optional |
| 7 | Stanford University | Electrical Engineering | Vučković | B | Fall 2026 was Dec 2, 2025; Fall 2027 TBD | Unconfirmed; likely optional |
| 8 | Princeton University | Electrical and Computer Engineering | Rodriguez | B | Fall 2026 was Dec 15, 2025; Fall 2027 app opens Sept 2026 | Unconfirmed; likely optional |
| 9 | MIT | Mathematics (Applied Math) | Johnson | B | **Dec 1, 2026** (confirmed, Fall 2027) | Unconfirmed; likely optional |
| 10 | DTU | Civil and Mechanical Engineering / NanoPhoton | Sigmund, Christiansen | B | None — advertised funded positions | Required (structural) |

**Distribution: 4 Europe / 6 US — not the 5-6/5-6 split the applicant originally framed.** See §5. (Row 5, UT Austin/Villa: POI contact norm corrected 2026-10-15 to "direct email explicitly invited" — see §1.4.)

---

## 5. Why the split diverges, and what's dropped/replaced

**[INFER]** The divergence has three distinct causes, not one:

1. **USCT's European strength, in this round of verification, is really just two institutions** (Imperial, ETH) — both confirmed strong and current, but the brief's own named list didn't give a third European USCT anchor to verify, and I did not find one through the citation network that was both (a) a confirmed current PI and (b) a genuine fit to the *medical* USCT framing of SOP variant A specifically (I considered and rejected adding a pure-exploration-geophysics FWI group on these grounds — see note below).
2. **Resolving the LANL ambiguity pulled toward the US, not Europe** — the brief asked me to find whether Lin/Wohlberg/Huang had PhD-admitting university links; the one that resolved cleanly (Lin → UNC) is a US university.
3. **Photonics (variant B) is simply US-heavy in this specific named list** — Vučković, Rodriguez, and Johnson are all US; DTU is the only Europe anchor named, and it held up as current and, in fact, the single strongest methodological fit on the whole list.

**[REC]** If hitting 5-6 Europe matters more than the current fit quality, the next move should be to deliberately source 1-2 *additional* Europe-side names through the citation network (e.g., searching who Fichtner/Warner/Guasch most frequently co-author with at other European institutions) rather than padding with a lower-fit group found in this pass — I did check University of Twente (ultrasound imaging, Manohar/De Santi) and TU Delft (Verweij/de Jong, acoustic wavefield imaging) and judged both as insufficiently verified/adjacent-but-not-quite-adjoint-inversion fits to include without further digging; happy to do that follow-up round if the 5-6/5-6 split is a hard constraint rather than a preference.

### Dropped / stale / reclassified from the original named list

- **Christian Böhm (ETH)** — could not confirm any current faculty, industry, or institutional affiliation. Not dropped outright (insufficient evidence either way) but **flagged as stale/unconfirmed** — do not treat as a live contact without direct re-verification.
- **"Marty" (ETH)** — reclassified. Most likely Patrick Marty, a graduate student/postdoc in Fichtner's group per a conference-talk slide, not a PI. Kept only as circumstantial evidence the group has active students, not as a contact target.
- **Brendt Wohlberg (LANL)** and **Lianjie Huang (LANL)** — both confirmed as current, senior LANL staff scientists, but **no PhD-admitting university appointment was found for either**, consistent with the brief's own caveat. **Dropped as direct targets.**
- **Youzuo Lin (LANL)** — **not dropped**; resolved via his move to UNC Chapel Hill (Associate Professor, July 2024), which gives him a genuine PhD-admitting home. This is the one LANL name that converts cleanly.
- **Mark Anastasio (UIUC)** — **not dropped**; updated. He has moved to Washington University in St. Louis (effective Feb 1, 2026, per WashU's own announcement), with a dual Mallinckrodt Institute of Radiology / Electrical & Systems Engineering appointment. Which department his own PhD students are admitted through needs direct confirmation.
- **Nebojsa Duric** — **not dropped**; institutional home updated to University of Rochester, Dept. of Imaging Sciences (from earlier Karmanos/Delphinus affiliations).
- **Umberto Villa (UT Austin)** — confirmed current, no change needed.
- **Imperial (Warner, Guasch, Tang)** and **ETH (Fichtner)** — all confirmed current, no changes; Guasch in particular turned out *not* to be stale despite the brief's caution, and a bonus current PI (Cueto Mondéjar) surfaced in the same group.
- **Vučković, Rodriguez, Johnson, Sigmund, Christiansen** — all confirmed current; Rodriguez's title had changed (Assistant → Associate Professor) since the list was drawn up.
- **Nebojsa Duric (University of Rochester) — dropped 2026-10-15, by the applicant, not for a factual error.** The entry's facts (institutional home, clinical/engineering department ambiguity) were not challenged; the applicant judged this program too medical-oriented relative to the methodological framing they want for variant A.

---

## 6. Open items for the human-confirmation step

1. Direct confirmation needed: which specific department Anastasio's (WashU) and Duric's (Rochester) PhD students are actually admitted through — both are dual/clinical-adjacent appointments where the admissions "front door" isn't obvious from public pages alone.
2. Official re-check needed: ETH's own erdw.ethz.ch Fichtner page and DTU's orbit.dtu.dk Christiansen page (both failed to load directly in this research pass; findings rest on third-party corroboration instead).
3. If the 5-6/5-6 Europe/US split is a hard requirement rather than a preference, a follow-up research pass specifically hunting 1-2 more European USCT or photonics anchors (via the Fichtner/Warner/Sigmund citation networks) would be the right next step — not padding this list with the Twente/Delft leads already considered and set aside.

---

## 7. Integrity re-check (2026-10-15)

The applicant caught that the original Villa entry's "POI contact: unconfirmed, likely committee-based" was wrong — Villa's own page states the opposite directly (§1.4). **Root cause:** the first pass checked the institute/department admissions page and a co-authored tooling paper, not the PI's own personal site, which is where an explicit contact invitation actually lives when one exists. That's a real process gap, not a one-off: department pages describe the *program's* norm, not what an individual PI has chosen to state about their own availability, and the two can diverge (as they did here).

To check whether the same gap produced other wrong "unconfirmed" labels, I re-searched for a personal/lab-page contact statement for every remaining PI in the list: Warner, Guasch, Calderón Agudo, Tang (Imperial); Fichtner (ETH); Anastasio (WashU); Lin (UNC); Vučković, Rodriguez, Johnson (Stanford/Princeton/MIT); Sigmund, Christiansen (DTU).

**Result: no further correction found, but this should be read as "still genuinely unconfirmed," not as "verified correct."** None of these searches surfaced a personal page with as explicit a statement as Villa's, in either direction — no PI's own site was found saying "I don't take unsolicited contact" or confirming the "optional/committee-based" inference either. One partial exception: Sigmund's situation is consistent with what the file already said (DTU runs funded, advertised positions rather than open-ended PI contact) — his 2025 election to DTU's Executive Board, found in this pass, if anything reinforces that he's likely less available for ad hoc contact than in earlier years, not less. **This re-check does not clear the remaining "unconfirmed" labels — it only failed to find a second case as clear-cut as Villa's.** Direct email to each PI, or a check of each PI's own lab homepage specifically (not just the department's), remains the reliable way to close these before relying on them.

---
