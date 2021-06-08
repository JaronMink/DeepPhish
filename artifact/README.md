# Artifact Overview

This folder contains the artifact used in the paper ["DeepPhish: Understanding User Trust Towards Artificially Generated Profiles in Online Social Networks"](https://jaronm.ink/assets/pdf/papers/deepphish_usenix22.pdf). This artifact has been successfully evaluated for availability, functionality, and reproducibility at USENIX Security 2022.

## Contents

- **quantitative\_analysis.Rmd**: This R notebook contains the analysis code used to produce all the tables, figures, statistical tests, and summary statistics found in the paper results.
- **expected\_quantitative\_analysis.pdf**: This pdf contains the expected output of the quantiative\_analysis.Rmd notebook.
- **codebook_kappa.py**: This python script outputs the interrater reliability of the primary and secondary codings found in the qualitative_codings.xlsx spreadsheet.
- **dependencies**: A folder containing the scripts and requirements file used in quantitative_analysis.Rmd and codebook\_kappa.py
- **README.md** - This file.

The following artifact components are not publicly available due to privacy restrictions on participant data.

- **qualitative\_codings.xlsx**: A file which contains the raw participant qualitative responses, primary and secondary codings, and the aggregated counts presented in the qualitative results (Section 5).
- **data**: A folder which which contains the raw anonyized participant responses by study and prompt.
