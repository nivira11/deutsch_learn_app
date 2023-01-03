import random
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

Builder.load_string("""

<Start>:
    MDBoxLayout:
    
        orientation: "vertical"
    	size_hint: (1, 1)
    	pos_hint: {"center_x": 0.5, "center_y":0.5}
    

        MDBoxLayout:
        Label:
            text: 'Learne Deutsch'
            valign: 'center'
            color: 0,0,0,1
        Button:
            text: 'Генерировать Verb'
            on_press: root.generate_verb()
            size_hint: (1, 1)
            valign: 'center'
        Button:
            text: 'Генерировать Wort'
            on_press: root.generate_wort()
            size_hint: (1, 1)
            valign: 'center'
            

    Label:
        id: random_verb
        text: '_'
        font_size: dp(19)
        color: 0,0,1
        pos_hint: {"x":-0.3, "y":0.3}
    Label:
        id: random_wort
        text: '_'
        font_size: dp(20)
        color: 0,0,1
        pos_hint: {"x":0.3, "y":0.3}
        

""")

class Start(Screen):

    def __int__(self, **kwargs):
        super(Start,self).__init__(**kwargs)

    def generate_verb(self):
        verbs = [
            'sein-быть',
            'haben-иметь',
            'werden-становиться',
            'können-мочь,уметь',
            'müssen-бытьдолжным',
            'sagen-сказать',
            'machen-делать',
            'geben-давать',
            'kommen-приходить',
            'sollen-долженствовать',
            'wollen-хотеть',
            'gehen-идти',
            'wissen-знать',
            'sehen-видеть',
            'lassen-велеть',
            'stehen-стоять',
            'finden-находить',
            'bleiben-оставаться,остаться',
            'liegen-лежать',
            'heißen-называться',
            'denken-думать',
            'nehmen-брать',
            'tun-делать',
            'dürfen-мочь(сразрешения)',
            'glauben-полагать,думать,считать',
            'halten-держать',
            'nennen-назвать',
            'mögen-любить',
            'zeigen-показать',
            'führen-вести',
            'sprechen-говорить',
            'bringen-приносить',
            'leben-жить',
            'fahren-ехать',
            'meinen-считать,полагать',
            'fragen-спрашивать',
            'kennen-знать',
            'gelten-стоить',
            'stellen-ставить',
            'spielen-играть',
            'arbeiten-работать',
            'brauchen-нуждаться',
            'folgen-следовать',
            'lernen-учиться',
            'bestehen-состоять,существовать,сдавать(экзамен)',
            'verstehen-понимать',
            'setzen-садиться,заниматьместо',
            'bekommen-получать',
            'beginnen-начать',
            'erzählen-рассказывать',
            'versuchen-пытаться',
            'schreiben-писать',
            'laufen-бегать',
            'erklären-объяснять',
            'entsprechen-соответствовать',
            'sitzen-сидеть',
            'ziehen-тянуть',
            'scheinen-казаться,светить',
            'fallen-падать',
            'gehören-принадлежать',
            'entstehen-возникать',
            'erhalten-получать',
            'treffen-встречать',
            'suchen-искать',
            'legen-класть',
            'vor·stellen-представлять,представлятьсебе',
            'handeln-торговаться,иметьдело',
            'erreichen-достигать',
            'tragen-нести,одевать',
            'schaffen-создавать,работать',
            'lesen-читать',
            'verlieren-терять',
            'dar·stellen-представлять(насцене,вкниге)',
            'erkennen-узнать',
            'entwickeln-развивать',
            'reden-говорить',
            'aus·sehen-выглядеть',
            'erschienen-появиться,появляться',
            'bilden-образовывать',
            'an·fangen-начать,начинать',
            'erwarten-ожидать',
            'wohnen-жить,проживать',
            'betreffen-касаться',
            'warten-ждать',
            'vergehen-пройти(овремени)',
            'helfen-помогать',
            'gewinnen-выигрывать,побеждать',
            'schließen-закрывать',
            'fühlen-чувствовать',
            'bieten-предлагать',
            'interessieren-интересоваться',
            'erinnern-помнить',
            'ergeben-выяснять,получать(врезультате)',
            'an·bieten-предлагать',
            'studieren-изучать,учиться(вуниверситете,институте)',
            'verbindenсоединять',
            'an·sehenсмотреть',
            'fehlen-отсутствовать,нехватать',
            'bedeuten-означать,значить',
            'vergleichen-сравнивать',
        ]
        self.ids.random_verb.text = random.choice(verbs)

    def generate_wort(self):
        worts = [
            'arbaiten',
            'schreiben'
        ]
        self.ids.random_wort.text = random.choice(worts)

class MainApp(MDApp):

    def build(self):
        return Start()

MainApp().run()