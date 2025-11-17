import argparse
from .sagittal_brain import run_averages


def main():
    parser = argparse.ArgumentParser(
        description="Compute sagittal averages from an input CSV file."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input CSV file"
    )
    parser.add_argument(
        "output_file",
        type=str,
        nargs="?",
        default="brain_average.csv",
        help="Output CSV file (default: brain_average.csv)"
    )

    args = parser.parse_args()

    run_averages(args.input_file, args.output_file)
    print(f"Average written to {args.output_file}")
