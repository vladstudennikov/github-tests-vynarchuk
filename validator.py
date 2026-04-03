def validate_title(title: str):
    if title is None or title.strip() == "":
        raise ValueError("Title cannot be empty")

    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long")