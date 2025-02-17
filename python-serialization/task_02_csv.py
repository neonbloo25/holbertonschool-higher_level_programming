#!/usr/bin/env python3
"""let's get serial, ft csf & json"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Target Func w/ Try/Except"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            data_list = list(csv_reader)

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (OSError, IOError) as e:
        print(f"Error reading file '{csv_filename}': {e}")
        return False
