import subprocess

#subprocess.run(["ls", "-aF"])
import subprocess

subprocess.run([
    "python", "sagittal_brain.py",
    "brain_sample.csv",
    "--file_output", "brain_average.csv"
], check=True)