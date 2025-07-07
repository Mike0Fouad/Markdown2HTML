
# Markdown to HTML Converter 📝➡️🌐

Convert Markdown (`.md`) files into clean HTML via a simple command-line tool.

---

## ⚙️ Features

- **File input validation**: Ensures the source exists and uses `.md` extension.
- **Flexible output options**: Accepts either a directory (auto-generates filename) or explicit output path.
- **Robust error handling**: Detects missing files, incorrect extensions, or unwritable locations.
- **Clean conversion**: Utilizes [Python‑Markdown](https://pypi.org/project/markdown/) to transform Markdown text to HTML :contentReference[oaicite:1]{index=1}.
- **Logging enabled**: Reports issues via Python's `logging` module.
- **Interactive CLI**: Guides the user through prompts for input and output paths.

---

## 🚀 Quickstart

1. **Clone the repo**

   ```bash
   git clone https://github.com/Mike0Fouad/Markdown2HTML.git
   cd Markdown2HTML


2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install markdown
   ```

4. **Run the converter**

   ```bash
   python main.py
   ```

   You’ll be prompted to enter:

   * Path to an existing `.md` file.
   * Output directory or desired `.html` filename.

---

## 🗂️ Project Structure

* `main.py`: Orchestrates user interaction, file validation, and conversion.
* `MarkdownToHTMLConverter` class:

  * `set_input_file(...)`: Validates source Markdown file.
  * `set_output_file(...)`: Determines output path and filename.
  * `conversion()`: Reads Markdown, converts to HTML, and writes output.
* Uses `logging` for error detection and tracing.

---

## 🧠 Tech & Skills

* **Language**: Python 3
* **Library**: `markdown` for Markdown → HTML conversion ([zetcode.com][1], [dev.to][2], [linode.com][3])
* **Core skills**: CLI development, file-system operations, exception handling, modular design, user prompts.

---


## 🔗 Repository

[GitHub: Mike0Fouad/Markdown2HTML](https://github.com/Mike0Fouad/Markdown2HTML)

---

[1]: https://zetcode.com/python/markitdown/?utm_source=chatgpt.com "Python markitdown - Markdown Parsing and Rendering - ZetCode"
[2]: https://dev.to/stokry/how-to-create-a-simple-markdown-to-html-converter-in-python-14li?utm_source=chatgpt.com "How to Create a Simple Markdown to HTML Converter in Python"
[3]: https://www.linode.com/docs/guides/how-to-use-python-markdown-to-convert-markdown-to-html/?utm_source=chatgpt.com "Use Python-Markdown to Convert Markdown to HTML - Linode"
[4]: https://www.devdungeon.com/content/convert-markdown-html-python?utm_source=chatgpt.com "Convert Markdown to HTML with Python - DevDungeon"
[5]: https://en.wikipedia.org/wiki/MkDocs?utm_source=chatgpt.com "MkDocs"
