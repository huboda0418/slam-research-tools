import argparse
import numpy as np


def summarize(values):
    values = np.asarray(values, dtype=float)

    print(f"Runs : {len(values)}")
    print(f"Mean : {values.mean():.6f}")
    print(f"Std  : {values.std(ddof=1):.6f}")
    print(f"Min  : {values.min():.6f}")
    print(f"Max  : {values.max():.6f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Summarize results from repeated SLAM experiments."
    )

    parser.add_argument(
        "values",
        nargs="+",
        type=float,
        help="Experimental values from multiple runs."
    )

    args = parser.parse_args()

    summarize(args.values)
