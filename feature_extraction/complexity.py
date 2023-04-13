import ast

def calculate_code_complexity(parsed_code):
    """
    Calculates the cyclomatic complexity of the parsed code.

    Args:
        parsed_code: The parsed code as an AST object.

    Returns:
        An integer value representing the cyclomatic complexity of the parsed code.
    """
    # Initialize the complexity count
    complexity_count = 1

    # Traverse the AST and count the number of control flow statements
    for node in ast.walk(parsed_code):
        if isinstance(node, (ast.If, ast.While, ast.For, ast.With, ast.Try)):
            complexity_count += 1
        elif isinstance(node, ast.FunctionDef):
            complexity_count += calculate_code_complexity(node)

    return complexity_count
