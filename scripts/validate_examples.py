"""Validate synthetic examples and public-safety boundaries."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".txt"}
EXPECTED_ROOT_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SKILL.md",
    "agents/openai.yaml",
    "docs/references.md",
    "quality-checklist.md",
]
FORBIDDEN_PATH_NAMES = {".codex", ".claude", "AGENTS.md", "CLAUDE.md"}
SENSITIVE_PATTERNS = {
    "local path": re.compile(r"([A-Z]:\\+(?:Users|OneDrive|Dropbox|Desktop|Documents|Projects|Research)\\+|/Users/|/home/)", re.IGNORECASE),
    "personal email": re.compile(r"\b[\w.+-]+@(?:gmail|outlook|hotmail|qq|163|126)\.com\b", re.IGNORECASE),
    "phone number": re.compile(r"(?<![\d./-])(?:\+?\d[\s.-]?){10,}(?![\d./-])"),
    "credential": re.compile(
        r"(sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
        r"AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|xox[baprs]-[0-9A-Za-z-]+|"
        r"api[_-]?key\s*[:=]|access[_-]?token\s*[:=]|secret\s*[:=]|password\s*[:=])",
        re.IGNORECASE,
    ),
    "private marker": re.compile(r"\b(confidential|internal only|proprietary|do not distribute)\b", re.IGNORECASE),
    "identity keyword": re.compile(r"(?:" + "户" + "口" + r"|" + "护" + "照" + r"|passport|hukou)", re.IGNORECASE),
}
SELF_PROVING_PATTERNS = [
    re.compile(r"自然で丁寧なメール", re.IGNORECASE),
    re.compile(r"以下.*メール.*作成", re.IGNORECASE),
    re.compile(r"\bAI\b", re.IGNORECASE),
]


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and (path.suffix.lower() in TEXT_SUFFIXES or path.name in {"README.md", "LICENSE"}):
            files.append(path)
    return files


def validate_examples() -> list[str]:
    errors: list[str] = []
    scenarios = [path for path in sorted(EXAMPLES.iterdir()) if path.is_dir()]
    if not scenarios:
        return ["No example scenario directories found."]

    for scenario in scenarios:
        input_path = scenario / "input.md"
        output_path = scenario / "output.md"
        if not input_path.is_file():
            errors.append(f"Missing input.md for {scenario.name}")
        if not output_path.is_file():
            errors.append(f"Missing output.md for {scenario.name}")
        if output_path.is_file():
            output = output_path.read_text(encoding="utf-8", errors="replace")
            asks_for_more_context = "補充" in output or "补充" in output or ("確認" in output and "情報" in output)
            if "件名：" not in output and not asks_for_more_context:
                errors.append(f"{scenario.name}/output.md should include a Japanese subject line or ask for missing essentials.")
            for pattern in SELF_PROVING_PATTERNS:
                if pattern.search(output):
                    errors.append(f"{scenario.name}/output.md contains self-proving or assistant-like phrasing.")
    return errors


def validate_public_text() -> list[str]:
    errors: list[str] = []
    for relative in EXPECTED_ROOT_FILES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Missing expected file: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"Expected file is empty: {relative}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and any(part in FORBIDDEN_PATH_NAMES for part in path.relative_to(ROOT).parts):
            errors.append(f"Forbidden local-agent path in public repo: {path.relative_to(ROOT).as_posix()}")

    for path in iter_text_files():
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"Potential {label} in {relative}")
    return errors


def main() -> int:
    errors = validate_examples() + validate_public_text()
    if errors:
        print("Example validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    scenario_count = len([path for path in EXAMPLES.iterdir() if path.is_dir()])
    print(f"Validated {scenario_count} academic email examples.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
