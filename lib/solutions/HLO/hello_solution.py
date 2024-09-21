# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    """
    Return a greeting message using the provided friend's name.

    Args:
        friend_name (str): The name of the friend.

    Returns:
        str: A greeting message for the friend.
    """
    return f'Hello, {friend_name}!'
