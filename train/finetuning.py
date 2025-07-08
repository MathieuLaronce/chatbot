from openai import OpenAI
from dotenv import load_dotenv 
load_dotenv()



OPENAI_FILE_ID = "file-TkQmRsqgeP7VkrPDmoKfHA"
OPENAI_MODEL = "gpt-4.1-nano-2025-04-14"

client = OpenAI()

ft_job = client.fine_tuning.jobs.create(
    training_file=OPENAI_FILE_ID,
    model=OPENAI_MODEL
)

print("Fine Tune Job has been created with id ", ft_job.id)
#ftjob-GXZkX86cwTLbeY2t1I5Dhs1M
#ftjob-GzMhoMOavhj1m3lHpuYBsNJo
#ftjob-TpgOY7HHtGs3xJ331DoyRNjg
#ftjob-lQygkLPui88hq9K4rPe7WgZZ