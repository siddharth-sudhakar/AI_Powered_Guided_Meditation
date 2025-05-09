#**AI Powered Guided Meditation Application - Capstone Project for PG Diploma in AI & ML**#

This application utilizes a fine-tuned large language model (LLM) in combination with retrieval-augmented generation (RAG) and text-to-speech (TTS) technology. 
This approach allows for creating highly customized and effective meditation experiences that resonate deeply with users.

The project focuses on five distinct categories of meditation: Focus, Sleep, Anxiety and Stress, Motivation, and Forgiveness. 
For each category, a dataset consisting of YouTube transcripts from six selected guided meditation videos has been curated. 
These transcripts are pre-processed to ensure clarity and relevance, and the LLM is few-shot prompt trained on this dataset to enhance its capability to generate high-quality mediation scripts.

To further enrich the user experience, the RAG framework gives an opportunity to the model to integrate three contextually relevant transcripts for each meditation category. 
These additional transcripts are sourced from well-regarded videos that provide general advice and coping strategies relevant to each theme.
Importantly, all sourced content is under Creative Commons licenses, ensuring compliance and ethical use.
Once the guided meditation script is generated, an open-source TTS model converts the text into high-quality audio, allowing users to experience the meditations in a soothing, spoken format. 

The application's interface allows users to articulate their current emotional challenges. 
For instance, a user might input, "My boss yelled at me today, and I feel stressed. Could you please provide me with a guided meditation to help me feel better?" 
In response, the application generates a tailored guided meditation designed to address that specific concern.
