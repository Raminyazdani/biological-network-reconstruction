# Biological Network Reconstruction (بازسازی شبکه های زیستی)

**Project Type:** University Project  
**Primary Stack:** Python/Jupyter

## Description

This is a biological network reconstruction project that focuses on metabolic network modeling and analysis. The project involves reconstructing biological networks, analyzing gene essentiality, comparing different metabolic models, and evaluating model accuracy using various reference datasets.

## Tech Stack

- Python 3.x
- Jupyter Notebook
- Pandas
- NumPy
- NetworkX (likely for network analysis)
- Metabolic modeling tools

## Folder Structure

```
بازسازی شبکه های زیستی/
├── python_prj/
│   └── pythonProject/
│       ├── project.ipynb                                    # Main Jupyter notebook
│       ├── MSB-14-e7573-s004.xlsx                          # Reference dataset
│       ├── msb4100050-s5.xls                               # Reference dataset
│       ├── pone.0236890.s001.ods                           # Reference dataset
│       ├── essentialgenes_list.xlsx                        # Essential genes data
│       ├── gene_accuracy_results_per_reference_and_metrics.csv
│       ├── model_accuracy_results_per_reference_and_metrics.csv
│       ├── gene_knockout_comparison.csv                    # Gene knockout analysis
│       ├── output.png                                       # Visualization output
│       ├── models/                                          # Metabolic models directory
│       ├── pickled/                                         # Serialized data
│       └── test.py                                          # Test script
├── فایل های استفاده شده از مقالات/                         # Files from papers
├── نتایج/                                                  # Results directory
├── گزارش.docx                                              # Project report (Persian)
└── README.md                                                 # This file
```

## Setup / Installation

Install required dependencies:
```bash
pip install pandas numpy openpyxl jupyter networkx matplotlib seaborn
```

For metabolic modeling (if using COBRApy):
```bash
pip install cobra
```

Or using requirements file:
```bash
pip install -r requirements.txt
```

## How to Run

1. Navigate to the project directory:
```bash
cd "بازسازی شبکه های زیستی/python_prj/pythonProject"
```

2. Start Jupyter Notebook:
```bash
jupyter notebook project.ipynb
```

3. Run cells sequentially from top to bottom

Alternatively, run the test script:
```bash
python test.py
```

## Inputs/Outputs

**Inputs:**
- `MSB-14-e7573-s004.xlsx` - Reference metabolic data
- `msb4100050-s5.xls` - Reference dataset  
- `pone.0236890.s001.ods` - Reference dataset
- `essentialgenes_list.xlsx` - List of essential genes
- `models/` - Metabolic network models

**Outputs:**
- `gene_accuracy_results_per_reference_and_metrics.csv` - Gene prediction accuracy
- `model_accuracy_results_per_reference_and_metrics.csv` - Model performance metrics
- `gene_knockout_comparison.csv` - Gene knockout simulation results
- `output.png` - Network or analysis visualization
- `pickled/` - Serialized analysis objects
- `نتایج/` - Comprehensive results directory

## Notes

- Project focuses on metabolic network reconstruction and validation
- Compares models against multiple reference datasets
- Analyzes gene essentiality and knockout effects
- All file paths are relative to the project directory
- Persian language documentation in گزارش.docx
- Uses multiple reference datasets from scientific publications

## Troubleshooting

- If you get import errors: `pip install pandas numpy openpyxl jupyter networkx`
- For Excel file reading issues: `pip install openpyxl xlrd`
- For ODS file support: `pip install odfpy`
- If metabolic modeling fails, ensure COBRApy is installed: `pip install cobra`
- For memory issues with large models, consider using sparse matrices
