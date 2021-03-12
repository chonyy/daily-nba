from transitions.extensions import GraphMachine
from utils import send_image_carousel, send_button_message, send_button_carousel, showGames, yesterGames, push_message, scrapeBoxscore, searchplayer, searchteam, showstanding, statleader, showschedule, showmeme, shownews, searchgame


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_lobby(self, event):
        text = event.message.text
        return True

    def is_going_to_testing(self, event):
        text = event.message.text
        return text.lower() == "testing"

    def is_going_to_searchplayer(self, event):
        text = event.message.text
        return text.lower() == "search player"

    def is_going_to_watchGame(self, event):
        text = event.message.text
        return text.lower() == "watch game"

    def is_going_to_todayGame(self, event):
        text = event.message.text
        return text.lower() == "today game"

    def is_going_to_yesterGame(self, event):
        text = event.message.text
        return text.lower() == "yesterday game"

    def is_going_to_searchgame(self, event):
        text = event.message.text
        return text.lower() == "search game"

    def is_going_to_showsearchgame(self, event):
        text = event.message.text
        return True

    def is_going_to_showplayer(self, event):
        return True

    def is_going_to_showstanding(self, event):
        text = event.message.text
        return text.lower() == "show standing"

    def is_going_to_gameBoxscore(self, event):
        text = event.message.text
        return text.lower() == "game box score"

    def is_going_to_showBoxscore(self, event):
        return True

    def is_going_to_backLobby(self, event):
        text = event.message.text
        return text.lower() == "no"

    def is_going_to_boxfromgame(self, event):
        text = event.message.text
        return text.lower() == "yes"

    def is_going_to_searchteam(self, event):
        text = event.message.text
        return text.lower() == "search team"

    def is_going_to_showteam(self, event):
        return True

    def is_going_to_statleader(self, event):
        text = event.message.text
        return text.lower() == "stat leader"

    def is_going_to_showschedule(self, event):
        text = event.message.text
        return text.lower() == "show schedule"

    def is_going_to_showmeme(self, event):
        text = event.message.text
        return text.lower() == "show meme"

    def is_going_to_shownews(self, event):
        text = event.message.text
        return text.lower() == "show news"

    def on_enter_lobby(self, event):
        userid = event.source.user_id
        send_button_carousel(userid)

    def on_enter_testing(self, event):
        print("I'm entering testing")
        # reply_token = event.reply_token
        userid = event.source.user_id

        url1 = 'https://pbs.twimg.com/media/ELFOUvGVAAA3-Tx.jpg'
        title = 'title'
        uptext = 'uptext'
        labels = ['yes', 'no']
        texts = ['yes', 'no']
        send_button_message(userid, url1, title, uptext, labels, texts)
        # send_news_carousel(userid, urls, labels, urls)
        # send_image_map(userid)
        self.go_back(event)

    def on_enter_searchplayer(self, event):
        print("I'm entering searchplayer")
        reply_token = event.reply_token
        userid = event.source.user_id

        lbj = 'https://cdn.nba.com/headshots/nba/latest/1040x760/2544.png'
        luka = 'https://www.talkbasket.net/wp-content/uploads/2019/11/THUMBNAIL_043-3.webp'
        freak = 'https://scd.infomigrants.net/media/resize/my_image_medium/4c1a91cf3cd1e4ec2f373a7e520e84b118a0f638.jpeg'
        harden = 'https://sportshub.cbsistatic.com/i/r/2019/10/07/3db9fcb5-5c81-46e1-ae16-fbb0f75b7e99/thumbnail/770x433/a0dfdaa544a8a4899f58aaada49772fd/james-harden.jpg'
        ad = 'https://specials-images.forbesimg.com/imageserve/1189030491/960x0.jpg?fit=scale'
        urls = [lbj, luka, freak, harden, ad]
        labels = ['LeBron James', 'Luka Doncic', 'Giannis', 'James Harden', 'A.D.']
        texts = ['LeBron James', 'Luka Dončić', 'Giannis Antetokounmpo', 'James Harden', 'Anthony Davis']
        send_image_carousel(userid, urls, labels, texts)

        msg = "Press on the \"GOATS\" above or enter a player name"
        push_message(userid, msg)

    def on_enter_watchGame(self, event):
        print("I'm entering watchGame")

        reply_token = event.reply_token
        userid = event.source.user_id

        img = 'https://images-na.ssl-images-amazon.com/images/I/61G5S99JAAL.jpg'
        title = 'Watch game scores'
        uptext = 'Which day would you like to watch?'
        labels = ['Game today', 'Game yesterday', 'Enter a date']
        texts = ['today game', 'yesterday game', 'search game']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_todayGame(self, event):
        print("I'm entering todayGame")
        reply_token = event.reply_token
        userid = event.source.user_id
        showGames(reply_token)

        img = 'https://img.bleacherreport.net/img/images/photos/002/780/942/4e99edcf959c5743a660a70c378fbc0f_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top'
        title = 'Watch more'
        uptext = 'Check out game result or back to menu?'
        labels = ['Game result', 'Back to menu']
        texts = ['yes', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_yesterGame(self, event):
        print("I'm entering yesterdayGame")
        reply_token = event.reply_token
        userid = event.source.user_id
        yesterGames(reply_token)

        img = 'https://img.bleacherreport.net/img/images/photos/002/780/942/4e99edcf959c5743a660a70c378fbc0f_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top'
        title = 'Watch more'
        uptext = 'Check out game result or back to menu?'
        labels = ['Game result', 'Back to menu']
        texts = ['yes', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_showplayer(self, event):
        print("I'm entering showplayer")
        userid = event.source.user_id
        reply_token = event.reply_token
        playername = event.message.text
        try:
            searchplayer(reply_token, userid, playername)
            img = 'https://clutchpoints.com/wp-content/uploads/2020/07/Top-24-NBA-players-under-24.jpg'
            title = 'Watch more'
            uptext = 'Please choose'
            labels = ['Search more players', 'Search team', 'Back to menu']
            texts = ['search player', 'search team', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message(userid, "No this player or wrong format, please try again")
            self.go_back(event)

    def on_enter_gameBoxscore(self, event):
        print("I'm entering gameBoxscore")
        reply_token = event.reply_token
        userid = event.source.user_id
        push_message(userid, "Please enter date and team, Ex: Dec 5, 2019 Houston Rockets")

    def on_enter_showBoxscore(self, event):
        print("I'm entering gameBoxscore")
        reply_token = event.reply_token
        userid = event.source.user_id
        msg = event.message.text
        try:
            scrapeBoxscore(userid, msg)
            img = 'https://a.espncdn.com/photo/2019/1020/nba_new_season_preview_1296x729.jpg'
            title = 'Watch more'
            uptext = 'Please choose'
            labels = ['Search player', 'Search team', 'Back to menu']
            texts = ['search player', 'search team', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message(userid, "Wrong format, please try again")
            self.go_back(event)

    def on_enter_searchteam(self, event):
        print("I'm entering searchteam")
        reply_token = event.reply_token
        userid = event.source.user_id

        lakers = 'https://www.skinit.com/media/catalog/product/cache/9dbe6a0c16a5b581719a1aa389879cfc/d/s/dstlak03_19.jpg'
        clippers = 'https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Los_Angeles_Clippers_%282015%29.svg/1200px-Los_Angeles_Clippers_%282015%29.svg.png'
        mavs = 'https://i.pinimg.com/originals/72/1a/8b/721a8bd73983160aa979575c9d65a085.jpg'
        bucks = 'https://www.chicagotribune.com/resizer/KBJvo-WTR6F4BynBsEdIJcUMPRk=/800x450/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/K5UTVZBPEJHUFF3KIFZR5WNRPU.jpg'
        celtics = 'https://images.homedepot-static.com/productImages/f10649b1-73a2-4a69-963d-2d40fd77fae7/svn/green-applied-icon-wall-decals-nbop0203-64_1000.jpg'

        urls = [mavs, bucks, celtics, lakers, clippers]
        labels = ['Mavericks', 'Bucks ', 'Celtics', 'LA Lakers', 'LA Clippers']
        texts = ['Dallas Mavericks', 'Milwaukee Bucks', 'Boston Celtics', 'Los Angeles Lakers', 'Los Angeles Clippers']
        send_image_carousel(userid, urls, labels, texts)

        msg = "Press on the hot teams above or enter a team name"
        push_message(userid, msg)

    def on_enter_showteam(self, event):
        print("I'm entering showteam")
        userid = event.source.user_id
        reply_token = event.reply_token
        teamname = event.message.text
        try:
            searchteam(reply_token, userid, teamname)
            img = 'https://i.pinimg.com/originals/a6/cf/0a/a6cf0a242b87999d55a530dc5a67d3f1.jpg'
            title = 'Watch more'
            uptext = 'Please choose'
            labels = ['Search player', 'Search more teams', 'Back to menu']
            texts = ['search player', 'search team', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message(userid, "No this team or wrong format, please try again")
            self.go_back(event)

    def on_enter_showstanding(self, event):
        print("I'm entering showstanding")
        userid = event.source.user_id
        showstanding(userid)

        img = 'https://baselinetimes.com/wp-content/uploads/2020/11/Screen-Shot-2020-11-13-at-12.03.48-PM-1030x497.png'
        title = 'Watch more'
        uptext = 'Search more teams or back to menu'
        labels = ['Search team', 'Back to menu']
        texts = ['search team', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_statleader(self, event):
        print("I'm entering statleader")
        userid = event.source.user_id
        statleader(userid)

        img = 'https://i.pinimg.com/originals/a6/cf/0a/a6cf0a242b87999d55a530dc5a67d3f1.jpg'
        title = 'Watch more'
        uptext = 'Search for player or back to menu'
        labels = ['Search player', 'back to menu']
        texts = ['search player', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_showschedule(self, event):
        print("I'm entering showschedule")
        userid = event.source.user_id
        showschedule(userid)

        img = 'https://pbs.twimg.com/media/Eoa1VfWXIAsRTd8.jpg'
        title = 'Watch more'
        uptext = 'Search for team or back to menu'
        labels = ['Search team', 'back to menu']
        texts = ['search team', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_showmeme(self, event):
        print("I'm entering showmeme")
        userid = event.source.user_id
        try:
            showmeme(userid)
            img = 'https://i.ytimg.com/vi/FcutTWwba7w/maxresdefault.jpg'
            title = 'Watch more'
            uptext = 'Watch NBA news or go back to menu'
            labels = ['NBA news', 'back to menu']
            texts = ['yes', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message(userid, "Network error, please try again")
            self.go_back(event)

    def on_enter_shownews(self, event):
        print("I'm entering shownews")
        userid = event.source.user_id
        shownews(userid)

        img = 'https://i.kym-cdn.com/entries/icons/original/000/018/489/nick-young-confused-face-300x256-nqlyaa.jpg'
        title = 'Watch more'
        uptext = 'Watch NBA meme or go back to menu'
        labels = ['NBA Meme', 'back to menu']
        texts = ['yes', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_searchgame(self, event):
        print("I'm entering searchgame")
        reply_token = event.reply_token
        userid = event.source.user_id

        msg = "Please enter the date of the game that you want to watch, Ex: Dec 3, 2019"
        push_message(userid, msg)

    def on_enter_showsearchgame(self, event):
        print("I'm entering showsearchgmae")
        userid = event.source.user_id
        reply_token = event.reply_token
        date = event.message.text

        try:
            searchgame(reply_token, date)
            img = 'https://img.bleacherreport.net/img/images/photos/002/780/942/4e99edcf959c5743a660a70c378fbc0f_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top'
            title = 'Watch more'
            uptext = 'Watch game result or go back to menu'
            labels = ['Game result', 'back to menu']
            texts = ['yes', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message(userid, "Wrong format, please try again")
            self.go_back(event)
