import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    if node == []:
        return 0

    childrenAttribs = 0
    for child in list(node):
        childrenAttribs += get_attr_number(child)

    return len(node.attrib) + childrenAttribs


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
