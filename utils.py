from mi import Note


def get_mention(note: Note) -> str:
    """
    Create a mention for the author of the note

    Parameters
    ----------
    note : Note

    Returns
    -------
    str
        mention

    Raises
    ------
    TypeError
        note is not a Note class
    """

    if not isinstance(note, Note):
        raise TypeError("note must be a Note")
    if note.author.host is None:
        return f'@{note.author.username}'
    return f'@{note.author.username}@{note.author.host}'
