import os
import sys
from google import genai
from google.genai import types

def run_study_assistant():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set your API key before running the script.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print("=" * 50)
    print("        AI Study Assistant & Quiz Generator        ")
    print("=" * 50)

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            print(f"\n[+] Processing file: {file_path}")
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    else:
        print("\nEnter or paste your study notes below (Press Enter twice or Ctrl+Z/Ctrl+D then Enter to finish):")
        lines = []
        try:
            while True:
                line = input()
                if not line and lines and not lines[-1]:
                    break
                lines.append(line)
        except EOFError:
            pass
        content = "\n".join(lines).strip()

    if not content:
        print("No input content provided. Exiting.")
        sys.exit(0)

    prompt = f"""
    You are an intelligent study assistant. Analyze the following study material and generate:
    1. A brief 3-sentence summary of the main concepts.
    2. 5 Key Study Flashcards (Question & Answer pairs).
    3. A 3-question multiple choice quiz with answers explained at the end.

    Study Material:
    {content}
    """

    print("\n[+] Generating study guide using Gemini AI...\n")

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
        )
        print("=" * 50)
        print(response.text)
        print("=" * 50)

    except Exception as e:
        print(f"An error occurred while generating content: {e}")

if __name__ == "__main__":
    run_study_assistant()