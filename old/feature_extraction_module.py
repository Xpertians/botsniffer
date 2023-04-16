import ast


def extract_features(parsed_code):
    features = {}

    # Extract indentation style and structure features
    features["indentation_consistency"] = calculate_indentation_consistency(parsed_code)
    features["style_guide_adherence"] = calculate_style_guide_adherence(parsed_code)

    # Extract code complexity features
    features["code_complexity"] = calculate_code_complexity(parsed_code)

    # Extract comment features
    features["comment_quality"] = analyze_comment_quality(parsed_code)

    # Extract repetitive pattern features
    features["repetitive_patterns"] = detect_repetitive_patterns(parsed_code)

    # Convert features dictionary to a format suitable for your ML model
    feature_vector = convert_to_feature_vector(features)

    return feature_vector

def calculate_indentation_consistency(parsed_code):
    indentation_levels = []

    # Traverse the AST and collect the indentation levels of all nodes
    for node in ast.walk(parsed_code):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            # Exclude function and class definitions from the indentation consistency calculation
            continue
        if hasattr(node, "col_offset"):
            # col_offset is the character offset of the node within its enclosing scope
            indentation_level = node.col_offset // 4
            indentation_levels.append(indentation_level)

    # Calculate the standard deviation of the indentation levels
    if len(indentation_levels) <= 1:
        # If there is only one or zero indentation levels, return perfect consistency
        return 1.0
    else:
        return 1.0 - (np.std(indentation_levels) / (len(indentation_levels) - 1))

def calculate_style_guide_adherence(parsed_code):
    # Load the PEP 8 style guide
    with open("pep8-style.txt", "r") as f:
        pep8_lines = f.readlines()

    # Normalize the PEP 8 lines by stripping whitespace and converting to lowercase
    pep8_lines = [line.strip().lower() for line in pep8_lines]

    # Traverse the AST and collect the names and attributes of all nodes
    node_names = set()
    node_attributes = set()
    for node in ast.walk(parsed_code):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            # Exclude function and class definitions from the style guide adherence check
            continue
        node_name = node.__class__.__name__
        node_names.add(node_name)
        node_attributes.update(dir(node))

    # Calculate the percentage of node names and attributes that appear in the PEP 8 style guide
    pep8_node_names = [line.split()[0] for line in pep8_lines]
    pep8_node_attributes = [line.split()[-1] for line in pep8_lines]
    name_adherence = len(node_names.intersection(pep8_node_names)) / len(pep8_node_names)
    attribute_adherence = len(node_attributes.intersection(pep8_node_attributes)) / len(pep8_node_attributes)

    # Return the average of the name and attribute adherence scores
    return (name_adherence + attribute_adherence) / 2.0

def calculate_code_complexity(parsed_code):
    num_edges = 0
    num_nodes = 0

    print('calculate_code_complexity')
    # Traverse the AST and count the number of edges and nodes in the control flow graph
    for node in ast.walk(parsed_code):
        print("NODE!")
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

def analyze_comment_quality(parsed_code):
    total_lines = 0
    comment_lines = 0

    # Traverse the AST and count the number of comment and total lines
    for node in ast.walk(parsed_code):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            # Exclude function and class definitions from the comment quality analysis
            continue
        source_lines, comment_lines = count_lines(node)
        total_lines += source_lines
        comment_lines += comment_lines

    # Calculate the ratio of comment lines to total lines
    if total_lines == 0:
        return 1.0
    else:
        return comment_lines / total_lines

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

def convert_to_feature_vector(features):
    feature_vector = []

    # Add feature values to the feature_vector list
    for key, value in features.items():
        feature_vector.append(value)

    # Convert the feature_vector list to a NumPy array, if required by your ML model
    feature_vector = np.array(feature_vector).reshape(1, -1)

    return feature_vector
