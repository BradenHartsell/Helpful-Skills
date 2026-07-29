from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
ROOT_README = REPOSITORY_ROOT / "README.md"
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
COMPILED_DATE_PATTERN = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
FRONTMATTER_NAME_PATTERN = re.compile(r"^name:\s*['\"]?([^'\"\s]+)['\"]?\s*$", re.MULTILINE)


def relative_path(path: Path) -> str:
    return path.relative_to(REPOSITORY_ROOT).as_posix()


def validate_internal_links(markdown_file: Path, errors: list[str]) -> None:
    text = markdown_file.read_text(encoding="utf-8")
    for match in MARKDOWN_LINK_PATTERN.finditer(text):
        raw_target = match.group(1).strip()
        if (
            not raw_target
            or raw_target.startswith(("#", "http://", "https://", "mailto:"))
        ):
            continue

        path_text = unquote(raw_target.split("#", 1)[0].split("?", 1)[0])
        if not path_text:
            continue

        target = (markdown_file.parent / path_text).resolve()
        try:
            target.relative_to(REPOSITORY_ROOT)
        except ValueError:
            errors.append(
                f"{relative_path(markdown_file)} links outside the repository: "
                f"{raw_target}"
            )
            continue

        if not target.exists():
            errors.append(
                f"{relative_path(markdown_file)} has a broken link: {raw_target}"
            )


def validate_compiled_date(skill_directory: Path, errors: list[str]) -> None:
    combined_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (skill_directory / "README.md", skill_directory / "SKILL.md")
    )
    matches = COMPILED_DATE_PATTERN.findall(combined_text)
    if not matches:
        errors.append(
            f"{relative_path(skill_directory)} has no YYYY-MM-DD compiled date"
        )
        return

    for value in matches:
        try:
            date.fromisoformat(value)
        except ValueError:
            errors.append(
                f"{relative_path(skill_directory)} has an invalid date: {value}"
            )


def validate_skill(skill_directory: Path, catalog_text: str, errors: list[str]) -> None:
    skill_id = skill_directory.name
    skill_file = skill_directory / "SKILL.md"
    readme_file = skill_directory / "README.md"

    for required_file in (skill_file, readme_file):
        if not required_file.is_file():
            errors.append(f"Missing required file: {relative_path(required_file)}")

    if not skill_file.is_file() or not readme_file.is_file():
        return

    skill_text = skill_file.read_text(encoding="utf-8")
    if not skill_text.startswith("---\n"):
        errors.append(f"{relative_path(skill_file)} has no YAML frontmatter")
    else:
        frontmatter_parts = skill_text.split("---", 2)
        if len(frontmatter_parts) < 3:
            errors.append(f"{relative_path(skill_file)} has unclosed YAML frontmatter")
        else:
            name_match = FRONTMATTER_NAME_PATTERN.search(frontmatter_parts[1])
            if not name_match:
                errors.append(f"{relative_path(skill_file)} has no frontmatter name")
            elif name_match.group(1) != skill_id:
                errors.append(
                    f"{relative_path(skill_file)} declares {name_match.group(1)!r}, "
                    f"expected {skill_id!r}"
                )

    if "[TODO" in skill_text or "TODO:" in skill_text:
        errors.append(f"{relative_path(skill_file)} contains unfinished template text")

    validate_compiled_date(skill_directory, errors)

    catalog_entry = f"skills/{skill_id}/"
    if catalog_entry not in catalog_text:
        errors.append(f"Root README has no catalog entry for {catalog_entry}")


def main() -> int:
    errors: list[str] = []

    if (REPOSITORY_ROOT / "SKILL.md").exists():
        errors.append("Skills must live under skills/<skill-id>, not at repository root")

    if not ROOT_README.is_file():
        errors.append("Missing root README.md")
        catalog_text = ""
    else:
        catalog_text = ROOT_README.read_text(encoding="utf-8")

    if not SKILLS_ROOT.is_dir():
        errors.append("Missing skills directory")
        skill_directories: list[Path] = []
    else:
        skill_directories = sorted(
            path
            for path in SKILLS_ROOT.iterdir()
            if path.is_dir() and not path.name.startswith(".")
        )

    if not skill_directories:
        errors.append("No skill packages found under skills/")

    for skill_directory in skill_directories:
        validate_skill(skill_directory, catalog_text, errors)

    for markdown_file in REPOSITORY_ROOT.rglob("*.md"):
        validate_internal_links(markdown_file, errors)

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Catalog validation passed for {len(skill_directories)} skill package(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
