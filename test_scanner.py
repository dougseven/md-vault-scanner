import pytest
from pydantic import ValidationError

from scanner import MarkdownFile, scan_vault


def test_markdownfile_validation_negative_word_count():
    """MarkdownFile should reject negative word counts."""
    with pytest.raises(ValidationError):
        MarkdownFile(filepath="test.md", word_count=-1)


def test_scan_vault_with_single_file(tmp_path):
    """scan_vault should return one MarkdownFile for one .md file."""
    vault_dir = tmp_path / "vault"
    vault_dir.mkdir()

    test_file = vault_dir / "test.md"
    test_content = "# Hello World\n\nThis is a test file with some words."
    test_file.write_text(test_content)

    results = scan_vault(str(vault_dir))

    assert len(results) == 1
    assert results[0].filepath == str(test_file)
    assert results[0].word_count == len(test_content.split())
    assert results[0].has_frontmatter is False
    