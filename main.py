
import os
import gradio as gr
from groq import Groq

# טעינת המפתח מקובץ .env
for line in open(".env", encoding="utf-8"):
    if line.startswith("GROQ_API_KEY="):
        os.environ["GROQ_API_KEY"] = line.strip().split("=", 1)[1]

client = Groq()

# קריאת הפרומפט
PROMPT = open("prompt_v3.txt", encoding="utf-8").read()


def to_command(text):
    response = client.chat.completions.create(
       model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0,
    )
    return response.choices[0].message.content


demo = gr.Interface(
    fn=to_command,
    inputs=gr.Textbox(label="הוראה בעברית"),
    outputs=gr.Textbox(label="פקודת CLI"),
    title="CLI Agent",
)
demo.launch()


