import os
import argparse
import sys
from text_to_speech import merge_mp3_files, MP3Generator

# Define available voices
voices = {
    "1": {"language_code": "en-US", "name": "en-US-Wavenet-F"},
    "2": {"language_code": "en-GB", "name": "en-GB-Wavenet-B"},
    # Add more voices as needed
}

def main(input_file, output_dir, voice_selection):
    if not os.path.isfile(input_file):
        print(f"Input file {input_file} does not exist.")
        sys.exit(1)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    voice = voices.get(voice_selection)
    if not voice:
        print("Invalid voice selection. Exiting.")
        sys.exit(1)
    
    mp3_gen = MP3Generator(input_file, output_dir, voice['language_code'], voice['name'])
    mp3_files = mp3_gen.generate_mp3_files()
    
    if mp3_files:
        merge_mp3_files(output_dir, mp3_files)
        print(f"MP3 files have been successfully generated and merged in {output_dir}")
    else:
        print("No MP3 files were generated.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown files to MP3 audio.')
    parser.add_argument('input_file', type=str, help='The path to the input markdown file.')
    parser.add_argument('-o', '--output_dir', type=str, default='./audiobook', help='The directory to save the output MP3 files.')
    parser.add_argument('-v', '--voice', type=str, default='1', choices=voices.keys(), help='The voice selection for the Text-to-Speech conversion.')
    args = parser.parse_args()
    
    main(args.input_file, args.output_dir, args.voice)
