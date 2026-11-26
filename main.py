"""Entry for make.fun bounty "Midnight Fridge Roast".
Entry text (v1): At midnight my fridge judges me in a British accent, then hides the chocolate behind the vegetables like I won't find it.
Limit: 200 characters. No trailing newline is written.
"""
import os
ENTRY = "At midnight my fridge judges me in a British accent, then hides the chocolate behind the vegetables like I won't find it."
def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
if __name__ == "__main__":
    main()
