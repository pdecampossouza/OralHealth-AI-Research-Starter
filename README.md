# 🦷 OralHealth AI Research Starter

> 🎓 **A reusable starter kit for research in artificial intelligence, computer vision, and oral-health imaging.**

This repository provides a reproducible starting point for MSc dissertations, student projects, and future research activities involving oral-health images. It is designed to be copied through GitHub's **Use this template** feature so that each researcher can create an independent project while keeping the published source repository stable.

> 💡 **For students**  
> Start with `notebooks/01_getting_started.ipynb`.

> 🔬 **Research principle**  
> **The Starter Kit is infrastructure, not a dissertation solution.** Model selection, annotation design, experimental methodology, validation, interpretation, and scientific contribution remain the responsibility of each researcher.

---

## 🌱 Why this repository exists

Research students should spend their time on the scientific problem rather than repeatedly rebuilding the same project structure, data-loading code, visualization utilities, or experiment scaffolding.

This kit therefore provides a common and reproducible foundation while deliberately leaving the key scientific decisions open.

It is intended to support:

- 🎓 MSc dissertations and student research projects;
- 🧪 reproducible experimentation;
- 🖼️ computer-vision studies with oral-health images;
- 👩‍⚕️ human-in-the-loop workflows;
- 🔁 future research tracks built on the same infrastructure.

---

## 📚 Dataset lineage and provenance

The canonical source repository is:

**SBBrasil TrainSheets / Pipeline for Oral Health Images**  
https://github.com/pdecampossouza/Pipeline-for-Oral-Health-Images

The sample data distributed with this starter kit are **demonstrative subsets** selected from the source material:

- 🧑 **20 adult intraoral images**
- 🧒 **20 pediatric intraoral images**

The subsets are included so that a fresh clone of this repository can be explored and executed immediately.

> 📌 **For dissertation experiments**  
> Researchers should retrieve the complete collection appropriate to their research question from the canonical source repository and document exactly which data were used.

The starter kit preserves provenance metadata so that sample images can be traced back to their source collection.

---

## 🚀 Quick start

Clone or create a repository from this template, then install the dependencies:

```bash
pip install -r requirements.txt
```

Open the first notebook:

```bash
jupyter notebook notebooks/01_getting_started.ipynb
```

The sample notebooks are designed to run without requiring the complete upstream repository.

To avoid downloading pretrained model weights during teaching, testing, or CI, set:

```bash
ORALHEALTH_SKIP_MODEL_DOWNLOAD=1
```

---

## 🧭 Recommended student workflow

1. Click **Use this template** on GitHub and create an independent repository for your project.
2. Record the starter-kit repository and version in your README for provenance.
3. Retrieve the complete source collection required for your dissertation.
4. Place project-specific images under `data/your_research_data/` or configure an external data location.
5. Copy `configs/template_research_project.yaml` and update the dataset paths.
6. Define the annotation protocol, subject-level split, model-selection strategy, evaluation methodology, and expert-validation protocol as part of the research.
7. Keep experiment configurations and results reproducible throughout the project.

> ⚠️ **Important**  
> Dataset partitions should be created at the **volunteer/subject level**, not by randomly splitting individual images. This helps reduce information leakage between training and evaluation sets.

### Suggested acknowledgement for derived student repositories

> This project was initiated from the OralHealth AI Research Starter and uses image resources derived from or referenced through the SBBrasil TrainSheets source repository. The research design, model selection, annotations, experiments, and conclusions are specific to this project.

---

## 📦 What is included

The repository contains a deliberately small but complete research scaffold:

- 🧑 representative adult sample dataset;
- 🧒 representative pediatric sample dataset;
- 📊 provenance metadata and config-driven data loading;
- 👥 subject-level splitting with leakage checks;
- 🔍 classical image-processing and edge-detection baselines;
- 🤖 a generic COCO-pretrained Mask R-CNN demonstration;
- 🖼️ visualization utilities;
- 👩‍⚕️ human-in-the-loop review scaffolding;
- 📏 evaluation utilities for segmentation-oriented experiments;
- 📓 seven pedagogical Jupyter notebooks;
- 🗺️ suggested research tracks and methodological guidance;
- ⚙️ reusable YAML configuration examples;
- ✅ automated tests for the reusable code and repository contract.

