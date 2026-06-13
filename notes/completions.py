# %%
import os

from rich import pretty, print

pretty.install()

import tiktoken
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_completion(prompt, model="gpt-3.5-turbo"):
    response = client.responses.create(model=model, input=prompt)
    return response.output_text


def get_completion_with_instructions(prompt, instructions, model="gpt-5.5"):
    response = client.responses.create(
        model=model,
        reasoning={"effort": "low"},
        input=prompt,
        instructions=instructions,
    )
    return response.output_text


# %% GPT Response Structure
response = client.responses.create(
    model="gpt-3.5-turbo",
    # reasoning={"effort": "low"},
    input="Testing 123",
)
response

# %%
prompt = "Testing 123"
result = get_completion(prompt)
result

# %%
prompt = "Write me a poem."
instructions = "You are a robot. Respond like a robot. Beep boop."
result = get_completion_with_instructions(prompt, instructions)
result
