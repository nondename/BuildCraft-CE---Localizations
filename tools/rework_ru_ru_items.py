#!/usr/bin/env python3
"""Fix reviewed legacy item, block and tooltip translations in ru_ru."""
from __future__ import annotations

import json
import re
from pathlib import Path

LANG = Path(__file__).resolve().parents[1] / "src/main/resources/assets/buildcraft/lang/ru_ru.json"

FIXES: dict[str, str] = {
    "item.PipePlug.name": "Заглушка трубы",
    "item.PipePowerCobblestone.name": "Булыжниковая кинезисная труба",
    "item.PipePowerDiamond.name": "Алмазная кинезисная труба",
    "item.PipePowerEmerald.name": "Изумрудная кинезисная труба",
    "item.PipePowerGold.name": "Золотая кинезисная труба",
    "item.PipePowerIron.name": "Железная кинезисная труба",
    "item.PipePowerQuartz.name": "Кварцевая кинезисная труба",
    "item.PipePowerSandstone.name": "Песчаниковая кинезисная труба",
    "item.PipePowerStone.name": "Каменная кинезисная труба",
    "item.PipePowerWood.name": "Деревянная кинезисная труба",
    "item.PipePowerWoodenDiamond.name": "Деревянная алмазная кинезисная труба",
    "item.PipeStructureCobblestone.name": "Булыжниковая структурная труба",
    "item.blueprintItem.name": "Чертёж",
    "item.buildcraft.filler_planner.name": "Планировщик заполнителя",
    "item.buildcraft.guide_note.name": "Заметка руководства BuildCraft",
    "item.buildcraft_pipe_andersite_polished_item.name": "Полированная андезитовая транспортная труба",
    "item.buildcraft_pipe_diorite_polished_item.name": "Полированная диоритовая транспортная труба",
    "item.buildcraft_pipe_granite_polished_item.name": "Полированная гранитная транспортная труба",
    "item.gateCopier.name": "Копировщик гейтов",
    "item.gel.name": "Загущённая вода",
    "item.light_sensor.name": "Датчик света",
    "item.markerConnector.name": "Соединитель маркеров",
    "item.package.name": "Посылка",
    "item.paintbrush.name": "Кисть",
    "item.pipeWaterproof.name": "Герметик для труб",
    "item.pipeWire.name": "Провод для труб",
    "item.pulsar.name": "Трубный пульсар",
    "item.redstoneCrystal.name": "Редстоуновый кристалл",
    "item.redstone_board.name": "Редстоуновая плата",
    "item.redstone_comp_chipset.name": "Редстоуновый компараторный чипсет",
    "item.redstone_diamond_chipset.name": "Алмазный чипсет",
    "item.redstone_emerald_chipset.name": "Изумрудный чипсет",
    "item.redstone_gold_chipset.name": "Золотой чипсет",
    "item.redstone_iron_chipset.name": "Железный чипсет",
    "item.redstone_pulsating_chipset.name": "Пульсирующий чипсет",
    "item.redstone_quartz_chipset.name": "Кварцевый чипсет",
    "item.redstone_red_chipset.name": "Редстоуновый чипсет",
    "item.schematicSingle": "Схема одного блока",
    "item.tablet.name": "Планшет",
    "item.templateItem.name": "Шаблон",
    "item.waterGel.name": "Гелификатор воды",
    "itemGroup.buildcraft.facades": "Фасады BuildCraft",
    "itemGroup.buildcraft.pipes": "Трубы BuildCraft",
    "itemGroup.buildcraft.plugs": "Компоненты труб BuildCraft",
    "tile.architect.allowCreative": "Режим: творческий",
    "tile.architect.excavate": "Раскопка: вкл.",
    "tile.architect.noallowCreative": "Режим: выживание",
    "tile.architect.noexcavate": "Раскопка: выкл.",
    "tile.architect.norotate": "Поворот: выкл.",
    "tile.architect.rotate": "Поворот: вкл.",
    "tile.architect.tooltip.allowCreative.1": "В творческом режиме разрешены все блоки — только для творческого режима!",
    "tile.architect.tooltip.allowCreative.2": "В режиме выживания неподдерживаемые блоки игнорируются",
    "tile.architectBlock.name": "Архитектурный стол",
    "tile.architectBlock.tip": "Создаёт чертежи и шаблоны по отмеченным областям",
    "tile.assemblyWorkbenchBlock.name": "Продвинутый верстак",
    "tile.builderBlock.tip": "Строит сооружения по чертежам и шаблонам",
    "tile.chargingTableBlock.name": "Стол зарядки",
    "tile.chargingTableBlock.tip": "Заряжает совместимые предметы энергией BuildCraft",
    "tile.chuteBlock.name": "Жёлоб",
    "tile.constructionMarkerBlock.name": "Строительный маркер",
    "tile.engineCreative.name": "Творческий двигатель",
    "tile.engineCreative.tip": "Нажмите ПКМ гаечным ключом, чтобы изменить уровень выходной мощности.",
    "tile.engineWood.name": "Редстоуновый двигатель",
    "tile.fillerBlock.tip": "Заполняет или очищает отмеченные области с помощью выбираемых шаблонов",
    "tile.filteredBufferBlock.name": "Фильтрующий буфер",
    "tile.integrationTableBlock.tip": "Объединяет совместимые предметы по рецептам интеграции",
    "tile.libraryBlock.name": "Электронная библиотека",
    "tile.libraryBlock.tip": "Хранит чертежи и шаблоны и позволяет ими управлять",
    "tile.markerBlock.name": "Ориентир",
    "tile.pathMarkerBlock.name": "Маркер пути",
    "tile.programmingTableBlock.tip": "Программирует редстоуновые платы для роботов BuildCraft",
    "tile.pumpBlock.name": "Насос",
    "tile.refineryBlock.name": "Нефтеперерабатывающая установка",
    "tile.requester.name": "Запросчик",
    "tile.stampingTableBlock.name": "Штамповочный стол",
    "tile.tankBlock.name": "Резервуар",
    "tile.zonePlannerBlock.tip": "Создаёт и редактирует рабочие зоны для роботов BuildCraft",
    "tip.PipeFluidsClay": "Вставляющая труба",
    "tip.PipeItemsClay": "Вставляющая труба",
    "tip.PipePowerEmerald": "Изумрудная кинезисная труба",
    "tip.deprecated": "Устарело",
    "tip.shift.PipeItemsClay": "Отдаёт приоритет механизмам и сундукам\\nперед соседними трубами.",
    "tip.shift.PipeItemsDaizuli": "Shift + ПКМ — изменить цвет",
    "tip.shift.PipeItemsEmzuli": "Настройте фильтры профилей извлечения в интерфейсе\\nПрофиль может окрашивать извлечённые предметы\\nПереключайте профили извлечения с помощью гейтов",
    "tip.shift.PipeItemsLapis": "Shift + ПКМ — изменить цвет",
    "tip.shift.PipeItemsObsidian": "Подайте энергию от двигателя\\nБольше энергии — больше радиус действия",
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

    LANG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    json.loads(LANG.read_text(encoding="utf-8"))
    print(f"Applied {changed} reviewed legacy item/block fixes")


if __name__ == "__main__":
    main()
