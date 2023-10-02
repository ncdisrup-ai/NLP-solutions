import gradio as gr
import Summarization
import NER


gr.close_all()

demo = gr.TabbedInterface([Summarization.app_summarize, NER.app_ner], ["Summarization", "NER"])

demo.launch(share=True) # (share=True for public link)

