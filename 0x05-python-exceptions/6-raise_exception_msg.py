#!/usr/bin/python3
def raise_exception_msg(message=""):
    """_summary_

    Args:
        message (str, optional): _description_. Defaults to "".

    Raises:
        NameError: _description_
    """
    print("{}".format(message), end="")
    raise NameError
