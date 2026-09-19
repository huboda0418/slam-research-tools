# SLAM Research Tools

A collection of lightweight utilities for **SLAM experiment evaluation, statistical analysis, result organization, and visualization**.

This repository is maintained during my research on **Visual SLAM** and **3D Gaussian Splatting SLAM**, with a particular focus on repeated experiments, ablation studies, parameter analysis, and compact mapping evaluation.

## Overview

SLAM experiments often involve multiple independent runs, parameter sweeps, trajectory evaluation, map-size statistics, runtime measurements, and image-quality metrics.

This repository collects reusable scripts for processing and analyzing these experimental results.

## Features

Current and planned utilities include:

- Multi-run statistical analysis
- Mean and standard deviation calculation
- ATE / trajectory result organization
- Gaussian map-size statistics
- Runtime analysis
- Parameter sensitivity analysis
- CSV result processing
- Experimental result visualization

## Repository Structure

```text
slam-research-tools/
├── README.md
├── statistics/
│   ├── README.md
│   └── summarize_runs.py
├── trajectory/
├── gaussian-analysis/
└── visualization/
```

## Statistics

### Multi-run Summary

`statistics/summarize_runs.py` computes basic statistics from repeated experimental runs.

Example:

```bash
python statistics/summarize_runs.py 0.151 0.139 0.130
```

The script reports:

- Number of runs
- Mean
- Sample standard deviation
- Minimum
- Maximum

It can be used for SLAM metrics such as:

- ATE RMSE
- Map size / Gaussian count
- Runtime
- PSNR
- SSIM
- LPIPS

## Research Context

My current research focuses on **dynamic-scene 3D Gaussian SLAM**.

A typical experimental workflow involves:

1. Running multiple independent experiments
2. Collecting trajectory and mapping results
3. Computing statistical summaries
4. Comparing different methods and ablation settings
5. Analyzing map compactness and runtime
6. Visualizing parameter sensitivity and experimental trends

The tools in this repository are intended to simplify and standardize this workflow.

## Planned Development

- [x] Multi-run statistics utility
- [ ] ATE result collection
- [ ] Gaussian-count analysis
- [ ] Runtime statistics
- [ ] Parameter sensitivity analysis
- [ ] CSV batch processing
- [ ] Result visualization
- [ ] Experiment summary generation

## Environment

Mainly developed and tested with:

- Python 3
- NumPy
- pandas
- Matplotlib
- Linux / Ubuntu

## Author

**Boda Hu**  
M.S. Student in Instrument Science and Technology  
Henan Polytechnic University  

Research interests: Robotic 3D Vision, Visual SLAM, 3D Gaussian Splatting, and Intelligent Perception.
