import ast

def calculate_code_complexitys(parsed_code):
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

def calculate_code_complexity(parsed_code):
    num_edges = 0
    num_nodes = 0

    # Traverse the AST and count the number of edges and nodes in the control flow graph
    for node in ast.walk(parsed_code):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Calculate complexity for functions and async functions separately
            num_edges += calculate_function_complexity(node)
        elif isinstance(node, ast.If):
            num_edges += 2
            num_nodes += 1
        elif isinstance(node, ast.While):
            num_edges += 2
            num_nodes += 1
        elif isinstance(node, ast.For):
            num_edges += 2
            num_nodes += 1
        elif isinstance(node, ast.With):
            num_edges += 2
            num_nodes += 1
        elif isinstance(node, ast.Try):
            num_edges += 3
            num_nodes += 1
        elif isinstance(node, ast.ExceptHandler):
            num_edges += 1
        elif isinstance(node, ast.AugAssign):
            num_edges += 1
        elif isinstance(node, ast.BoolOp):
            num_edges += len(node.values) - 1
        elif isinstance(node, ast.BinOp):
            num_edges += 1
        elif isinstance(node, ast.Compare):
            num_edges += len(node.ops)
        elif isinstance(node, ast.Call):
            num_edges += 1
        elif isinstance(node, ast.Return):
            num_edges += 1

    # Calculate the McCabe complexity metric
    if num_nodes == 0:
        return 1.0
    else:
        return num_edges - num_nodes + 2