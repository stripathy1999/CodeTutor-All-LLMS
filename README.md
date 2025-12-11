# CodeTutor-All-LLMS

Repository of small-programming-task experiments for multiple LLM prompting
strategies. It bundles the HumanEval problems (with an added LeetCode-style
prefix), rubric/config assets for automated grading, raw model generations, and
evaluation summaries/plots.

## Repository layout
- `combined_humanEval_leetcode_dataset.jsonl` — merged HumanEval-style tasks,
  each JSONL row contains `task_id`, `prompt` (problem statement + signature),
  `entry_point`, `canonical_solution`, and `test` (the provided unit tests).
- `llm_coding_tutor/configs/`
  - `blueprint_weighted_v4.yaml` — hierarchical rubric describing correctness,
    edge cases, readability, efficiency, security, robustness, comments, type
    hints, and docstrings with weights and teaching/production/research modes.
  - `ecnn*/`, `gepn/` — saved TF-IDF and model weights (`*.joblib`, `*.csv`,
    `meta.json`) for error classifiers/taggers used in post-run analysis.
- `llm_coding_tutor/generated/` — per-variant model outputs. Each variant
  directory (e.g., `baseline_seed1`, `baseline_primitive_seed1`,
  `adw_weighted_v4_teaching`, `adw_weighted_v4_teaching_seed1`,
  `adb_v1_from_adw_weighted`, `adb_v11_from_adw_weighted`,
  `adb_v11_from_adw_weighted_seed1`) contains `HumanEval/<task_id>/` folders
  with:
  - `meta.txt` — run metadata (prompt variant, seed, timing).
  - `<model>.log.txt` — raw generation transcript for
    `Qwen/Qwen2.5-Coder-0.5B-Instruct`.
  - `<model>.py` — the generated candidate solution.
- `llm_coding_tutor/results/`
  - CSV/JSON summaries (pass rates, confidence intervals, latency, token
    counts) such as `summary_baseline.json` (40.24% pass on 328 runs across
    seeds 1–2) and `adw_adb_pipeline_summary.json` (56.71% pass for the
    ADW→ADB combined pipeline).
  - Ablation tables (`pipeline_ablation_summary.csv`,
    `ecnn_ablation_summary.json`) and error analyses
    (`error_taxonomy_v1.csv`, `error_heatmap_*`).
  - Visuals (`ablation_*`, `error_heatmap_plot_v1.png`,
    `plots_passrate_adw_adb_v11.png`).
  - `ieps/` — ECNN training data snapshots; `prompt_comparisons/` — example
    prompt deltas.

## How to browse the data
1. Inspect a problem: open a row in `combined_humanEval_leetcode_dataset.jsonl`
   to see the prompt, canonical solution, and tests for that task.
2. Review a generation: pick a variant under
   `llm_coding_tutor/generated/<variant>/HumanEval/<task_id>/` and read the
   `.py` candidate plus its `.log.txt` transcript.
3. Check aggregate performance: open the JSON/CSV files in
   `llm_coding_tutor/results/` or view the PNG plots for a quick visual.

## Notes
- Models used in these runs: `Qwen/Qwen2.5-Coder-0.5B-Instruct`.
- Rubric `blueprint_weighted_v4.yaml` encodes the scoring focus used in the ADW
  (autoreview with weights) and ADB (autoreview + debugging) pipelines.
- No execution scripts are included here; this repo is the artifact store for
  prompts, generations, and evaluations.