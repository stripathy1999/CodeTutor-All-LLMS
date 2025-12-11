# Modular Enhancement Pipeline for Small Code LLMs (CS297 Project)
Author: Sakshi Sanskruti Tripathy  
San José State University — Fall 2024  
Advisor: Prof. Amith Kamath Belman

This repository is artifact-complete for the CS297 project “Modular Enhancement Pipeline for Code-Generating LLMs.” We test whether a 0.5B model (`Qwen/Qwen2.5-Coder-0.5B-Instruct`) can be improved via external prompting, debugging, error classification, and risk prediction—without retraining. All runs used 164 HumanEval tasks under controlled seeds on Google Colab.

## 📌 What’s here
- HumanEval-style dataset with prompts, canonical solutions, and tests (`combined_humanEval_leetcode_dataset.jsonl`).
- Rubrics/configs for structured prompting (`llm_coding_tutor/configs/blueprint_weighted_v4.yaml`).
- Generated model candidates and repair attempts (`llm_coding_tutor/generated/`).
- Evaluation summaries, ablations, and plots (`llm_coding_tutor/results/`).
- Classifier assets for error/risk prediction (ECNN, GEPN).

## 📁 Repository structure (accurate)
```
CodeTutor-All-LLMS/
├── combined_humanEval_leetcode_dataset.jsonl   # tasks + canonical tests
├── llm_coding_tutor/
│   ├── configs/               # ADW rubric + model assets
│   │   ├── blueprint_weighted_v4.yaml
│   │   ├── ecnn/ ecnn_v3/ ecnn_v4/ ecnn_plus/   # TF-IDF + model joblibs, metadata
│   │   └── gepn/              # GEPN metadata and settings
│   ├── generated/             # per-variant generations/repairs
│   │   ├── baseline_seed1/
│   │   ├── baseline_primitive_seed1/
│   │   ├── adw_weighted_v4_teaching/
│   │   ├── adw_weighted_v4_teaching_seed1/
│   │   ├── adb_v1_from_adw_weighted/
│   │   ├── adb_v11_from_adw_weighted/
│   │   └── adb_v11_from_adw_weighted_seed1/
│   ├── results/               # CSV/JSON summaries, plots, ablations, error taxonomy
│   │   ├── ablation_barplot_v1.png
│   │   ├── ablation_cost_accuracy_scatter_v1.png
│   │   ├── ablation_curve_v1.png
│   │   ├── ablation_radar_v1.png
│   │   ├── error_heatmap_plot_v1.png
│   │   ├── pipeline_ablation_summary.csv
│   │   ├── summary_baseline.json
│   │   ├── adw_adb_pipeline_summary.json
│   │   └── summary_pipeline_v11.csv
│   ├── ecnn_v2/               # ECNN dataset snapshots and weights
│   ├── gepn/                  # GEPN feature matrices + model files
│   ├── adw/                   # ADW prompt builders
│   ├── adb/                   # ADB debugging modules
│   └── notebooks/             # (if present) Colab notebooks used to run experiments
└── README.md
```

## 🧩 Enhancement modules (implemented)
- **Baseline (40.24%)** — Raw Qwen2.5-Coder-0.5B; deterministic seed; strict execution harness. Artifacts: `generated/baseline_seed1/<task_id>/`, summary `results/summary_baseline.json`.
- **Primitive baseline (12.19%)** — Minimal prompt, higher temperature. Artifacts: `generated/baseline_primitive_seed1/`.
- **ADW v4 (29.88%)** — Advanced Dynamic Weighting using `blueprint_weighted_v4.yaml`; hierarchical dimensions (~35 subcriteria) with teaching-mode corruption to stress robustness. Artifacts: `generated/adw_weighted_v4_teaching/`, `results/adw_weighted_v4_teaching.csv`.
- **ADB v11 (~26.83% recovery on ADW fails)** — Single-round automated debugging; consumes prompt + failing code + traceback to patch shallow issues. Artifacts: `generated/adb_v11_from_adw_weighted/`, `results/adb_from_adw_summary.csv`.
- **ADW→ADB pipeline (56.71%)** — Sequential ADW then ADB; combined view in `results/adw_adb_pipeline_summary.json` and `results/summary_pipeline_v11.csv`.
- **Controlled failure dataset** — Synthetic + real labeled failures across six categories. Stored in `results/controlled_failures_v1.csv` and `ecnn_v2/ecnn_train_mini.csv`.
- **ECNN** — 6-class error classifier (TF-IDF + structural signals). Assets in `configs/ecnn*` and `ecnn_v2/`.
- **GEPN** — Risk predictor (TF-IDF + numeric features). Assets in `configs/gepn/` and `gepn/`; gating results in `results/adw_gepn_gate_v*.csv`.
- **GEPN-gated controller (46.95%)** — Chooses cheap/normal/heavy generation and when to call ADB/ECNN. Artifacts: `generated/gepn_gated_adw_adb_ecnn/`, `results/gepn_gated_summary.json`.
- **Union-mode ensemble (56.71%)** — Counts success if any candidate across baseline/ADW/ADB/ECNN passes. See `results/pipeline_ablation_summary.csv`.

## 📊 Results (from repo artifacts)
| Variant / source file | Tasks | Passed | Pass rate | Notes |
| --- | --- | --- | --- | --- |
| Baseline (`summary_baseline.json`) | 328 (seeds 1–2) | 132 | 40.24% | Raw model runs |
| Baseline subset (`summary_pipeline_v11.csv`) | 164 | 66 | 40.24% | 164-task slice |
| ADW weighted v4 teaching (`summary_pipeline_v11.csv`) | 164 | 49 | 29.88% | Rubric prompting |
| ADB v11 from ADW (`summary_pipeline_v11.csv`) | 115 | 44 | 38.26% | Repairs ADW failures only |
| ADW→ADB combined (`adw_adb_pipeline_summary.json`) | 164 | 93 | 56.71% | Best combined in this set |

## 📚 How to browse
1) Problems/tests: open rows in `combined_humanEval_leetcode_dataset.jsonl`.  
2) Specific generation: `llm_coding_tutor/generated/<variant>/HumanEval/<task_id>/` → read `.py` and `.log.txt`.  
3) Metrics/plots: CSV/JSON + PNGs under `llm_coding_tutor/results/`.  
4) Diagrams already rendered: `error_heatmap_plot_v1.png`, `plots_passrate_adw_adb_v11.png`, `ablation_barplot_v1.png`, `ablation_curve_v1.png`, `ablation_radar_v1.png`, `ablation_cost_accuracy_scatter_v1.png`.

## 🛠 How to reproduce (conceptual)
- Runs were executed in Google Colab using notebooks under `llm_coding_tutor/notebooks` (not included here).  
- Typical flow: load HumanEval → run baseline or ADW → run ADB on ADW failures → optional ECNN/GEPN scoring → GEPN-gated controller → gather results/plots under `results/` and generations under `generated/`.

## Notes
- Model: `Qwen/Qwen2.5-Coder-0.5B-Instruct`.
- Rubric for ADW/ADB: `llm_coding_tutor/configs/blueprint_weighted_v4.yaml`.
- This repo is an artifact store; execution environment setup is not part of the repo.