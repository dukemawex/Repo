= Miniature Stance Detection for Misinformation Triage
== Abstract
We develop a compact stance classification workflow for claim-response pairs with transparent metrics and error analysis. The system is tuned for low runtime and reproducible CI execution.

== Method
TF-IDF + linear classifier for stance labels with class-balanced evaluation.

== Experiments
We run a CPU-only benchmark with fixed seed and report accuracy.

== Limitations
Small synthetic/curated data and simplified metrics reduce external validity.

== Ethical Considerations
The tool is intended for decision support; human oversight is required.
