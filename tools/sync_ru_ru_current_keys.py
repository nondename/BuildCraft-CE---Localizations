#!/usr/bin/env python3
"""Add Russian translations for keys present in current BCCE en_us."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANG = ROOT / "src/main/resources/assets/buildcraft/lang/ru_ru.json"

UPDATES = {
    "block.buildcraftenergy.spout_oil": "Нефть (§bХолодная§r)",
    "buildcraft.error.empty_fluid": "ОШИБКА! ЖИДКОСТЬ ОТСУТСТВУЕТ!",
    "buildcraft.guide.chapter.submod.compat": "Совместимость",
    "buildcraft.guide.chapter.subtype.pipe_fe": "Передача FE",
    "buildcraft.guide.chapter.subtype.unlisted": "Прочее",
    "buildcraft.guide.contents.title": "Оглавление",
    "buildcraft.guide.fallback.active": "Резервный интерфейс руководства активен в Minecraft 1.21.11.",
    "buildcraft.guide.fallback.port": "Полные страницы руководства временно недоступны, пока выполняется перенос рендерера документов на Minecraft 1.21.11.",
    "buildcraft.guide.fallback.status": "Рука: %s  Стак: %s",
    "buildcraft.guide.hand.main": "Основная рука",
    "buildcraft.guide.hand.off": "Вторая рука",
    "buildcraft.jei.heat_exchange.mode.cool": "Охлаждение",
    "buildcraft.jei.heat_exchange.mode.heat": "Нагрев",
    "buildcraft.jei.heat_exchange.range": "%s %s → %s",
    "buildcraft.param.facing.down": "Снизу",
    "buildcraft.param.facing.east": "Восток",
    "buildcraft.param.facing.north": "Север",
    "buildcraft.param.facing.south": "Юг",
    "buildcraft.param.facing.up": "Сверху",
    "buildcraft.param.facing.west": "Запад",
    "fluid_type.buildcraftenergy.spout_oil": "Нефть (§bХолодная§r)",
    "gui.ledger.help.hint": "Наведите курсор на подсвеченный элемент управления, чтобы увидеть справку.",
    "item.buildcraftcore.spring_oil_oil": "Нефтяной источник",
    "item.buildcraftcore.spring_water_water": "Водный источник",
    "item.buildcraftlib.guide": "Руководство по BuildCraft",
    "item.buildcraftlib.guide_note": "Заметка руководства BuildCraft",
    "item.filler_planner.name": "Планировщик заполнителя",
}

data = json.loads(LANG.read_text(encoding="utf-8"))
data.update(UPDATES)
LANG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Synced {len(UPDATES)} current en_us keys into ru_ru")
