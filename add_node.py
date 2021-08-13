from __future__ import division, print_function
import json
from math import inf
import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip


def add_node(
    id: str, label: str, group: int, parent: str, name="prof/miserables.json", value=4
):
    """Creates new node and add it to the JSON file
        The JSON file is used for the skills D3 bubble chart

    Args:
        id (str): ID of the node usually the same as label unless we add new cluster set
        label (str): Text that would be written on the node
        group (int): cluster number
        parent (str): parent of the node (the way I designed it it's a number of id of the cluster (read the json the logic would look clear there))
        name (str, optional): JSON filename Defaults to "prof/miserables.json".
        value (int, optional): The length of the edge. Defaults to 4.
    """
    with open(name) as f:
        d = json.load(f)

    d["nodes"].append({"id": id, "group": group, "label": label})
    d["links"].append({"source": parent, "target": id, "value": value})

    with open(name, "w") as f:
        json.dump(d, f)


if __name__ == "__main__":
    # command line argument splitted by space
    # Example:
    # Jupyter Jupyter 1 1
    id, label, group, parent = input().split(" ")
    add_node(id, label, int(group), parent)
