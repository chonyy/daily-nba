from fsm import TocMachine


def create_machine():
    machine = TocMachine(
        states=["user", "testing", "searchplayer", "watchGame", "todayGame", "yesterGame", "showplayer", "lobby", "gameBoxscore", "showBoxscore",
                "searchteam", "showteam", "showstanding", "statleader", "showschedule", "showmeme", "shownews", "searchgame", "showsearchgame"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "lobby",
                "conditions": "is_going_to_lobby",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "testing",
                "conditions": "is_going_to_testing",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "searchplayer",
                "conditions": "is_going_to_searchplayer",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "watchGame",
                "conditions": "is_going_to_watchGame",
            },
            {
                "trigger": "advance",
                "source": "watchGame",
                "dest": "todayGame",
                "conditions": "is_going_to_todayGame",
            },
            {
                "trigger": "advance",
                "source": "watchGame",
                "dest": "yesterGame",
                "conditions": "is_going_to_yesterGame",
            },
            {
                "trigger": "advance",
                "source": "searchplayer",
                "dest": "showplayer",
                "conditions": "is_going_to_showplayer",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "gameBoxscore",
                "conditions": "is_going_to_gameBoxscore",
            },
            {
                "trigger": "advance",
                "source": "gameBoxscore",
                "dest": "showBoxscore",
                "conditions": "is_going_to_showBoxscore",
            },
            {
                "trigger": "advance",
                "source": ["todayGame", "yesterGame", "showsearchgame", "showBoxscore", "showstanding", "statleader", "showschedule", "shownews", "showmeme", "showplayer", "showteam"],
                "dest": "lobby",
                "conditions": "is_going_to_backLobby",
            },
            {
                "trigger": "advance",
                "source": ["todayGame", "yesterGame", "showsearchgame"],
                "dest": "gameBoxscore",
                "conditions": "is_going_to_boxfromgame",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "searchteam",
                "conditions": "is_going_to_searchteam",
            },
            {
                "trigger": "advance",
                "source": "searchteam",
                "dest": "showteam",
                "conditions": "is_going_to_showteam",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "showstanding",
                "conditions": "is_going_to_showstanding",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "statleader",
                "conditions": "is_going_to_statleader",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "showschedule",
                "conditions": "is_going_to_showschedule",
            },
            {
                "trigger": "advance",
                "source": "showBoxscore",
                "dest": "searchplayer",
                "conditions": "is_going_to_searchplayer",
            },
            {
                "trigger": "advance",
                "source": "showBoxscore",
                "dest": "searchteam",
                "conditions": "is_going_to_searchteam",
            },
            {
                "trigger": "advance",
                "source": "showstanding",
                "dest": "searchteam",
                "conditions": "is_going_to_searchteam",
            },
            {
                "trigger": "advance",
                "source": "statleader",
                "dest": "searchplayer",
                "conditions": "is_going_to_searchplayer",
            },
            {
                "trigger": "advance",
                "source": "showschedule",
                "dest": "searchteam",
                "conditions": "is_going_to_searchteam",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "showmeme",
                "conditions": "is_going_to_showmeme",
            },
            {
                "trigger": "advance",
                "source": "lobby",
                "dest": "shownews",
                "conditions": "is_going_to_shownews",
            },
            {
                "trigger": "advance",
                "source": "watchGame",
                "dest": "searchgame",
                "conditions": "is_going_to_searchgame",
            },
            {
                "trigger": "advance",
                "source": "searchgame",
                "dest": "showsearchgame",
                "conditions": "is_going_to_showsearchgame",
            },
            {
                "trigger": "advance",
                "source": "shownews",
                "dest": "showmeme",
                "conditions": "is_going_to_showsearchgame",
            },
            {
                "trigger": "advance",
                "source": "showmeme",
                "dest": "shownews",
                "conditions": "is_going_to_boxfromgame",
            },
            {
                "trigger": "advance",
                "source": "showplayer",
                "dest": "searchteam",
                "conditions": "is_going_to_searchteam",
            },
            {
                "trigger": "advance",
                "source": "showteam",
                "dest": "searchplayer",
                "conditions": "is_going_to_searchplayer",
            },
            {
                "trigger": "advance",
                "source": "showteam",
                "dest": "searchteam",
                "conditions": "is_going_to_searchteam",
            },
            {
                "trigger": "advance",
                "source": "showplayer",
                "dest": "searchplayer",
                "conditions": "is_going_to_searchplayer",
            },
            {"trigger": "go_back", "source": ["testing", "searchplayer", "showplayer", "watchGame", "todayGame", "yesterGame", "gameBoxscore", "showBoxscore",
                                              "showteam", "showstanding", "statleader", "showschedule", "showmeme", "shownews", "searchgame", "showsearchgame"], "dest": "lobby"},
            {"trigger": "go_searchplayer", "source": ["showplayer"], "dest": "searchplayer"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine
