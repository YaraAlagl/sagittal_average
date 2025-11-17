import numpy as np
import sys
import os

# Correct import path based on your folder structure
from src.sagittal_average.sagittal_brain import run_averages

# --- Step 1 recap: define the test input and expected output ---

# File paths inside sagittal_repo
INPUT_FILE = "src/sagittal_average/brain_sample.csv"
OUTPUT_FILE = "src/sagittal_average/brain_average.csv"

data_input = np.zeros((20, 20))
data_input[-1, :] = 1  # simple pattern to make differences visible

# Save input file for test
np.savetxt(INPUT_FILE, data_input, fmt='%d', delimiter=',')

# Run student's code
run_averages(INPUT_FILE, OUTPUT_FILE)

# --- Step 2: Load output ---
output = np.loadtxt(OUTPUT_FILE, delimiter=',')

# --- Step 3: Expected result ---
expected_output = np.zeros((20, 20))
expected_output[-1, :] = 1

# --- Step 4: The actual test assertion ---
def test_sagittal_average_correctness():
    assert np.allclose(output, expected_output)
