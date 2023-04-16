import ast
import your_feature_extraction_module
import your_ml_model_module

def detect_ai_generated_code(source_code_file):
    # Parse the source code
    with open(source_code_file, "r") as f:
        code = f.read()
    parsed_code = ast.parse(code)

    # Extract features
    features = your_feature_extraction_module.extract_features(parsed_code)

    # Load the trained machine learning model
    model = your_ml_model_module.load_model()

    # Make a prediction
    prediction = model.predict(features)

    if prediction == 1:
        print("AI-generated code")
    else:
        print("Human-written code")

if __name__ == "__main__":
    source_code_file = "path/to/source/code/file"
    detect_ai_generated_code(source_code_file)
