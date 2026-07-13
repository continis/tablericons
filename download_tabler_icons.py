#!/usr/bin/env python
"""
Download the latest tablericons zip file and select only the optimized icons.
"""

from __future__ import annotations

import argparse
import os
import subprocess
from io import BytesIO
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="dotted version number")
    args = parser.parse_args(argv)
    version: str = args.version

    proc = subprocess.run(
        [
            "curl",
            "--fail",
            "--location",
            f"https://github.com/tabler/tabler-icons/archive/refs/tags/v{version}.zip",
        ],
        stdout=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise SystemExit(1)

    input_zip = ZipFile(BytesIO(proc.stdout))
    input_prefix = f"tabler-icons-{version}/icons/"

    output_path = "src/tablericons/tablericons.zip"

    try:
        os.remove(output_path)
    except FileNotFoundError:
        pass
    with ZipFile(
        output_path, "w", compression=ZIP_DEFLATED, compresslevel=9
    ) as output_zip:
        for name in sorted(input_zip.namelist()):
            if name.startswith(input_prefix) and name.endswith(".svg"):
                info = input_zip.getinfo(name)
                data = input_zip.read(name)
                if data.startswith(b"<!--"):
                    if (comment_end := data.find(b"-->")) != -1:
                        data = data[comment_end + 3 :]

                new_name = name[len(input_prefix) :]

                info.filename = new_name
                output_zip.writestr(info, data.strip())
                print(new_name)

    print("\n✅ Written!")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
