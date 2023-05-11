""" Solicit John's Brain with a Question """

import os
from llama_index import download_loader, GPTSimpleVectorIndex

# noinspection SpellCheckingInspection
os.environ["OPENAI_API_KEY"] = "YOUR KEY"


def main():
    """Asks a question to John's Brain"""

    obsidian_reader = download_loader("ObsidianReader")

    # obsidian_reader is a class-like function, and it takes arguments built dynamically from the download_loader
    # method above.

    # noinspection PyArgumentList
    documents = obsidian_reader("/home/john/Dropbox/Notes/Base").load_data()

    # Construct a simple vector index
    index = GPTSimpleVectorIndex(documents)

    # You can reload this after creating it and save a lot of time + money
    index.save_to_disk("obsidian_index.json")

    # Querying the index
    response = index.query("How should I help Dan?")
    print(response)
