# OralHealth AI Research Starter - Design Specification

**Status:** Approved design, pre-implementation  
**Date:** 2026-09-26  
**Intended role:** Reusable reference research starter kit for MSc students and future research projects in oral-health computer vision at NOVA IMS.

## 1. Purpose

The project will be a standalone, reusable research template that students can copy into their own independent repositories. It is not the repository of the published paper and must not modify or blur the role of the paper artifact.

The starter kit should make a new clone immediately executable with a small representative image subset while directing students to the original oral-health image repository for complete collections and future research datasets.

The project has four goals:

1. reduce setup friction for students beginning computer-vision research on oral-health images;
2. preserve clear scientific provenance from the original dataset and paper repository;
3. provide reproducible infrastructure without solving the student's dissertation research question;
4. serve as a durable NOVA IMS research-software artifact that can be versioned, cited, registered, and reused by future students.

## 2. Source repository context

The supplied source archive is `Pipeline-for-Oral-Health-Images-main.zip`. Its README describes a reproducible human-in-the-loop pipeline that transforms public SB Brasil 2023 oral-health training materials into a machine-readable dataset for computer-vision research. The repository contains extraction code, metadata, images organized by view, clustering outputs, review tools, and an unsupervised/human-in-the-loop toolkit.

The archive currently contains these top-level image collections:

- permanent dentition - CPOD training: 122 images;
- permanent dentition - DAI training: 121 images;
- deciduous dentition - ceod training: 93 images;
- deciduous dentition - occlusion training: 93 images;
- trauma training: 6 images;
- PUFA training: 6 images.

The source archive also contains reusable research infrastructure such as `metadata/`, `images_by_view/`, `review/`, and `unsupervised_kit/`.

The downloaded archive does not include `.git` metadata. Therefore the starter kit must not invent a source commit identifier. At release time, provenance should record the canonical source repository URL and, if available, the actual Git tag or commit used to select sample images.

## 3. Repository relationship and artifact lineage

The intended lineage is:

```text
SB Brasil public training materials
        |
        v
Published oral-health image/pipeline repository
        |
        v
OralHealth AI Research Starter
        |
        v
Student-created independent repository
        |
        v
MSc dissertation / article / software artifact
```

The original paper repository remains the canonical source for the full image collections and original pipeline. The starter kit is a separate educational/research artifact. Students should use the starter kit as a template or reference, then create their own repository for dissertation work.

## 4. Core design principles

### 4.1 Executable from first clone

A new user should be able to install dependencies and execute the introductory notebooks without downloading the full dataset. To support this, the repository will include a small representative adult sample and a small representative pediatric sample.

### 4.2 Representative, not exhaustive

The embedded sample data should be large enough to demonstrate the workflow but small enough that students must return to the source repository for substantive research.

Initial target:

- approximately 20 adult images;
- approximately 20 pediatric images;
- images selected across multiple volunteers/subjects where the source metadata permits this;
- visual diversity rather than cherry-picked easy examples;
- metadata sufficient to teach subject-level splitting and provenance.

The starter sample is demonstration data, not a dissertation dataset.

### 4.3 Infrastructure, not a dissertation solution

The kit should provide data loading, visualization, configuration, reproducibility helpers, simple baselines, result galleries, and research guidance. It should not provide an optimized dental model, complete expert annotations, final architecture comparisons, optimal hyperparameters, final clinical labels, or a finished missing-tooth algorithm.

A prominent repository statement will read:

> **The Starter Kit is infrastructure, not a dissertation solution.** It provides reproducible examples, sample data, baseline workflows and research organization. Model selection, annotation design, experimental methodology, validation, interpretation and scientific contribution remain the responsibility of each researcher.

### 4.4 Domain-expert involvement remains explicit

Dental interpretation must not be silently encoded by the kit. Tasks such as defining healthy/altered tooth classes, trauma categories, or clinically meaningful absence labels require an explicit annotation ontology and validation protocol with domain experts.

### 4.5 Subject-level separation by default

Where subject/volunteer identity is available, examples and utilities must teach and enforce separation by subject rather than random image-level splitting. The documentation should explain the leakage risk when multiple views from the same person appear in train and test partitions.

## 5. Proposed repository structure

