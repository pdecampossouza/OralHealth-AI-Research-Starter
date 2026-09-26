# OralHealth AI Research Starter

Reference starter repository for reproducible computer-vision research with oral-health images. It is intended to be reused for MSc dissertations and future research projects while keeping the published source repository stable.

> **The Starter Kit is infrastructure, not a dissertation solution.** Model selection, annotation design, experimental methodology, validation, interpretation, and scientific contribution remain the responsibility of each researcher.

## Lineage

Canonical source repository: https://github.com/pdecampossouza/Pipeline-for-Oral-Health-Images

The embedded data are a **demonstrative** subset: 20 adult images and 20 pediatric images selected deterministically from the source snapshot. For dissertation experiments, retrieve the complete collection appropriate to the research question from the canonical repository.

## Quick start

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_getting_started.ipynb
```

The sample notebooks run without the full upstream repository. To avoid downloading pretrained model weights during teaching/CI, set `ORALHEALTH_SKIP_MODEL_DOWNLOAD=1`.

## Student workflow

1. On GitHub, choose **Use this template** to create an independent student repository.
2. Keep the starter repository/version in your README for provenance.
3. Retrieve the complete source collection needed for the dissertation.
4. Put project-specific images under `data/your_research_data/` or point a YAML config to an external data location.
5. Copy `configs/template_research_project.yaml` and update dataset paths.
6. Define annotation, split, model-selection, evaluation, and expert-validation protocols as part of the dissertation.

Suggested acknowledgement in a derived student repository:

> This project was initiated from the OralHealth AI Research Starter and uses image resources derived from or referenced through the SBBrasil TrainSheets source repository. The research design, model selection, annotations, experiments, and conclusions are specific to this project.

## What is included

- representative adult and pediatric sample datasets;
- provenance metadata and config-driven loading;
- subject-level splitting with leakage checks;
- classical edge-processing baselines;
- generic COCO-pretrained Mask R-CNN demonstration;
- visualization and human-review scaffolding;
- seven pedagogical notebooks;
- research-method guidance and suggested research tracks.

## What is intentionally not included

No dental model is preselected as the dissertation solution. The kit does not provide complete tooth masks, healthy/altered labels, missing-tooth inference, tooth numbering, or an odontogram.

## Licensing and sample data

Software code is MIT-licensed. Sample-image redistribution terms are separate from the software license and must be verified before public redistribution or registration. See `data/README.md`.

## Citation

`CITATION.cff` contains citation metadata for the starter software. Researchers should also cite the canonical source dataset/publication when their work uses those image resources. No DOI is claimed until one is formally assigned.
