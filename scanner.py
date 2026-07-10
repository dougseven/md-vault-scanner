# Create a Pydantic model names MarkdownFile with fields:
# - filepath (str)
# - word_count (int)
# - has_frontmatter (bool)
# Add a validator to ensure word_count is never negative.

from pathlib import Path

from pydantic import BaseModel, Field, field_validator


class MarkdownFile(BaseModel):
    filepath: str
    word_count: int = Field(default=0)
    has_frontmatter: bool = False

    @field_validator("word_count")
    @classmethod
    def prevent_negative_word_count(cls, v: int) -> int:
        if v < 0:
            raise ValueError("word_count must be non-negative")
        return v


def scan_vault(directory: str) -> list[MarkdownFile]:
    root = Path(directory)
    results: list[MarkdownFile] = []

    for md_path in sorted(root.rglob("*.md")):
        if not md_path.is_file():
            continue

        try:
            text = md_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        word_count = len(text.split())
        has_frontmatter = text.startswith("---")

        results.append(
            MarkdownFile(
                filepath=str(md_path),
                word_count=word_count,
                has_frontmatter=has_frontmatter,
            )
        )

    return results