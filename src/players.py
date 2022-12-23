from enum import Enum

class Players(Enum):
    ANDY_G = (1, 'Andy G.')
    ANDY_D = (2, 'Andy D.')
    CHARLES = (3, 'Charles')
    CHARLES_Z = (4, 'Charles Z.')
    FCY = (5, 'Fcy')
    HUDSON = (6, 'Hudson')
    LILY = (7, 'Lily')
    MARCO = (8, 'Marco')
    SEAN = (9, 'Sean')
    SJC = (10, 'Sjc')
    SKY = (11, 'Sky')
    THOMAS = (12, 'Thomas')
    TINNA = (13, 'Tinna')
    JASMINE = (14, 'Jasmine')
    YOCHEN = (15, 'YoChen')


PLAYER_COUNT = len(Players)

PLAYERS_DICT = {
    '5#': Players.JASMINE,
    'Andy G.': Players.ANDY_G,
    'Andy Jr.': Players.ANDY_G,
    'Andy Sr.': Players.ANDY_D,
    'Cat': Players.ANDY_D,
    'Charles': Players.CHARLES,
    'Charles Z.': Players.CHARLES_Z,
    'Duck': Players.SJC,
    'Fcy': Players.FCY,
    'Hudson': Players.HUDSON,
    'Jasmine': Players.JASMINE,
    'Lily': Players.LILY,
    'Marco': Players.MARCO,
    'Pig': Players.SEAN,
    'Sean': Players.SEAN,
    'Sjc': Players.SJC,
    'Sky': Players.SKY,
    'Thomas': Players.THOMAS,
    'Tinna': Players.TINNA,
    'YoChen': Players.YOCHEN}



