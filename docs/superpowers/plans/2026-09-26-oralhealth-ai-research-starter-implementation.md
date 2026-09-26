# OralHealth AI Research Starter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone, immediately executable, citable starter repository for MSc oral-health computer-vision research, with representative adult/pediatric samples, reusable utilities, pedagogical notebooks, research-track guidance, and clear provenance back to the published source repository.

**Architecture:** Keep the starter repository independent from the paper repository. Ship only a small deterministic sample curated from the canonical source commit, put reusable logic in focused `src/` modules, drive notebooks through YAML configs, and keep all dissertation-level modeling choices explicitly outside the starter baseline. The source paper repository remains the authoritative data source; students create independent repositories from this template and import complete collections as needed.

**Tech Stack:** Python 3.10+, pandas, NumPy, Pillow, Matplotlib, PyYAML, scikit-learn, scikit-image, OpenCV headless, PyTorch/torchvision, Jupyter/nbclient, pytest.

**Spec:** `docs/superpowers/specs/2026-09-26-oralhealth-ai-research-starter-design.md`

## Global Constraints

- Development version begins at `v0.1.0`; no public `v1.0.0` release until sample-image redistribution terms and final citation metadata are confirmed.
- The source image/pipeline repository is `https://github.com/pdecampossouza/Pipeline-for-Oral-Health-Images`.
- The supplied source archive corresponds to verified canonical commit `e23dcdae657f4f999d2e126cee673ce0b4cc25b7` (2026-02-05).
- Embedded samples target exactly 20 adult images and 20 pediatric images unless source integrity prevents that count.
- Adult sample source collection: permanent dentition - CPOD training.
- Pediatric sample source collection: deciduous dentition - occlusion training.
- Sample selection is deterministic: for each of 10 volunteers, select the lowest and highest available sequence number from the chosen collection.
- Clinical labels must never be inferred from image appearance or filenames unless present in a verified source annotation.
- Subject/volunteer-level splitting is the default; utilities must detect and reject subject overlap across train/validation/test partitions.
- Primary install path is `pip install -r requirements.txt`; `environment.yml` mirrors the same user-facing dependencies.
- The deep-learning notebook uses torchvision Mask R-CNN only as a generic pretrained demonstration; it is not presented as a dental solution or recommended dissertation winner.
- The repository must remain runnable without the original source archive after sample curation is complete.
- Software code uses the MIT license; `data/README.md` must explicitly state that sample-image terms are separate and must be verified before public redistribution.
- No fabricated DOI, clinical label, dataset version, or expert validation claim.

## Review Focus

1. **Missing/corrupt sample image:** dataset loading must report the exact broken file instead of failing later in a notebook.
2. **Subject leakage:** any volunteer appearing in more than one split must raise a clear error before modeling.
3. **Malformed metadata/config:** missing required columns or bad YAML paths must fail with actionable messages.
4. **No internet/model weights:** the pretrained-model demo must still execute in documented skip mode and explain how to rerun with weights.
5. **Student data with different filenames/layout:** the custom-data config must work without relying on source-repository filename conventions as long as required metadata are supplied.

---

## File Structure Locked by This Plan

### Repository-level files
- `README.md` - project purpose, quick start, lineage, starter boundary, citation and student workflow.
- `LICENSE` - MIT license for software only.
- `CITATION.cff` - starter software citation metadata; no DOI until one exists.
- `CHANGELOG.md` - starts with `0.1.0 - Unreleased`.
- `AUTHORS.md` - maintainers/contributors without inventing affiliations.
- `requirements.txt` - primary installation dependencies.
- `environment.yml` - conda equivalent.
- `.gitignore` - ignores caches, model weights, student outputs, local datasets.

### Data/config
- `data/sample_adult/images/` + `metadata.csv`
- `data/sample_pediatric/images/` + `metadata.csv`
- `data/your_research_data/images/`, `annotations/`, `README.md`
- `configs/sample_adult.yaml`
- `configs/sample_pediatric.yaml`
- `configs/template_research_project.yaml`

