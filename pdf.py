# This script builds pdfs of every chapter using the myst command myst build my-document.md --pdf

import subprocess

chapters = [
    "0_intro.md",
    "1_assess.md",
    "2_plan.md",
    "3_implement.md",
    "4_analyze.md",
    "5_share.md",
    "6_close.md",
    "7_annex.md"
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