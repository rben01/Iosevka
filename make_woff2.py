from fontTools.subset import main as run_subset
from pathlib import Path

SUBSET_ARGS = [
    "--flavor=woff2",
    "--layout-features=kern,liga,clig,calt",
    "--unicodes=*",
]


def subset_one(src: Path) -> int:
    woff2_dir = src.parent.parent.joinpath("woff2-unhinted")
    woff2_dir.mkdir(exist_ok=True)

    dst = woff2_dir.joinpath(src.stem).with_suffix(".woff2")

    args = [f"{src}", f"--output-file={dst}", *SUBSET_ARGS]
    print(args)
    return run_subset(args)


def subset_all(font_family_dir: Path) -> int:
    for f in font_family_dir.glob("*.ttf"):
        if status := subset_one(f):
            return status


def main() -> int:
    for font_family in [
        "iosevka-rltb-mono",
        "iosevka-rltb-mono-alt",
        "iosevka-rltb-proportional-sans",
    ]:
        font_family_dir = Path("dist").joinpath(font_family, "ttf-unhinted")
        if status := subset_all(font_family_dir):
            return status


if __name__ == "__main__":
    import sys

    if status := main():
        sys.exit(status)
