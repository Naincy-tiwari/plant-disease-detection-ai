import tensorflow as tf

def inspect_indices(model_path):
    print(f"--- Indices for {model_path} ---")
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    for i, detail in enumerate(input_details):
        print(f"Details[{i}]: Index={detail['index']}, Name={detail['name']}, Shape={detail['shape']}")

inspect_indices("Plant_Disease_Predictor_with_Weather.tflite")
