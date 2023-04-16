import ast

def analyze_comment_quality(parsed_code):
    """
    Analyzes the quality of comments in the parsed code.

    Args:
        parsed_code: The parsed code as an AST object.

    Returns:
        A float value between 0 and 1 representing the quality of comments in the parsed code.
        A value of 1 indicates high-quality comments, while a value of 0 indicates low-quality comments.
    """
    total_comments = 0
    high_quality_comments = 0

    # Traverse the AST and count the number of comments
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
            total_comments += 1
            if is_high_quality_comment(node.value.s):
                high_quality_comments += 1

    # Calculate the quality of comments as a fraction of the total number of comments
    if total_comments > 0:
        quality = high_quality_comments / total_comments
    else:
        quality = 0.0

    return quality

def is_high_quality_comment(comment):
    """
    Determines whether a comment is a high-quality comment.

    Args:
        comment: A string containing the text of the comment.

    Returns:
        True if the comment is a high-quality comment, False otherwise.
    """
    # Define a set of words and phrases that indicate a high-quality comment
    high_quality_words = {"TODO", "FIXME", "NOTE", "HACK", "XXX"}

    # Check if the comment contains any high-quality words or phrases
    for word in high_quality_words:
        if word in comment.upper():
            return True

    return False
