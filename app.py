import streamlit as st
from music21 import stream, note
import random

st.title("🎵 AI Music Generation Tool")
st.write("Yeh task AI aur **music21** library ka use kar ke note sequences generate karta hai aur unhein MIDI file mein convert karta hai!")

# Model simulation / Data generation using music21
if st.button("Generate New Music Sequence"):
    # Create a music stream
    s = stream.Stream()
    
    # Predefined notes simulating AI model sequence generation
    scale_notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'G4', 'E4']
    
    generated_sequence = []
    for _ in range(16):
        n_name = random.choice(scale_notes)
        n = note.Note(n_name)
        n.quarterLength = 0.5
        s.append(n)
        generated_sequence.append(n_name)
        
    st.write("**Generated Note Sequences:**", generated_sequence)
    
    # Convert generated sequences to MIDI and save[cite: 7]
    midi_file_path = "AI_Generated_Music.mid"
    s.write('midi', fp=midi_file_path)
    
    st.success("Music sequence successfully converted to MIDI!")
    
    # Download button to save or play the audio/MIDI file[cite: 7]
    with open(midi_file_path, "rb") as f:
        st.download_button(
            label="Download Generated MIDI File",
            data=f,
            file_name="CodeAlpha_Music.mid",
            mime="audio/midi"
        )
else:
    st.info("Click the button above to generate a new AI music sequence.")