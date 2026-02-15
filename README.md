# Long-Document-Multi-Document-Abstractive-Summarization


This repository contains the complete project pipeline for long-document and multi-document abstractive summarization using sparse-attention Transformer models. The project focuses on efficient handling of long sequences and multi-document inputs with LED and PRIMERA-style architectures.

Project Overview

Long-document summarization is challenging due to quadratic attention cost and loss of global context in standard Transformer models. This project implements a data-centric pipeline and model-level experiments for multi-document abstractive summarization, including cleaning, clustering, filtering, model inference, and evaluation.

Project Structure
Project 1/
│
├── data/
│   ├── raw/                 # Clustered raw datasets (JSON)
│   ├── Cleaned/             # Cleaned NewsSumm dataset (CSV/XLSX)
│   ├── train.csv            # Training split
│   └── val.csv              # Validation split
│
├── scripts/
│   ├── clean_newssumm.py
│   ├── create_clusters.py
│   ├── filter_multidoc.py
│   ├── prepare_for_model.py
│   ├── dataset_stats.py
│   ├── evaluate_rouge.py
│   ├── test_led_inference.py
│   └── primera_inference.py
│
├── models/
│   ├── primera/
│   └── category_aware_led.py
│
└── README.md

Pipeline

Raw NewsSumm
→ Cleaning
→ Document Clustering
→ Multi-Document Filtering
→ Train/Validation Split
→ LED / PRIMERA Inference
→ ROUGE Evaluation

Models Used

Longformer Encoder–Decoder (LED)

PRIMERA

Category-Aware LED (custom variant)

Datasets

NewsSumm (English)

Multi-document clusters generated from NewsSumm

Evaluation Metrics

ROUGE-1

ROUGE-2

ROUGE-L

Human Evaluation (fluency, coherence, coverage)

Features

End-to-end dataset preparation pipeline

Multi-document clustering

Long-sequence summarization support

Comparative model evaluation

Research-ready project structure

How to Run (High-Level)

Clean the dataset

Create document clusters

Filter multi-document samples

Prepare training and validation splits

Run LED / PRIMERA inference

Evaluate with ROUGE

Use Case

This project is intended for:

Final-year academic projects

Research experiments in NLP

Long-document and multi-document summarization studies

Comparative analysis of sparse-attention Transformer models

Citation

If you use this project in your research or report, please cite the relevant LED and PRIMERA papers.

Author

Rajan S B
