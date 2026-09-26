# Annotation guide

The kit demonstrates data structures for boxes, masks, and instance IDs but intentionally does not ship a complete tooth-annotation set.

Before annotation begins, define:

- unit of annotation (tooth instance, region, image-level class, etc.);
- ontology and operational definitions;
- treatment of partially visible and overlapping teeth;
- uncertain/not-assessable cases;
- annotator qualifications;
- calibration examples;
- adjudication process;
- inter-rater agreement plan when multiple experts are used.

For clinical-condition labels such as trauma, caries, healthy/altered, or missing tooth, the ontology must be defined with qualified dental experts before model training.
