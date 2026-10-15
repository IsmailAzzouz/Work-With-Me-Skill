import argparse
import hashlib
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


DISTRIBUTION_FILES = (
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "skills/learn-project/LICENSE",
    "skills/learn-project/SKILL.md",
    "skills/learn-project/references/conventions.md",
    "skills/work-with-me/LICENSE",
    "skills/work-with-me/SKILL.md",
    "skills/work-with-me/references/session-layout.md",
    "templates/AGENTS.md",
)


def main():
    parser = argparse.ArgumentParser(description="Package the Markdown skills for release.")
    parser.add_argument("version", help="Release version, for example 0.1.0")
    arguments = parser.parse_args()
    if not re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", arguments.version):
        parser.error("version must be MAJOR.MINOR.PATCH without a v prefix")

    root = Path(__file__).resolve().parent.parent
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## {arguments.version}" not in changelog.splitlines():
        parser.error("add the release version to CHANGELOG.md before packaging")

    contents = {
        relative: (root / relative).read_text(encoding="utf-8").encode("utf-8")
        for relative in DISTRIBUTION_FILES
    }
    for relative in ("skills/learn-project/LICENSE", "skills/work-with-me/LICENSE"):
        if contents[relative] != contents["LICENSE"]:
            parser.error(f"{relative} must match the root LICENSE")

    package_name = f"work-with-me-v{arguments.version}"
    output = root / "dist"
    output.mkdir(exist_ok=True)
    archive_path = output / f"{package_name}.zip"
    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        for relative, content in sorted(contents.items()):
            entry = ZipInfo(f"{package_name}/{relative}", date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.compress_type = ZIP_DEFLATED
            archive.writestr(entry, content)

    checksum = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    checksum_path = output / f"{archive_path.name}.sha256"
    checksum_path.write_text(f"{checksum}  {archive_path.name}\n", encoding="utf-8")
    print(f"Archive: {archive_path}")
    print(f"SHA-256: {checksum}")
    print(f"Checksum file: {checksum_path}")


if __name__ == "__main__":
    main()
