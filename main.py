import os

FIRST = "You will find the bug today \u2014 it has been hiding in "
SECOND = "the code you wrote to find it."

TEXT = FIRST + SECOND


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
