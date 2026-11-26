import os

ENTRY = "I'm away and honestly relieved — your email joins 214 unread friends. I'll reply when I'm back, probably Tuesday, definitely with coffee."
ENTRY_FILENAME = "entry.txt"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
