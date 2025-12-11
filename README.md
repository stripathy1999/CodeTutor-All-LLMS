# CodeTutor-All-LLMS

Artifacts and results for CS297 (Fall 2024) — “Modular Enhancement Pipeline for Code-Generating LLMs.” The goal: push a small code model (Qwen2.5-Coder-0.5B-Instruct) using external prompting, debugging, and risk-prediction modules—no model retraining required.

## Overview
- Full enhancement pipeline implementation and artifacts
- Evaluation results on 164 HumanEval tasks
- Controlled failure dataset + error classification experiments
- GEPN risk prediction model
- All generated artifacts, repaired variants, and metadata

## Base Model
- Model: **Qwen2.5-Coder-0.5B-Instruct**
- Chosen to study: brittleness, failure modes, recoverability, prompt sensitivity
- Focus: improve reliability via external reasoning modules instead of scaling parameters

## Repository Structure
```
llm_coding_tutor/
├── configs/                      # ADW blueprints, GEPN config, metadata (e.g., blueprint_weighted_v4.yaml)
├── generated/                    # All model generations and repairs (baseline, ADW, ADB, GEPN-gated, etc.)
├── results/                      # CSV/JSON summaries, plots, error taxonomies, ablations
├── ecnn_v2/                      # ECNN dataset and model weights
├── gepn/                         # GEPN feature matrices + model files
├── adw/                          # ADW prompt builders and stress tests
├── adb/                          # ADB multi-round debugging modules
└── notebooks/                    # End-to-end execution notebooks (Colab-style)
```
Additional top-level:
- `combined_humanEval_leetcode_dataset.jsonl` — task prompt, entry point, canonical solution, and tests

## Enhancement Pipeline (CS297)
1) **Baseline** — Raw Qwen2.5-Coder-0.5B on 164 HumanEval tasks; deterministic seed; isolated exec harness. *Pass rate: 40.24%*. Artifacts: `generated/baseline_seed1/<task_id>/`  
2) **Primitive baseline** — Minimal prompt, higher temperature. *Pass rate: 12.19%*. Artifacts: `generated/baseline_primitive_seed1/`  
3) **ADW (Advanced Dynamic Weighting)** — Hierarchical rubric-driven prompting (`blueprint_weighted_v4.yaml`), 10 pedagogical dimensions, weighted sub-criteria, teaching-mode stress (35% corruption). *Pass rate: 29.88%*. Artifacts: `generated/adw_weighted_v4_teaching/`, `results/adw_weighted_v4_teaching.csv`  
4) **ADB (Automated Debugging Workflow)** — Single-round automated debugging on failing ADW outputs (traceback + prompt); fixes shallow structural errors. *Recovery: ~26.83% of ADW fails*. Artifacts: `generated/adb_v11_from_adw_weighted/`, `results/adb_from_adw_summary.csv`  
5) **Controlled failure dataset** — 410 synthetic + 64 real labeled failures; six categories (DOCSTRING, EDGE_CASES, LOGIC_RANGE, RETURNS_NOT_PRINT, SIGNATURE, TYPE_CAST). Artifacts: `ecnn_v2/ecnn_train_mini.csv`, `results/controlled_failures_v1.csv`  
6) **ECNN (Error Correction Neural Networks)** — 6-class error classifier using TF-IDF + structural signals (fast MLP/logistic). High train accuracy; limited generalization but useful for routing repairs. Artifacts: `ecnn_v2/ecnn_tfidf.joblib`, `ecnn_v2/ecnn_mlp.joblib`  
7) **GEPN (Generative Error Prediction Networks) ** — Risk predictor over TF-IDF + numeric signals (2,047 samples, 5,022 features); calibrated logistic regression. Metrics: Acc 79.27%, ROC-AUC 0.8957, Brier 0.1437. Artifacts: `gepn/gepn_model_v8.joblib`, `gepn/gepn_tfidf.joblib`, `gepn/gepn_train.csv`  
8) **GEPN-gated controller** — Chooses cheap/normal/heavy generation, when to call ADB/ECNN, and token budgets. *Pass rate: ~46.95%*. Artifacts: `generated/gepn_gated_adw_adb_ecnn/`, `results/gepn_gated_summary.json`  
9) **Union ensemble (post-hoc)** — Baseline + ADW + ADB; marks task correct if any candidate passes. *Best pass rate: ~56.71%*.  

## Key Results
| Variant | Pass rate (approx.) |
| --- | --- |
| Baseline | 40.24% |
| Primitive baseline | 12.19% |
| ADW | 29.88% |
| ADB (from ADW) | 26.83% recovery on fails |
| GEPN-gated ADW+ADB+ECNN | 46.95% |
| Union ensemble | 56.71% |

## How to Explore
- Browse problems/tests: open rows in `combined_humanEval_leetcode_dataset.jsonl`
- Inspect generations: `llm_coding_tutor/generated/<variant>/HumanEval/<task_id>/`
- View summaries/plots: CSV/JSON and PNGs in `llm_coding_tutor/results/` (e.g., `error_heatmap_plot_v1.png`, `plots_passrate_adw_adb_v11.png`)

## How to Run (artifact-focused)
- Orchestrated via notebooks under `notebooks/` (if present); this repo primarily stores artifacts/results.
- Typical flow: install deps → load Qwen2.5-Coder-0.5B → load HumanEval → run baseline or ADW/ADB variants → generate artifacts → run post-processing/plots → run ablations or GEPN-gated experiments.

## Notes
- Model used: `Qwen/Qwen2.5-Coder-0.5B-Instruct`
- Rubric: `blueprint_weighted_v4.yaml` encodes the scoring focus for ADW/ADB pipelines