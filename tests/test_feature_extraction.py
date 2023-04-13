import ast
import numpy as np
import pytest
from ai_detector.feature_extraction.indentation import calculate_indentation_consistency
from ai_detector.feature_extraction.style_guide import calculate_style_guide_adherence
from ai_detector.feature_extraction.complexity import calculate_code_complexity
from ai_detector.feature_extraction.comments import analyze_comment_quality
from ai_detector.feature_extraction.patterns import detect_repetitive_patterns

@pytest.fixture(scope="module")
def parsed_code():
    code = '''
    def foo():
        for i in range(10):
            print(i)
    '''
    parsed = ast.parse(code)
    return parsed

def test_calculate_indentation_consistency(parsed_code):
    assert calculate_indentation_consistency(parsed_code) == 1.0

def test_calculate_style_guide_adherence(parsed_code):
    assert calculate_style_guide_adherence(parsed_code) == 0.5

def test_calculate_code_complexity(parsed_code):
    assert calculate_code_complexity(parsed_code) == 5.0

def test_analyze_comment_quality(parsed_code):
    assert analyze_comment_quality(parsed_code) == 0.0

def test_detect_repetitive_patterns(parsed_code):
    assert detect_repetitive_patterns(parsed_code) == 0.0
