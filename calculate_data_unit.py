def calculate_bytes(num_of_bytes, suffix="B"):
    """a function just to calculate how many KB/MB/GB or TB of data we sent using number of bytes we provide it with

    Args:
        num_of_bytes (int): number of bytes
        suffix (str, optional): the suffix of the unit (eg. MB). Defaults to "B".

    Returns:
        [str]: the result from the calculations
    """
    
    for unit in ["", "K", "M", "G", "T"]:
        if abs(num_of_bytes) < 1024.0:
            return f"{num_of_bytes:3.1f} {unit}{suffix}"
        num_of_bytes /= 1024.0
    return f"{num_of_bytes:.1f}Yi{suffix}"