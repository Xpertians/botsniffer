import ast


def calculate_code_complexity(parsed_code):
    # Calculte the McCabe complexity metric from the parsed code.
    # This code is a hack, needs a lot of improvement, like for exmple
    # the nested dupliczated function
    num_edges = 0
    num_nodes = 0
    for node in ast.walk(parsed_code):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            num_edges += calculate_nested_complexity(node)
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
    if num_nodes == 0:
        # McCabe complexity metric returns 1.0 as default
        return 1.0
    else:
        return num_edges - num_nodes + 2


def calculate_nested_complexity(node, depth=0, max_depth=10):
    num_edges = 0
    if depth == max_depth:
        return num_edges

    for subnode in ast.iter_child_nodes(node):
        if isinstance(subnode, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Increase the depth only for nested functions
            num_edges += calculate_nested_complexity(
                                subnode, depth=depth, max_depth=max_depth)
        elif isinstance(subnode, ast.If):
            num_edges += 2
            num_edges += calculate_nested_complexity(
                                subnode, depth=depth+1, max_depth=max_depth)
        elif isinstance(subnode, ast.While):
            num_edges += 2
            num_edges += calculate_nested_complexity(
                                subnode, depth=depth+1, max_depth=max_depth)
        elif isinstance(subnode, ast.For):
            num_edges += 2
            num_edges += calculate_nested_complexity(
                                subnode, depth=depth+1, max_depth=max_depth)
        elif isinstance(subnode, ast.With):
            num_edges += 2
            num_edges += calculate_nested_complexity(
                                subnode, depth=depth+1, max_depth=max_depth)
        elif isinstance(subnode, ast.Try):
            num_edges += 3
            num_edges += calculate_nested_complexity(
                                subnode, depth=depth+1, max_depth=max_depth)
        elif isinstance(subnode, ast.ExceptHandler):
            num_edges += 1
        elif isinstance(subnode, ast.AugAssign):
            num_edges += 1
        elif isinstance(subnode, ast.BoolOp):
            num_edges += len(subnode.values) - 1
        elif isinstance(subnode, ast.BinOp):
            num_edges += 1
        elif isinstance(subnode, ast.Compare):
            num_edges += len(subnode.ops)
        elif isinstance(subnode, ast.Call):
            num_edges += 1
        elif isinstance(subnode, ast.Return):
            num_edges += 1

    return num_edges
