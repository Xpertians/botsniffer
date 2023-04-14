import ast

def detect_repetitive_patterns(file_path, parsed_code):
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
