from texts import lang_
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from database import dbase

class keyboards_:
    def __init__(self, lang='ru'):
        self.lang = lang_().get_language(language=lang)

    def generate_reply_markup(self, buttons, back=None, sign_in=None):
        markup = types.ReplyKeyboardMarkup(selective=False, resize_keyboard=True)
        for row in buttons:
            if row:
                if len(row) != 1:
                    markup.add(*row)
                else:
                    markup.add(row[0])
        if sign_in:
            markup.add(self.lang.sign_in())
        if back:
            markup.add(self.lang.back())
        return markup

    def generate_inline_markup(self, buttons):
        markup = types.InlineKeyboardMarkup()
        for data in buttons:
            row = []
            for button in data:
                name = button.get('name')
                if 'callback' in button:
                    callback = button.get('callback')
                    row.append(types.InlineKeyboardButton(name, callback_data=callback))
                elif 'webapp' in button:
                    webapp = button.get('webapp')
                    row.append(types.InlineKeyboardButton(name, web_app=WebAppInfo(url=webapp)))
                elif 'url' in button:
                    url = button.get('url')
                    row.append(types.InlineKeyboardButton(name, url=url))
            if row:

                if len(row) != 1:
                    markup.add(*row)
                else:
                    markup.add(row[0])
        return markup

    def home_kb(self, user):
        if not user:
            user = {}
        is_admin = user.get('is_admin')
        buttons = [
            [
                self.lang.balance(),
                self.lang.chat_name()

            ],
            [
                self.lang.cabinet(),
                self.lang.information()
            ]
        ]
        if is_admin:
            buttons.append([self.lang.admin()])

        markup = self.generate_reply_markup(buttons=buttons)
        return markup

    def balances_kb(self):
        buttons = [
            [
                {
                    'name': self.lang.deposit(),
                    'callback': 'deposit'
                },
            ]
        ]
        markup = self.generate_inline_markup(buttons=buttons)
        return markup

    def deposit_kb(self):
        buttons = [
            [
                {
                    'name': self.lang.back(),
                    'callback': 'balance'
                },
            ]
        ]
        markup = self.generate_inline_markup(buttons=buttons)
        return markup

    def back_kb(self):
        markup = self.generate_reply_markup(buttons=[[]], back=True)
        return markup

    def deposit_admin_kb(self, id_transaction):
        buttons = [
            [
                {
                    'name': self.lang.confirm(),
                    'callback': f'deposit_confirm_{id_transaction}'
                },
                {
                    'name': self.lang.unconfirm(),
                    'callback': f'deposit_unconfirm_{id_transaction}'
                }
            ]
        ]
        markup = self.generate_inline_markup(buttons=buttons)
        return markup

    def plans_kb(self, active_trial=False):
        plans = dbase.take_plans()
        buttons = []
        for plan in plans:
            id = plan.get('id')
            amount = plan.get('amount')
            days = plan.get('days')
            is_trial = plan.get('is_trial')
            is_active = plan.get('is_active')
            name = ''

            if is_active:
                if is_trial:
                    if active_trial:
                        continue
                    name += '🎁'
                else:
                    name += '🛍'
                name += f'${int(amount)} / {days} days📆'
                buttons.append(
                    [
                        {
                            'name': name,
                            'callback': f'plan_buy_{id}'
                        }
                    ]
                )
        markup = self.generate_inline_markup(buttons=buttons)
        return markup

    def buy_plan_kb(self, id):
        buttons = [
            [
                {
                    'name': self.lang.yes(),
                    'callback': f'plan_confirm_{id}'
                },
                {
                    'name': self.lang.no(),
                    'callback': f'plan_unconfirm'
                }
            ]
        ]
        markup = self.generate_inline_markup(buttons=buttons)
        return markup

    def team_kb(self):
        buttons = [
            [
                {
                    'name': self.lang.my_team(),
                    'callback': f'team'
                }
            ]
        ]
        markup = self.generate_inline_markup(buttons=buttons)
        return markup

    def funnel_kb(self):
        buttons = [
            [
                self.lang.we_talking()
            ],
            [
                self.lang.how_take()
            ],
            [
                self.lang.how_work()
            ],
            [
                self.lang.masters_connect()
            ]

        ]
        markup = self.generate_reply_markup(buttons=buttons)
        return markup

    def how_take_kb(self):
        buttons = [
            [
                self.lang.we_talking()
            ],
            [
                self.lang.full_version()
            ],
            [
                self.lang.who_use()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True)
        return markup

    def sign_in(self):
        buttons = [
            [
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True, sign_in=True)
        return markup

    def how_work_kb(self):
        buttons = [
            [
                self.lang.referal_system()
            ],
            [
                self.lang.bonus_system()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True)
        return markup

    def who_use_kb(self):
        buttons = [
            [
                self.lang.who_do_not_use()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True, sign_in=True)
        return markup

    def we_talking_kb(self):
        buttons = [
            [
                self.lang.not_finansistic()
            ],
            [
                self.lang.finance_stop()
            ],
            [
                self.lang.not_time()
            ],
            [
                self.lang.not_motivation()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True)
        return markup

    def not_finansistic_kb(self):
        buttons = [
            [
                self.lang.finance_stop()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True, sign_in=True)
        return markup

    def finance_stop_kb(self):
        buttons = [
            [
                self.lang.not_time()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True, sign_in=True)
        return markup

    def not_time_kb(self):
        buttons = [
            [
                self.lang.not_motivation()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True, sign_in=True)
        return markup

    def not_motivation_kb(self):
        buttons = [
            [
                self.lang.not_finansistic()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True, sign_in=True)
        return markup

    def masters_connect_kb(self):
        buttons = [
            [
                self.lang.feedback_users()
            ]
        ]
        markup = self.generate_reply_markup(buttons=buttons, back=True, sign_in=True)
        return markup
