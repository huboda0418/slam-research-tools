# Experiment Statistics

Utilities for statistical analysis of repeated SLAM experiments.

## Multi-run Summary

`summarize_runs.py` calculates basic statistics from repeated experimental results.

Example:

```bash
python summarize_runs.py 0.151 0.139 0.130
## Outputs:

Number of runs
Mean
Sample standard deviation
Minimum
Maximum

This is useful for reporting SLAM metrics such as ATE RMSE, map size, runtime, PSNR, SSIM, and LPIPS across repeated experiments.
