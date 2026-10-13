
# Context for the next agent

Last updated 2026-10-07. Written from a long advisory conversation (Sep–Oct 2026) about applying for a PhD starting Fall 2027.

How to read this file:

- **Section 1** is about who I am. It should stay mostly stable.
- **Section 2** states my goals in abstract form. Use it to judge any option, including ones not named here.
- **Section 3** records what was discussed and where it landed. It is a recommendation, not a fixed plan. Revisit it if new evidence appears, but do not reopen a point without a new argument.

---

## 1. About me

### Trajectory

- **Childhood:** wanted to be a mathematician in primary school and a physicist in junior high. My family is mostly in medicine and knew little about engineering or business. I drifted into electrical engineering without a clear picture.
- **Fatigue:** I had been tired since the second year of high school, and it got worse in university.
- **BS, NTU Electrical Engineering.** 
	- No idea about engineering, teaching are bad in the school (no gradual guidance). Try to learn too seriously and stuck at the first few chapters when the courses move on, resulting in very bad GPA. (e.g., fighting with distribution when learning Delta function, fighting with sigma algebra when learning probability and statistics, fighting with the better framework of dynamic system when learning block diagram, trying to learn transmission line theory when learning circuit design, etc.) 
	- Undergraduate research in an antenna lab: ultrasound–microwave fused phase synchronization for UAV-based phased arrays. APMC 2021, second author.
- **MS, NTU Graduate Institute of Communication Engineering (thesis July 2025).**
    - **First work:** Continue on past students compressed sensing microwave imaging work. Write the whole codebase but couldn't think of new approach to improve the performance.
    - **Break:** in the first MS year (late end of second semester) I suspended my studies because I was too stressed. I did my mandatory military service meantime. Service was a calm, happy period. Afterwards I decided to finish the remaining one year and a half regardless of what came next.
        
    - **Thesis:** "Methodologies for Antenna Design Automation: A Study of Machine Learning and Optimization." It treats one inverse problem in three generations:
        
        1. an offline surrogate model (FNN, RNN, TabTransformer) for PIFA tuning;
        2. ML-assisted genetic-algorithm topology search;
        3. adjoint-based SIMP topology optimization with Adam, implemented on CST through Python/VBA, following Hassan–Wadbro–Berggren (2014).
        
        I concluded on my own that surrogates break down in high dimensions and that gradient methods are needed to scale.
        
    - **How the work was done:** mostly self-taught. My advisor's expertise is antennas, not ML or optimization; he gave mental support. A friend taught me the ML foundations.
        
    - **Known gaps in the thesis work:**
        
        - no solver of my own; the commercial solver was a black box;
        - no density filter, Heaviside projection, or robust formulation, so designs stay grayscale;
        - no finite-difference check of the adjoint gradient.
    - **Teaching:** 
	    - worked as a teaching assistant for a year, teaching one calculus course weekly to both Taiwanese and international students, and I graded their exams.
	    - in my last semester I wanted to become a teacher and planned to take the education program. My parents strongly objected, so I dropped it.
        
	- **Pivot interim (August 2025 - March 2026):** After graduate, I am quite lost, not knowing why but rejecting the idea to work in IC design or phone companies, and wanted to pivot. Since the high school teacher route was rejected, I tried to be a doctor because my mother have had a serious chronic kidney illness for a long time, spending a few months preparing and retaking the medical entrance exam. It went badly since I lost the ability to cram through dry, memorizing exams (feeling like doing hundereds of tedious elementary computations without enough time). Only afterwards did I learn that biomedical engineering and medical radiation fields exist. And I tried to apply for some research assistant position.
- **Now: one-year research assistant at NYCU, PET scatter correction.** The PI is a 67-year-old University of Arizona Optical Sciences PhD. He knew from the start that I would apply for a PhD. I chose this year to test whether I care about the field or about the method. The result: the method.
- **IEEE AP-S 2026: first of eight authors.** Remain connection with my master advisor and published a paper during work. Approved after graduate when I work in NYCU. ML surrogate auto-tuning of PIFA. About 99.9% of the work is mine; the other authors provided computers or a few discussions.
- **Recommenders:** MS advisor; NYCU PET PI; ASUS researcher who collaborated with me in my MS lab for a year.

### Character

