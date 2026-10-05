#!/usr/bin/env python3
"""Unpacks the traffic sign dataset into dataset/.

1. Download tsr_train.zip from Moodle (keep it in Downloads or put it next to this script).
2. python download.py

    python download.py                              # finds tsr_train.zip and unpacks train/
    python download.py --zip path/to/tsr_train.zip  # explicit path
    python download.py --split heldout              # at the live demo: finds tsr_heldout.zip
    python download.py --split heldout --url URL    # or downloads it from a direct link

Only the Python standard library is used.
"""

import argparse
import csv
import os
import shutil
import sys
import tempfile
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = [HERE, os.getcwd(), os.path.expanduser("~/Downloads")]


def find_zip(split):
    name = f"tsr_{split}.zip"
    for d in SEARCH_DIRS:
        path = os.path.join(d, name)
        if os.path.isfile(path):
            return path
    return None


def download(url, dest):
    print(f"Downloading {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "tsr-download"})
    with urllib.request.urlopen(req) as r, open(dest, "wb") as f:
        total = int(r.headers.get("Content-Length") or 0)
        done = 0
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            f.write(chunk)
            done += len(chunk)
            if total:
                print(f"\r  {done / 1e6:7.1f} / {total / 1e6:.1f} MB", end="", flush=True)
            else:
                print(f"\r  {done / 1e6:7.1f} MB", end="", flush=True)
    print()


def extract(zip_path, root, split, force):
    target = os.path.join(root, "dataset", split)
    with zipfile.ZipFile(zip_path) as z:
        if not any(n.startswith(f"dataset/{split}/") for n in z.namelist()):
            sys.exit(f"The zip file does not contain dataset/{split}/ - wrong file or wrong --split?")
    if os.path.isdir(os.path.join(target, "images")) and \
            any(f != ".gitkeep" for f in os.listdir(os.path.join(target, "images"))):
        if not force:
            sys.exit(f"{target} already contains images. Use --force to overwrite.")
        shutil.rmtree(os.path.join(target, "images"))
    other = "heldout" if split == "train" else "train"
    with zipfile.ZipFile(zip_path) as z:
        names = z.namelist()
        # the train zip also carries an empty heldout/ skeleton: never touch the other split
        members = [n for n in names if not n.startswith(f"dataset/{other}/")]
        for n in members:
            dest = os.path.realpath(os.path.join(root, n))
            if not dest.startswith(os.path.realpath(root) + os.sep):
                sys.exit(f"Unsafe path in zip file: {n}")
        z.extractall(root, members)
    print(f"Extracted to {target}")


def summary(root, split):
    d = os.path.join(root, "dataset", split)
    images = {f for f in os.listdir(os.path.join(d, "images")) if f.lower().endswith((".png", ".jpg", ".jpeg"))}
    with open(os.path.join(d, "labels.csv"), encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    missing = {r["filename"] for r in rows} - images
    print(f"{split}: {len(images)} images, {len(rows)} labelled signs, "
          f"{len({r['filename'] for r in rows})} images with signs, "
          f"{len({r['class_id'] for r in rows})} classes present")
    if missing:
        print(f"WARNING: {len(missing)} files in labels.csv are missing in images/")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--split", choices=["train", "heldout"], default="train")
    ap.add_argument("--zip", help="path to tsr_<split>.zip (default: search next to the script, here, ~/Downloads)")
    ap.add_argument("--url", help="direct download link instead of a local zip file")
    ap.add_argument("--force", action="store_true", help="overwrite existing images")
    args = ap.parse_args()

    if args.url:
        with tempfile.TemporaryDirectory() as tmp:
            zip_path = os.path.join(tmp, f"tsr_{args.split}.zip")
            download(args.url, zip_path)
            extract(zip_path, HERE, args.split, args.force)
    else:
        zip_path = args.zip or find_zip(args.split)
        if not zip_path or not os.path.isfile(zip_path):
            where = "\n  ".join(SEARCH_DIRS)
            sys.exit(f"tsr_{args.split}.zip not found. Download it from Moodle and put it in one of:\n  {where}\n"
                     f"or pass the path with --zip.")
        print(f"Using {zip_path}")
        extract(zip_path, HERE, args.split, args.force)
    summary(HERE, args.split)


if __name__ == "__main__":
    main()
