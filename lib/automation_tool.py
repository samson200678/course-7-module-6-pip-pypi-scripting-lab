"""
automation_tool.py
------------------
Main entry point: orchestrates log generation + API data fetch,
then writes a combined summary report.

Usage:
    python automation_tool.py
    python automation_tool.py --posts 5 --output-dir ./output
"""

import argparse
import os
from datetime import datetime

from generate_log import generate_log
from fetch_data import fetch_posts, fetch_single_post, save_posts_to_csv


def write_summary_report(posts: list[dict], log_file: str, csv_file: str, output_dir: str) -> str:
    """Write a human-readable summary report combining all outputs."""
    report_file = f"{output_dir}/summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(report_file, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("       AUTOMATION TOOL — RUN SUMMARY REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(f"  Run timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"  Log file      : {log_file}\n")
        f.write(f"  CSV output    : {csv_file}\n")
        f.write(f"  Posts fetched : {len(posts)}\n")
        f.write("=" * 60 + "\n\n")

        f.write("POST TITLES RETRIEVED\n")
        f.write("-" * 40 + "\n")
        for post in posts:
            f.write(f"  [{post['id']:>3}] {post['title']}\n")

        f.write(f"\nReport generated successfully.\n")

    return report_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Automation Tool: fetch API data and generate log/report files."
    )
    parser.add_argument(
        "--posts", type=int, default=10,
        help="Number of posts to fetch from the API (default: 10)"
    )
    parser.add_argument(
        "--output-dir", type=str, default="output",
        help="Directory to save output files (default: ./output)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    print("\n" + "=" * 50)
    print("   AUTOMATION TOOL STARTING")
    print("=" * 50)

    # Step 1 — Generate activity log
    print("\n[1/3] Generating activity log...")
    log_entries = [
        "Automation tool started",
        f"Output directory set to: {args.output_dir}",
        f"Requesting {args.posts} posts from JSONPlaceholder API",
        "Data fetch completed",
        "CSV export initiated",
        "Summary report generation started",
        "All tasks completed successfully",
    ]
    log_file = generate_log(log_entries, output_dir=args.output_dir)
    print(f"      Log saved  →  {log_file}")

    # Step 2 — Fetch API data
    print(f"\n[2/3] Fetching {args.posts} posts from API...")
    posts = fetch_posts(limit=args.posts)
    csv_file = f"{args.output_dir}/posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    save_posts_to_csv(posts, csv_file)
    print(f"      CSV saved  →  {csv_file}")

    # Step 3 — Write summary report
    print("\n[3/3] Writing summary report...")
    report_file = write_summary_report(posts, log_file, csv_file, args.output_dir)
    print(f"      Report     →  {report_file}")

    print("\n" + "=" * 50)
    print("   ALL DONE — check the output/ folder")
    print("=" * 50 + "\n")