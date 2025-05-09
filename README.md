# AI-Powered Guided Meditation Application

**Capstone Project – PG Diploma in AI & ML**

This application generates personalized guided meditations using a few-shot prompted Large Language Model (LLM) combined with Retrieval-Augmented Generation (RAG) and Text-to-Speech (TTS) technologies. The goal is to create calming, emotionally resonant meditation experiences tailored to the user's current state of mind.

## Features
- 5 Meditation Categories:

    1. Focus

    2. Sleep

    3. Anxiety & Stress

    4. Motivation

    5. Forgiveness

- Customized Meditations:
Users describe their emotional state (e.g., "I feel anxious after a tough meeting"), and the app generates a meditation script that addresses it.

- Context-Enriched Generation:
The model uses RAG to integrate three relevant transcripts (sourced from Creative Commons YouTube videos) for deeper contextual grounding.

- Natural-Sounding Audio:
Scripts are converted into soothing speech using an open-source TTS model.

## Technical Overview
LLM Few-Shot Prompting:

- Few-shot prompting on curated transcripts.

- Emphasis on clarity, emotional resonance, and theme adherence.

Retrieval-Augmented Generation (RAG): Dynamically retrieves three additional transcripts from a preprocessed set of general advice and coping strategy content.

Text-to-Speech (TTS): Converts generated scripts to audio for a complete guided experience.

## Example Use Case
User Input:

"My boss yelled at me today, and I feel stressed. Could you provide a guided meditation to help me feel better?"

Output:

A calming, stress-reducing meditation script tailored to the user's situation, delivered via soothing audio.

## Licensing
All source content (transcripts) used in this project is obtained under Creative Commons licenses to ensure legal and ethical use.
