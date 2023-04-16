import ast

def detect_repetitive_patternsx(parsed_code):
    # Detects repetitive patterns in the parsed code.
    # This code is very very dummy, needs improvement
    pattern_count = 0

    # Traverse the AST and look for repetitive patterns
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.For):
            # Check if the loop variable is used in the body of the loop
            if any(isinstance(n, ast.Name) and n.id == node.target.id for n in node.body):
                pattern_count += 1
        elif isinstance(node, ast.While):
            # Check if the condition variable is used in the body of the loop
            if any(isinstance(n, ast.Name) and n.id == node.test.id for n in node.body):
                pattern_count += 1

    return pattern_count

def detect_repetitive_patterns(parsed_code):
    pattern_counts = {}

    # Traverse the AST and count the number of occurrences of each node type and text
    for node in ast.walk(parsed_code):
        if hasattr(node, "lineno") and hasattr(node, "col_offset"):
            # Ignore nodes without line and column information (e.g., module)
            node_key = (node.__class__.__name__, node.lineno, node.col_offset, ast.dump(node))
            if node_key not in pattern_counts:
                pattern_counts[node_key] = 0
            pattern_counts[node_key] += 1

    # Calculate the total number of repetitive patterns
    total_patterns = sum([count for count in pattern_counts.values() if count > 1])

    # Normalize the number of patterns by the number of nodes in the code
    if len(pattern_counts) == 0:
        return 0.0
    else:
        return total_patterns / len(pattern_counts)