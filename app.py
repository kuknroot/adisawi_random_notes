# %%
# import
import json
import requests
import numpy as np
import pandas as pd
import streamlit as st
import time

# %%
# function
def make_adisawi_great_again(user_id: str, offset: int, limit: int = 100) -> requests.Response:
    """
    id
    """

    requests_url: str = f"https://misskey.io/api/users/notes"
    payload = json.dumps({"userId": f"{user_id}", "offset": offset, "limit": limit})

    proxies = {
        "http": None,
        "https": None,
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(
        requests_url,
        proxies=proxies,
        headers=headers,
        data=payload,
    )

    return response

def generate_random_number() -> int:
    random_number: int = np.random.randint(0, 500)
    return random_number

# %%
# var
user_id: str = "9db9irafsf"

# %%
# get kemono no notes, kemonotes
kemono_notes_json_list = []
n: int
for n in range(5):
    tmp_notes_json: dict = make_adisawi_great_again(user_id, offset=n*100).json()
    kemono_notes_json_list += tmp_notes_json

# %%
# kurorekishi wo sentaku
random_number: int = generate_random_number()
selected_kemonotes: dict = kemono_notes_json_list[random_number]
notes_url = f"""https://misskey.io/notes/{selected_kemonotes["id"]}"""
cw = selected_kemonotes["cw"]
text = selected_kemonotes["text"]

# %%
# streamlit bu
st.title("Adisawi@misskey.io さんノートガチャ")
st.markdown(f"# notes_url")
st.markdown(f"**{notes_url}**")
st.markdown(f"# cw")
st.markdown(f"**{cw}**")
st.markdown(f"# text")
st.markdown(f"**{text}**")
