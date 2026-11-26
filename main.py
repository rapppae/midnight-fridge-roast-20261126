"""Entry for make.fun bounty "Midnight Fridge Roast".
Entry text (revised v2): At 3 a.m. my fridge turns on its light like a bouncer and says, 'You're not on the list.' I live here. I pay the electric bill.
Limit: 200 characters. No trailing newline is written.
"""
import os
ENTRY = "At 3 a.m. my fridge turns on its light like a bouncer and says, 'You're not on the list.' I live here. I pay the electric bill."
def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
if __name__ == "__main__":
    main()