```text
OralHealth-AI-Research-Starter/
|
|-- README.md
|-- LICENSE
|-- CITATION.cff
|-- CHANGELOG.md
|-- AUTHORS.md
|-- requirements.txt
|-- environment.yml
|-- .gitignore
|
|-- data/
|   |-- README.md
|   |-- sample_adult/
|   |   |-- images/
|   |   `-- metadata.csv
|   |-- sample_pediatric/
|   |   |-- images/
|   |   `-- metadata.csv
|   `-- your_research_data/
|       |-- images/
|       |-- annotations/
|       `-- README.md
|
|-- configs/
|   |-- sample_adult.yaml
|   |-- sample_pediatric.yaml
|   `-- template_research_project.yaml
|
|-- notebooks/
|   |-- 01_getting_started.ipynb
|   |-- 02_explore_images.ipynb
|   |-- 03_classical_edge_detection.ipynb
|   |-- 04_pretrained_model_demo.ipynb
|   |-- 05_annotation_and_masks.ipynb
|   |-- 06_results_gallery.ipynb
|   `-- 07_student_experiment_template.ipynb
|
|-- src/
|   |-- data_loader.py
|   |-- metadata.py
|   |-- preprocessing.py
|   |-- visualization.py
|   |-- split_utils.py
|   `-- evaluation.py
|
|-- human_in_the_loop/
|   |-- README.md
|   `-- review_schema.csv
|
|-- docs/
|   |-- getting_started.md
|   |-- original_dataset.md
|   |-- research_rules.md
|   |-- annotation_guide.md
|   |-- experimental_design.md
|   |-- evaluation_guide.md
|   |-- student_project_checklist.md
|   `-- suggested_research_directions.md
|
`-- research_tracks/
    |-- adult_tooth_segmentation.md
    |-- pediatric_tooth_segmentation.md
    |-- tooth_condition.md
    |-- trauma.md
    `-- ideas_for_future_projects.md
```

## 6. Sample-data design

### 6.1 Adult sample

The initial adult sample should be drawn primarily from one of the permanent-dentition collections, with preference for images spanning multiple volunteers and heterogeneous views/visual difficulty. A small number of examples from another compatible permanent-dentition collection may be included if this improves representativeness without confusing the provenance story.

### 6.2 Pediatric sample

The pediatric sample should be drawn from the deciduous-dentition collections and should similarly span multiple volunteers and heterogeneous views where possible.

### 6.3 Metadata schema

Each sample metadata file should contain only source-supported fields. Expected columns are:

```text
sample_id
group
original_filename
original_collection
volunteer_id
source_repository
source_path
source_version
starter_purpose
```

`source_version` should contain a real tag/commit only when one is known. Otherwise it should be blank or state that the distributed archive did not preserve Git revision metadata. Clinical labels must never be inferred from filenames or image appearance unless they are explicitly available in a verified source annotation.

## 7. Notebook learning progression

### 7.1 `01_getting_started.ipynb`

Purpose: make the first successful run immediate.

It should:

- load configuration;
- load adult and pediatric sample metadata;
- open representative images;
- explain the repository data layout;
- show how to point the same code at `data/your_research_data/`;
- identify which components are starter infrastructure versus student research decisions.

### 7.2 `02_explore_images.ipynb`

Purpose: teach dataset inspection before modeling.

It should demonstrate:

- image counts;
- width/height/aspect-ratio distributions;
- missing/corrupt-file checks;
- volunteer/subject distribution where available;
- representative galleries;
- group-aware splitting demonstration;
- leakage warning and rationale.

### 7.3 `03_classical_edge_detection.ipynb`

Purpose: provide a deliberately simple historical/comparative baseline.

It should demonstrate selected classical operations such as grayscale conversion, smoothing, Sobel/Canny edges, thresholding, and optionally watershed. The notebook must state that visual plausibility is not evidence of tooth-instance segmentation quality.

The notebook exists to establish a baseline and motivate modern segmentation methods, not to prescribe the dissertation method.

### 7.4 `04_pretrained_model_demo.ipynb`

Purpose: demonstrate a modern pretrained-model workflow without solving the dental task.

It should:

- explain detection vs semantic segmentation vs instance segmentation;
- run a generic pretrained vision model on a few sample images;
- visualize outputs;
- save a prediction artifact;
- explain why zero-shot/generic outputs are only a starting point;
- point students toward model families to investigate rather than selecting a dissertation winner.

Fine-tuning on the dental dataset is intentionally outside the starter baseline.

### 7.5 `05_annotation_and_masks.ipynb`

Purpose: teach annotation representations.

It should illustrate, on only one or two pedagogical examples:

- bounding boxes;
- binary masks;
- instance IDs;
- polygon representation;
- expected annotation-directory structure;
- conversion or visualization helpers.

It must not ship a complete annotated tooth dataset.

### 7.6 `06_results_gallery.ipynb`

Purpose: turn predictions into inspectable research evidence.

It should generate an image gallery containing, where available:

- original image;
- predicted overlay;
- model/config identifier;
- confidence or status fields;
- placeholders for human review.

### 7.7 `07_student_experiment_template.ipynb`

Purpose: provide structure but not answers.

Sections should include:

- research question;
- hypothesis;
- dataset version and provenance;
- train/validation/test definition;
- model and baseline definitions;
- preprocessing;
- metrics selected before final experiments;
- experiment log;
- results;
- error analysis;
- limitations;
- interpretation.

## 8. Pedagogical code markers

Code and notebooks should use consistent annotations to distinguish supplied infrastructure from student decisions:

```python
# KIT EXAMPLE:
# Infrastructure supplied by the reference starter repository.

