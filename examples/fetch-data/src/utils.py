# Mixing prolific id for privacy
import random
import string

# Logging
import csv
import os
import pytz
from datetime import datetime
from typing import Dict


def append_to_csv(data_dict: Dict) -> None:
    """Append single subject's initial screener data to csv."""

    def get_timestamp() -> str:
        """Get the current time in Pacific Time and format it."""
        pacific = pytz.timezone("America/Los_Angeles")

        utc_now = datetime.now(pytz.utc)
        pst_now = utc_now.astimezone(pacific)

        date_format = "%I:%M:%S%p %m-%d-%Y"

        formatted_time = pst_now.strftime(date_format)[:-3].replace(" ", "_")
        return formatted_time

    fieldnames = [
        "prolific_id",
        "privacy_notice",
        "timing_of_study",
        "structure_of_study",
        "include_subject",
        "date",
    ]

    timestamp = get_timestamp()

    filename = f"./out/initial_screener_data_{timestamp}.csv"

    # Check if the file exists
    file_exists = os.path.exists(filename)

    # Open the file in append mode; write header if file does not exist
    with open(filename, mode="a+", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data_dict)


def mix_id(prolific_id: str) -> str:
    # Append 5 random alphanumeric characters (letters and digits)
    random_chars = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    new_string = prolific_id + random_chars

    # Convert the string to a list and shuffle it
    shuffled_list = list(new_string)
    random.shuffle(shuffled_list)

    # Convert the list back to a string
    shuffled_string = "".join(shuffled_list)
    return shuffled_string
