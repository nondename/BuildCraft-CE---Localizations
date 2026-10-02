#!/usr/bin/env python3
import json
from pathlib import Path
import sys

LANG = Path('src/main/resources/assets/buildcraft/lang/ru_ru.json')
GUIDE = Path('src/main/resources/assets/buildcraft/guide/text/ru_ru.json')

LANG_FIXES = {
    'block.engineWood': ('Деревянный двигатель', 'Редстоуновый двигатель'),
    'block.engineStone': ('Каменный двигатель', 'Двигатель Стирлинга'),
    'block.engineIron': ('Железный двигатель', 'Двигатель внутреннего сгорания'),
    'gate.trigger.light.dark': ('Темно', 'Тёмно'),
    'gui.leftToBreak': ('Сломать', 'Осталось сломать'),
    'gui.leftToPlace': ('Поставить', 'Осталось поставить'),
    'item.buildcraftcore.volume_box': ('Короб области', 'Объёмная рамка'),
    'tip.PipePowerDiamond': ('Труба с регулируемой пропускной мощностью', 'Труба с регулируемой пропускной способностью'),
    'tip.PipePowerIron': ('Труба с регулируемой пропускной мощностью', 'Труба с регулируемой пропускной способностью'),
}

LANG_SUBSTRING_FIXES = {
    'buildcraftrobotics.help.zone_planner.map.desc': [
        ('Зажми ЛКМ и протяни мышь', 'Зажмите ЛКМ и протяните мышь'),
    ],
    'buildcraftrobotics.help.zone_planner.fullscreen.desc': [
        ('Нажми M или Esc', 'Нажмите M или Esc'),
    ],
}

GUIDE_GLOBAL_REPLACEMENTS = [
    ('Красную плату', 'Редстоуновую плату'),
    ('красную плату', 'редстоуновую плату'),
    ('Красная плата', 'Редстоуновая плата'),
    ('красная плата', 'редстоуновая плата'),
    ('красной плате', 'редстоуновой плате'),
    ('архитекторском столе', 'столе архитектора'),
    ('архитекторского стола', 'стола архитектора'),
    ('архитекторский стол', 'стол архитектора'),
]

GUIDE_PAGE_REPLACEMENTS = {
    'buildcraftcore/item/map_location': [
        ('Карта местности записывает точку, область, путь или зону Robotics.', 'Карта местоположения записывает точку, область, путь или рабочую зону роботов.'),
    ],
    'buildcraftcore/block/engine_creative': [
        ('творческий источник легко скрывает слабое место сети или перегрузить испытательную установку', 'творческий источник легко может скрыть слабое место сети или перегрузить испытательную установку'),
    ],
    'buildcraftbuilders/block/builder': [
        ('Вставьте использованный Blueprint или Template в слот снимка.', 'Вставьте заполненный чертёж или шаблон в слот снимка.'),
        ('Blueprint требует именно записанные в нём блоки. Template воспроизводит сохранённую форму подходящими блоками из доступных ресурсов.', 'Чертёж требует именно записанные в нём блоки. Шаблон воспроизводит сохранённую форму подходящими блоками из доступных ресурсов.'),
        ('относительно направления Builder', 'относительно направления строителя'),
        ('маршрут Path Marks, Builder может', 'маршрут путевых маркеров, строитель может'),
    ],
    'buildcraftbuilders/block/filler': [
        ('Поставьте Filler рядом с Land Marks или Volume Box', 'Поставьте заполнитель рядом с ориентирами или объёмной рамкой'),
        ('шаблоны clear, fill, box, frame, horizon, flatten, cylinder, pyramid и stairs', 'шаблоны очистки, заполнения, коробки, каркаса, горизонта, выравнивания, цилиндра, пирамиды и лестницы'),
        ('направлением, поворотом, facing, осью, центром', 'направлением, поворотом, ориентацией, осью, центром'),
    ],
    'buildcraftfactory/block/mining_well': [
        ('Mining Well ищет строго вниз от своей позиции', 'Буровая скважина работает строго вниз от своей позиции'),
    ],
    'buildcraftbuilders/block/quarry': [
        ('Поставьте Quarry рядом с соединёнными Land Marks', 'Поставьте карьер рядом с соединёнными ориентирами'),
        ('Quarry может запрашивать chunk tickets', 'Карьер может запрашивать тикеты загрузки чанков'),
        ('ограничить tickets', 'ограничить тикеты загрузки чанков'),
        ('удалённая Quarry', 'удалённый карьер'),
        ('Сначала Quarry сканирует область', 'Сначала карьер сканирует область'),
        ('владельца Quarry', 'владельца карьера'),
    ],
    'buildcraftrobotics/item/robot': [
        ('Установите Docking Station на трубу и примените к ней запрограммированного Robot.', 'Установите станцию роботов на трубу и примените к ней запрограммированного робота.'),
        ('Действия Gate на Docking Station управляют', 'Действия гейтов на станции роботов управляют'),
    ],
    'buildcraftlib/config/registry_overview': [
        ('независимый от языка manifest Guide Book', 'независимый от языка манифест руководства'),
        ('Manifest не содержит переводимого текста.', 'Манифест не содержит переводимого текста.'),
        ('Каждый ключ страницы из manifest', 'Каждый ключ страницы из манифеста'),
        ('statement и требуемый мод', 'логическое выражение и требуемый мод'),
        ('если настроен fallback', 'если настроено резервное наследование перевода'),
    ],
    'buildcraftlib/config/json_insn_format': [
        ('используйте упакованные manifest и языковые ресурсы', 'используйте упакованные манифесты и языковые ресурсы'),
    ],
    'buildcraftlib/config/guide_page_format': [
        ('настройки Lore и Hints', 'настройки «Лор» и «Подсказки»'),
        ('Fallback и алиасы', 'Резервный перевод и алиасы'),
        ('цепочки fallback', 'цепочки резервного перевода'),
        ('ссылки на предмет или statement', 'ссылки на предмет или логическое выражение'),
    ],
}

