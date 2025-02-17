#!/usr/bin/env python3
"""let's get serial ft.xml"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Func Serialize"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Func deSerialize w/ Try/Except"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result_dict = {child.tag: child.text for child in root}
        return result_dict

    except (OSError, IOError, ET.ParseError) as e:
        print(f"Error loading file '{filename}': {e}")
        return None
