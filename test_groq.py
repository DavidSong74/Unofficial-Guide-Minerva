import os, groq, dotenv
dotenv.load_dotenv()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))
models = client.models.list()
for m in models.data:
    print(m.id)
