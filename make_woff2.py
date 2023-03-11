from fontTools.subset import main as run_subset
from pathlib import Path
import argparse


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


def main(args: argparse.Namespace) -> int:
    args = vars(args)
    font_family = args["font-family"]
    font_family_dir = Path("dist").joinpath(font_family, "ttf-unhinted")

    if not font_family_dir.exists():
        raise ValueError(f"{font_family_dir} does not exist")

    if status := subset_all(font_family_dir):
        return status


if __name__ == "__main__":
    import sys

    parser = argparse.ArgumentParser(prog="make_woff2.py")
    _ = parser.add_argument("font-family")

    args = parser.parse_args()

    if status := main(args):
        sys.exit(status)
