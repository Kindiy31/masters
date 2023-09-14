import data

class ru_language:
    def __init__(self):
        self.name_language = 'Русский'
        self.name = 'Masters'
        self.base_token = 'USDT'
    def new_partner(self, refer_name, line):
        return f'🎉 Поздравляем! У вас появился новый партнер {refer_name} в {line} линии'

    def start_msg(self, refer):
        msg = f'Привествуем в боте {self.name} 🖐️'
        if refer:
            msg += f'\nВаш наставник: {refer}'
        return msg

    def home_hello(self):
        return '''⚡️Сейчас ты находишься на главной странице и отсюда тебе открываются все пути по боту мастерс:

В разделе Masters Chat  ты можешь оплатить подписку и стать участником клуба, на выбор есть пробная/премиум подписка на  чат Masters  💬

В разделе Баланс можно просмотреть сколько средств есть на личном счету в системе 💰

В разделе Личный кабинет ты получишь реферальную ссылку для приглашения новых участников и получишь информацию, сколько людей ты смог привести. (Больше иформации во вкладке реферальная система)💻

В разделе Инструкции мы проведем тебе краткий экскурс по главным темам чата, что ты получишь и как он устроен 💡

Занимай свое место в чате Masters вместе с нами 🧠'''

    def balance(self):
        return 'Баланс💸'

    def admin(self):
        return 'Администратор'

    def chat_name(self):
        return f'{self.name} Chat'

    def deposit(self):
        return 'Пополнить'

    def deposit_info(self):
        return f'Для пополнения пополните баланс в {self.base_token} TRC-20 по адресу `{data.adress_deposit}`'

    def balance_info(self, balance):
        return f'💰Ваш баланс: {balance[self.base_token]} {self.base_token}'

    def new_deposit(self, transaction, user):
        return f'''Новая заявка на пополнение №{transaction['id']}
ID {user}: {transaction['id_user']}
Сумма: {transaction['amount']} {transaction['token']}
Дата: {transaction['transaction_time']}'''
    def send_deposit(self, transaction):
        return f'''Ваша заявка на пополнение №{transaction['id']}
Сумма: {transaction['amount']} {transaction['token']}
Дата: {transaction['transaction_time']}

Отправлена администратору на рассмотрение!'''

    def confirm(self):
        return '✅Одобрить'

    def unconfirm(self):
        return '❌Отклонить'

    def confirmed_deposit(self, transaction):
        return f'''✅Ваша заявка №{transaction["id"]} успешна!
Вам начислено {transaction['amount']} {transaction['token']}'''

    def confirmed_deposit_admin(self):
        return '✅Заявка успешно одобрена'

    def unconfirmed_deposit_admin(self):
        return '❌Заявка отклонена'

    def unconfirmed_deposit(self, transaction):
        return f'''❌Ваша заявка №{transaction["id"]} отклонена!
Сумма {transaction['amount']} {transaction['token']}'''

    def back(self):
        return 'Назад'

    def i_pay(self):
        return '✅Я оплатил(-а)'

    def insert_amount_deposit(self, token=None):
        if not token:
            token = self.base_token
        return f'Введите суму пополнения в {token}'
    def enter_photo_deposit(self, amount, token=None):
        if not token:
            token = self.base_token
        return f'📱Отправьте скриншот с пополнением на суму {amount} {token}'
    def only_photo(self):
        return 'Отправьте только фото'
    def deposit_info_2(self):
        return '💲В данный момент пополнения происходят в следующих валютах:\nUSDT (TRC-20): минимальная - 10'
    def only_integer(self):
        return 'Введите только суму, например 120 или 120.5'
    def chat_info(self):
        return '''Тут вы сможете купить подписку на клуб и получить следующие преимущества:
- Реферальная система с возможностью пассивного дохода💰
- Бонусы от партнеров;
- Доступ к чату на месяц 🎯
- Доступ ко всем материалам и записям.

Заходи в чат, мы ждем именно тебя🫵🏼'''
    def you_confirm_trial(self, amount, days, is_trial):
        msg = f'Вы желаете подключить подписку ${amount}/{days} days?'
        if is_trial:
            msg += '\n\n❗ Данный тариф пробный и активируется только 1 раз!'
        return msg
    def yes(self):
        return '✅Да'
    def no(self):
        return "❌Нет"
    def yout_plan(self, plan, final_date):
        return f'''Поздравляем теперь ты член клуба Masters ! От того как ты выбираешь окружение, будет зависеть твой будущий успех🧠
Ваш тариф: ${plan["amount"]} / {plan["days"]} days

Дата окончания тарифа: {final_date}
Ссылка на чат: `https://t.me/+c30rmAQ_rBcxYmMy`'''
    def edited_before(self):
        return 'Заявка уже обратана ранее'
    def cabinet(self):
        return 'Личный кабинет'
    def cabinet_info(self, id):
        return f'''Вы можете пригласить друзей и получать кэшбек от их покупок тарифов.

Ваша реферальная ссылка: {data.link_bot}?start={id}'''
    def my_team(self):
        return 'Моя команда🚀'

    def team_info(self, team):
        if team.get('count') == 0:
            return f'😥У вас пока нет команды, пригласить можете по ссылке ниже:\n\n{data.link_bot}?start={team.get("head_id")}'
        else:
            msg = f"Сейчас у вас в команде: {team.get('count')} человек!👍\n"
            for line in team:
                if str(line).isdigit():
                    msg += f'\n{line} линия - {len(team[line])} человек'
            return msg
    def error_by_plan(self):
        return 'Случилась ошибка при покупке пакета, обратитесь к службе поддержки.👩‍💻'

    def you_take_bonus(self, info, partner_name, bonus_amount):
        return f'🎉Поздравляем! Ваш партнёр {partner_name} в {info["line"]} линии купил подписку.\nВы получаете ${bonus_amount} от покупки ({info["percent"]}%)🎉'

    def you_take_bonus_for_percent(self, info, partner_name, bonus_amount):
        return f'🎉Поздравляем! Ваш партнёр {partner_name} в {info["line"]} получил бонус по партнёрской программе.\nВы получаете ${bonus_amount} от дохода ({info["percent"]}%)🎉'

    def buy_complete(self):
        return '✅Покупка тарифа успешно обработана!'

    def we_talking(self):
        return 'Наши обсуждения 💬'

    def how_take(self):
        return 'Что получу 💎'

    def who_use(self):
        return 'Кому подойдёт🎯'

    def how_work(self):
        return 'Как устроено⚙️'

    def how_take_text(self):
        return ''

    def full_version(self):
        return 'Что входит в полный доступ?'

    def full_version_about(self):
        return """🔥В полный доступ входит:

 -Реферальная система с возможностью пассивного дохода💰
- Бонусы от партнеров;
- Доступ к чату на месяц 🎯
- Доступ ко всем материалам и записям.

Заходи в чат, мы ждем именно тебя🫵🏼"""

    def sign_in(self):
        return "Присоиденится"

    def kb_choose(self):
        return 'Выберите варинат из клавиатуры'

    def how_work_about(self):
        return '''<b>❗️Встречи Master`s utro проходят три раза в неделю:

ПН - 7:00 am;
СР -  7:00 am, 11:00 am
ПТ -  7:00 am</b>

Также Masters включает в себя крутую реферальную систему👇🏼'''

    def referal_system(self):
        return 'Реферальная система'

    def referal_system_about(self):
        return '''<b>🔥Реферальная система Masters</b> - это настоящее сокровище, кроме того, что благодаря реферальной ссылке вам удобно поделиться чатом с близкими и друзьями, вы еще и получите до 71%❗️от дохода за каждого приведенного участника💸

 Это возможность не только самосовершенствоваться, но еще и заработать, чем большую команду ты соберешь, тем больше сможешь накопить💰

Больше о реферальной системе смотри в этом видео 👇🏼'''

    def who_use_about(self):
        return '''❗️Этот чат точно для тебя если: 

- Ты хочешь саморазвиваться ;
- Ты желаешь стать на 100% уверенным в себе 💯
- Хочешь улучшить самодисциплину ;
- Хочешь работать и зарабатывать в нетворкинге 💻
- Чувствуешь, что время уходит в пустую (теряешь часы, дни, годы).

Здесь ты сможешь найти ответы на все вопросы и стать лучшей версией самого себя🏆'''

    def who_do_not_use(self):
        return 'Кому не подойдёт'

    def who_do_not_use_about(self):
        return '''❗️Этот чат точно НЕ для тебя: 

- Если у тебя нет цели стать лучше;
- Ты не хочешь развиваться;
- Ждешь лучших времен;
- Не желаешь ничего менять в своей жизни;
- Ты  знаешь, что у тебя ничего не получится.'''

    def banner(self):
        return 'banner'

    def not_finansistic(self):
        return 'Развитие личности💪'

    def finance_stop(self):
        return 'Уверенность в себе🏆 '

    def not_time(self):
        return 'Нетворкинг 🪢'

    def not_motivation(self):
        return 'Мотивация и энергия 🔥'

    def not_finansistic_about(self):
        return '''Каждый день - это возможность открыть новые горизонты и стать лучшей версией самого себя, постоянно развивая свою уникальную личность 💪
Если ты хочешь присоединиться к клубу, развиваться вместе с нами и стать одним из нас, жми на кнопку 👇🏼'''

    def finance_stop_about(self):
        return '''Увереность в себе открывает двери к невероятным возможностям и помогает преодолеть любые вызовы жизни🧗🏻
Если ты хочешь присоединиться к клубу, развиваться вместе с нами и стать одним из нас, жми на кнопку 👇🏼'''

    def not_time_about(self):
        return '''Каждый новый контакт - это возможность построить крепкий мост в мире возможностей и достижений через сотрудничество и обмен идеями🔥
Если ты хочешь присоединиться к клубу, развиваться вместе с нами и стать одним из нас, жми на кнопку 👇🏼'''

    def not_motivation_about(self):
        return '''Мотивация – это внутреннее страстное желание, которое придает энергии для преодоления любых препятствий и достижения самых высоких вершин🏆'
Если ты хочешь присоединиться к клубу, развиваться вместе с нами и стать одним из нас, жми на кнопку 👇🏼'''
    def we_talking_about(self):
        return '''Masters – это место, где ты сможешь осуществить самоанализ, отточить самодисциплину и увеличить свою внутреннюю энергию 🧗🏻

Здесь каждый день – это возможность расти, развивать свое мышление и реализовывать свой потенциал💪
Здесь мы собрали фрагменты из 4 тем, которые рассматриваются на наших встречах:

I   Развитие личности💪
II  Уверенность в себе 🎯
III Нетворкинг 🔥
IV Мотивация и энергия🏆'''

    def masters_connect(self):
        return f'Первое знакомство с {self.name}'

    def masters_connect_about(self):
        return f'''👋🏼{self.name} – это уникальная возможность, стать лучшей версией самого себя, здесь: 

- <b>Утренние лекции</b> для положительного заряда на целый день;
- <b>Групповые обсуждения</b> наиболее интересных вопросов вместе с 
- <b>В чате ты найдешь</b> много единомышленников, с которыми будешь постоянно расти;
- <b>Поддержка ментора</b> 24/7;
- <b>Удобная реферальная система</b> для приглашения друзей.

🌏Погрузись в мир Masters и знакомься с мастерством саморазвития, которое станет твоим лучшим спутником на пути к успеху. Невозможно перечислить все преимущества Masters, но ты можешь попробовать их вместе с нами 🎯

<b>За кнопкой присоединиться под этим текстом👇🏼</b>'''

    def feedback_users(self):
        return 'Отзывы участников✨'

    def feedback_users_about(self):
        return 'Влад - Лучший бот ...\nИлья - ...\nМихаил - ...'

    def information(self):
        return 'О чате❗'

    def bonus_system(self):
        return 'Система бонусов'

    def bonus_system_about(self):
        return 'Система бонусов дает ...'


class lang_:
    def get_language(self, language='ru'):
        if language == 'ru':
            language = ru_language()
        else:
            language = ru_language()
        return language
