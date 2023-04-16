import ast

def calculate_style_guide_adherence(parsed_code):
    """
    Calculates the adherence to a style guide of the parsed code.

    Args:
        parsed_code: The parsed code as an AST object.

    Returns:
        A float value between 0 and 1 representing the adherence to a style guide
        of the parsed code. A value of 1 indicates perfect adherence to the style guide,
        while a value of 0 indicates no adherence to the style guide.
    """
    # Define the style guide as a dictionary of allowed AST nodes and their attributes
    style_guide = {
        ast.FunctionDef: {"args": {"vararg": None, "kwonlyargs": [], "kw_defaults": [], "kwarg": None}},
        ast.ClassDef: {"bases": [], "keywords": []},
        ast.Call: {"func": {"id": "print", "attr": None}},
        ast.Compare: {"ops": [ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.Is, ast.IsNot, ast.In, ast.NotIn]},
        ast.Attribute: {"attr": None},
    }

    # Count the number of style guide violations in the parsed code
    style_violations = 0
    for node in ast.walk(parsed_code):
        if isinstance(node, tuple(style_guide.keys())):
            for attribute, allowed_values in style_guide[type(node)].items():
                if hasattr(node, attribute):
                    value = getattr(node, attribute)
                    if isinstance(value, (list, tuple)):
                        for v in value:
                            if v not in allowed_values:
                                style_violations += 1
                    elif value not in allowed_values:
                        style_violations += 1

    # Calculate the style guide adherence as a fraction of the total number of nodes
    total_nodes = sum(1 for node in ast.walk(parsed_code))
    adherence = 1 - style_violations / total_nodes

    return adherence