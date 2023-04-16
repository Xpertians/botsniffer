import ast


def detect_repetitive_patterns(parsed_code):
    # Detects repetitive patterns in the parsed code.
    # This code is very very dummy, needs improvement
    pattern_counts = {}
    # Traverse the AST and count the number
    # of occurrences of each node type and text
    for node in ast.walk(parsed_code):
        if hasattr(node, "lineno") and hasattr(node, "col_offset"):
            # Ignore nodes without line and column information (e.g., module)
            node_key = (node.__class__.__name__, ast.dump(node))
            if node_key not in pattern_counts:
                pattern_counts[node_key] = 0
            pattern_counts[node_key] += 1
    # Find patterns that occur more than once
    repetitive_patterns = [
        pattern for pattern, count in pattern_counts.items()
        if count > 1
    ]

    # Calculate the total number of repetitive patterns
    total_patterns = len(repetitive_patterns)

    # Normalize the number of patterns by the number of nodes in the code
    if len(pattern_counts) == 0:
        return 0.0
    else:
        return total_patterns / len(pattern_counts)
