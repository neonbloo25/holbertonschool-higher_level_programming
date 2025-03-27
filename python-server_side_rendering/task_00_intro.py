#!/usr/bin/env python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(p, dict) for p in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, start=1):
        name = person.get("name") or "N/A"
        event_title = person.get("event_title") or "N/A"
        event_date = person.get("event_date") or "N/A"
        event_location = person.get("event_location") or "N/A"

        output_text = template
        output_text = output_text.replace("{name}", name)
        output_text = output_text.replace("{event_title}", event_title)
        output_text = output_text.replace("{event_date}", event_date)
        output_text = output_text.replace("{event_location}", event_location)

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(output_text)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
