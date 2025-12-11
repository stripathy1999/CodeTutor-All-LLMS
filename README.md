# CodeTutor-All-LLMS

Concise artifacts and metrics for the CS297 (Fall 2024) project “Modular Enhancement Pipeline for Code-Generating LLMs.” We test whether a small code model (`Qwen/Qwen2.5-Coder-0.5B-Instruct`) can be improved with prompting, lightweight debugging, and risk prediction—without retraining.

## What’s here
- HumanEval-style dataset with prompts, canonical solutions, and tests (`combined_humanEval_leetcode_dataset.jsonl`).
- Rubrics/configs for structured prompting (`llm_coding_tutor/configs/blueprint_weighted_v4.yaml`).
- Generated model candidates and repair attempts (`llm_coding_tutor/generated/`).
- Evaluation summaries, ablations, and plots (`llm_coding_tutor/results/`).
- Classifier assets for error/risk prediction (ECNN, GEPN).

## Directory map (high level)
- `llm_coding_tutor/configs/` — rubric + TF-IDF/model joblibs for ECNN/GEPN.
- `llm_coding_tutor/generated/` — per-variant outputs (e.g., `baseline_seed1`, `baseline_primitive_seed1`, `adw_weighted_v4_teaching`, `adb_v11_from_adw_weighted`, `adb_v11_from_adw_weighted_seed1`, `adw_weighted_v4_teaching_seed1`).
- `llm_coding_tutor/results/` — CSV/JSON metrics, error taxonomy, ablations, plots (`error_heatmap_plot_v1.png`, `plots_passrate_adw_adb_v11.png`).
- `combined_humanEval_leetcode_dataset.jsonl` — tasks with prompt, entry point, canonical solution, and tests.
- Quick tree (top-level, trimmed):
```
CodeTutor-All-LLMS/
├── combined_humanEval_leetcode_dataset.jsonl
├── llm_coding_tutor/
│   ├── configs/
│   ├── generated/
│   ├── results/
│   ├── ecnn_v2/
│   ├── gepn/
│   ├── adw/
│   ├── adb/
│   └── notebooks/   (execution notebooks live here, not shipped in this repo snapshot)
└── README.md
```

## Variants and artifacts
- **Baseline** — Raw model on HumanEval. Artifacts: `generated/baseline_seed1/<task_id>/` (`meta.txt`, generation log, `.py`). Summary: `results/summary_baseline.json`.
- **Primitive baseline** — Minimal prompt, higher temperature. Artifacts: `generated/baseline_primitive_seed1/`.
- **ADW (Advanced Dynamic Weighting)** — Rubric-driven prompting built from `blueprint_weighted_v4.yaml`: hierarchical dimensions (correctness, edge cases, readability, efficiency, security, robustness, comments, typing, docstrings), weighted sub-criteria, and “teaching” mode with intentional prompt noise to stress robustness. Artifacts: `generated/adw_weighted_v4_teaching/`, summary CSV in `results/adw_weighted_v4_teaching.csv`.
- **ADB (Automated Debugging Workflow)** — Single-round repair of failing ADW outputs; consumes the prompt + failing code + traceback to propose a patched solution. Targets shallow structural/logic issues with one pass. Artifacts: `generated/adb_v11_from_adw_weighted/`, summary CSV `results/adb_from_adw_summary.csv`.
- **ADW→ADB pipeline** — Sequential ADW then ADB; combined view in `results/adw_adb_pipeline_summary.json` and `results/summary_pipeline_v11.csv`.
- **Error/risk models** — ECNN assets under `ecnn*` directories; GEPN assets under `gepn/` with metadata and joblib files.

## Results (from repo artifacts)
| Variant / source file | Tasks | Passed | Pass rate | Notes |
| --- | --- | --- | --- | --- |
| Baseline (`summary_baseline.json`) | 328 (seeds 1–2) | 132 | 40.24% | Raw model runs |
| Baseline subset (`summary_pipeline_v11.csv`) | 164 | 66 | 40.24% | Same rate on 164-task slice |
| ADW weighted v4 teaching (`summary_pipeline_v11.csv`) | 164 | 49 | 29.88% | Rubric prompting |
| ADB v11 from ADW (`summary_pipeline_v11.csv`) | 115 | 44 | 38.26% | Repairs ADW failures only |
| ADW→ADB combined (`adw_adb_pipeline_summary.json`) | 164 | 93 | 56.71% | Best combined in this set |

## How to browse
1. Problems/tests: open rows in `combined_humanEval_leetcode_dataset.jsonl`.
2. A specific generation: `llm_coding_tutor/generated/<variant>/HumanEval/<task_id>/` → read `.py` and `.log.txt`.
3. Metrics/plots: CSV/JSON + PNGs under `llm_coding_tutor/results/`.
- Diagrams (already rendered as PNGs):
  - `results/error_heatmap_plot_v1.png` — normalized error heatmap.
  - `results/plots_passrate_adw_adb_v11.png` — pass-rate comparison across variants.
  - `results/ablation_barplot_v1.png`, `results/ablation_curve_v1.png`, `results/ablation_radar_v1.png` — ablation summaries.
  - `results/ablation_cost_accuracy_scatter_v1.png` — cost vs accuracy trade-off.

## Notes
- Model: `Qwen/Qwen2.5-Coder-0.5B-Instruct`.
- Rubric for ADW/ADB: `llm_coding_tutor/configs/blueprint_weighted_v4.yaml`.
- This repo is an artifact store; notebooks/scripts to re-run are not included here.
- Experiments were run in Google Colab; the repo captures artifacts and metrics, not the execution environment setup.