FORBIDDEN = [
    'Blueprint', 'Template', 'Filler', 'Land Marks', 'Volume Box', 'Path Marks',
    'Mining Well', 'chunk tickets', 'Docking Station', 'programmed Robot', 'Actions Gate',
]

def load(path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def save(path, data, compact=False):
    with path.open('w', encoding='utf-8', newline='\n') as f:
        if compact:
            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
        else:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

def replace(text, pairs, changes, label):
    out = text
    for old, new in pairs:
        if old in out:
            out = out.replace(old, new)
            changes.append(f'{label}: {old!r} -> {new!r}')
    return out

def main():
    if not LANG.is_file() or not GUIDE.is_file():
        print('Target localization files are missing', file=sys.stderr)
        return 2

    lang = load(LANG)
    guide = load(GUIDE)
    pages = guide.get('pages')
    if not isinstance(pages, dict):
        print('Guide pages object is missing', file=sys.stderr)
        return 3

    changes = []
    warnings = []

    for key, (old, new) in LANG_FIXES.items():
        current = lang.get(key)
        if current == old:
            lang[key] = new
            changes.append(f'lang {key}')
        elif current == new:
            pass
        else:
            warnings.append(f'lang {key}: expected {old!r}, found {current!r}')

    for key, pairs in LANG_SUBSTRING_FIXES.items():
        current = lang.get(key)
        if not isinstance(current, str):
            warnings.append(f'lang {key}: missing/non-string')
        else:
            lang[key] = replace(current, pairs, changes, f'lang {key}')

    for page, values in pages.items():
        if isinstance(values, list):
            for i, value in enumerate(values):
                if isinstance(value, str):
                    values[i] = replace(value, GUIDE_GLOBAL_REPLACEMENTS, changes, f'guide {page}[{i}]')

    for page, pairs in GUIDE_PAGE_REPLACEMENTS.items():
        values = pages.get(page)
        if not isinstance(values, list):
            warnings.append(f'guide page missing: {page}')
            continue
        for i, value in enumerate(values):
            if isinstance(value, str):
                values[i] = replace(value, pairs, changes, f'guide {page}[{i}]')

    leftovers = []
    for page, values in pages.items():
        if not isinstance(values, list):
            continue
        for i, value in enumerate(values):
            if not isinstance(value, str):
                continue
            for token in FORBIDDEN:
                if token in value:
                    leftovers.append(f'{page}[{i}]: {token}')

    if warnings:
        print('Unexpected source state:', file=sys.stderr)
        for item in warnings:
            print('  WARN', item, file=sys.stderr)
        return 4
    if leftovers:
        print('English gameplay leftovers remain:', file=sys.stderr)
        for item in leftovers:
            print('  LEFT', item, file=sys.stderr)
        return 5

    save(LANG, lang, compact=False)
    save(GUIDE, guide, compact=True)
    load(LANG)
    load(GUIDE)

    print(f'Applied {len(changes)} localization fixes')
    for item in changes:
        print('  FIX', item)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