# STUDENT DECISION:
# This choice must be justified experimentally in the dissertation.

# RESEARCH EXTENSION:
# Possible research direction; not implemented as a final solution here.
```

These markers should appear sparingly and only where they teach an important research boundary.

## 9. Baseline boundary

The starter kit may provide a pipeline equivalent to:

```text
load image -> basic preprocessing -> simple baseline -> display result -> save prediction
```

The starter kit must not provide:

- a dental-specific model already optimized on the full image collection;
- optimal hyperparameters;
- a comprehensive architecture benchmark;
- full tooth-instance masks for the sample set;
- finalized healthy/unhealthy tooth labels;
- a missing-tooth classifier;
- a tooth-numbering/odontogram solution;
- results that already answer the students' proposed dissertation research questions.

## 10. Human-in-the-loop demonstration

The first release should contain a minimal review schema rather than a full clinical validation system.

Suggested fields:

```text
prediction_id
image_id
review_status
comment
reviewer_id_optional
review_timestamp_optional
```

Recommended `review_status` values:

- `accept`;
- `reject`;
- `uncertain`.

The starter kit should explicitly document how future projects may extend this schema, while stating that clinical categories require domain-expert definition and validation.

## 11. Research tracks

Research-track documents are guidance, not fixed protocols.

### 11.1 Adult tooth segmentation

Focus: detection and instance segmentation of individual teeth in adult intraoral photographs.

Suggested starting research question:

> How accurately can pretrained instance-segmentation architectures isolate individual teeth in heterogeneous intraoral photographs?

Potential extensions may include normal-versus-altered visual appearance and exploratory spatial gap analysis, but these are outside the starter baseline.

### 11.2 Pediatric tooth segmentation

Focus: detection and instance segmentation in primary and mixed dentition, with emphasis on domain shift, transfer learning, and robustness.

Suggested starting research question:

> How do primary and mixed dentition affect the robustness and transferability of tooth instance-segmentation models?

The track should explicitly warn that visible spacing in pediatric dentition must not automatically be interpreted as a missing tooth.

### 11.3 Tooth-condition research

Focus: future classification of tooth-level visual condition after instance extraction. The track should require a domain-expert-approved ontology before model training.

### 11.4 Trauma research

Focus: future investigation using the trauma image collection. Because the source collection is small, the document should present it as an exploratory research direction rather than promise a statistically adequate standalone training dataset.

### 11.5 Future topics

Examples may include image-quality assessment, active learning, domain adaptation, self-supervised learning, view classification, uncertainty estimation, expert validation, and multimodal extensions.

## 12. Reuse by students

The repository should be configured for use as a GitHub Template Repository when published.

Recommended student workflow:

1. open the reference starter repository;
2. choose **Use this template**;
3. create an independent repository for the MSc project;
4. record the starter-kit version used;
5. retrieve the complete image collection(s) needed from the original paper repository;
6. document exact data provenance and selection criteria;
7. maintain the dissertation's code, annotations, trained models, experiments, and results in the student's own repository.

Student repositories should include a statement such as:

```text
This research repository was initiated from OralHealth-AI-Research-Starter, version X.Y.Z.
```

## 13. Student project checklist

The starter documentation should include a checklist covering at least:

- define the research question;
- identify source image collections;
- record dataset provenance and version;
- define the unit of analysis;
- define subject-level train/validation/test splitting;
- define annotation protocol;
- define one or more baselines;
- select candidate architectures from the literature;
- define evaluation metrics before final experiments;
- record random seeds and configurations;
- save experiment logs;
- perform error analysis;
- validate domain-relevant outputs with qualified experts when applicable;
- report limitations and uncertainty;
- preserve reproducibility materials.

## 14. Reproducibility and configuration

All notebooks should call reusable functions from `src/` rather than duplicate substantial logic. Paths and primary experiment settings should be stored in YAML configuration files.

The initial implementation should prefer a small, mature Python stack and avoid unnecessary dependencies. The exact deep-learning dependency used for the pretrained-model demonstration should be selected during implementation based on installation reliability and CPU-friendly first-run behavior.

The kit should provide both `requirements.txt` and `environment.yml`, but one should be designated as the primary installation path in the README to avoid ambiguity.

## 15. Evaluation utilities

The starter evaluation module should provide basic reusable helpers, not a finished benchmark suite. Candidate utilities include:

- image-level data-integrity checks;
- split overlap checks;
- generic classification metrics;
- generic mask overlap metrics such as IoU and Dice when ground truth exists;
- instance count comparison helpers;
- result-table export.

Any metric that depends on a specific research task should be documented as a student decision.

## 16. Documentation and provenance

### 16.1 `data/README.md`

Must explain:

- that embedded images are a small representative sample;
- where they came from;
- why they are included;
- that serious experiments should obtain complete collections from the original repository;
- where students place their own research images and annotations;
- that sample-image inclusion does not imply new clinical labels.

### 16.2 `docs/original_dataset.md`

Must describe the relationship between the paper repository and the starter kit and list the available image collections observed in the supplied archive.

### 16.3 Exact provenance

Before public release, all sample images should be traceable to their source paths. If the canonical source repository provides a commit or tag, that version should be recorded. If not, the documentation should state the limitation rather than manufacture a version identifier.

## 17. Citation and research-software registration

The repository should include `CITATION.cff` from the first public-ready release.

The README should distinguish:

- how to cite the original dataset/paper;
- how to cite the starter software artifact.

No DOI should be fabricated. If the repository is later archived in Zenodo or another registration service, the DOI can be added in a subsequent release.

The starter repository is intended to be suitable for future research-software registration and to provide a visible institutional artifact for NOVA IMS.

## 18. Licensing boundary

Software and sample images must be treated separately.

The supplied source README displays an MIT license badge, but the downloaded archive currently does not contain a top-level `LICENSE` file. The implementation must therefore avoid assuming that a software license automatically relicenses image content.

Before public release:

1. confirm the intended software license for the new starter repository;
2. confirm the applicable terms for redistributed sample images;
3. document those terms clearly in `data/README.md`;
4. retain provenance information for each embedded sample image.

Until those terms are confirmed, the repository may be developed locally but should not present an unverified license statement for the images.

## 19. Versioning

Development starts at `v0.1.0`.

Suggested lifecycle:

- `v0.1.x`: internal development and validation;
- `v1.0.0`: first stable, public, citable starter kit;
- `v1.x`: backward-compatible additions such as new notebooks or evaluation helpers;
- `v2.0.0`: major framework changes that alter expected project structure or interfaces.

A `CHANGELOG.md` should record user-visible changes.

## 20. Error handling and robustness

The kit should fail with clear messages when:

- configured image directories do not exist;
- metadata rows reference missing images;
- images cannot be decoded;
- required metadata columns are absent;
- train/validation/test subject overlap is detected;
- prediction output directories cannot be created;
- optional deep-learning dependencies are unavailable.

Notebooks should surface these failures in student-readable terms rather than swallowing exceptions.

## 21. Testing strategy

The implementation plan should include lightweight automated tests for reusable code, including:

- metadata loading;
- path resolution;
- sample image readability;
- deterministic subject-level splitting;
- no-overlap checks;
- simple evaluation functions;
- configuration parsing.

Notebook smoke testing should verify that each notebook can execute through its intended demonstration path using the embedded sample data. Tests should not require GPU hardware.

## 22. Acceptance criteria for v0.1.0

The development release is considered successful when:

1. a fresh environment can install the documented dependencies;
2. the repository includes representative adult and pediatric samples with traceable metadata;
3. the introductory and exploration notebooks run using only embedded sample data;
4. the classical baseline runs and saves reproducible output;
5. the pretrained-model demo runs on CPU or degrades gracefully with clear instructions;
6. annotation representations can be displayed for at least one pedagogical example;
7. the results gallery can be generated;
8. subject-level splitting utilities are tested and demonstrated;
9. documentation clearly identifies student research decisions versus starter infrastructure;
10. no supplied component claims to solve the dissertation's scientific questions;
11. provenance, citation, and licensing limitations are documented without fabricated information;
12. the repository can be converted into a GitHub Template Repository without restructuring.

## 23. Deliberate non-goals for the first release

The first release will not attempt to:

- create an odontogram;
- identify FDI tooth numbers;
- diagnose disease;
- define clinical healthy/unhealthy labels without expert ontology work;
- train a high-performing dental instance-segmentation model;
- provide a complete labeling platform;
- host every source image collection;
- replace the published dataset repository;
- prescribe a single deep-learning architecture for student dissertations.

## 24. Expected long-term role

The starter kit should remain stable enough that multiple cohorts of students can begin from the same research conventions while producing independent repositories and artifacts. Future work may add new research tracks or generic infrastructure, but additions should preserve the principle that the starter kit supplies reproducible scaffolding rather than completed dissertation solutions.
