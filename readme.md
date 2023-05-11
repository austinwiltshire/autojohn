Based on [this](https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5) tutorial

May also want to check out [how to query an index using llama-index 0.5.7](https://gpt-index.readthedocs.io/en/v0.5.27/reference/indices/vector_store_query.html)

You can get an api token and watch your account [here](https://platform.openai.com/account)

Usage from the command line:

Set up an index.

```python create_obsidian_index.py "path/to/your/obsidian/archive/root" ```

To query that index:

```python solicit.py "Question for yourself?" ```

Only supports one index right now, saved as obsidian_index.json in the project directory
