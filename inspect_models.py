import tensorflow as tf
import numpy as np

def inspect_model(model_path):
    print(f"--- Inspecting {model_path} ---")
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    for detail in input_details:
        print(f"Input: {detail['name']}")
        print(f"  Shape: {detail['shape']}")
        print(f"  Type: {detail['dtype']}")
        print(f"  Quantization: {detail['quantization']}")
    
    for detail in output_details:
        print(f"Output: {detail['name']}")
        print(f"  Shape: {detail['shape']}")
        print(f"  Type: {detail['dtype']}")
        print(f"  Quantization: {detail['quantization']}")

inspect_model("Plant_Classification_Model.tflite")
inspect_model("Plant_Disease_Predictor_with_Weather.tflite")
