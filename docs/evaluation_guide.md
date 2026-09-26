# Evaluation guide

For segmentation, consider Dice and IoU together with instance-level errors such as merged teeth, split teeth, missed teeth, and false instances. Boundary-sensitive metrics may be appropriate when contour quality is central to the research question.

For detection, report precision/recall and mAP where appropriate. For classification, report class-specific precision, recall, F1, confusion matrices, and class balance rather than accuracy alone.

Clinical review should use a predefined form and sampling protocol. Human review does not replace quantitative testing; it complements it by assessing failure modes and clinical interpretability.
