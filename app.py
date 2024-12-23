import gradio as gr
import numpy as np
from textblob import TextBlob

def analyze_text(text):
    if not text:
        return "Please enter some text to analyze.", 0, 0, 0

    blob = TextBlob(text)

    sentiment = blob.sentiment.polarity

    word_count = len(text.split())
    char_count = len(text)
    avg_word_length = char_count / word_count

    return [
        round(sentiment, 2),
        word_count,
        char_count,
        round(avg_word_length, 2),
    ]

with gr.Blocks() as demo:
    gr.Markdown("# Text Analysis App")
    gr.Markdown("Enter some text to analyze its sentiment and get basic statistics.")

    with gr.Row():
        text_input = gr.Textbox(
            label="Input Text",
            placeholder="Type your text here...",
            lines=5,
        )
    
    with gr.Row():
        analyze_button = gr.Button("Analyze")
    
    with gr.Row():
        sentiment_output = gr.Number(label="Sentiment Score (-1 to 1)")
        word_count_output = gr.Number(label="Word Count")
        char_count_output = gr.Number(label="Character Count")
        avg_length_output = gr.Number(label="Average Word Length")
    
    analyze_button.click(
        fn=analyze_text,
        inputs=text_input,
        outputs=[
            sentiment_output,
            word_count_output,
            char_count_output,
            avg_length_output,
        ]
    )

if __name__ == "__main__":
    demo.launch()