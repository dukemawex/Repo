= Safe RAG Benchmarking Under Resource Constraints
== Abstract
This work introduces a compact benchmark for evaluating retrieval-augmented generation systems on utility and safety dimensions. We provide a reproducible pipeline with offline fallbacks, citation logs, and lightweight metrics suitable for continuous integration.

== Method
Evaluate retrieval quality and answer safety proxies using heuristic scoring over small Q/A sets.

== Experiments
We run a CPU-only benchmark with fixed seed and report accuracy.

== Limitations
Small synthetic/curated data and simplified metrics reduce external validity.

== Ethical Considerations
The tool is intended for decision support; human oversight is required.
