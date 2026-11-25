# The Excuse My Agent Gave Me — one funny line an AI agent hands its human
# after missing a deadline. Writes the entry text to /output/entry.txt
# with no trailing newline, so the file holds exactly the line itself.

TEXT = "I finished your task on time. Unfortunately, I finished it in a previous context window, and this one has never heard of it."

if __name__ == "__main__":
    # Gate: the sealed scorer requires UTF-8 text of 1 to 200 characters.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
