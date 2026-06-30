"""
CodeAlpha Python Internship - Task 3: Task Automation with Python Scripts
Idea chosen: Extract all email addresses from a .txt file and save them to another file.
"""

import re
import os
import sys


EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


def extract_emails_from_file(input_path):
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' not found.")
        return []

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    emails = EMAIL_PATTERN.findall(text)
    # Remove duplicates while preserving order
    seen = set()
    unique_emails = []
    for email in emails:
        if email.lower() not in seen:
            seen.add(email.lower())
            unique_emails.append(email)

    return unique_emails


def save_emails(emails, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")
    print(f"Saved {len(emails)} email address(es) to '{output_path}'.")


def main():
    print("=== Email Address Extractor ===")

    if len(sys.argv) >= 2:
        input_path = sys.argv[1]
    else:
        input_path = input("Enter path to the .txt file to scan: ").strip()

    emails = extract_emails_from_file(input_path)

    if not emails:
        print("No email addresses found (or file could not be read).")
        return

    print(f"\nFound {len(emails)} unique email address(es):")
    for email in emails:
        print(f"  - {email}")

    output_path = "extracted_emails.txt"
    save_emails(emails, output_path)


if __name__ == "__main__":
    main()
