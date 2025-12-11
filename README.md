🚀 Overview

This repository contains all code, configuration files, artifacts, and evaluation results from CS297 (Fall 2024) for the project:

“Modular Enhancement Pipeline for Code-Generating LLMs”

The project evaluates whether a small 0.5B code model can be made more reliable without retraining, using a modular enhancement stack built entirely around the model rather than inside the model.

The implemented pipeline wraps the model with:

structured prompting

automated debugging

learned error correction

generative failure prediction

ensemble-style recovery

This repository includes:

the complete enhancement pipeline implementation

evaluation results on 164 HumanEval tasks

controlled failure dataset

error classification experiments

GEPN risk prediction model

all generated artifacts, repaired variants, and metadata

🧠 Base Model

The entire CS297 pipeline is built around:

Qwen2.5-Coder-0.5B-Instruct

A lightweight open-source code model chosen intentionally to explore:

brittleness

failure modes

recoverability

prompt sensitivity

The goal of CS297 was not to scale the model, but to determine whether external reasoning modules can lift its performance.

📁 Repository Structure (Structure A — Artifact-Focused)
llm_coding_tutor/
│
├── configs/                      # ADW blueprints, GEPN config, metadata
│   └── blueprint_weighted_v4.yaml
│
├── generated/                    # All model generations and repairs
│   ├── baseline_seed1/
│   ├── baseline_primitive_seed1/
│   ├── adw_weighted_v4_teaching/
│   ├── adb_v11_from_adw_weighted/
│   ├── adb_v2_from_adw_weighted/
│   └── gepn_gated_adw_adb_ecnn/
│
├── results/                      # CSVs, json summaries, plots
│   ├── baseline_seed1.csv
│   ├── baseline_primitive_seed1.csv
│   ├── adw_weighted_v4_teaching.csv
│   ├── adb_from_adw_summary.csv
│   ├── gepn_gated_summary.json
│   ├── pipeline_ablation_summary.csv
│   ├── error_taxonomy_v1.csv
│   ├── error_heatmap_plot_v1.png
│   └── plots_passrate_adw_adb_v11.png
│
├── ecnn_v2/                      # ECNN dataset (real + synthetic), model weights
│   ├── ecnn_tfidf.joblib
│   ├── ecnn_mlp.joblib
│   └── ecnn_train_mini.csv
│
├── gepn/                         # GEPN feature matrices + model files
│   ├── gepn_tfidf.joblib
│   ├── gepn_model_v8.joblib
│   └── gepn_train.csv
│
├── adw/                          # ADW prompt builders and stress-tests
│   └── adw_v4_hierarchical.py
│
├── adb/                          # ADB multi-round debugging modules
│   └── adb_v11.py
│
└── notebooks/                    # End-to-end execution notebooks (Colab)


This structure is produced exactly by your CS297 code execution harness, with artifact directories dynamically created for every variant.

🧩 Enhancement Modules Implemented (CS297)

Your pipeline includes 7 modules, implemented in the order below and documented in your CS297 report.

All descriptions below come directly from your code, results, and project report.

1️⃣ Baseline Model Evaluation

Raw Qwen2.5-Coder-0.5B on 164 HumanEval tasks

Deterministic seed = 42

Strict Python execution harness with isolated temp directories

Pass Rate: 40.24%

Artifacts stored under:

generated/baseline_seed1/<task_id>/

2️⃣ Primitive Baseline (No-structure Prompt)

Minimal instruction prompt

Higher temperature (0.7)

Extremely brittle

Pass Rate: 12.19%

Artifacts:

generated/baseline_primitive_seed1/

3️⃣ ADW v4 — Advanced Dynamic Weighting (Hierarchical Weighted Prompting)

A structured, rubric-based prompt builder using:

hierarchical blueprint (blueprint_weighted_v4.yaml)

10 pedagogical dimensions (correctness, edge cases, readability, etc.)

weighted and sampled sub-criteria

teaching mode with 35% intentional corruption to stress-test robustness

Results:

Pass Rate: 29.88%

Artifacts:

generated/adw_weighted_v4_teaching/
results/adw_weighted_v4_teaching.csv

4️⃣ ADB v11 — Automated Debugging Workflow

ADB takes:

failing ADW output

traceback + logs

original prompt

And produces a repaired candidate.

Key details (from code + conversations):

Single-shot repair

1 round only

Triggered after ADW outputs

Designed to fix shallow structural errors

Results:

Repair recovery rate: 26.83%

Cannot fix deep logic issues

Artifacts:

generated/adb_v11_from_adw_weighted/
results/adb_from_adw_summary.csv

5️⃣ Controlled Failure Dataset (Synthetic + Real)

To train error classifiers, you generated:

410 synthetic failures

64 real labeled failure examples

6 error categories (DOCSTRING, EDGE_CASES, LOGIC_RANGE, RETURNS_NOT_PRINT, SIGNATURE, TYPE_CAST)

Dataset stored in:

ecnn_v2/ecnn_train_mini.csv
results/controlled_failures_v1.csv


This dataset powers ECNN training.

6️⃣ ECNN v2 — Error Correction Neural Network

A hybrid classifier using:

TF-IDF (traceback text)

AST-derived structural features

Fast MLP/logistic model for 6-class prediction

Training accuracy (overfitted): 100%
Validation generalizability: weak, but still useful to trigger targeted repair actions.

Artifacts:

ecnn_v2/ecnn_tfidf.joblib
ecnn_v2/ecnn_mlp.joblib

7️⃣ GEPN v8 — Generative Error Prediction Network

A risk predictor built on:

2047 samples (1558 original fails + 489 injected passes)

5022 total features (TF-IDF + numeric signals)

Calibrated logistic regression

Metrics:

Accuracy: 79.27%

ROC-AUC: 0.8957

Brier score: 0.1437

Artifacts:

gepn/gepn_model_v8.joblib
gepn/gepn_tfidf.joblib
gepn/gepn_train.csv

8️⃣ GEPN-Gated Unified Controller

This is your highest engineering contribution in CS297.

GEPN decides:

cheap / normal / heavy generation

whether to call ADB

whether to call ECNN

whether to increase token budget

Final Pass Rate:

⭐ 46.95% (vs. 40.24% baseline)

Artifacts:

generated/gepn_gated_adw_adb_ecnn/
results/gepn_gated_summary.json

9️⃣ Union-Mode Ensemble Recovery (Post-Hoc)

If any candidate from:

baseline

ADW

ADB

ECNN

passes the test, the task is marked correct.

Final union pass-rate:

⭐ 56.71% — the highest in the entire project
📊 Key Results Summary (CS297)
Variant	Pass Rate
Baseline	40.24%
Primitive	12.19%
ADW v4	29.88%
ADB v11 (from ADW)	26.83%
GEPN-Gated ADW+ADB+ECNN	46.95%
Union-Mode Ensemble	56.71%

Plots stored under:

results/error_heatmap_plot_v1.png
results/plots_passrate_adw_adb_v11.png
results/pipeline_ablation_summary.csv

🔧 How to Run the Pipeline

All execution happens through the Colab notebooks under:

notebooks/


Steps:

Install dependencies

Load Qwen2.5-Coder-0.5B

Load HumanEval dataset

Run baseline or ADW/ADB variants

Generate + save artifacts

Run post-processing & visualizations

Run ablation or GEPN-gated experiments