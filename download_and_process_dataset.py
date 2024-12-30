import os
import pretty_midi
from scipy.io.wavfile import write

def midi_to_wav(midi_file, output_dir):
    """Convert a MIDI file to WAV."""
    midi_data = pretty_midi.PrettyMIDI(midi_file)
    audio_data = midi_data.fluidsynth()  # Uses default soundfont
    output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(midi_file))[0] + ".wav")
    
    # Write to WAV file
    write(output_path, 44100, audio_data)
    print(f"Saved WAV file: {output_path}")

def batch_convert_midi_to_wav(input_dir, output_dir):
    """Batch convert all MIDI files in a directory to WAV."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file in os.listdir(input_dir):
        if file.endswith(".mid") or file.endswith(".midi"):
            midi_to_wav(os.path.join(input_dir, file), output_dir)

if __name__ == "__main__":
    # Replace these with your actual directories
    input_midi_dir = "path/to/midi_files"
    output_wav_dir = "path/to/output_wav_files"

    batch_convert_midi_to_wav(input_midi_dir, output_wav_dir)
