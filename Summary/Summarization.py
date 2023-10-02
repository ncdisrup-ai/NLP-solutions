from transformers import pipeline
import gradio as gr

get_completion = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize(input):
    output = get_completion(input)
    return output[0]['summary_text']

app_summarize = gr.Interface(fn=summarize,
                    inputs=[gr.Textbox(label="Text to summarize", lines=6)],
                    outputs=[gr.Textbox(label="Result", lines=3)],
                    title="Text summarization with distilbart-cnn",
                    description="Summarize any text using the `sshleifer/distilbart-cnn-12-6` model under the hood!",
                    allow_flagging="never"
                   )
