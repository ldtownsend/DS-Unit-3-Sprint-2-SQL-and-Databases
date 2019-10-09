import sqlite3
from tabulate import tabulate

def character_count():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    char_count = curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchone()
    print("Total Characters: ", char_count[0])

def character_count_sub_cleric():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    char_count_sub = curs.execute('SELECT COUNT(*) FROM charactercreator_cleric;').fetchone()
    print("Clerics: ", char_count_sub[0])

def character_count_sub_mage():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    char_count_sub = curs.execute('SELECT COUNT(*) FROM charactercreator_mage;').fetchone()
    print("Mages : ", char_count_sub[0])

def character_count_sub_thief():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    char_count_sub = curs.execute('SELECT COUNT(*) FROM charactercreator_thief;').fetchone()
    print("Thiefs: ", char_count_sub[0])

def character_count_sub_fighter():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    char_count_sub = curs.execute('SELECT COUNT(*) FROM charactercreator_fighter;').fetchone()
    print("Fighters: ", char_count_sub[0])

def total_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    item_count = curs.execute('SELECT COUNT(*) FROM armory_item;').fetchone()
    print("Total Items: ", item_count[0])

def weapon_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    weapon_count = curs.execute('SELECT COUNT(*) FROM armory_weapon;').fetchone()
    print("Total Weapons: ", weapon_count[0])

def non_weapon_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    item_count = curs.execute('SELECT COUNT(*) FROM armory_item;').fetchone()

    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    weapon_count = curs.execute('SELECT COUNT(*) FROM armory_weapon;').fetchone()

    non_weapon_count = item_count[0] - weapon_count[0]
    print("Non-weapon items: ", non_weapon_count)

def char_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    char_items = curs.execute('SELECT character_id, COUNT (*) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;').fetchall()
    print(tabulate(char_items, headers=['Character ID', 'Inventory Count']))

def char_weapons():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    char_weapons = curs.execute("""SELECT cc.character_id, cc.name,
                                COUNT()
                                FROM charactercreator_character AS cc
                                INNER JOIN charactercreator_character_inventory AS cci
                                ON cc.character_id = cci.character_id
                                INNER JOIN armory_item as ai
                                ON cci.item_id = ai.item_id
                                INNER JOIN armory_weapon AS aw
                                ON ai.item_id = aw.item_ptr_id
                                GROUP BY cc.character_id
                                LIMIT 20;
                                 """).fetchall()
    print(tabulate(char_weapons, headers=['ID', 'Character Name', 'Weapon Count']))

def avg_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    avg_items = curs.execute("""SELECT AVG(item_count) FROM
                                (
                                SELECT cc.character_id, COUNT(cci.item_id) AS item_count
                                FROM charactercreator_character AS cc
                                    LEFT JOIN charactercreator_character_inventory AS cci
                                    ON cc.character_id = cci.character_id
                                GROUP BY cc.character_id
                                );
                                 """).fetchone()
    print("Average Items per Character : ", avg_items[0])

def avg_weapons():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    avg_weapons = curs.execute("""SELECT AVG(weapon_count) FROM
                                  (
                                  SELECT cc.character_id, COUNT(aw.item_ptr_id) AS weapon_count
                                  FROM charactercreator_character AS cc
                                        INNER JOIN charactercreator_character_inventory as cci
                                        ON cc.character_id = cci.character_id
                                        INNER JOIN armory_item as ai
                                        ON cci.item_id = ai.item_id
                                        LEFT JOIN armory_weapon as aw
                                        ON ai.item_id = aw.item_ptr_id
                                  GROUP BY cc.character_id
                                  );""").fetchone()
    print("Average Weapons per Character : ", avg_weapons[0])

if __name__ == '__main__':
    character_count()
    character_count_sub_cleric()
    character_count_sub_mage()
    character_count_sub_thief()
    character_count_sub_fighter()
    total_items()
    weapon_items()
    non_weapon_items()
    char_items()
    char_weapons()
    avg_items()
    avg_weapons()
