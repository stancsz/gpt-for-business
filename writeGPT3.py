"""
write a topic for {} in chapter {}, the book is about "OpenAI's GPT for Business and Harnessing the Power of Artificial Intelligence for Maximum Profit". make it similar to an o'reilly book.
"""

import yaml
from ChatGPT3 import CallAPI, write_logs

import time

def retry_call(prompt):
    """
    write a python function to retry 10 times to print hello world, wait 5 seconds between each retry
    Note: This function will retry 10 times to print "Hello, World!" and wait 5 seconds between each retry. The try-except block is used to catch any exception that may occur, and the break statement is used to exit the loop once the print statement is successful.
    :return:
    """
    for i in range(10):
        try:
            return CallAPI(prompt)
        except:
            print("Call failed, wait 5 seconds to try again")
            time.sleep(5)
            continue

with open("ai-for-business.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        # print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

file = "ai-for-business2.md"

for chapter in data:
    write_logs(file, f"# {chapter}\n")
    # print(chapter)
    for topic in data[chapter]:
        # print(topic)
        write_logs(file, f"## {topic}\n")
        prompt = f"""you are writing a o'reilly book. write a few paragraphs about {topic} for the {chapter},the theme of the book about "OpenAI's GPT for Business and Harnessing the Power of Artificial Intelligence for Maximum Profit". provide case study or code examples where possible. Don't explain what GPT is. Be technical and use hooks occasionally."""
        response = retry_call(prompt)
        write_logs(file, f"{response}\n\n")
        print(prompt, response)


# a chatbot with a white background, minimal, vecto
