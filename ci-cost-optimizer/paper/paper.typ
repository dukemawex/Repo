= CI Cost Optimization with Lightweight Surrogate Modeling
== Abstract
We propose a micro-tool that models build duration and compute cost from pipeline configuration features. The approach enables practical what-if analysis and recommendation generation within CI environments.

== Method
Train a simple regressor on simulated workflow metadata and optimize for cost under latency constraints.

== Experiments
We run a CPU-only benchmark with fixed seed and report accuracy.

== Limitations
Small synthetic/curated data and simplified metrics reduce external validity.

== Ethical Considerations
The tool is intended for decision support; human oversight is required.
