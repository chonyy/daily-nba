<p align=center>
    <img src="img/features/menu.jpg" width="400" height="566.6">
</p>

<p align=center>
    <a target="_blank" href="https://travis-ci.com/chonyy/daily-nba" title="Build Status"><img src="https://travis-ci.com/chonyy/daily-nba.svg?branch=master"></a>
    <a target="_blank" href="#" title="top language"><img src="https://img.shields.io/github/languages/top/chonyy/daily-nba?color=orange"></a>
    <a target="_blank" href="https://img.shields.io/github/pipenv/locked/python-version/chonyy/daily-nba" title="Python version"><img src="https://img.shields.io/github/pipenv/locked/python-version/chonyy/daily-nba?color=green"></a>
    <a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
    <a target="_blank" href="#" title="repo size"><img src="https://img.shields.io/github/repo-size/chonyy/daily-nba"></a>
    <a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
</p>

> 🏀 The NBA LINE Bot with 9 features!

Watch NBA games, check the schedule, lookup the stats, search for players by using Daily-NBA. [Button carousel templates](https://developers.line.biz/en/reference/messaging-api/#buttons) are designed and implemented in every feature. Instead of directly typing the commands to the LINE bot, users can just simply **press buttons** on the carousel template to browse the features and access the NBA information!

There are four main componenets in this project

- **LINE Bot:** Built by the official [LINE Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/)
- **Web Scraping:** Use [BeutifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape several websites to retrieve NBA information
- **Backend:** Built the backend with [Flask](https://www.palletsprojects.com/p/flask/) to handle the webhook
- **FSM:** Create FSMs with [pytransitions](https://github.com/pytransitions/transitions) for the users state management

## FSM

<p align=center>
    <img src="img/fsm.png">
</p>

[**Finite State Machine**](https://en.wikipedia.org/wiki/Finite-state_machine) is implemented for the state management of the users. A FSM is maintained for each individual user. This way, every user has their own independent state, and the operations between two different users will not affect each other.

Finite state machine is a model in [Theory of Computation](https://en.wikipedia.org/wiki/Theory_of_computation). This model is implemented in Daily-NBA. Each feature is represented by a **state**, and the button that user pressed on the carousel template will trigger the **transitions** between states. The FSM graph is drawn by **GraphMachine** in [transitions.extensions](https://github.com/pytransitions/transitions).

## Features

### Watch Games
Checking out all the scores of the games on that day. (Today / Yesterday / Manually input date)
<p align=center>
    <img src="img/features/game1.jpg" width="240" height="340">
</p>
<p align=center>
    <img src="img/features/game2.jpg" width="240" height="340">
</p>

### Search Player
Searching for a specific player. (Manually input player name)
<p align=center>
    <img src="img/features/player1.jpg" width="240" height="340">
</p>
<p align=center>
    <img src="img/features/player2.jpg" width="240" height="340">
</p>
<p align=center>
    <img src="img/features/player3.jpg" width="240" height="340">
</p>

### Search Team
Searching for a specific team. (Manually input team name)
<p align=center>
    <img src="img/features/team1.jpg" width="240" height="340">
</p>
<p align=center>
    <img src="img/features/team2.jpg" width="240" height="340">
</p>

### Standings
Showing the team standing from both Eastern and Western conference.
<p align=center>
    <img src="img/features/standings.jpg" width="240" height="340">
</p>

### Game Schedule
Showing the game schedule tomorrow.
<p align=center>
    <img src="img/features/schedule.jpg" width="240" height="340">
</p>

### Stat Leader
Showing the stat leaders. (Most Points / Assist / Rebound / 3PM / Steal / Block)
<p align=center>
    <img src="img/features/statleader.jpg" width="240" height="340">
</p>

### Game Result
Checking out the box score of a specific game. (Manually input date and team)
<p align=center>
    <img src="img/features/result.jpg" width="240" height="340">
</p>

## Special Features

### NBA Meme
My favoritie feature! Brininging the best and newest NBA meme to you by pressing one button.
<p align=center>
    <img src="img/features/meme.jpg" width="240" height="340">
</p>

### NBA News
Bringing the hottest NBA news to you by pressing one button.
<p align=center>
    <img src="img/features/news.jpg" width="240" height="340">
</p>

## Play with it!
<p align=center>
    <img src="img/qrcode.png">
</p>

## Reference

All data comes from [basketball-reference.com](https://www.basketball-reference.com/).<br>
NBA memes come from [twitter@NBAMemes](https://twitter.com/NBAMemes).<br>
NBA news come from [realgm](https://basketball.realgm.com).<br>

## License

MIT © [chonyy](https://github.com/chonyy)


## Demo
<p align=center>
<img src="img/demo/1.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/2.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/3.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/4.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/5.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/6.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/7.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/8.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/9.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/10.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/11.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/12.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/13.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/14.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/15.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/16.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/17.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/18.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/19.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/20.jpg" width="384" height="682.4">
</p>
<p align=center>
<img src="img/demo/21.jpg" width="384" height="682.4">
</p>
