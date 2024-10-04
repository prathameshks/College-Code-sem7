# %% 
import numpy as np

# %% Initialize weights with numpy array
def initialize_weights(input_size):
    return np.zeros(input_size)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def update_weights_and_bias(weights, bias, inputs, target, learning_rate):
    prediction = np.dot(inputs, weights) + bias
    error = target - prediction
    weights += learning_rate * error * inputs
    bias += learning_rate * error
    return weights, bias

def predict(weights, bias, inputs):
    activation = np.dot(inputs, weights) + bias
    return sigmoid(activation)

# %% Initialize weights and biases
weight_and = initialize_weights(2)
weight_or = initialize_weights(2)
weight_xor = initialize_weights(2)
bias_and = 0
bias_or = 0
bias_xor = 0

# Define the input and output for the AND, OR, and XOR gates
inputs = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
outputs_and = np.array([0, 0, 0, 1])  # Changed from -1 and 1 to 0 and 1 for sigmoid output
outputs_or = np.array([0, 1, 1, 1])
outputs_xor = np.array([0, 1, 1, 0])

# Train the network 
epochs = 10000  # Increased epochs for better training convergence
learning_rate = 0.1

for _ in range(epochs):
    for x, y in zip(inputs, outputs_and):
        weight_and, bias_and = update_weights_and_bias(weight_and, bias_and, x, y, learning_rate)

for _ in range(epochs):
    for x, y in zip(inputs, outputs_or):
        weight_or, bias_or = update_weights_and_bias(weight_or, bias_or, x, y, learning_rate)

for _ in range(epochs):
    for x, y in zip(inputs, outputs_xor):
        weight_xor, bias_xor = update_weights_and_bias(weight_xor, bias_xor, x, y, learning_rate)
        
# Predict the values on test dataset using predict()
tests = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])

# Test the network
for x in tests:
    and_pred = predict(weight_and, bias_and, x)
    or_pred = predict(weight_or, bias_or, x)
    xor_pred = predict(weight_xor, bias_xor, x)
    
    # Binarize output for display purposes
    and_output = 1 if and_pred >= 0.5 else -1
    or_output = 1 if or_pred >= 0.5 else -1
    xor_output = 1 if xor_pred >= 0.5 else -1
    
    print(f"Inputs: {x}, AND: {and_output}, OR: {or_output}, XOR: {xor_output}")
