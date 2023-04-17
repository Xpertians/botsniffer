import ast
import math
import numpy as np


def calculate_indentation_consistency(parsed_code, indentation_size=4):
    # Calculates the indentation consistency of the parsed code.
    indentation_levels = []
    # Traverse the AST and collect the indentation levels of all nodes
    for node in ast.walk(parsed_code):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            # Exclude function and class definitions
            # from the indentation consistency calculation
            continue
        if not isinstance(node, ast.AST):
            # Exclude non-AST nodes (such as comments)
            continue
        if not hasattr(node, "lineno"):
            # Exclude nodes without a line number (such as the root Module node)
            continue
        indentation_level = node.col_offset // indentation_size
        indentation_levels.append(indentation_level)
    # Calculate the median absolute deviation (MAD) of the indentation levels
    if len(indentation_levels) <= 1:
        # If there is only one or zero indentation levels,
        # return perfect consistency
        return 1.0
    else:
        mad = np.median(np.abs(indentation_levels - np.median(indentation_levels)))
        return 1.0 - (mad / (np.median(indentation_levels) * 2))