---

## 📓 Notebook pathway

| Notebook | Purpose |
|---|---|
| `01_getting_started.ipynb` | Load the starter datasets and understand the repository structure |
| `02_explore_images.ipynb` | Explore image characteristics and metadata |
| `03_classical_edge_detection.ipynb` | Examine intentionally simple classical computer-vision baselines |
| `04_pretrained_model_demo.ipynb` | Demonstrate the use of a generic pretrained model |
| `05_annotation_and_masks.ipynb` | Introduce annotation and mask representations |
| `06_results_gallery.ipynb` | Visualize outputs in a review-oriented gallery |
| `07_student_experiment_template.ipynb` | Provide a clean structure for the student's own experiment |

> 🔬 **Research decision**  
> The included baselines are intentionally simple. They are starting points for comparison, not recommended final models.

---

## 🧪 Research tracks

The `research_tracks/` directory contains starting points for possible projects, including:

- 🦷 adult tooth detection and instance segmentation;
- 🧒 pediatric tooth detection and segmentation;
- 🔎 tooth visual-condition research;
- 🩹 trauma-related image analysis;
- 💡 future computer-vision research directions.

These documents suggest questions to investigate without prescribing a final architecture or experimental answer.

---

## 👩‍⚕️ Human-in-the-loop

The `human_in_the_loop/` directory provides a minimal review scaffold that can be extended for expert validation.

The starter workflow uses neutral review states such as:

- `accept`
- `reject`
- `uncertain`

Clinical labels or diagnostic ontologies are **not** imposed by the starter kit. Those decisions should be defined and validated within the scope of the individual research project.

---

## 🚫 What is intentionally not included

To preserve the scientific contribution of each dissertation, the starter kit does **not** provide:

- a preselected “best” dental AI model;
- a fully fine-tuned tooth-segmentation model;
- complete tooth-level ground-truth masks;
- healthy/altered clinical labels;
- missing-tooth inference;
- tooth numbering;
- automatic odontogram generation;
- optimized hyperparameters or final dissertation results.

> 🎓 The student is expected to justify model choice, annotations, experimental design, metrics, validation strategy, and interpretation from the literature and experimental evidence.

---

## 🗂️ Using your own research data

The directory:

```text
data/your_research_data/
```

shows where project-specific images and annotations can be placed.

A typical student project can adapt:

```text
configs/template_research_project.yaml
```

instead of changing the starter code directly.

This separation helps keep dataset paths, experiments, and research decisions explicit and reproducible.

---

## 🧰 Repository structure

```text
OralHealth-AI-Research-Starter/
├── configs/
├── data/
│   ├── sample_adult/
│   ├── sample_pediatric/
│   └── your_research_data/
├── docs/
├── human_in_the_loop/
├── notebooks/
├── research_tracks/
├── src/
├── tests/
├── tools/
├── CITATION.cff
├── LICENSE
├── requirements.txt
└── README.md
```

---

## 📖 Citation

The file `CITATION.cff` contains citation metadata for this starter software.

Researchers using image resources from the canonical dataset should also cite the corresponding source dataset/publication.

> 📌 No DOI is claimed for this starter kit until one is formally assigned.

---

## ⚖️ License and sample images

The software code in this repository is released under the **MIT License**.

Sample-image redistribution terms are separate from the software license and should be verified before public redistribution, registration, or reuse outside the intended research context.

See `data/README.md` for dataset-specific provenance and guidance.

---

## 🤝 Research and teaching use

This repository is designed as a reusable research and teaching artifact associated with **NOVA IMS**.

It can serve as a common starting point for different students while allowing each project to become an independent repository, with its own research question, methods, experiments, results, and scientific contribution.

> 🌱 **Designed to grow**  
> New research tracks and utilities can be added over time without changing the role of the repository: providing a stable, transparent, and reusable starting point for oral-health AI research.
