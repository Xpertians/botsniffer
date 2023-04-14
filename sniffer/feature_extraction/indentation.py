import ast

def calculate_indentation_consistency(file_path, parsed_code):
    # Calculates the indentation consistency of the parsed code.
    indent_levels = []

    # Traverse the AST and collect the indentation levels of each line
    for node in ast.walk(parsed_code):
        if hasattr(node, "col_offset"):
            indent_levels.append(node.col_offset)

    # Calculate the standard deviation of the indentation levels
    if len(indent_levels) > 1:
        std_dev = sum((x - sum(indent_levels) / len(indent_levels)) ** 2 for x in indent_levels) / len(indent_levels)
        indent_consistency = 1 - std_dev / max(indent_levels)
    else:
        indent_consistency = 1.0

    return indent_consistency
