import ast
from .comments import analyze_comment_quality
from .indentation import calculate_indentation_consistency
#from .complexity import calculate_code_complexity
#from .indentation import , calculate_style_guide_adherence
#from .patterns import detect_repetitive_patterns

def extract_features(file_path, parsed_code):
    # Dict with features
    features = {}

    # Extract comment features
    features["comment_quality"] = analyze_comment_quality(file_path, parsed_code)
    features["code_identation"] = calculate_indentation_consistency(file_path, parsed_code)
    
    print(features)

    return features
