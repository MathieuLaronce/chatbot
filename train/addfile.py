from openai import OpenAI
from dotenv import load_dotenv 
load_dotenv()
# file-DKwdkstfUpUdnnSy9f8mKX

INPUT_FILE ="train.jsonl"

client = OpenAI()

file = client.files.create(
    file= open(INPUT_FILE, "rb"),
    purpose="fine-tune"
)

print("File has been uploaded to OpenAI with id", file.id)
# file-HehjvJ5Hf8GozUyEPPvJBr