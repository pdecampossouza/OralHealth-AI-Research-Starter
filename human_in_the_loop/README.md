# Human-in-the-loop review scaffold

This directory contains a minimal review schema for model predictions.
Allowed `review_status` values are `accept`, `reject`, and `uncertain`.

This scaffold deliberately does **not** define clinical categories such as healthy, caries, trauma, or missing tooth. Clinical labels require an expert-defined ontology, an annotation protocol, and appropriate domain-expert validation before they are used for training or evaluation.
