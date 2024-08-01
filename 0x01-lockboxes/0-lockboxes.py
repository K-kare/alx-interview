#!/usr/bin/python3
"""locked boxes"""
def canUnlockAll(boxes):
    """
    take boxes
        create set of keys
     """
    total_boxes = len(boxes)
    sets = [0]
    counter = 0
    index = 0

    while index < len(sets):
        setkey = sets[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in sets:
                sets.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
