import ast
from collections import defaultdict


def detect_repetitive_patterns(parsed_code):
    pattern_counts = defaultdict(int)
    # Traverse the AST and count the number of occurrences of each pattern
    for node in ast.walk(parsed_code):
        if hasattr(node, "lineno") and hasattr(node, "col_offset"):
            # Ignore nodes without line and column information (e.g., module)
            node_pattern = get_node_pattern(node)
            pattern_counts[node_pattern] += 1
    repetitive_patterns = [pattern for pattern, count in pattern_counts.items() if count > 1]
    total_patterns = len(repetitive_patterns)
    num_nodes = sum(1 for _ in ast.walk(parsed_code))
    if num_nodes == 0:
        return 0.0
    else:
        return total_patterns / num_nodes


def get_node_pattern(node):
    if isinstance(node, ast.Call):
        # For function calls, include the function name and argument types
        arg_types = [get_node_pattern(arg) for arg in node.args]
        return f"Call:{get_node_pattern(node.func)}.{','.join(arg_types)}"
    elif isinstance(node, ast.Assign):
        # For assignments, include the target names and value type
        target_names = [get_node_pattern(target) for target in node.targets]
        value_type = get_node_pattern(node.value)
        return f"Assign:{','.join(target_names)}={value_type}"
    elif isinstance(node, ast.Name):
        # For variable names, return the name
        return node.id
    elif isinstance(node, ast.Attribute):
        # For attributes, recursively get the pattern of the value and concatenate the attribute name
        return f"{get_node_pattern(node.value)}.{node.attr}"
    else:
        # For other node types, return the class name
        return node.__class__.__name__

