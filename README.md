 Long-Document & Multi-Document Abstractive Summarization
 
A complete research pipeline for long-document and multi-document abstractive summarization. This project leverages sparse-attention Transformer architectures to overcome the O(n2 ) complexity of traditional models, enabling the processing of sequences up to 16K tokens.

  Key Features
End-to-End Pipeline: From raw NewsSumm data to ROUGE evaluation.
Sparse Attention: Efficiently handles very long articles using LED and PRIMERA.
Multi-Doc Clustering: Custom pipeline to group related articles by semantic similarity and category.
Category-Awareness: Experimental variant incorporating metadata into the summarization process.
Research-Ready: Detailed dataset characterization and reproducible structure.

 System Pipeline
   The workflow ensures scalable experimentation and reliable evaluation:

Code snippet
 graph TD
    A[Raw NewsSumm Dataset] --> B[Cleaning & Feature Engineering]
    B --> C[Dataset Characterization]
    C --> D[Category Classification & Clustering]
    D --> E[Multi-Doc Dataset Creation]
    E --> F[Train / Validation Split]
    F --> G[LED / PRIMERA Inference]
    G --> H[Summary Generation]
    H --> I[ROUGE Evaluation]
    
  Models & Architectures
   We evaluate state-of-the-art models designed specifically for long-context windows.

Model	Description	Context Window

LED	Longformer Encoder-Decoder for long-document tasks.	Up to 16K
PRIMERA	Pre-trained specifically for Multi-Doc Summarization (MDS).	Up to 16K
Category-Aware LED	Custom variant using news categories to guide context.	Up to 16K

Dataset Analysis: NewsSumm
The pipeline uses the NewsSumm dataset, characterized by its high compression requirements.

 Quick Stats
 
 Metric	Value
 Total Samples	      22,780
 Avg. Article Length	903.68 tokens
 Avg. Summary Length	90.66 tokens
 Compression Ratio  	~10:1 (Highly Abstractive)
 
Length Distribution

Median Length: 651 tokens
Max Length: 41,454 tokens
Standard Deviation: 1146

Note: The high standard deviation and 40k+ max length justify the need for sparse-attention models over standard BERT/BART architectures.

Evaluation Results
 Performance is benchmarked using standard ROUGE metrics:

Metric	Score	Description
ROUGE-1	~0.50	Unigram overlap
ROUGE-2	~0.29	Bigram overlap
ROUGE-L	~0.37	Longest Common Subsequence

Project Structure

project
│
├── data/               # Raw and processed NewsSumm files
├── scripts/            # Cleaning, clustering, and evaluation logic
├── models/             # Implementation of LED, PRIMERA, and custom variants
├── results/            # ROUGE scores and generated summaries
└── README.md           # Project documentation

 How to Run
   Preprocessing: Run scripts/cleaning and scripts/clustering.
   Dataset Prep: Execute multi-doc creation and train/val split.
   Inference: Run the model scripts in models/ (e.g., python models/led/inference.py).
   Evaluation: Use scripts/evaluation to generate ROUGE reports.

Research Contribution

MDS NewsSumm: A newly clustered multi-document version of the NewsSumm dataset.
Pipeline Efficiency: A framework for handling 16K+ token sequences on consumer-grade research hardware.
Comparative Study: Empirical data on LED vs. PRIMERA for news-specific clusters.
