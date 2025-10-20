# MetaFlux: E. coli Metabolic Network Analysis and Gene Essentiality Prediction

**A computational biology tool for constraint-based metabolic modeling and gene essentiality analysis**

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![COBRApy](https://img.shields.io/badge/COBRApy-0.26+-green.svg)](https://opencobra.github.io/cobrapy/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

## Overview

MetaFlux is a computational biology pipeline for analyzing E. coli genome-scale metabolic models using constraint-based modeling (COBRApy). The tool systematically validates gene essentiality predictions across 60+ metabolic models against experimental datasets, providing comprehensive accuracy metrics and comparative analysis.

### Key Features

- **Multi-model analysis**: Process and compare 60+ E. coli genome-scale metabolic models from the BiGG database
- **Gene essentiality prediction**: Perform in-silico gene knockout simulations using flux balance analysis (FBA)
- **Comprehensive validation**: Compare predictions against multiple experimental reference datasets
- **Accuracy metrics**: Calculate precision, recall, F1-score, and Matthews correlation coefficient
- **Batch processing**: Parallel model analysis with automatic caching for efficient reanalysis
- **Visualization**: Generate comparative charts and network visualizations

## Scientific Background

**Genome-scale metabolic models (GEMs)** are mathematical representations of cellular metabolism that enable computational predictions of metabolic phenotypes, including gene essentiality. However, model quality and predictive accuracy vary significantly across different reconstructions.

This project addresses the critical need to:
1. **Systematically evaluate** the accuracy of metabolic models against experimental data
2. **Compare models** to identify which reconstructions provide the most reliable predictions
3. **Assess gene essentiality predictions** across different growth conditions and model versions

The analysis pipeline uses **constraint-based modeling** (specifically Flux Balance Analysis) to simulate gene knockouts and predict their effects on cellular growth, then validates these predictions against published experimental gene essentiality datasets.

## Tech Stack

### Core Technologies
- **Python 3.7+** - Primary programming language
- **COBRApy** - Constraint-Based Reconstruction and Analysis in Python
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Jupyter Notebook** - Interactive analysis environment

### Additional Libraries
- **NetworkX** - Network analysis and visualization
- **Matplotlib/Seaborn** - Data visualization
- **OpenPyXL/XlRD** - Excel file handling
- **ODFpy** - ODS file support
- **Requests** - Model downloading from BiGG database

## Repository Structure

```
metabolic-network-essentiality-analyzer/
├── src/                                   # Main source code (formerly python_prj/pythonProject/)
│   ├── metabolic_analysis.ipynb          # Primary analysis notebook
│   ├── test.py                           # Utility script
│   ├── models/                           # SBML model files (60+ E. coli models, ~687MB)
│   ├── pickled/                          # Cached model objects for faster loading
│   ├── data/                             # Reference datasets
│   │   ├── MSB-14-e7573-s004.xlsx       # Reference dataset (Joyce et al.)
│   │   ├── msb4100050-s5.xls            # Reference dataset (Baba et al.)
│   │   ├── pone.0236890.s001.ods        # LB medium composition
│   │   └── essentialgenes_list.xlsx     # Essential genes list
│   └── results/                          # Analysis outputs
│       ├── gene_accuracy_results_per_reference_and_metrics.csv
│       ├── model_accuracy_results_per_reference_and_metrics.csv
│       ├── gene_knockout_comparison.csv
│       └── output.png                    # Visualization
├── docs/                                  # Documentation and archived files
├── .gitignore                            # Git ignore patterns
├── README.md                             # This file
└── requirements.txt                       # Python dependencies
```

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Jupyter Notebook
- 4+ GB RAM (for loading large metabolic models)
- 2+ GB disk space (for models and results)

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/Raminyazdani/biological-network-reconstruction.git
cd biological-network-reconstruction
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install pandas numpy openpyxl xlrd odfpy jupyter networkx matplotlib seaborn cobra
```

3. **Verify COBRApy installation:**
```bash
python -c "import cobra; print(f'COBRApy version: {cobra.__version__}')"
```

### Optional: Virtual Environment
It's recommended to use a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## How to Run

### Running the Main Analysis

1. **Navigate to the source directory:**
```bash
cd src
```

2. **Launch Jupyter Notebook:**
```bash
jupyter notebook metabolic_analysis.ipynb
```

3. **Execute the analysis:**
   - Run cells sequentially from top to bottom
   - The notebook will automatically download required models from BiGG database if not present
   - Analysis may take 30-60 minutes depending on system performance
   - Results will be saved to the `results/` directory

### Running from Command Line

For automated analysis without interactive notebook:
```bash
cd src
jupyter nbconvert --execute --to notebook metabolic_analysis.ipynb
```

### Quick Test

Run the test script to verify installation:
```bash
cd src
python test.py
```

## Usage Guide

### Analysis Pipeline Overview

The notebook implements the following workflow:

1. **Model Loading**: Fetches E. coli metabolic models from BiGG database
2. **Medium Configuration**: Sets up growth medium conditions (LB medium)
3. **Gene Knockout Simulation**: Performs in-silico knockouts using FBA
4. **Data Comparison**: Compares predictions with experimental datasets
5. **Accuracy Calculation**: Computes precision, recall, F1, MCC metrics
6. **Results Export**: Saves comprehensive results to CSV files
7. **Visualization**: Generates comparative charts

### Key Analysis Components

**Gene Essentiality Prediction:**
- Uses COBRApy's `model.genes.get_by_id(gene).knock_out()` method
- Simulates growth with and without each gene
- Classifies genes as essential if knockout prevents growth (growth rate < threshold)

**Model Comparison:**
- Processes 60+ E. coli genome-scale models
- Includes models from iJR904 to iML1515 spanning different E. coli strains
- Compares model predictions against 3 reference datasets

**Accuracy Metrics:**
- **Precision**: Proportion of predicted essential genes that are truly essential
- **Recall**: Proportion of truly essential genes that are correctly predicted
- **F1-Score**: Harmonic mean of precision and recall
- **MCC**: Matthews correlation coefficient (balanced metric for imbalanced datasets)

## Data and Inputs

### Input Files

The analysis uses several reference datasets from published studies:

1. **MSB-14-e7573-s004.xlsx** - Joyce et al. reference dataset
   - Gene essentiality data for E. coli
   
2. **msb4100050-s5.xls** - Baba et al. Keio collection
   - Systematic gene knockout library data
   
3. **pone.0236890.s001.ods** - LB medium composition
   - Growth medium metabolite concentrations
   
4. **essentialgenes_list.xlsx** - Curated essential genes
   - Reference list of known essential genes

### Metabolic Models

Models are automatically downloaded from the BiGG database on first run:
- **60+ E. coli genome-scale models** in SBML format
- Stored in `src/models/` directory
- Include major reconstructions: iJR904, iAF1260, iJO1366, iML1515
- Also includes human models: RECON1, Recon3D, Human-GEM

### Cached Data

The `pickled/` directory contains serialized model objects:
- Faster loading for repeated analysis
- Automatically generated on first run
- Safe to delete - will be regenerated if needed

## Outputs and Results

### Output Files

All results are saved in the `results/` directory:

1. **gene_accuracy_results_per_reference_and_metrics.csv**
   - Per-gene accuracy metrics across all models and reference datasets
   - Columns: Gene ID, Model, Reference Dataset, Prediction, Actual, Correct
   
2. **model_accuracy_results_per_reference_and_metrics.csv**
   - Aggregated model performance metrics
   - Columns: Model, Reference, Precision, Recall, F1-Score, MCC, Total Genes
   
3. **gene_knockout_comparison.csv**
   - Detailed knockout simulation results
   - Growth rates before/after knockout for each gene-model combination
   
4. **output.png**
   - Visualization comparing model accuracies
   - Bar charts or heatmaps showing performance across models

### Interpreting Results

- **High F1-Score (>0.8)**: Model provides reliable gene essentiality predictions
- **High Precision, Low Recall**: Model is conservative (misses some essential genes)
- **Low Precision, High Recall**: Model over-predicts essentiality
- **MCC close to 1**: Excellent overall prediction quality
- **MCC close to 0**: Predictions no better than random

## Reproducibility Notes

### Environment
- **Python version**: 3.7+ recommended (tested on 3.8, 3.9, 3.10)
- **Operating systems**: Linux, macOS, Windows (with path adjustments)
- **Memory**: 4GB+ RAM recommended for large models
- **Disk space**: 2GB+ for models and cached data

### Deterministic Analysis
- COBRApy FBA solutions are deterministic for the same model and constraints
- Random seeds are not required for this analysis
- Results should be reproducible across different systems

### Known Variations
- Model download times vary based on network speed
- Computation time depends on CPU performance (30-60 minutes typical)
- Floating-point precision may cause minor numerical differences across platforms

### Version Compatibility
- Tested with COBRApy 0.26.0+
- Compatible with Pandas 1.5.0+ and NumPy 1.21.0+
- Jupyter Notebook or JupyterLab both supported

## Troubleshooting

### Common Issues and Solutions

**Import Errors:**
```bash
# If cobra is not found
pip install cobra

# If openpyxl/xlrd are missing
pip install openpyxl xlrd odfpy

# If matplotlib/seaborn errors occur
pip install matplotlib seaborn
```

**Memory Errors:**
- Close other applications to free RAM
- Process models in smaller batches
- Use pickled data for subsequent runs

**Model Download Failures:**
- Check internet connection
- Verify BiGG database accessibility: http://bigg.ucsd.edu
- Manually download models and place in `src/models/` directory

**File Not Found Errors:**
- Ensure you're running from the correct directory
- Use absolute paths if relative paths fail
- Check that reference data files are in `src/data/`

**Slow Performance:**
- First run is slow (downloads and processes all models)
- Subsequent runs use cached pickled data (much faster)
- Consider processing fewer models for testing

**Path Issues on Windows:**
- Use forward slashes in paths or pathlib
- Avoid directory names with non-ASCII characters
- Run Jupyter from the project root directory

### Getting Help
- Check COBRApy documentation: https://cobrapy.readthedocs.io/
- BiGG Models database: http://bigg.ucsd.edu/
- Report issues on the GitHub repository

## Citation and References

### Datasets Used
1. Joyce et al. - Gene essentiality data (MSB-14-e7573-s004.xlsx)
2. Baba et al. - Keio collection (msb4100050-s5.xls)
3. LB medium composition (pone.0236890.s001.ods)

### Key Tools
- COBRApy: Ebrahim et al. (2013). COBRApy: COnstraints-Based Reconstruction and Analysis for Python. BMC Systems Biology.
- BiGG Models: King et al. (2016). BiGG Models: A platform for integrating, standardizing and sharing genome-scale models. Nucleic Acids Research.

## License

This project is available for academic and research purposes. Please cite appropriately if you use this code or methodology in your research.

## Keywords

`computational-biology` `metabolic-modeling` `systems-biology` `gene-essentiality` `cobra` `flux-balance-analysis` `genome-scale-models` `e-coli` `bioinformatics` `constraint-based-modeling`

---

**Project maintained by:** [Raminyazdani](https://github.com/Raminyazdani)  
**Last updated:** December 2025
