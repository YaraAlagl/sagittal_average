# test_sagittal_brain.py
import sys
from pathlib import Path
import numpy as np

# --- Add src folder to Python path for editable installs ---
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))

# --- Import your module ---
from sagittal_brain import run_averages

# --- Paths ---
test_dir = Path(__file__).parent
input_file = test_dir / "brain_sample.csv"
output_file = test_dir / "brain_average.csv"

# --- Step 1: create test input ---
data_input = np.zeros((20, 20))
data_input[-1, :] = 1  # simple pattern to make differences visible

# Save input CSV in test directory
np.savetxt(input_file, data_input, fmt='%d', delimiter=',')

# --- Step 2: run the function ---
try:
    run_averages(input_file, output_file)
except Exception as e:
    raise RuntimeError(f"Error while running run_averages: {e}")

# --- Step 3: read the output ---
assert output_file.exists(), f"Output file not found: {output_file}"
result = np.loadtxt(output_file, delimiter=',')

# --- Step 4: define expected result ---
expected_output = np.zeros((20, 20))
expected_output[-1, :] = 1  # adjust to match expected sagittal average

# --- Step 5: check if the result matches ---
def test_sagittal_average():
    assert np.allclose(result, expected_output), (
        f"Output does not match expected.\nOutput:\n{result}\nExpected:\n{expected_output}"
    )
