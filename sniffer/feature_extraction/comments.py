import tokenize
from io import BytesIO

def analyze_comment_quality(file_path, parsed_code):
    total_comments = 0
    high_quality_comments = 0
    fObj = open(file_path, 'r')
    for toktype, tok, start, end, line in tokenize.generate_tokens(fObj.readline):
        if toktype == tokenize.COMMENT:
            total_comments += 1
            if is_high_quality_comment(tok):
                high_quality_comments += 1
    if total_comments > 0:
        quality = high_quality_comments / total_comments
    else:
        quality = 0.0
    return quality

def is_high_quality_comment(comment):
    # DEFINE a set of words and phrases that indicate a high-quality comment
    high_quality_words = {"TODO", "FIXME", "NOTE", "HACK", "XXX", "DEFINE"}

    # Check if the comment contains any high-quality words or phrases
    for word in high_quality_words:
        if word in comment.upper():
            return True

    return False
