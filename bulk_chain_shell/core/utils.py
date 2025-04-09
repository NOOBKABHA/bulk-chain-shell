def handle_table_name(name):
    return name. \
        replace('-', '_'). \
        replace('.', "_")


def parse_filepath(filepath, default_filepath=None, default_ext=None):
    """ This is an auxiliary function for handling sources and targets from cmd string.
    """
    if filepath is None:
        return default_filepath, default_ext, None
    info = filepath.split(":")
    filepath = info[0]
    meta = info[1] if len(info) > 1 else None
    ext = filepath.split('.')[-1] if default_ext is None else default_ext
    return filepath, ext, meta

