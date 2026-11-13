import tiktoken

def tokenize_text(text):
    """Tokenize text using the cl100k_base encoding."""

    encoding = tiktoken.get_encoding("cl100k_base")

    return encoding.encode(text)