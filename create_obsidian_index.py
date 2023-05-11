""" Functions used to index and store documents and other context for later querying using ChatGPT """
from llama_index import download_loader, GPTSimpleVectorIndex


def create_obsidian_index(location: str, index_name: str) -> None:
    """
    Create an GPTSimpleVectorIndex from an Obsidian Database

    :param location: The location of the root of the Obsidian archive
    :param index_name: The name of the index file to generate
    """

    obsidian_reader = download_loader("ObsidianReader")

    # obsidian_reader is a class-like function, and it takes arguments built dynamically from the download_loader
    # method above.
    # noinspection PyArgumentList
    documents = obsidian_reader(location).load_data()

    index = GPTSimpleVectorIndex(documents)

    index.save_to_disk(index_name)


if __name__ == "__main__":
    print("This will take some time")
    create_obsidian_index("/home/john/Base", "obsidian_index.json")
