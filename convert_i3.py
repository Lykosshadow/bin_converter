import readinsight3
from pathlib import Path

#Set your input file here
input_file = Path(".bin")
output_file = input_file.with_suffix(".csv")

#Load Insight3 .bin file
i3_data = readinsight3.loadI3File(str(input_file))

#Save as CSV
i3_data.toCSV(str(output_file))

print(f"Converted {input_file} → {output_file}")
