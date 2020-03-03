import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# from transitions.extensions import GraphMachine
from fsm import TocMachine
from utils import send_text_message, send_image_url

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

machine = {}

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if event.source.user_id not in machine:
            machine[event.source.user_id] = TocMachine(
                states=["user", "testing", "searchplayer", "watchGame", "todayGame", "yesterGame", "showplayer", "lobby", "gameBoxscore", "showBoxscore", "searchteam", "showteam", "showstanding", "statleader", "showschedule", "showmeme", "shownews", "searchgame", "showsearchgame"],
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
                    {"trigger": "go_back", "source": ["testing", "searchplayer", "showplayer", "watchGame", "todayGame", "yesterGame", "gameBoxscore", "showBoxscore", "showteam", "showstanding", "statleader", "showschedule", "showmeme", "shownews", "searchgame", "showsearchgame"], "dest": "lobby"},
                    {"trigger": "go_searchplayer", "source": ["showplayer"], "dest": "searchplayer"},
                ],
                initial="user",
                auto_transitions=False,
                show_conditions=True,
                )

        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        # print(f"\nFSM STATE: {machine.state}")
        # print(f"REQUEST BODY: \n{body}")

        response = machine[event.source.user_id].advance(event)
        if response == False:
            send_text_message(event.reply_token, "Invalid command, try again")

    return "OK"


# @app.route("/show-fsm", methods=["GET"])
# def show_fsm():
#     machine.get_graph().draw("fsm.png", prog="dot", format="png")
#     return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    # machine.get_graph().draw("fsm.png", prog="dot", format="png")
    # send_file("fsm.png", mimetype="image/png")
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port)