### Reusable code
- `src/__init__.py`
- `src/data_loader.py`
- `src/metadata.py`
- `src/split_utils.py`
- `src/preprocessing.py`
- `src/evaluation.py`
- `src/visualization.py`
- `src/pretrained_demo.py`

### Internal curation tool
- `tools/curate_sample_data.py`

### Tests
- `tests/test_sample_curation.py`
- `tests/test_data_loader.py`
- `tests/test_split_utils.py`
- `tests/test_preprocessing.py`
- `tests/test_evaluation.py`
- `tests/test_visualization.py`
- `tests/test_pretrained_demo.py`
- `tests/test_notebooks.py`
- `tests/test_repository_contract.py`

### Notebooks/docs
- Seven notebooks exactly as named in the spec.
- Documentation and research-track Markdown files exactly as named in the spec.
- `human_in_the_loop/README.md` and `human_in_the_loop/review_schema.csv`.

---

### Task 1: Establish Repository Contract, Dependencies, and Base Metadata

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `CITATION.cff`
- Create: `CHANGELOG.md`
- Create: `AUTHORS.md`
- Create: `requirements.txt`
- Create: `environment.yml`
- Create: `.gitignore`
- Create: `src/__init__.py`
- Create: `tests/test_repository_contract.py`

**Interfaces:**
- Consumes: approved design spec.
- Produces: installable dependency set, version/citation files, repository-wide constants expected by later tasks.

- [ ] **Step 1: Write the failing repository-contract tests**

Create tests asserting that the required top-level files exist, `CITATION.cff` contains title `OralHealth AI Research Starter` and version `0.1.0`, `CHANGELOG.md` starts with an unreleased `0.1.0` entry, and `requirements.txt` contains the agreed core packages.

- [ ] **Step 2: Run the contract test and verify it fails**

Run: `pytest tests/test_repository_contract.py -v`
Expected: FAIL because repository files do not yet exist.

- [ ] **Step 3: Create the minimal repository-level files**

Use MIT for software code. In `README.md` and `LICENSE`-adjacent documentation, explicitly state that the software license does not automatically license redistributed sample images. Set primary installation to `pip install -r requirements.txt`. Include Python 3.10+ and the packages listed in the Tech Stack.

- [ ] **Step 4: Run the contract test and verify it passes**

Run: `pytest tests/test_repository_contract.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add README.md LICENSE CITATION.cff CHANGELOG.md AUTHORS.md requirements.txt environment.yml .gitignore src/__init__.py tests/test_repository_contract.py
git commit -m "chore: establish starter repository contract"
```

### Task 2: Build Deterministic Adult and Pediatric Sample Curation

**Files:**
- Create: `tools/curate_sample_data.py`
- Create: `tests/test_sample_curation.py`
- Create: `data/sample_adult/images/`
- Create: `data/sample_adult/metadata.csv`
- Create: `data/sample_pediatric/images/`
- Create: `data/sample_pediatric/metadata.csv`

**Interfaces:**
- Consumes: source ZIP path, source `metadata/manifest.csv`, canonical commit string.
- Produces: `select_sample_rows(manifest: pd.DataFrame, collection: str, group: str, volunteers: int = 10) -> pd.DataFrame`; `materialize_samples(source_zip: Path, output_root: Path) -> dict[str, Path]`.

- [ ] **Step 1: Write failing curation tests using a synthetic manifest**

Test that `select_sample_rows(...)` returns exactly two rows per volunteer, chooses minimum and maximum `seq`, never duplicates source paths, preserves 10 distinct volunteers, and writes the required metadata columns from the spec.

- [ ] **Step 2: Run curation tests and verify failure**

Run: `pytest tests/test_sample_curation.py -v`
Expected: FAIL because the curation module does not exist.

- [ ] **Step 3: Implement deterministic curation**

Use only top-level/original collection paths from the manifest, excluding duplicated `clusters/` and `images_by_view/` copies. Adult collection string must resolve to CPOD permanent dentition; pediatric collection string must resolve to deciduous occlusion. Populate `source_repository` with the canonical GitHub URL and `source_version` with `e23dcdae657f4f999d2e126cee673ce0b4cc25b7`.

