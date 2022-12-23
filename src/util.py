from src.players import *

def verify_player_name(name_str):
    assert type(name_str) == str
    slash = name_str.find('/')
    if slash != -1:
        return name_str[:slash] in PLAYERS_DICT and verify_player_name(name_str[slash+1:])
    return name_str in PLAYERS_DICT

def convert_name_to_player(name_str):
    assert type(name_str) == str
    slash = name_str.find('/')
    if slash != -1:
        assert name_str[:slash] in PLAYERS_DICT
        return [PLAYERS_DICT[name_str[:slash]]] + convert_name_to_player(name_str[slash + 1:])
    else:
        assert name_str in PLAYERS_DICT
        return [PLAYERS_DICT[name_str]]