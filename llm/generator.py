import pandas as pd # type: ignore
import subprocess
import random
from llm.retriever import retrieve_relevant_advice
from bark import SAMPLE_RATE, generate_audio, preload_models # type: ignore
from scipy.io.wavfile import write as write_wav # type: ignore
import os
import uuid
import numpy as np  #type:ignore
import textwrap
import nltk
from nltk.tokenize import sent_tokenize


#nltk.download('punkt')
#nltk.download('punkt_tab')

os.makedirs(os.path.join(os.path.dirname(__file__), "output"), exist_ok=True)

# Load few-shot examples
df = pd.read_csv("C:/Users/Siddharth/OneDrive/Desktop/meditation-backend/data/df_guided.csv")

# Group and sample 2 examples per category
few_shot_df = df.groupby("Meditation Type").apply(lambda x: x.sample(min(2, len(x)))).reset_index(drop=True)

# Preload Bark models once
preload_models()

# Bark voices (subset)
BARK_SPEAKER_PRESETS = {
    "calm_female": "v2/en_speaker_9",
    "neutral_male": "v2/en_speaker_3",
    "soothing_female": "v2/en_speaker_5",
}

def text_to_speech_bark(text: str, output_path, speaker="soothing_female", max_chars=120):
    speaker_style = BARK_SPEAKER_PRESETS.get(speaker, "v2/en_speaker_5")
    # Break text into sentences first
    sentences = sent_tokenize(text)
    # Group sentences into chunks ≤ max_chars
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_chars:
            current_chunk += " " + sentence if current_chunk else sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    # Generate audio for each chunk
    audio_arrays = []
    for chunk in chunks:
        audio = generate_audio(chunk, history_prompt=speaker_style)
        audio_arrays.append(audio)

    # Concatenate all audio chunks
    full_audio = np.concatenate(audio_arrays)
    write_wav(output_path, SAMPLE_RATE, full_audio)
    
    return output_path

def build_few_shot_prompt():
    prompt = ""
    for _, row in few_shot_df.iterrows():
        prompt += (
            f"User: I want a guided meditation for {row['Meditation Type']}\n"
            f"Assistant:\n{row['Processed Transcript'].strip()}\n\n"
        )

    return prompt


def query_llama3(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()


def generate_meditation(user_input, speaker="calm_female"):
    # Step 1: Build the full prompt
    few_shot = build_few_shot_prompt()

    # Step 2: RAG – Get 3 relevant science/advice chunks
    rag_chunks = retrieve_relevant_advice(user_input)
    rag_context = "\n".join(rag_chunks)

    # Step 3: Full prompt
    prompt = (
        few_shot +
        f"User: {user_input.strip()}\n"
        f"(The assistant also knows the following helpful insights, which it may use subtly in its response:)\n"
        f"{rag_context}\n"
        f"Assistant:\n"
    )

    # Step 4: Generate text
    output_text = query_llama3(prompt).strip()

    # Step 5: Convert to audio using Bark
    output_path = os.path.join(os.path.dirname(__file__), "output", f"audio_{uuid.uuid4().hex[:8]}.wav")
    audio_file = text_to_speech_bark(output_text, output_path, speaker)

    return output_text, audio_file