import numpy as np
import sys
from sagittal_brain import run_averages  # adjust to match Charlene’s module

# --- Step 1 recap: define the test input and expected output ---
data_input = np.zeros((20, 20))
data_input[-1, :] = 1  # simple pattern to make differences visible

# Save input for Charlene's code
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

# Run Charlene’s code (it should read brain_sample.csv and write brain_average.csv)
try:
    run_averages("brain_sample.csv", "brain_average.csv")
except Exception as e:
    print(f"Error while running Charlene’s code: {e}")
    sys.exit(1)

# --- Step 2: Read back Charlene's output ---
output = np.loadtxt("brain_average.csv", delimiter=',')

# --- Define expected result ---
# (You should adjust this based on what the sagittal average is supposed to do)
expected_output = np.zeros((20, 20))
expected_output[-1, :] = 1

# --- Compare and exit with success/failure ---
if np.allclose(output, expected_output):
    print("✅ Test passed: output matches expected.")
    sys.exit(0)
else:
    print("❌ Test failed: output does not match expected.")
    print("Output:\n", output)
    print("Expected:\n", expected_output)
    sys.exit(1)
