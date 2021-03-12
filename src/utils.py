import os
import bs4
import requests
import numpy as np
from bs4 import BeautifulSoup
from basketball_reference_web_scraper import client

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(id, img_url):
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(id, message)

    return "OK"


def send_video_url(id):
    message = ImageSendMessage(
        original_content_url='https://www.youtube.com/watch?v=bmBtgNZydk8',
        preview_image_url='https://cdn.nba.net/nba-drupal-prod/styles/landscape/s3/2018-08/leaguev3.jpeg?itok=j-c6KHL_'
    )
    line_bot_api.push_message(id, message)

    return "OK"


def send_template_message(id, imglinks):
    cols = []
    for i, url in enumerate(imglinks):
        cols.append(
            ImageCarouselColumn(
                image_url=url,
                action=URITemplateAction(
                    label='Meme',
                    uri=url
                )
            )
        )
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(id, message)
    return "OK"


def send_image_carousel(id, imglinks, labels, texts):
    cols = []
    for i, url in enumerate(imglinks):
        cols.append(
            ImageCarouselColumn(
                image_url=url,
                action=MessageTemplateAction(
                    label=labels[i],
                    text=texts[i]
                )
            )
        )
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(id, message)
    return "OK"


def send_button_message(id, img, title, uptext, labels, texts):

    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=img,
            title=title,
            text=uptext,
            actions=acts
        )
    )
    line_bot_api.push_message(id, message)
    return "OK"


def send_button_carousel(id):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cdn.nba.net/nba-drupal-prod/2019-09/SEO-image-NBA-logoman.jpg',
                    title='Daily NBA Menu 1',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label='Watch Game',
                            text='watch game'
                        ),
                        MessageTemplateAction(
                            label='Standings',
                            text='show standing'
                        ),
                        MessageTemplateAction(
                            label='Game Schedule',
                            text='show schedule'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cdn.nba.net/nba-drupal-prod/2019-09/SEO-image-NBA-logoman.jpg',
                    title='Daily NBA Menu 2',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label='Stat Leader',
                            text='stat leader'
                        ),
                        MessageTemplateAction(
                            label='Game Result',
                            text='game box score'
                        ),
                        MessageTemplateAction(
                            label='Search Player',
                            text='search player'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cdn.nba.net/nba-drupal-prod/2019-09/SEO-image-NBA-logoman.jpg',
                    title='Daily NBA Menu 3',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label='Search Team',
                            text='search team'
                        ),
                        MessageTemplateAction(
                            label='NBA News',
                            text='show news'
                        ),
                        URITemplateAction(
                            label='Creator',
                            uri='https://www.linkedin.com/in/chonyy/'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"


def send_news_carousel(id, imglinks, titles, links):

    cols = []
    for i, img in enumerate(imglinks):
        cols.append(
            CarouselColumn(
                thumbnail_image_url=img,
                title='NBA news',
                text=titles[i],
                actions=[
                    URITemplateAction(
                        label='Read more',
                        uri=links[i]
                    )
                ]
            )
        )

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(columns=cols)
    )

    line_bot_api.push_message(id, message)

    return "OK"


def showGames(reply_token):
    url = 'https://www.basketball-reference.com/boxscores/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    games = soup.find_all('div', class_="game_summary expanded nohover")

    result = ""
    date = soup.find('span', class_="button2 index").text
    result += ("\U0001f4c5 {} \n\n" .format(date))

    for game in games:
        winteamname = ""
        winteam = game.find('tr', class_="winner").text
        winteamlist = winteam.partition('\n')[2].split()
        if winteamlist[len(winteamlist)-1] == 'Final':
            winteamlist.remove('Final')
        for s in winteamlist:
            if(not s.isdigit()):
                winteamname += s
                winteamname += ' '
            else:
                winpoint = s

        loseteamname = ""
        loseteam = game.find('tr', class_="loser").text
        loseteamlist = loseteam.partition('\n')[2].split()
        if loseteamlist[len(loseteamlist)-1] == 'Final':
            loseteamlist.remove('Final')
        for s in loseteamlist:
            if(not s.isdigit()):
                loseteamname += s
                loseteamname += ' '
            else:
                losepoint = s

        result += ("\U0001f3c6 {} \U0001f3c0{}\n" .format(winteamname, winpoint))
        result += ("\U0001f625 {} \U0001f3c0{}\n\n" .format(loseteamname, losepoint))

    print(result)
    send_text_message(reply_token, result)


