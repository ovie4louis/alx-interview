#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def look_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    allboxes = {}
    while True:
        if len(allboxes) == 0:
            allboxes[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_next_opened_box(allboxes)
        if keys:
            for key in keys:
                try:
                    if allboxes.get(key) and allboxes.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    allboxes[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in allboxes.values()]:
            continue
        elif len(allboxes) == len(boxes):
            break
        else:
            return False

    return len(allboxes) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