- **I am a methodologist dressed in an application field.** Across antennas, PET, and what comes next, the physics changes. Inverse problems plus optimization stay constant.
- **I am greedy for knowledge, which makes choosing hard.** I want to know everything, so lists grow instead of converging. My thesis shows this: wide coverage, not enough depth.
- **I am non-competitive but not unambitious.** I give way when others seem to need something more, and I pick up work nobody wants. My science-fair teacher in elementary school called me low in ambition, and I agree with that.
    - _Earlier assessment:_ the "not competitive" part is a research asset. The giving-way part hurts me in resource allocation: topics, credit, and negotiation, e.g. giving credit to 8 people on my paper.
- **I have very high tolerance for solitary, unstructured, under-supervised work.**
    - The strength: I finish hard things alone.
    - The risk: I may stay too long in a bad environment if the larger goal feels meaningful.
- **My self-assessment is honest to the point of self-harm.** I compare myself with geniuses, keep a journal to remind myself of my original intention, and lack confidence. I tend to under-count what I have actually done.
- **My taste divides on derivable versus table-lookup.**
    - I liked EM fields and transmission-line theory, for its own sake.
    - I disliked analog circuits and most of microwave engineering. Both were taught as drilling and memorized topologies with no visible reason, like solving complicated sudoku by hand.
    - I find hands-on experiments fun, and applications interesting, but a difficult craft to master, and competing with my finite time of theoretical learning. For example, my weakness in circuits is a learning debt from avoidance.
- **I want to think things through:** understand structure, see that different things are the same thing.

### Beliefs and what drives me

- **Meaning is the gate; interest is the tie-breaker.** Without meaning I cannot settle into work, however interesting it is. With a larger goal I can endure a lot.
- **What I want:** to explore the ocean of knowledge, and for the world to be a little better because I existed. Everything else is noise.
- **I prefer fixing things to "changing the world."** I dislike "change the world" rhetoric. Technology's side effects are real (guns, drugs, social-media addiction). 五色令人目盲: excess dulls perception.
- **A simple life would be enough:** support a family, serve people well, and in my spare time do mathematics, read physics, and occasionally run an experiment to understand nature. With that being said, financial capability is still very important.
- **Discipline is the foundation of any aim.** The first step is managing body and mind well. Persistence alone achieves a lot, and staying in a good mood spreads positive energy.
- **I am calmer now.** Since military service I have more questions but less confusion.
- **I am drawn toward medical work.** I expect to feel happier and calmer doing it. 

---

## 2. Goals (abstract)

### Goals

1. **Do research I find meaningful, in a medical or broadly beneficial direction,** with enough depth to understand it properly. Interest matters, but it comes second.
2. **Build a solid foundation.** Fill gaps in fundamentals I learned only on the surface.
3. **Accumulate transferable depth.** Choose tools and methods that keep their value across fields and decades, not knowledge tied to one industry or technology generation.
4. **Find good supervision and a healthy environment.** I have rarely been well mentored, and I want to learn what good taste in research looks like. Stay well in body and mind throughout. A PhD should not be a race or a proof of worth. 

---

## 3. Discussion so far and current recommendation

_Not a fixed goal. Treat as the best current judgment, with reasons attached._

### 3.1 How the field choice converged

**Starting point:** "medical imaging seems done; I don't know what to do."

- **Correction:** generalizing from PET works is a biased sample.
    - Classical reconstruction is mature, and the 2016–2022 deep-learning reconstruction wave has saturated.
    - What is still alive: acquisition and co-design, quantification and uncertainty, and low-dose imaging.
- **Core identity:** wave physics, PDE-constrained inverse problems, and the adjoint method.
    - The scarce combination is: build the forward model, differentiate through it, and know the optimization.
    - The adjoint method is reverse-mode autodiff on a PDE solve. It has migrated across six fields in fifty years: optimal control, structures, aerodynamics, weather data assimilation, photonics, and backpropagation.

**Filters applied (later revised into a softer structure):**

|Layer|What it holds|
|---|---|
|Hard constraint|Only one: the path should not require becoming mainly an experiment or fabrication person.|
|Objectives (traded off)|Transferable depth; meaning; whether I would enjoy the daily work ("derive and implement" versus "run tools and tabulate").|
|Tie-breakers|Industry outlook, geography, school name, single-employer concentration risk.|

"Dislike circuits" was first used as a hard veto. It was demoted to a soft preference. Re-checking showed the main exclusions were over-determined anyway.

**Dropped, with reasons:**

