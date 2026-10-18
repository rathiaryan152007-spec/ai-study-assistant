# AI Study Assistant & Quiz Generator

A Python CLI application powered by the Google Gemini API (gemini-2.5-flash) that transforms study notes and documents into summaries, flashcards, and practice quizzes.

*Author:* Aryan Rathi  
*CU ID:* CU26220292  

---

## Features
- Direct file input or interactive terminal note pasting.
- Generates concise 3-sentence topic summaries.
- Creates 5 key Q&A flashcards for revision.
- Builds multiple-choice quizzes with detailed answer explanations.

---

## Setup & Usage

### 1. Install dependencies
```bash
pip install google-genai
```
### 2. Set your Gemini API Key
-**Windows (CMD) :**
 `set GEMINI_API_KEY=your_api_key_here`
 -**Linux/Mac:**
  `export GEMINI_API_KEY=your_api_key_here`
  ```
### 3. Run the tool
-**Analyze notes from a file:**
 `python main.py notes.txt`
-**Interactive mode (paste notes directly):**
 `python main.py`
 ```
