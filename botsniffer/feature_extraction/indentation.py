import ast
import math


def calculate_indentation_consistency(parsed_code):
    # Calculates the indentation consistency of the parsed code.
    indentation_levels = []
    # Traverse the AST and collect the indentation levels of all nodes
    for node in ast.walk(parsed_code):
        if isinstance(node, (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef
        )):
            # Exclude function and class definitions
            # from the indentation consistency calculation
            continue
        if hasattr(node, "col_offset"):
            # col_offset is the character offset
            # of the node within its enclosing scope
            indentation_level = node.col_offset // 4
            indentation_levels.append(indentation_level)
    # Calculate the standard deviation of the indentation levels
    if len(indentation_levels) <= 1:
        # If there is only one or zero indentation levels,
        # return perfect consistency
        return 1.0
    else:
        return 1.0 - (
            calculate_std_dev(indentation_levels) /
            (len(indentation_levels) - 1)
        )


def calculate_std_dev(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)
    return std_dev
