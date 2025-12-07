from flask import Flask, render_template, abort
from markupsafe import Markup
import markdown2
from pathlib import Path

app = Flask(__name__)
PAGES_DIR = Path("pages")

def render_markdown(filename):
    file_path = PAGES_DIR / filename
    if not file_path.exists():
        abort(404)
    md = file_path.read_text(encoding="utf-8")
    html = markdown2.markdown(md, extras=[
    "fenced-code-blocks", "code-friendly", "tables", "highlightjs-lang"
])
    # Mark as safe HTML so Jinja doesn’t re-escape
    return Markup(html)

@app.route("/")
def home():
    content = render_markdown("index.md")
    return render_template("base.html", content=content)

@app.route("/<page>.html")
def page(page):
    content = render_markdown(f"{page}.md")
    return render_template("base.html", content=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
