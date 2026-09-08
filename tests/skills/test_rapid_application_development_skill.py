from pathlib import Path


ROOT = Path(__file__).parents[2]
SKILL = ROOT / "software-development" / "rapid-application-development" / "SKILL.md"
README = ROOT / "README.md"
ROLES = ROOT / "Roles.md"


def _frontmatter(text: str) -> dict[str, str]:
    assert text.startswith("---\n")
    raw, _ = text[4:].split("\n---\n", 1)
    values = {}
    for line in raw.splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def test_skill_frontmatter_meets_repo_contract():
    text = SKILL.read_text(encoding="utf-8")
    frontmatter = _frontmatter(text)

    assert frontmatter["name"] == "rapid-application-development"
    assert len(frontmatter["description"]) <= 60
    assert frontmatter["description"].endswith(".")
    assert frontmatter["version"] == "0.1.0"
    assert frontmatter["author"].startswith("FerdinandM")
    assert "platforms:" in text
    assert "metadata:" in text
    assert "related_skills:" in text


def test_skill_is_documentation_only_and_has_ordered_tasks():
    text = SKILL.read_text(encoding="utf-8")

    assert "does not write executable code" in text
    assert "### Task 1:" in text
    assert "### Task 8:" in text
    task_positions = [text.index(f"### Task {number}:") for number in range(1, 9)]
    assert task_positions == sorted(task_positions)
    assert text.count("Completion criterion:") >= 25
    assert "## Verification" in text
    assert "## Sources" in text


def test_role_indexes_reference_the_streamlined_skill():
    readme = README.read_text(encoding="utf-8")
    roles = ROLES.read_text(encoding="utf-8")

    assert "software-development/rapid-application-development/SKILL.md" in readme
    assert "rapid-application-development" in readme
    # RAD is governed separately and intentionally not covered by Roles.md.
    assert "governed separately" in roles
    assert "Role 7" not in roles


def test_supporting_reference_is_present():
    reference = SKILL.parent / "references" / "rad-methodology.md"
    assert reference.is_file()
    assert "Requirements planning" in reference.read_text(encoding="utf-8")
    assert "Cutover" in reference.read_text(encoding="utf-8")
