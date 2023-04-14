import ast

def calculate_code_complexity(parsed_code):
    # Traverse the AST and count the number of edges and nodes in the control flow graph
    # This needs to be moved to a better implementation
    # consider this as a ugly hack, aklos I'm out of beer
    # Initialize the complexity count
    complexity_count = 1

    # Traverse the AST and count the number of control flow statements
    for node in ast.walk(parsed_code):
        if isinstance(node, (ast.If, ast.While, ast.For, ast.With, ast.Try)):
            complexity_count += 1
        elif isinstance(node, ast.FunctionDef):
            complexity_count += calculate_code_complexity(node)

    return complexity_count
