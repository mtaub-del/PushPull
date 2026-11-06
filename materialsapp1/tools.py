def convert_lod_to_dol (lod, dol):
    """
    Converts a List of Dicts (lod) to a Dict of Lists (dol):

    Args:
        lod (list): List of dictionaries
        dol (dict): Dictionary of lists

    Returns:
        dict: Dictionary of lists
    """
    dol = {}
    keys = lod[0].keys()
    for key in keys:
        dol[key] = []
    for row in lod:
        for key in keys:
            dol[key].append(row[key])
    return dol

def convert_dol_to_lod (dol, lod):
    """
    Converts a Dict of Lists (dol) to a List of Dicts (lod):

    Args:
        dol (dict): Dictionary of lists
        lod (list): List of dictionaries

    Returns:
        list: List of dictionaries
    """
    lod = []
    keys = list(dol.keys())
    num_rows = len(list(dol[keys[0]]))
    for i in range(num_rows):
        row = {}
        for key in keys: 
            row[key] = dol[key][i]
        lod.append(row)
    return lod

def create_markdown_table (data):
    """
    Creates a markdown table from a list of dictionaries.

    Args:
        data (list): List of dictionaries

    Returns:
        str: Markdown table as a string
    """
    if isinstance(data, dict):
        data = convert_dol_to_lod(data, [])
    if not data:
        return ""
    keys = list(data[0].keys())
    header = "| " + " | ".join(keys) + " |"
    seperator = "| " + " | ".join(["---"] * len(keys)) + " |"
    rows = []
    for row_dict in data:
        row = "| " + " | ".join(str(row_dict[key]) for key in keys) + " |"
        rows.append(row)

        markdown_table = "\n".join([header, seperator] + rows
                               )  
    return markdown_table    