from pathlib import Path
import nbformat
from nbclient import NotebookClient

ROOT=Path(__file__).resolve().parents[1]
NAMES=[
 '01_getting_started.ipynb','02_explore_images.ipynb','03_classical_edge_detection.ipynb',
 '04_pretrained_model_demo.ipynb','05_annotation_and_masks.ipynb','06_results_gallery.ipynb',
 '07_student_experiment_template.ipynb']


def test_notebook_contract():
    for name in NAMES:
        p=ROOT/'notebooks'/name
        assert p.exists(), name
        nb=nbformat.read(p,as_version=4)
        text='\n'.join(c.source for c in nb.cells)
        assert '/mnt/data' not in text
        assert 'KIT EXAMPLE' in text or 'STUDENT DECISION' in text or 'RESEARCH EXTENSION' in text


def test_core_notebooks_execute(monkeypatch):
    monkeypatch.setenv('ORALHEALTH_SKIP_MODEL_DOWNLOAD','1')
    for name in [NAMES[i] for i in [0,1,2,4,5,6]]:
        nb=nbformat.read(ROOT/'notebooks'/name,as_version=4)
        client=NotebookClient(nb,timeout=180,kernel_name='python3',resources={'metadata':{'path':str(ROOT)}})
        client.execute()
