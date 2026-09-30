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

    # Legacy/common UI and guide terminology.
    "block.tankBlock": "Резервуар",
    "buildcraft.boardRobotClean": "Чистильщик",
    "buildcraft.boardRobotCrafter": "Создатель",
    "buildcraft.christmas.fluid.fuel_dense": "Тёмный шоколад",
    "buildcraft.christmas.fluid.fuel_mixed_heavy": "Тёмный шоколадный микс",
    "buildcraft.christmas.fluid.oil_dense": "Сырой тяжёлый шоколад",
    "buildcraft.christmas.fluid.oil_heavy": "Сырой шоколад",
    "buildcraft.guide.chapter.contents": "Оглавление",
    "buildcraft.guide.contents.all_group": "Прочее",
    "buildcraft.guide.group.from.buildcraft.full_power_providers": "Приёмники полной мощности",
    "buildcraft.guide.group.from.buildcraft.laser_power_providers": "Приёмники лазерной энергии",
    "buildcraft.guide.group.from.buildcraft.pipe_power_providers": "Приёмники энергии из труб",
    "buildcraft.guide.group.to.buildcraft.area_markers": "Маркеры области",
    "buildcraft.guide.group.to.buildcraft.full_power_providers": "Источники полной мощности",
    "buildcraft.guide.group.to.buildcraft.laser_power_providers": "Источники лазерной энергии",
    "buildcraft.guide.group.to.buildcraft.pipe_power_providers": "Источники энергии для труб",
    "buildcraft.guide.meta.group.linked_from": "Ссылки отсюда",
    "buildcraft.guide.meta.group.linking_to": "Ссылки сюда",
    "buildcraft.guide.recipe.use": "Использование",
    "buildcraft.guide.recipe.use.plural": "Использования",
    "buildcraft.guide.too_many_results": "Слишком много результатов для отображения: %s",
    "buildcraft.help.tank.generic": "Используйте вёдра или совместимые контейнеры для жидкостей, чтобы наполнить или опустошить резервуар.",
    "chat.buildcraft.quarry.chunkloadInfo": "[BuildCraft] Карьер на координатах %d %d %d будет поддерживать загрузку %d чанков",
    "chat.buildcraft.quarry.tooSmall": "[BuildCraft] Размер карьера выходит за границы принудительной загрузки чанков или слишком мал: %d %d (%d)",
    "chat.gateCopier.warning.actionParameters": "§6Предупреждение: у цели меньше параметров действия!",
    "chat.gateCopier.warning.load": "§6Предупреждение: некоторые триггеры или действия гейта могут отсутствовать!",
    "chat.gateCopier.warning.logic": "§6Предупреждение: у цели другой тип логики!",
    "chat.gateCopier.warning.slots": "§6Предупреждение: у цели меньше слотов!",
    "chat.gateCopier.warning.triggerParameters": "§6Предупреждение: у цели меньше параметров триггера!",
    "chat.pipe.power.iron.level.2560": "Полная пропускная способность",
    "chat.pipe.power.iron.level.320": "Выше среднего",
    "command.buildcraft.buildcraft.deop.help": "Снимает права оператора с FakePlayer BuildCraft (от его имени работают карьеры, роботы и другие механизмы).",
    "command.buildcraft.buildcraft.op.help": "Даёт права оператора FakePlayer BuildCraft (от его имени работают карьеры, роботы и другие механизмы).",
    "command.buildcraft.noperms": "У вас нет прав на выполнение этой команды.",
    "config.blueprints": "Чертежи",
    "config.builders.dropBrokenBlocks": "Выбрасывать разрушенные блоки",
    "config.display.hideFluidValues": "Скрывать количество жидкости",
    "config.display.hidePowerValues": "Скрывать количество энергии",
    "config.experimental": "Экспериментальное",
    "config.general.fuel.fuel.combustion": "Множитель расхода топлива ДВС",
    "config.general.fuel.fuel.combustion.energyOutput": "Выход энергии ДВС на топливе",
    "config.general.fuel.oil.combustion": "Множитель расхода нефти ДВС",
    "config.general.fuel.oil.combustion.energyOutput": "Выход энергии ДВС на нефти",
    "config.general.itemLifespan": "Время существования предметов (сек.)",
    "config.general.oilIsDense": "Плотная нефть",
    "config.general.pipes.facadeBlacklistAsWhitelist": "Инвертировать чёрный список фасадов",
    "config.general.quarry.oneTimeUse": "Одноразовое использование",
    "config.network": "Сеть",
    "config.power": "Энергопотребление",
    "config.power.chipsetCostMultiplier": "Множитель стоимости чипсетов",
    "config.power.gateCostMultiplier": "Множитель стоимости гейтов",
    "config.power.miningUsageMultiplier": "Множитель энергопотребления добычи",
    "config.worldgen": "Генерация мира",
    "config.worldgen.biomes.excessiveOilIDs": "Биомы, изобилующие нефтью",
    "config.worldgen.biomes.increasedOilIDs": "Биомы с повышенным содержанием нефти",
    "config.worldgen.oilWellGenerationRate": "Частота генерации нефтяных скважин",
    "config.worldgen.spawnOilSprings": "Генерировать нефтяные источники",
    "direction.center.0": "Северо-запад",
    "direction.center.6": "Юго-запад",
    "direction.center.8": "Юго-восток",
    "fillerpattern.box": "Коробка",
    "fluid.fuel_mixed_heavy": "Смешанное тяжёлое топливо",
    "fluid.fuel_mixed_light": "Смешанное лёгкое топливо",
    "fluid.oil_heavy": "Тяжёлая нефть",
    "gate.action.extraction": "Профиль извлечения: %s",
    "gate.action.pipe.power_limit": "Переключить лимит на %d MJ/т",
    "gate.material.nether_brick": "Незер-кирпичный",
    "gate.params": "Параметры слота: %s",
    "gate.params.action": "Параметры действия: %s",
    "gate.params.trigger": "Параметры триггера: %s",
    "gate.trigger.coolantLevelBelow": "Уровень охлаждающей жидкости ниже %d%%",
    "gate.trigger.engine.blue": "Двигатель: синий",
    "gate.trigger.engine.green": "Двигатель: зелёный",
    "gate.trigger.engine.red": "Двигатель: красный",
    "gate.trigger.engine.yellow": "Двигатель: жёлтый",
    "gate.trigger.pipe.tooMuchEnergy": "Перегрузка мощности",
    "gui.currentOutput": "Текущий выход",
    "gui.pipes.emzuli.title": "Профили извлечения",
    "item.Facade.state_hollow": "Полый",
    "item.FacadePhased": "Фазовый фасад",
    "item.FacadePhased.name": "Фазовый фасад",
    "item.FacadePhased.state_default": "По умолчанию: %s",
    "item.PipeItemsDaizuli": "Диазулитовая транспортная труба",
    "item.PipeItemsDaizuli.name": "Диазулитовая транспортная труба",
    "item.PipeItemsEmzuli": "Эмзулитовая транспортная труба",
    "item.PipeItemsEmzuli.name": "Эмзулитовая транспортная труба",
    "item.PipeItemsStripes.name": "Полосатая транспортная труба",
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
    json.loads(LANG.read_text(encoding="utf-8"))
    print(f"Applied {changed} reviewed ru_ru fixes")


if __name__ == "__main__":
    main()