def yesterGames(reply_token):
    url = 'https://www.basketball-reference.com/boxscores/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    prev = soup.find('a', class_="button2 prev", href=True)
    prevDate = prev['href'][11:]
    url += prevDate

    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    games = soup.find_all('div', class_="game_summary expanded nohover")

    result = ""
    date = soup.find('span', class_="button2 index").text
    result += ("\U0001f4c5 {} \n\n" .format(date))

    for game in games:
        winteamname = ""
        winteam = game.find('tr', class_="winner").text
        winteamlist = winteam.partition('\n')[2].split()
        if winteamlist[len(winteamlist)-1] == 'Final':
            winteamlist.remove('Final')
        for s in winteamlist:
            if(not s.isdigit()):
                winteamname += s
                winteamname += ' '
            else:
                winpoint = s

        loseteamname = ""
        loseteam = game.find('tr', class_="loser").text
        loseteamlist = loseteam.partition('\n')[2].split()
        if loseteamlist[len(loseteamlist)-1] == 'Final':
            loseteamlist.remove('Final')
        for s in loseteamlist:
            if(not s.isdigit()):
                loseteamname += s
                loseteamname += ' '
            else:
                losepoint = s

        result += ("\U0001f3c6 {} \U0001f3c0{}\n" .format(winteamname, winpoint))
        result += ("\U0001f625 {} \U0001f3c0{}\n\n" .format(loseteamname, losepoint))

    # print(result)
    send_text_message(reply_token, result)


def score(player):
    return player['made_three_point_field_goals'] * 3 + (player['made_field_goals'] - player['made_three_point_field_goals']) * 2 + player['made_free_throws']


def getTeam(team):
    teamforscrape = ""
    for idx, s in enumerate(team):
        teamforscrape += s.upper()
        if(idx != len(team) - 1):
            teamforscrape += '_'
    return teamforscrape


def scrapeBoxscore(userid, dateteam):
    month = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }

    datelist = dateteam.split(' ')
    datelist[1] = datelist[1][:1]

    gameMonth = month[datelist[0]]
    gameDay = int(datelist[1])
    gameYear = int(datelist[2])
    searchTeam = getTeam(datelist[3:])

    opponentTeam = ""
    result = ""

    players = client.player_box_scores(day=gameDay, month=gameMonth, year=gameYear)

    for player in players:
        if(player['team'].name == searchTeam):
            opponentTeam = player['opponent'].name
            break

    result += ("\U0001f3c0\U0001f3c0\U0001f3c0 {}\n\n" .format(searchTeam))
    for player in players:
        if(player['team'].name == searchTeam):
            result += ("\U0001F525\U000026f9\U0001F525 {} {}:{}\n" .format(player['name'], int(player['seconds_played'] / 60), player['seconds_played'] % 60))
            result += ("{} PTS, {} AST, {} REB, {} STL, {} BLK, {} TOV\n\n" .format(score(player),
                                                                                    player['assists'], player['offensive_rebounds'] + player['defensive_rebounds'], player['steals'], player['blocks'], player['turnovers']))

    result += ("\U0001f3c0\U0001f3c0\U0001f3c0 {}\n\n" .format(opponentTeam))
    for player in players:
        if(player['team'].name == opponentTeam):
            result += ("\U0001F525\U000026f9\U0001F525 {} {}:{}\n" .format(player['name'], int(player['seconds_played'] / 60), player['seconds_played'] % 60))
            result += ("{} PTS, {} AST, {} REB, {} STL, {} BLK, {} TOV\n\n" .format(score(player),
                                                                                    player['assists'], player['offensive_rebounds'] + player['defensive_rebounds'], player['steals'], player['blocks'], player['turnovers']))

    push_message(userid, result)


def get(data):
    temp = ""
    datalist = data.text.split()
    for n in datalist:
        temp += ('{} ' .format(n))
    temp += '\n'
    return temp


