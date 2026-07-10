from pathlib import Path

import click

from scanner import scan_vault


@click.command()
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
)
def main(path: Path) -> None:
    files = scan_vault(str(path))

    if not files:
        click.echo("No markdown files found.")
        return

    path_w = max(len("File"), *(len(item.filepath) for item in files))
    words_w = max(len("Words"), *(len(str(item.word_count)) for item in files))
    fm_w = len("Frontmatter")

    sep = f"+-{'-' * path_w}-+-{'-' * words_w}-+-{'-' * fm_w}-+"
    click.echo(sep)
    click.echo(
        f"| {'File'.ljust(path_w)} | {'Words'.rjust(words_w)} | {'Frontmatter'.ljust(fm_w)} |"
    )
    click.echo(sep)

    for item in files:
        fm = "yes" if item.has_frontmatter else "no"
        click.echo(
            f"| {item.filepath.ljust(path_w)} | {str(item.word_count).rjust(words_w)} | {fm.ljust(fm_w)} |"
        )

    click.echo(sep)
    click.echo(f"Total files: {len(files)}")
    click.echo(f"Total words: {sum(item.word_count for item in files)}")


if __name__ == "__main__":
    main()