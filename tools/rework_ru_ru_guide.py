#!/usr/bin/env python3
"""Apply reviewed Russian Guide Book translation fixes."""
from __future__ import annotations

import json
from pathlib import Path

GUIDE = Path("src/main/resources/assets/buildcraft/guide/text/ru_ru.json")

REPLACEMENTS = {
    "Надёжный механизм начинается с правильно изготовленной деревянная шестерни.":
        "Надёжный механизм начинается с правильно изготовленной деревянной шестерни.",
    "Надёжный механизм начинается с правильно изготовленной каменная шестерни.":
        "Надёжный механизм начинается с правильно изготовленной каменной шестерни.",
    "Надёжный механизм начинается с правильно изготовленной железная шестерни.":
        "Надёжный механизм начинается с правильно изготовленной железной шестерни.",
    "Надёжный механизм начинается с правильно изготовленной золотая шестерни.":
        "Надёжный механизм начинается с правильно изготовленной золотой шестерни.",
    "Надёжный механизм начинается с правильно изготовленной алмазная шестерни.":
        "Надёжный механизм начинается с правильно изготовленной алмазной шестерни.",
    "<bold>Подсказка:</bold> Назначьте цветам постоянные значения: например, топливо, масло, вода и переполнение. Так ошибки видны сразу.":
        "<bold>Подсказка:</bold> Назначьте цветам постоянные значения: например, топливо, нефть, вода и переполнение. Так ошибки видны сразу.",
}


def main() -> None:
    text = GUIDE.read_text(encoding="utf-8")
    changed = 0
    for old, new in REPLACEMENTS.items():
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"Expected exactly one occurrence, found {count}: {old}")
        text = text.replace(old, new)
        changed += 1

    GUIDE.write_text(text, encoding="utf-8")
    data = json.loads(GUIDE.read_text(encoding="utf-8"))
    if data.get("language") != "ru_ru":
        raise SystemExit("Unexpected guide language")
    print(f"Applied {changed} reviewed ru_ru guide fixes")


if __name__ == "__main__":
    main()