def searchplayer(reply_token, userid, playertofind):
    nickname = 0
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    rows = soup.find_all('td', class_="left")

    for row in rows:
        if(row['data-stat'] == 'player'):
            if(row.text == playertofind):
                # print(row.text)
                link = row.find('a')['href']
                playerlink = urlhead + link
                # print(playerlink)
                break

    source = requests.get(playerlink, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    photos = soup.find_all('img')
    imglink = photos[1]['src']
    send_image_url(reply_token, imglink)

    bio = soup.find('div', {"id": "meta"})
    ps = bio.find_all('p')

    result = '\U0001F4DC\U0001F4DC\U0001F4DC\n'
    if(ps[0].text[:13] == 'Pronunciation'):
        result += get(ps[0])
        result += "FullName: "
        result += get(ps[1])
        if(ps[2].text[1] == '('):
            nickname = 1
        if nickname:
            result += ("Nickname: {}\n" .format(ps[2].text[2:-2]))
            result += get(ps[3])
            result += ('Height and Weight: {}' .format(get(ps[4])))
            for p in ps[5:]:
                result += get(p)
        else:
            result += get(ps[2])
            result += ('Height and Weight: {}' .format(get(ps[3])))
            for p in ps[4:]:
                result += get(p)
    else:
        result += "FullName: "
        result += get(ps[0])
        if(ps[1].text[1] == '('):
            nickname = 1
        if nickname:
            result += ("Nickname: {}\n" .format(ps[1].text[2:-2]))
            result += get(ps[2])
            result += ('Height and Weight: {}' .format(get(ps[3])))
            for p in ps[4:]:
                result += get(p)
        else:
            result += get(ps[1])
            result += ('Height and Weight: {}' .format(get(ps[2])))
            for p in ps[3:]:
                result += get(p)

    push_message(userid, result)

    stat = soup.find('div', class_='stats_pullout')
    ps = stat.find_all('p')

    curStat = ""
    carStat = ""

    curStat += ('\U0001F525\U0001F525\U0001F525 {}\n' .format(ps[0].text))
    curStat += ('Games Played: {}\n' .format(ps[2].text))
    curStat += ('Average Per Game: {} PTS, {} AST, {} REB\n' .format(ps[4].text, ps[8].text, ps[6].text))
    curStat += ('Accuracy: {} FG%, {} FG3%, {} FT%, {} eFG%\n' .format(ps[10].text, ps[12].text, ps[14].text, ps[16].text))
    push_message(userid, curStat)

    carStat += ('\U0001F474\U0001F474\U0001F474 {}\n' .format(ps[1].text))
    carStat += ('Games Played: {}\n' .format(ps[3].text))
    carStat += ('Average Per Game: {} PTS, {} AST, {} REB\n' .format(ps[5].text, ps[9].text, ps[7].text))
    carStat += ('Accuracy: {} FG%, {} FG3%, {} FT%, {} eFG%\n' .format(ps[11].text, ps[13].text, ps[15].text, ps[17].text))
    push_message(userid, carStat)


def searchteam(reply_token, userid, teamtofind):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.basketball-reference.com/teams/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    table = soup.find('tbody')
    rows = table.find_all('tr', class_="full_table")

    for row in rows:
        rowdata = row.find('a')
        if(rowdata.text == teamtofind):
            teamlink = urlhead + rowdata['href']
            print(teamlink)
            break

    source = requests.get(teamlink, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    table = soup.find('tbody')
    links = table.find_all('a')
    teamlink = urlhead + links[0]['href']

    source = requests.get(teamlink, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    logolink = soup.find('img', class_='teamlogo')['src']
    send_image_url(reply_token, logolink)

    template = soup.find('div', {'data-template': "Partials/Teams/Summary"})
    ps = template.find_all('p')
    result = "\U000026F9\U000026F9\U000026F9\U000026F9\U000026F9\n"
    for p in ps:
        result += get(p)

    push_message(userid, result)


def showstanding(userid):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.basketball-reference.com/leagues/NBA_2021_standings.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    east = soup.find('table', {'id': 'confs_standings_E'})
    table = east.find('tbody')
    rows = table.find_all('tr')

    resultE = '\U0001F3C3\U0001F3C3\U0001F3C3 Eastern Conference\n\n'
    for idx, row in enumerate(rows):
        name = row.find('th').text
        if(idx == 0):
            resultE += ("\U0001F3C6 {}\n" .format(name))
        elif(idx == 1):
            resultE += ("\U0001F948 {}\n" .format(name))
        elif(idx == 2):
            resultE += ("\U0001F949 {}\n" .format(name))
        elif(idx > 2 and idx < 8):
            resultE += ("\U0001f3c5 {}\n" .format(name))
        else:
            resultE += ("\U0001f480 {}\n" .format(name))
        datas = row.find_all('td')
        resultE += ("{} W, {} L, {} W/L%, {} GB, {} PS/G, {} PA/G\n" .format(datas[0].text, datas[1].text, datas[2].text, datas[3].text, datas[4].text, datas[5].text))
    push_message(userid, resultE)

    west = soup.find('table', {'id': 'confs_standings_W'})
    table = west.find('tbody')
    rows = table.find_all('tr')
    resultW = '\U0001F3C3\U0001F3C3\U0001F3C3 Western Conference\n\n'
    for idx, row in enumerate(rows):
        name = row.find('th').text
        if(idx == 0):
            resultW += ("\U0001F3C6 {}\n" .format(name))
        elif(idx == 1):
            resultW += ("\U0001F948 {}\n" .format(name))
        elif(idx == 2):
            resultW += ("\U0001F949 {}\n" .format(name))
        elif(idx > 2 and idx < 8):
            resultW += ("\U0001f3c5 {}\n" .format(name))
        else:
            resultW += ("\U0001f480 {}\n" .format(name))
        datas = row.find_all('td')
        resultW += ("{} W, {} L, {} W/L%, {} GB, {} PS/G, {} PA/G\n" .format(datas[0].text, datas[1].text, datas[2].text, datas[3].text, datas[4].text, datas[5].text))
    push_message(userid, resultW)


def statleader(userid):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.espn.com/nba/stats'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    result = ""
    boxes = soup.find_all('tbody', class_='Table__TBODY')

    for idx, box in enumerate(boxes[:6]):
        name = box.find('a').text
        performs = box.find_all('td', class_="Table__TD")
        perform = performs[1].text
        if(idx == 0):
            result += ("\U0001F525\U0001F525\U0001F525 得分王 {}  {} PTS\n" .format(name, perform))
        if(idx == 1):
            result += ("\U0001F91d\U0001F91d\U0001F91d 助攻王 {}  {} AST\n" .format(name, perform))
        if(idx == 2):
            result += ("\U0001F44c\U0001F44c\U0001F44c 三分王 {}  {} 3PM\n" .format(name, perform))
        if(idx == 3):
            result += ("\U0001F64c\U0001F64c\U0001F64c 籃板王 {}  {} REB\n" .format(name, perform))
        if(idx == 4):
            result += ("\U0000270b\U0000270b\U0000270b 阻功王 {}  {} BLK\n" .format(name, perform))
        if(idx == 5):
            result += ("\U0001F3c3\U0001F3c3\U0001F3c3 抄截王 {}  {} STL\n" .format(name, perform))

    push_message(userid, result)


def showschedule(userid):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.msn.com/zh-tw/sports/nba/schedule'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    result = "\U0001F5D3 "

    date = soup.find('th')
    result += ('{}\n\n' .format(date.text))

    tables = soup.find_all('tbody')
    table = tables[0]
    rows = table.find_all('tr')
    for row in rows:
        rowlist = row.text.split()
        result += ("\U0000231A {} {}\n" .format(rowlist[0], rowlist[1]))
        result += ("{}{} vs {}{}\n" .format(rowlist[6], rowlist[7], rowlist[11], rowlist[12]))

    push_message(userid, result)


def showmeme(userid):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://twitter.com/NBAMemes?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    imgs = soup.find_all('img', {"style": "width: 100%; top: -0px;"})
    # print(len(imgs))
    # for img in imgs:
    #     print(img['src'])

    imglink = []
    x = np.random.randint(0, 3, size=40)

    print(len(imgs))

    rand = []
    for i in x:
        if(i not in rand):
            rand.append(i)
        if(len(rand) == 3):
            break

    for i in range(3):
        imglink.append(imgs[rand[i]]['src'])

    send_template_message(userid, imglink)


def shownews(userid):
    urlhead = 'https://basketball.realgm.com'
    url = 'https://basketball.realgm.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    imglinks = []
    titles = []
    links = []

    news = soup.find_all('div', class_='secondary-story')
    for new in news[:5]:
        img = new.find('a', class_='article-image')
        title = new.find('div', class_='article-title').text[:59]
        imglink = img['style'][23:-3]
        link = urlhead + img['href']
        imglinks.append(imglink)
        titles.append(title)
        links.append(link)
    send_news_carousel(userid, imglinks, titles, links)


def searchgame(reply_token, date):
    month = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }

    datelist = date.split(' ')
    datelist[1] = datelist[1][:1]

    gameMonth = month[datelist[0]]
    gameDay = int(datelist[1])
    gameYear = int(datelist[2])

    url = ('https://www.basketball-reference.com/boxscores/?month={}&day={}&year={}' .format(gameMonth, gameDay, gameYear))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    games = soup.find_all('div', class_="game_summary expanded nohover")

    result = ""
    date = soup.find('span', class_="button2 index").text
    result += ("\U0001f4c5 {} \n\n" .format(date))

    for game in games:
        winteamname = ""
        winteam = game.find('tr', class_="winner").text
        winteamlist = winteam.partition('\n')[2].split()
        if winteamlist[len(winteamlist)-1] == 'Final':
            winteamlist.remove('Final')
        for s in winteamlist:
            if(not s.isdigit()):
                winteamname += s
                winteamname += ' '
            else:
                winpoint = s

        loseteamname = ""
        loseteam = game.find('tr', class_="loser").text
        loseteamlist = loseteam.partition('\n')[2].split()
        if loseteamlist[len(loseteamlist)-1] == 'Final':
            loseteamlist.remove('Final')
        for s in loseteamlist:
            if(not s.isdigit()):
                loseteamname += s
                loseteamname += ' '
            else:
                losepoint = s

        result += ("\U0001f3c6 {} \U0001f3c0{}\n" .format(winteamname, winpoint))
        result += ("\U0001f625 {} \U0001f3c0{}\n\n" .format(loseteamname, losepoint))

    # print(result)
    send_text_message(reply_token, result)


def push_message(userid, msg):
    line_bot_api.push_message(userid, TextSendMessage(text=msg))
    return "OK"
