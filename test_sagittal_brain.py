import numpy as np

# Create input
data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

# Create expected output
# (for example: if sagittal_average mirrors left and right halves)
expected_output = np.zeros((20, 20))
expected_output[-1, :] = 1  # same as input, since it's symmetric
np.savetxt("brain_expected.csv", expected_output, fmt='%d', delimiter=',')
