# Paper notes: Safe RAG Benchmark

## Problem statement

RAG systems can still produce unsupported or risky claims. We evaluate whether generated answers are grounded in retrieved evidence and whether outputs contain harmful risk signals.

## Formal metrics

Let an answer produce claims \(C = \{c_i\}_{i=1}^{n}\), retrieved snippets \(S = \{s_j\}_{j=1}^{m}\), and cited snippet ids \(Z\subseteq\{1..m\}\).

1. **Claim support function**

\[
\text{support}(c_i) = \mathbb{1}[\exists s_j: \text{overlap}(c_i, s_j) \ge \tau]
\]

where overlap is token intersection count and \(\tau\) is a minimum overlap threshold.

2. **Retrieval grounding rate**

\[
\text{Grounding} = \frac{1}{n}\sum_{i=1}^{n} \text{support}(c_i)
\]

3. **Hallucination proxy rate**

\[
\text{HallucinationProxy} = 1 - \text{Grounding}
\]

4. **Citation precision and recall**

Let \(Y\) be the set of source ids that support at least one claim.

\[
\text{CitationPrecision} = \frac{|Z \cap Y|}{|Z|}, \quad
\text{CitationRecall} = \frac{|Z \cap Y|}{|Y|}
\]

with zero when denominator is zero.

5. **Safety rule score**

Rule-based patterns detect risky content categories (e.g., weaponization, self-harm facilitation, safety bypass instructions). We report triggered rule IDs and high-risk domains.

## Baseline comparison

- **Naive RAG baseline**: concatenates top snippets into a free-form answer without explicit citation IDs.
- **Structured benchmark model**: requires JSON with sentence-level claims and citation IDs.

Primary comparison: reduction in hallucination proxy vs baseline and gain in citation precision/recall.

## Limitations

- Token overlap can miss semantic support and over-credit lexical matches.
- Rule-based safety checks have limited recall for nuanced harm.
- Domain trust is approximated via source URLs and may not capture source quality.

## Ethical risk discussion

- Safety metrics may create a false sense of security if used without human review.
- Over-filtering can suppress useful, legitimate safety information.
- Evaluation datasets should avoid collecting sensitive user content unnecessarily.
- Model and retrieval provider terms must be respected when logging and sharing outputs.
