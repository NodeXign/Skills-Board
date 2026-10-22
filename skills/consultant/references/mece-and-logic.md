# MECE and hypothesis-driven logic / MECE与假设驱动

MECE means mutually exclusive and collectively exhaustive within a stated universe. In real business systems, use it as a disciplined design goal, not an unsupported claim that a framework fully represents reality.

## Five decomposition methods

| Method / 方法 | Use / 适用 | Boundary check / 边界检查 |
|---|---|---|
| A versus not-A / 二分 | A precisely defined property | Define the universe and treatment of unknowns. Income and expenditure are not universal logical complements. |
| Process / 过程 | Stages of a lifecycle or workflow | Define start/end and assign cross-stage activities; include loops and hand-offs. |
| Components / 要素 | Physical, geographic or conceptual parts | Choose one level and one partition rule; capability traits can overlap. |
| Formula / 公式 | Quantifiable drivers | Verify identity, units, time and scope. Revenue = price × volume only for compatible definitions; use sum(price_i × volume_i) across products. Multiplicative drivers are not disjoint sets and may interact. |
| Matrix / 矩阵 | Two decision dimensions | Define thresholds, boundary and unknown cases on each axis. Axes need conceptual distinction, not statistical independence. Categories may exceed 2×2. |

## Mature frameworks as lenses

Use 3C for company/customer/competitor questions, 4P for marketing choices, 7S for organisational alignment and value-chain analysis for activities and hand-offs only when they fit the decision. These are useful lenses, not inherently exhaustive or non-overlapping partitions. Add missing context such as regulation, partners or technology when material, and document overlap instead of forcing false MECE.

An `Other / 其他` bucket may be a valid residual, especially with incomplete data. Define it, quantify its size and decision relevance, and split it when material. Never delete inconvenient observations merely to make the tree look complete.

## Tree construction

1. Write the root question and scope; clarify whether this is a cause or solution tree.
2. Select the partition rule; test a few concrete observations against all sibling branches.
3. Identify duplicates, gaps, ambiguous assignment and cross-branch interactions.
4. Expand only branches that affect the decision; avoid ornamental depth.
5. Attach hypotheses and evidence tests, then prioritise by likely impact, uncertainty and cost/time to learn.

Useful working table:

| Issue / 议题 | Hypothesis / 假设 | Evidence for and against / 正反证据 | Source and date / 来源日期 | Test / 验证动作 | Decision consequence / 决策影响 |
|---|---|---|---|---|---|

Deduction: premise → related premise → necessary conclusion; validate each premise and the inference. Induction: observations → common explanation; state uncertainty and plausible alternatives. Correlation or a persuasive narrative does not establish causation.

## Example: delayed delivery / 项目延期

Do not start by assuming insufficient staff. Define the schedule baseline and actual milestone gap. Test demand/scope, effective capacity, execution flow and external dependencies as diagnostic lenses, explicitly allowing their interactions. Compare the causal evidence before proposing hiring, scope reduction or resequencing. A test that could disprove the favoured explanation is more valuable than a tree designed only to support it.
