import numpy as np
import tensorflow as tf


#img = cv2.imread("Dog.png")
#img = cv2.resize(img, (128,128))
#img = np.array(img, dtype="float32")
#img = np.reshape(img, (1,128,128,3))
num = np.array([1,1,1,1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,1,1,2])
num = num.astype(np.float32)
num = np.reshape(num, (1,21))

num1 = np.array([1,1,1,1,1,1,1,1,1,1,2,1,1,2,2,2,1,1,1,1,2])
num1 = num1.astype(np.float32)
num1 = np.reshape(num1, (1,21))

# Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test the model on random input data.
input_shape = input_details[0]['shape']

print("*"*50, input_details)
interpreter.set_tensor(input_details[0]['index'], num)

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)


#output_details = tf.constant([2,20,30,3,6])
#tf.math.argmax(output_details)# A[2] is maximum in tensor A
#print(output_details)
