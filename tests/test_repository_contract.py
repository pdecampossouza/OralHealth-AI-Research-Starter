from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_top_level_files_exist():
    required = [
        'README.md','LICENSE','CITATION.cff','CHANGELOG.md','AUTHORS.md',
        'requirements.txt','environment.yml','.gitignore'
    ]
    missing=[name for name in required if not (ROOT/name).exists()]
    assert not missing, f'Missing: {missing}'


def test_citation_and_version_contract():
    text=(ROOT/'CITATION.cff').read_text(encoding='utf-8')
    assert 'title: "OralHealth AI Research Starter"' in text
    assert 'version: 0.1.0' in text
    changelog=(ROOT/'CHANGELOG.md').read_text(encoding='utf-8')
    assert '## [0.1.0] - Unreleased' in changelog


def test_requirements_contains_core_packages():
    text=(ROOT/'requirements.txt').read_text(encoding='utf-8').lower()
    for pkg in ['pandas','numpy','pillow','matplotlib','pyyaml','scikit-learn','scikit-image','opencv-python-headless','torch','torchvision','jupyter','nbclient','pytest']:
        assert pkg in text

def test_required_research_docs_and_tracks_exist():
    required=[
      'data/README.md','data/your_research_data/README.md','docs/getting_started.md','docs/original_dataset.md',
      'docs/research_rules.md','docs/annotation_guide.md','docs/experimental_design.md','docs/evaluation_guide.md',
      'docs/student_project_checklist.md','docs/suggested_research_directions.md',
      'research_tracks/adult_tooth_segmentation.md','research_tracks/pediatric_tooth_segmentation.md',
      'research_tracks/tooth_condition.md','research_tracks/trauma.md','research_tracks/ideas_for_future_projects.md']
    missing=[p for p in required if not (ROOT/p).exists()]
    assert not missing, f'Missing docs: {missing}'


def test_readme_contains_student_workflow_and_boundary():
    text=(ROOT/'README.md').read_text(encoding='utf-8')
    assert 'The Starter Kit is infrastructure, not a dissertation solution.' in text
    assert 'https://github.com/pdecampossouza/Pipeline-for-Oral-Health-Images' in text
    assert 'pip install -r requirements.txt' in text
    assert 'demonstrative' in text.lower() or 'demonstration' in text.lower()
    assert 'Use this template' in text
    assert 'data/your_research_data/' in text

def test_unreleased_citation_does_not_claim_release_date():
    text=(ROOT/'CITATION.cff').read_text(encoding='utf-8')
    assert 'date-released:' not in text
