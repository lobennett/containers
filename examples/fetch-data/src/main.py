# Clean data
import ast
import os
import json
import datetime

# Math stuff
import pandas as pd
from dotenv import load_dotenv

# Local imports
from utils import mix_id, append_to_csv
from fetch import fetch_data

# Typing
import typing
from typing import Dict, Tuple


def get_current_date(data: Dict) -> str:
    if "dateTime" not in data.keys():
        print("dateTime does not exist in date.keys()")
        return "N/A"
    timestamp_ms = data["dateTime"]
    timestamp_s = timestamp_ms / 1000
    # Convert to datetime
    date_time = datetime.datetime.fromtimestamp(timestamp_s)

    # Format as mm/dd/yy
    formatted_date = date_time.strftime("%m/%d/%y")
    return formatted_date


def res_to_df_w_date(fetched_data: str) -> Tuple[pd.DataFrame, str]:
    data = ast.literal_eval(fetched_data)
    date = get_current_date(data)
    trialdata = json.loads(data["trialdata"])

    df = pd.DataFrame(trialdata)
    return df, date


def preprocess_data(data: Dict):
    """Preprocessing fetched data to neat format"""
    results = data["results"]
    for res in results:
        prolific_id = res["prolific_id"]

        if prolific_id is None:
            continue

        prolific_id = mix_id(prolific_id)

        df, date = res_to_df_w_date(res["data"])

        try:
            privacy_notice = df["privacy_notice"].dropna().iloc[0]
            timing_of_study = df["timing_of_study"].dropna().iloc[0]
            structure_of_study = df["structure_of_study"].dropna().iloc[0]
            include_subject = df["include_subject"].dropna().iloc[0]

            res_dict = {
                "prolific_id": prolific_id,
                "privacy_notice": privacy_notice,
                "timing_of_study": timing_of_study,
                "structure_of_study": structure_of_study,
                "include_subject": include_subject,
                "date": date,
            }

            if prolific_id:
                append_to_csv(res_dict)

        except KeyError as key:
            print(f"Missing key {key} for result object: {res}\n")


def main():
    if not os.path.exists("./out"):
        os.mkdir("./out")

    load_dotenv()

    for data in fetch_data():
        preprocess_data(data)


if __name__ == "__main__":
    main()
