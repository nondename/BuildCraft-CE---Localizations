#!/usr/bin/env python3
"""Apply reviewed Russian translation fixes without touching localization keys."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANG = ROOT / "src/main/resources/assets/buildcraft/lang/ru_ru.json"

FIXES: dict[str, str] = {
    "_comment": "Русская локализация BuildCraft Community Edition.",
    "achievement.aLotOfCraftingAchievement": "Много крафта",
    "achievement.aLotOfCraftingAchievement.desc": "Создайте автоматический верстак",
    "achievement.architectAchievement.desc": "Создайте архитектурный стол",
    "achievement.blueprintAchievement": "Строительный проект",
    "achievement.blueprintAchievement.desc": "Создайте чертёж",
    "achievement.blueprintLibraryAchievement": "Идеи остаются",
    "achievement.blueprintLibraryAchievement.desc": "Создайте электронную библиотеку",
    "achievement.builderAchievement.desc": "Создайте строителя",
    "achievement.chunkDestroyerAchievement.desc": "Создайте карьер",
    "achievement.diamondGearAchievement": "Блестит!",
    "achievement.engineAchievement1.desc": "Создайте редстоуновый двигатель",
    "achievement.engineAchievement2.desc": "Создайте двигатель Стирлинга",
    "achievement.engineAchievement3.desc": "Создайте двигатель внутреннего сгорания",
    "achievement.fasterFillingAchievement": "Ускоренное заполнение",
    "achievement.fasterFillingAchievement.desc": "Создайте заполнитель",
    "achievement.ironGearAchievement": "Нержавеющая?",
    "achievement.refineAndRedefineAchievement": "Переработать и переосмыслить",
    "achievement.refineAndRedefineAchievement.desc": "Создайте нефтеперерабатывающую установку",
    "achievement.stoneGearAchievement": "Твёрдая, как скала",
    "achievement.straightDownAchievement.desc": "Создайте буровую установку",
    "achievement.templateAchievement.desc": "Создайте шаблон",
    "achievement.timeForSomeLogicAchievement.desc": "Создайте сборочный стол",
    "achievement.tinglyLaserAchievement.desc": "Создайте лазер",
    "achievement.woodenGearAchievement": "Грубовата по краям",
    "achievement.woodenGearAchievement.desc": "Создайте деревянную шестерню",
    "achievement.wrenchAchievement": "Просто стукните!",
    "achievement.wrenchAchievement.desc": "Создайте гаечный ключ",
    "advancements.buildcraftbuilders.destroying_the_world.description": "Запустите одновременно не менее двух карьеров размером 64 × 64 на полной скорости",
    "advancements.buildcraftbuilders.paving_the_way.description": "Используйте строителя вместе с маркерами пути, чтобы проложить дорогу",
    "advancements.buildcraftenergy.fine_riches.description": "Найдите нефтяное месторождение",
    "advancements.buildcraftenergy.ice_cool.description": "Охладите двигатель внутреннего сгорания чем-либо, кроме воды, если это возможно",
    "advancements.buildcraftfactory.fluid_storage.description": "Поместите жидкость в резервуар",
    "advancements.buildcrafttransport.sealing_fluids.description": "Переплавьте кактус в зелёный краситель и создайте герметик для труб",
}

PLACEHOLDER_RE = re.compile(r"%(?:\d+\$)?[-#+ 0,(]*\d*(?:\.\d+)?[a-zA-Z%]")


def placeholders(value: str) -> list[str]:
    return PLACEHOLDER_RE.findall(value)


def main() -> None:
    data = json.loads(LANG.read_text(encoding="utf-8"))
    missing = [key for key in FIXES if key not in data]
    if missing:
        raise SystemExit("Missing localization keys: " + ", ".join(missing))

    changed = 0
    for key, new_value in FIXES.items():
        old_value = data[key]
        if placeholders(old_value) != placeholders(new_value):
            raise SystemExit(
                f"Placeholder mismatch for {key}: "
                f"{placeholders(old_value)} -> {placeholders(new_value)}"
            )
        if old_value != new_value:
            data[key] = new_value
            changed += 1

    LANG.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    # Re-read immediately so malformed output fails before it can be committed.
    json.loads(LANG.read_text(encoding="utf-8"))
    print(f"Applied {changed} reviewed ru_ru fixes")


if __name__ == "__main__":
    main()
