import ast
from .comments import analyze_comment_quality
from .complexity import calculate_code_complexity
from .indentation import calculate_indentation_consistency, calculate_style_guide_adherence
from .patterns import detect_repetitive_patterns

def extract_features(parsed_code):
    """
    Extracts a dictionary of features from the parsed code.

    Args:
        parsed_code: The parsed code as an AST object.

    Returns:
        A dictionary containing the extracted features.
    """
    features = {}

    # Extract indentation style and structure features
    features["indentation_consistency"] = calculate_indentation_consistency(parsed_code)
    features["style_guide_adherence"] = calculate_style_guide_adherence(parsed_code)

    # Extract code complexity features
    features["code_complexity"] = calculate_code_complexity(parsed_code)

    # Extract comment features
    features["comment_quality"] = analyze_comment_quality(parsed_code)

    # Extract repetitive pattern features
    features["repetitive_patterns"] = detect_repetitive_patterns(parsed_code)

    return features
