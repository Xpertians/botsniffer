import ast
import radon.complexity as radon_cc


def calculate_code_complexity(parsed_code):
    # Calculate the cyclomatic complexity of the given source code
    cc = radon_cc.cc_visit_ast(parsed_code)
    total_complexity = sum(func.complexity for func in cc)
    return total_complexity