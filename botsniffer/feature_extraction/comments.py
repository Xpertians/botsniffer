import ast
import tokenize
from io import BytesIO


def analyze_comment_quality(file_path, parsed_code):
    # This code tokenize the content of the file
    # looking for comments. I planned to use AST
    # but after python 3.8 comments output it's
    # not supported also, I'm tired and out of
    # coffee, so implementation is dummy it works
    total_lines = 0
    total_comments = 0
    high_quality_comments = 0
    fObj = open(file_path, 'r')
    for toktype, tok, start, end, line in (
        tokenize.generate_tokens(fObj.readline)
    ):
        total_lines += 1
        if toktype == tokenize.COMMENT:
            total_comments += 1
            if is_high_quality_comment(tok):
                high_quality_comments += 1
    if high_quality_comments > 0:
        quality = (high_quality_comments / total_comments) + 1
    elif total_comments > 0:
        quality = total_comments / total_lines
    else:
        quality = 0.0
    return quality


def is_high_quality_comment(comment):
    # Set of words and phrases that indicate a high-quality comment
    high_quality_words = {"TODO", "FIXME", "NOTE", "HACK", "FIX", "DEFINE"}
    # Check if the comment contains any high-quality words or phrases
    for word in high_quality_words:
        if word in comment.upper():
            return True
    return False