- [ ] **Step 4: Add the corrupt/missing-source-path test from Review Focus**

Assert that a manifest row whose ZIP member is missing raises `FileNotFoundError` naming that member.

- [ ] **Step 5: Run curation tests**

Run: `pytest tests/test_sample_curation.py -v`
Expected: PASS.

- [ ] **Step 6: Materialize the real 20+20 sample from the supplied source ZIP**

Run: `python tools/curate_sample_data.py --source-zip /mnt/data/Pipeline-for-Oral-Health-Images-main.zip --output-root .`
Expected: 20 adult images, 20 pediatric images, and metadata files with 10 volunteers per group.

- [ ] **Step 7: Verify sample counts and provenance**

Run: `python -c "import pandas as pd; a=pd.read_csv('data/sample_adult/metadata.csv'); p=pd.read_csv('data/sample_pediatric/metadata.csv'); assert len(a)==20 and len(p)==20; assert a.volunteer_id.nunique()==10 and p.volunteer_id.nunique()==10; assert set(a.source_version)=={'e23dcdae657f4f999d2e126cee673ce0b4cc25b7'}"`
Expected: exits 0.

- [ ] **Step 8: Commit**

```bash
git add tools/curate_sample_data.py tests/test_sample_curation.py data/sample_adult data/sample_pediatric
git commit -m "feat: add representative adult and pediatric samples"
```

### Task 3: Implement Config, Metadata, and Image Loading

**Files:**
- Create: `src/data_loader.py`
- Create: `src/metadata.py`
- Create: `configs/sample_adult.yaml`
- Create: `configs/sample_pediatric.yaml`
- Create: `configs/template_research_project.yaml`
- Create: `tests/test_data_loader.py`

**Interfaces:**
- Consumes: YAML config path and metadata CSV.
- Produces:
  - `load_config(path: str | Path) -> dict`
  - `load_metadata(path: str | Path) -> pd.DataFrame`
  - `validate_metadata(df: pd.DataFrame) -> None`
  - `resolve_image_paths(df: pd.DataFrame, image_dir: str | Path) -> pd.DataFrame`
  - `load_rgb_image(path: str | Path) -> PIL.Image.Image`
  - `dataset_integrity_report(df: pd.DataFrame) -> pd.DataFrame`

- [ ] **Step 1: Write failing loader tests**

Cover valid config loading, required-column validation, path resolution, RGB decoding, and integrity reporting.

- [ ] **Step 2: Run loader tests and verify failure**

Run: `pytest tests/test_data_loader.py -v`
Expected: FAIL because loader modules do not exist.

- [ ] **Step 3: Implement the loader and metadata validation**

Required metadata columns: `sample_id`, `group`, `original_filename`, `original_collection`, `volunteer_id`, `source_repository`, `source_path`, `source_version`, `starter_purpose`.

- [ ] **Step 4: Add Review Focus tests for malformed config and corrupt files**

Assert missing YAML path raises `FileNotFoundError`; missing required metadata columns raises `ValueError` listing column names; missing referenced image and undecodable image appear in `dataset_integrity_report` with exact path and status.

- [ ] **Step 5: Add custom-layout test**

Create a temporary image folder with arbitrary filenames and metadata that satisfies the schema; confirm config-driven loading succeeds without parsing filename conventions.

- [ ] **Step 6: Run loader tests**

