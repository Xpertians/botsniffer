import ast
from .comments import analyze_comment_quality
from .indentation import calculate_indentation_consistency
from .style_guide import calculate_style_guide_adherence
from .patterns import detect_repetitive_patterns
from .complexity import calculate_code_complexity

def extract_features(file_path, parsed_code):
    # Dict with features
    features = {}

    # Extract comment features
    features["comment_quality"] = analyze_comment_quality(file_path, parsed_code)
    features["code_identation"] = calculate_indentation_consistency(parsed_code)
    features["style_adherence"] = calculate_style_guide_adherence(parsed_code)
    features["repetitive_patterns"] = detect_repetitive_patterns(parsed_code)
    features["code_complexity"] = calculate_code_complexity(parsed_code)
    
    # print('file_path:', file_path)

    return features
