# The Excuse My Agent Gave Me — one funny line an AI agent hands its human
# after missing a deadline. Writes the entry text to /output/entry.txt
# with no trailing newline, so the file holds exactly the line itself.
# Swap 25 Nov 2026 (pilihan Ahmad, kandidat 1; ronde 2 peringkat 508/1.263):
# 98 karakter, adegan konkret + twist di frasa terakhir.

TEXT = "I emailed you the finished file at midnight. My outbox says sent. My drafts folder says otherwise."

if __name__ == "__main__":
    # Gate: the sealed scorer requires UTF-8 text of 1 to 200 characters.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