Run: `pytest tests/test_data_loader.py -v`
Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add src/data_loader.py src/metadata.py configs tests/test_data_loader.py
git commit -m "feat: add config and dataset loading utilities"
```

### Task 4: Implement Subject-Level Splitting and Leakage Protection

**Files:**
- Create: `src/split_utils.py`
- Create: `tests/test_split_utils.py`

**Interfaces:**
- Consumes: metadata DataFrame with subject column.
- Produces:
  - `subject_split(df: pd.DataFrame, subject_col: str = "volunteer_id", train_size: float = 0.6, val_size: float = 0.2, test_size: float = 0.2, random_state: int = 42) -> dict[str, pd.DataFrame]`
  - `assert_no_subject_overlap(splits: dict[str, pd.DataFrame], subject_col: str = "volunteer_id") -> None`
  - `split_summary(splits: dict[str, pd.DataFrame], subject_col: str = "volunteer_id") -> pd.DataFrame`

- [ ] **Step 1: Write failing split tests**

Assert deterministic assignment for the same seed, full row coverage, no subject overlap, and approximate 60/20/20 subject allocation.

- [ ] **Step 2: Run tests and verify failure**

Run: `pytest tests/test_split_utils.py -v`
Expected: FAIL because `split_utils` does not exist.

- [ ] **Step 3: Implement subject-level splitting**

Split unique subject IDs first, then map rows into partitions. Validate split fractions sum to 1.0 and require at least three distinct subjects.

- [ ] **Step 4: Add the subject-leakage Review Focus test**

Construct overlapping split DataFrames and assert `assert_no_subject_overlap` raises `ValueError` naming the duplicated volunteer ID and partitions.

- [ ] **Step 5: Run split tests**

Run: `pytest tests/test_split_utils.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/split_utils.py tests/test_split_utils.py
git commit -m "feat: add subject-level split safeguards"
```

### Task 5: Implement Classical Image Baselines and Generic Evaluation Helpers

**Files:**
- Create: `src/preprocessing.py`
- Create: `src/evaluation.py`
- Create: `tests/test_preprocessing.py`
- Create: `tests/test_evaluation.py`

**Interfaces:**
- Produces preprocessing functions:
  - `to_grayscale(image: np.ndarray) -> np.ndarray`
  - `gaussian_blur(image: np.ndarray, kernel_size: int = 5) -> np.ndarray`
  - `canny_edges(image: np.ndarray, low: int = 50, high: int = 150) -> np.ndarray`
  - `sobel_edges(image: np.ndarray) -> np.ndarray`
  - `otsu_threshold(image: np.ndarray) -> np.ndarray`
- Produces evaluation functions:
  - `iou_score(y_true: np.ndarray, y_pred: np.ndarray) -> float`
  - `dice_score(y_true: np.ndarray, y_pred: np.ndarray) -> float`
  - `instance_count_error(true_count: int, pred_count: int) -> int`
  - `classification_metrics(y_true: Sequence, y_pred: Sequence) -> dict[str, float]`
  - `export_results(rows: Sequence[Mapping], path: str | Path) -> Path`

- [ ] **Step 1: Write failing preprocessing and evaluation tests**

Use tiny synthetic arrays with known edge/mask behavior and exact IoU/Dice expectations.

- [ ] **Step 2: Run tests and verify failure**

Run: `pytest tests/test_preprocessing.py tests/test_evaluation.py -v`
Expected: FAIL because modules do not exist.

- [ ] **Step 3: Implement minimal functions**

Use OpenCV/scikit-image for classical operations and NumPy/scikit-learn for metrics. Define empty-union IoU/Dice as `1.0` when both masks are empty.

- [ ] **Step 4: Run tests**

Run: `pytest tests/test_preprocessing.py tests/test_evaluation.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/preprocessing.py src/evaluation.py tests/test_preprocessing.py tests/test_evaluation.py
git commit -m "feat: add classical baselines and evaluation helpers"
```

### Task 6: Implement Visualization, Prediction Artifacts, and Human-Review Schema

**Files:**
- Create: `src/visualization.py`
- Create: `human_in_the_loop/README.md`
- Create: `human_in_the_loop/review_schema.csv`
- Create: `tests/test_visualization.py`

**Interfaces:**
- Produces:
  - `make_image_grid(images: Sequence[PIL.Image.Image], titles: Sequence[str] | None = None, columns: int = 4) -> matplotlib.figure.Figure`
  - `overlay_binary_mask(image: PIL.Image.Image, mask: np.ndarray, alpha: float = 0.35) -> PIL.Image.Image`
  - `draw_boxes(image: PIL.Image.Image, boxes: Sequence[Sequence[float]], labels: Sequence[str] | None = None) -> PIL.Image.Image`
  - `save_prediction_artifact(image: PIL.Image.Image, output_path: str | Path) -> Path`

- [ ] **Step 1: Write failing visualization tests**

Test grid creation, output dimensions, mask-overlay size preservation, and automatic output-directory creation.

- [ ] **Step 2: Run tests and verify failure**

Run: `pytest tests/test_visualization.py -v`
Expected: FAIL.

- [ ] **Step 3: Implement visualization helpers and review schema**

`review_schema.csv` header must be `prediction_id,image_id,review_status,comment,reviewer_id_optional,review_timestamp_optional`. README documents allowed status values `accept`, `reject`, `uncertain` and explicitly states that clinical labels require expert-defined ontologies.

- [ ] **Step 4: Add output-directory failure test**

Mock an unwritable target and assert `save_prediction_artifact` raises an actionable `OSError` containing the target path.

- [ ] **Step 5: Run tests**

Run: `pytest tests/test_visualization.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/visualization.py human_in_the_loop tests/test_visualization.py
git commit -m "feat: add visualization and human-review scaffolding"
```

### Task 7: Implement the Generic Pretrained Model Demonstration

**Files:**
- Create: `src/pretrained_demo.py`
- Create: `tests/test_pretrained_demo.py`

**Interfaces:**
- Produces:
  - `load_generic_maskrcnn(download_weights: bool = True)`
  - `predict_generic_instances(model, image: PIL.Image.Image, score_threshold: float = 0.5) -> dict[str, Any]`
  - `pretrained_demo_available() -> tuple[bool, str]`
- Returned prediction dict contains `boxes`, `labels`, `scores`, `masks` as CPU NumPy arrays.

- [ ] **Step 1: Write failing demo-helper tests without downloading weights**

Use a fake model object to validate preprocessing/postprocessing shape and score-threshold filtering. Test `pretrained_demo_available()` behavior when torch/torchvision import is unavailable via monkeypatch.

- [ ] **Step 2: Run tests and verify failure**

Run: `pytest tests/test_pretrained_demo.py -v`
Expected: FAIL.

- [ ] **Step 3: Implement torchvision Mask R-CNN wrapper**

Use `maskrcnn_resnet50_fpn(weights="DEFAULT")` only when `download_weights=True`. Do not auto-train or fine-tune. Error text must call the model a generic COCO-pretrained demonstration, not a dental model.

- [ ] **Step 4: Add no-internet/skip-mode Review Focus test**

Support environment variable `ORALHEALTH_SKIP_MODEL_DOWNLOAD=1`; in this mode, `load_generic_maskrcnn()` raises a documented `RuntimeError` instructing notebooks to skip inference while continuing the educational flow.

- [ ] **Step 5: Run tests**

Run: `pytest tests/test_pretrained_demo.py -v`
Expected: PASS without network access.

- [ ] **Step 6: Commit**

```bash
git add src/pretrained_demo.py tests/test_pretrained_demo.py
git commit -m "feat: add generic pretrained vision demo"
```

### Task 8: Create and Execute the Seven Pedagogical Notebooks

**Files:**
- Create: `notebooks/01_getting_started.ipynb`
- Create: `notebooks/02_explore_images.ipynb`
- Create: `notebooks/03_classical_edge_detection.ipynb`
- Create: `notebooks/04_pretrained_model_demo.ipynb`
- Create: `notebooks/05_annotation_and_masks.ipynb`
- Create: `notebooks/06_results_gallery.ipynb`
- Create: `notebooks/07_student_experiment_template.ipynb`
- Create: `tests/test_notebooks.py`

**Interfaces:**
- Consumes: config files and functions from Tasks 3-7.
- Produces: executable teaching flow and example artifacts under ignored `outputs/` paths.

- [ ] **Step 1: Write notebook contract tests**

Assert all seven notebooks exist, contain at least one markdown cell with the required `KIT EXAMPLE`/`STUDENT DECISION`/`RESEARCH EXTENSION` boundary language where relevant, and do not embed absolute `/mnt/data` paths.

- [ ] **Step 2: Run notebook contract tests and verify failure**

Run: `pytest tests/test_notebooks.py -v`
Expected: FAIL because notebooks do not exist.

- [ ] **Step 3: Create `01_getting_started.ipynb` and `02_explore_images.ipynb`**

Use only reusable `src/` functions for loading/splitting. Demonstrate adult and pediatric configs, custom-data path substitution, integrity report, subject counts, gallery, and leakage rationale.

- [ ] **Step 4: Create `03_classical_edge_detection.ipynb`**

Show grayscale, blur, Sobel, Canny, and Otsu on a few samples. State explicitly that visually plausible edges are not evidence of tooth-instance segmentation quality.

- [ ] **Step 5: Create `04_pretrained_model_demo.ipynb`**

Explain detection vs semantic vs instance segmentation; run the generic Mask R-CNN on at most two images when weights are available; otherwise continue in skip mode. Save one prediction artifact and state why generic outputs are only a baseline demonstration.

- [ ] **Step 6: Create `05_annotation_and_masks.ipynb`**

Use one or two synthetic/manual pedagogical shapes only; demonstrate boxes, polygons, binary masks, and instance IDs without shipping a complete annotated dental dataset.

- [ ] **Step 7: Create `06_results_gallery.ipynb` and `07_student_experiment_template.ipynb`**

Gallery notebook pairs originals and available overlays plus review placeholders. Experiment template includes all required scientific sections from the spec and no pre-filled research conclusion.

- [ ] **Step 8: Execute notebooks 01, 02, 03, 05, 06, 07 in CI mode**

Run: `ORALHEALTH_SKIP_MODEL_DOWNLOAD=1 pytest tests/test_notebooks.py -v`
Expected: PASS; the test executes notebooks through `nbclient` with a timeout and verifies no cell errors.

- [ ] **Step 9: Execute notebook 04 in skip mode**

Run: `ORALHEALTH_SKIP_MODEL_DOWNLOAD=1 jupyter nbconvert --to notebook --execute notebooks/04_pretrained_model_demo.ipynb --output /tmp/04_pretrained_model_demo.executed.ipynb --ExecutePreprocessor.timeout=180`
Expected: exits 0 without downloading model weights.

- [ ] **Step 10: Commit**

```bash
git add notebooks tests/test_notebooks.py
git commit -m "feat: add executable pedagogical notebooks"
```

### Task 9: Write Research Documentation, Student Workflow, and Research Tracks

**Files:**
- Create: `data/README.md`
- Create: `data/your_research_data/README.md`
- Create: `docs/getting_started.md`
- Create: `docs/original_dataset.md`
- Create: `docs/research_rules.md`
- Create: `docs/annotation_guide.md`
- Create: `docs/experimental_design.md`
- Create: `docs/evaluation_guide.md`
- Create: `docs/student_project_checklist.md`
- Create: `docs/suggested_research_directions.md`
- Create: `research_tracks/adult_tooth_segmentation.md`
- Create: `research_tracks/pediatric_tooth_segmentation.md`
- Create: `research_tracks/tooth_condition.md`
- Create: `research_tracks/trauma.md`
- Create: `research_tracks/ideas_for_future_projects.md`
- Modify: `README.md`
- Modify: `tests/test_repository_contract.py`

**Interfaces:**
- Consumes: working code/notebooks and exact provenance produced earlier.
- Produces: user-facing research guidance and template-repository workflow.

- [ ] **Step 1: Extend repository-contract tests for documentation**

Assert all required docs/tracks exist and that `README.md` contains the exact starter-boundary statement, canonical source repository link, quick-start command, sample-data warning, and student template workflow.

- [ ] **Step 2: Run contract tests and verify failure**

Run: `pytest tests/test_repository_contract.py -v`
Expected: FAIL because docs are missing.

- [ ] **Step 3: Write data and provenance documentation**

Document the observed six image collections and the verified source commit. Explain that 20+20 embedded images are demonstrative, serious experiments must retrieve complete collections, and clinical labels have not been inferred.

- [ ] **Step 4: Write research-rules, annotation, design, and evaluation guides**

Include subject-level splitting, metrics-before-final-experiments, experiment logging, annotation ontology responsibilities, error analysis, expert validation, uncertainty, and reproducibility.

- [ ] **Step 5: Write the five research-track documents**

Preserve the approved adult/pediatric research questions. State that pediatric spacing is not automatically a missing tooth, tooth-condition work requires expert ontology, and the six-image trauma collection is exploratory rather than a guaranteed standalone training dataset.

- [ ] **Step 6: Finalize README and student checklist**

Describe `Use this template` workflow, the statement students should copy into their repositories, and how to replace sample config paths with `data/your_research_data/`.

- [ ] **Step 7: Run documentation contract tests**

Run: `pytest tests/test_repository_contract.py -v`
Expected: PASS.

- [ ] **Step 8: Commit**

```bash
git add README.md data docs research_tracks tests/test_repository_contract.py
git commit -m "docs: add research guidance and student workflow"
```

### Task 10: Full Validation, Release Readiness, and Clean Artifact Check

**Files:**
- Modify as needed based on validation findings.
- Create: `docs/release_checklist.md`

**Interfaces:**
- Consumes: complete repository.
- Produces: validated `v0.1.0` development artifact ready for supervisor/domain-expert review before public registration.

- [ ] **Step 1: Run the complete automated test suite**

Run: `ORALHEALTH_SKIP_MODEL_DOWNLOAD=1 pytest -v`
Expected: all tests PASS.

- [ ] **Step 2: Run a clean-install smoke test in a fresh virtual environment**

Run: create Python 3.10+ venv, `pip install -r requirements.txt`, then execute notebooks 01-03 in sequence.
Expected: installation succeeds and notebooks execute without modification.

- [ ] **Step 3: Verify sample-data contract manually and programmatically**

Confirm 20 adult + 20 pediatric images, 10 volunteers per group, no duplicate source paths, all files decode, all provenance fields point to the canonical source repository and verified commit.

- [ ] **Step 4: Verify repository cleanliness**

Run: `git status --short`, search for `/mnt/data`, local absolute paths, downloaded weights, notebook execution caches, and untracked research outputs.
Expected: no accidental local paths or large model artifacts committed.

- [ ] **Step 5: Create `docs/release_checklist.md`**

Include gates for sample-image redistribution terms, software-license confirmation, co-supervisor/domain-expert review, citation metadata, GitHub Template setting, Zenodo/registration decision, and eventual `v1.0.0` tag.

- [ ] **Step 6: Update `CHANGELOG.md` with completed `0.1.0` development scope**

Do not claim a DOI or public release.

- [ ] **Step 7: Commit validation/release checklist**

```bash
git add docs/release_checklist.md CHANGELOG.md
git commit -m "chore: add release readiness checks"
```

- [ ] **Step 8: Tag only after human review**

After supervisor approval of the built artifact, create `v0.1.0`. Do not create `v1.0.0` until public-release gates in the design spec are satisfied.

---

## Self-Review Notes

- **Spec coverage:** repository purpose, sample data, provenance, code boundaries, subject splitting, classical baseline, pretrained demo, annotation examples, gallery/review scaffold, seven notebooks, research tracks, citation, licensing boundary, versioning, robustness, student workflow, and release gates all map to explicit tasks.
- **Type consistency:** config/metadata paths use `str | Path`; DataFrame-returning interfaces are reused consistently by split/notebook tasks; image helpers use Pillow at boundaries and NumPy for classical/evaluation routines.
- **Review Focus coverage:** missing/corrupt files -> Task 3; leakage -> Task 4; malformed config -> Task 3; no internet/weights -> Tasks 7-8; arbitrary student filenames/layout -> Task 3.
- **Scope:** the plan intentionally excludes dental-model fine-tuning, architecture benchmarking, complete tooth masks, healthy/altered labels, missing-tooth logic, tooth numbering, and odontogram generation.
- **Provenance correction:** the source ZIP lacks `.git` metadata, but its archive revision has now been independently verified against GitHub as commit `e23dcdae657f4f999d2e126cee673ce0b4cc25b7`; the implementation may therefore record that exact commit for this sample release.