| Direction                             | Reason dropped                                                                                                                                            |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Microwave medical imaging             | Resolution–penetration trade-off; Lazebnik 2007 found only about 10% tumor–fibroglandular contrast; hardware-heavy.                                       |
| Computational lithography             | Low meaning for me; concentrated in one company's ecosystem (ASML).                                                                                       |
| Thermal / radiative-cooling photonics | Same method as nanophotonics. The coating end has shallow physics and is crowded. The deep end (fluctuational electrodynamics) was noted but not pursued. |
| Stellarator optimization              | Quite interesting to me. Dropped for low admission probability, and because it is too far from my domain knowledge.                                       |
| Geophysical FWI (as its own line)     | Merged into USCT; it is the same community.                                                                                                               |
| Applied-math departments              | Qualifying exams in analysis are a harder gate, with less scaffolding.                                                                                    |

**Current ranking (my own judgment after reading):**

1. **Ultrasound computed tomography / full-waveform inversion (USCT FWI)**
    - **Why first:** best fit for my interest and meaning. Medical, nonlinear wave inversion, no circuit design, and still open (cycle-skipping, non-convexity).
        
    - **Groups:**
        
        |Where|Who|
        |---|---|
        |Imperial College London|Warner, Guasch (Earth Science); Tang (Bioengineering)|
        |ETH Zürich|Fichtner, Boehm, Marty (Earth Sciences)|
        |US|Anastasio (UIUC), Villa (UT Austin, Oden), Lin / Wohlberg / Huang (LANL), Duric (clinical)| 
        
    - **Tooling:** Stride (open source, built on Devito).
        
    - **Key reads:**
        
        - Guasch et al. 2020, _npj Digital Medicine_
        - Warner & Guasch 2016, AWI, _Geophysics_
        - Plessix 2006, adjoint review
2. **MRI and nanophotonics, roughly equal.**
    - **MRI:** more medical, uses my whole toolkit, but I cannot yet name a research problem in it.
        - If kept, the fitting sub-areas are Halbach magnet design (magnetostatic topology optimization) and pulse-sequence design (optimal control on the Bloch equations).
        - Reconstruction is too crowded.
    - **Nanophotonics:** more interesting and better paid, and the direct continuation of my thesis. Probably the highest admission probability.
        - **Groups:** Vučković (Stanford), Rodriguez (Princeton), Johnson (MIT Math), Sigmund and Christiansen (DTU).
        - **Tooling:** ceviche, Meep adjoint.

**My recent leaning:** treat MRI and nanophotonics as "job-oriented" options, and go wherever admits me.

**Advisor's counter-recommendation (unresolved):**

- _Against the job-oriented framing:_ don't apply anywhere you would not genuinely do research. Nanophotonics has mature tools, but its problems are not solved: 3D scale, the simulation-to-fabrication gap, and the gap between achievability bounds and the best designs.
- _Against "go wherever admits me":_ advisor and group quality dominate everything else. My tolerance for poor supervision is a known risk. Choose deliberately in March. A gap year with a stronger artifact is a legitimate option, not a failure.
- _On MRI:_ within about two days, either name an open problem in MRI or drop it.

### 3.2 Application strategy (recommended)

- **School list:**
    
    - 10–12 programs, frozen. Adding one means removing one.
    - Suggested split: Europe 5–6, US 5–6.
    - The strongest USCT groups are in Europe, and US biomedical funding is weakest.
- **Two SOP variants:**
    
    - (A) medical wave inversion;
    - (B) photonic inverse design.
    
    The core claim is the same in both: "adjoint-based PDE-constrained optimization on wave problems."
    
    - The opening frames the thesis as a methodological arc: three generations of the same inverse problem, leading to the conclusion that gradient methods scale.
    - Be precise about the gaps. Saying what my implementation lacks reads as maturity.
    - Never name professors from different communities in one statement.
- **Technical artifact** (highest-value work):
    
    1. a 2D FDFD solver with PML, written from scratch;
    2. the adjoint gradient, **validated against finite differences**;
    3. density filter, Heaviside projection, and β-continuation on a waveguide bend;
    4. the same machinery ported to the 2D acoustic wave equation as a toy FWI, **including one deliberately cycle-skipped run**;
    5. a README deriving the adjoint.
    
    This is also the test of whether I enjoy the method. Then try Stride.
    
- **Findability:** Google Scholar, ORCID, a one-page personal site, and a GitHub link in the CV.
    
- **TOEFL, GRE:** do not retake unless two or more target programs require a section score above mine.