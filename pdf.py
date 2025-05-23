# This script builds pdfs of every chapter using the myst command myst build my-document.md --pdf

import subprocess

chapters = [
    "1_intro.md",
    "2_assess.md",
    "3_plan.md",
    "4_implement.md",
    "5_analyze.md",
    "6_share.md",
    "7_close.md",
    "8_annex.md"
]

for filename in chapters:
    try:
        subprocess.run(
            ["myst", "build", filename, "--pdf"],
            check=True
        )
        print(f"Built PDF for {filename}")
    except subprocess.CalledProcessError:
        print(f"Failed to build PDF for {filename}")