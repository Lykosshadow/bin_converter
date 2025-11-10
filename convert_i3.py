#!/usr/bin/env python3

import readinsight3
from pathlib import Path
import sys
import pandas as pd

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_i3.py <input_file.bin>")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    if not input_file.is_file():
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    output_file = input_file.with_suffix(".csv")

    # Load Insight3 .bin file
    i3_data = readinsight3.loadI3File(str(input_file))

    # Convert structured array to DataFrame
    df = pd.DataFrame(i3_data)

    # Save as CSV
    df.to_csv(output_file, index=False)

    print(f"Converted {input_file} → {output_file}")

if __name__ == "__main__":
    main()
