def movement():
    rooms = {
        "Dungeon Cell" : {
            "name" : "Dungeon Cell",
            "north" : "Dungeon Hallway"
        },
        "Dungeon Hallway" : {
            "name" : "Dungeon Hallway",
            "north" : "Staircase",
            "east" : "Armory",
            "south" : "Dungeon Cell"
        },
        "Armory" : {
            "name" : "Armory",
            "west" : "Dungeon Cell"
        },
        "Staircase" : {
            "name" : "Staircase",
            "south" : "Dungeon Hallway",
            "go up" : "Dungeon Mainfloor"
        },
        "Dungeon Mainfloor" : {
            "name" : "Dungeon Mainfloor",
            "exit" : "Exit Dungeon",
            "east" : "Dungeon Mainfloor Room 1",
            "west" : "Dungeon Mainfloor Room 2",
            "go down" : "Staircase"
        },
        "Exit Dungeon" : {
            "name" : "Exit Dungeon",
            "north" : "Sign",
            "enter" : "Dungeon Mainfloor",
        },
        "Dungeon Mainfloor Room 1" : {
            "name" : "Dungeon Mainfloor Room 1",
            "west" : "Dungeon Mainfloor"
        },
        "Dungeon Mainfloor Room 2" : {
            "name" : "Dungeon Mainfloor Room 2",
            "east" : "Dungeon Mainfloor"
        },
        "Sign" : {
            "name" : "Sign",
            "east" : "Forest",
            "south" : "Exit Dungeon",
            "west" : "Bandit Camp"
        },
        "Bandit Camp" : {
            "name" : "Bandit Camp",
            "north" : "Bandit House Entrance",
            "east" : "sign"
        },
        "Bandit House Entrance" : {
            "name" : "Bandit House Entrance",
            "enter" : "Bandit House Floor 1",
            "south" : "Bandit Camp"
        },
        "Bandit House Floor 1" : {
            "name" : "Bandit House Floor 1",
            "exit" : "Bandit House Entrance"
        },
        "Forest" : {
            "name" : "Forest",
            "east" : "Village",
            "west" : "Sign"
        },
        "Village" : {
            "name" : "Village",
            "north" : "Village Plaza",
            "west" : "Forest"
        },
        "Village Plaza" : {
            "name" : "Village Plaza",
            "north" : "Villager Quest",
            "east" : "Shop",
            "south" : "Village"
        },
        "Shop" : {
            "name" : "Shop",
            "west" : "Village Plaza"
        },
        "Villager Quest" : {
            "name" : "Villager Quest",
            "south" : "Village Plaza"
        }
    }
    current_room = rooms["Dungeon Cell"]