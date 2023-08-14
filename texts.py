import data

class ru_language:
    def __init__(self):
        self.name_language = 'Русский'
        self.name = 'Masters'
        self.base_token = 'USDT'
    def new_partner(self, refer_name, line):
        return f'🎉 Поздравляем! У вас появился новый партнер {refer_name} в {line} линии'
    def start_msg(self, refer):
        msg = f'Привествуем в боте {self.name}'
        if refer:
            msg += f'\nВаш наставник: {refer}'
        return msg
    def home_hello(self):
        return 'Вы в главном меню'
    def balance(self):
        return 'Баланс'
    def admin(self):
        return 'Администратор'
    def chat_name(self):
        return f'{self.name} Chat'
    def deposit(self):
        return 'Пополнить'
    def deposit_info(self):
        return f'Для пополнения пополните баланс в {self.base_token} TRC-20 по адресу `{data.adress_deposit}`'
    def balance_info(self, balance):
        return f'Ваш баланс: {balance[self.base_token]} {self.base_token}'
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
        return 'Одобрить'
    def unconfirm(self):
        return 'Отклонить'
    def confirmed_deposit(self, transaction):
        return f'''Ваша заявка №{transaction["id"]} успешна!
Вам начислено {transaction['amount']} {transaction['token']}'''
    def confirmed_deposit_admin(self):
        return 'Заявка успешно одобрена'
    def unconfirmed_deposit_admin(self):
        return 'Заявка отклонена'
    def unconfirmed_deposit(self, transaction):
        return f'''Ваша заявка №{transaction["id"]} отклонена!
Сумма {transaction['amount']} {transaction['token']}'''
    def back(self):
        return 'Назад'
    def i_pay(self):
        return 'Я оплатил(-а)'
    def insert_amount_deposit(self, token=None):
        if not token:
            token = self.base_token
        return f'Введите суму пополнения в {token}'
    def enter_photo_deposit(self, amount, token=None):
        if not token:
            token = self.base_token
        return f'Отправьте скриншот с пополнением на суму {amount} {token}'
    def only_photo(self):
        return 'Отправьте только фото'
    def deposit_info_2(self):
        return 'В данный момент пополнения происходят в следующих валютах:\nUSDT (TRC-20): минимальная - 10'
    def only_integer(self):
        return 'Введите только суму, например 120 или 120.5'
    def chat_info(self):
        return 'Тут вы сможете купить подписку на клуб и получить следующие преимущества: ...'
    def you_confirm_trial(self, amount, days, is_trial):
        msg = f'Вы желаете подключить подписку ${amount}/{days} days?'
        if is_trial:
            msg += '\n\nДанный тариф пробный и активируется только 1 раз!'
        return msg
    def yes(self):
        return 'Да'
    def no(self):
        return "Нет"
    def yout_plan(self, plan, final_date):
        return f'''Ваш тариф: ${plan["amount"]} / {plan["days"]} days

Дата окончания тарифа: {final_date}
Ссылка на чат: `link...`'''
    def edited_before(self):
        return 'Заявка уже обратана ранее'
    def cabinet(self):
        return 'Личный кабинет'
    def cabinet_info(self, id):
        return f'''Вы можете пригласить друзей и получать кэшбек от их покупок тарифов.

Ваша реферальная ссылка: {data.link_bot}?start={id}'''
    def my_team(self):
        return 'Моя команда'

    def team_info(self, team):
        if team.get('count') == 0:
            return f'У вас пока нет команды, пригласить можете по ссылке ниже:\n\n{data.link_bot}?start={team.get("head_id")}'
        else:
            msg = f"Сейчас у вас в команде: {team.get('count')} человек!\n"
            for line in team:
                if str(line).isdigit():
                    msg += f'\n{line} линия - {len(team[line])} человек'
            return msg
    def error_by_plan(self):
        return 'Случилась ошибка при покупке пакета, обратитесь к службе поддержки.'

    def you_take_bonus(self, info, partner_name, bonus_amount):
        return f'Поздравляем! Ваш партнёр {partner_name} в {info["line"]} линии купил подписку.\nВы получаете ${bonus_amount} от покупки ({info["percent"]}%)'

    def you_take_bonus_for_percent(self, info, partner_name, bonus_amount):
        return f'Поздравляем! Ваш партнёр {partner_name} в {info["line"]} получил бонус по партнёрской программе.\nВы получаете ${bonus_amount} от дохода ({info["percent"]}%)'

    def buy_complete(self):
        return 'Покупка тарифа успешно обработана!'

    def we_talking(self):
        return 'Наши обсуждения'

    def how_take(self):
        return 'Что получу'

    def who_use(self):
        return 'Кому подойдёт'

    def how_work(self):
        return 'Как устроено'

    def how_take_text(self):
        return 'Вы получите ...'

    def full_version(self):
        return 'Что входит в полный доступ?'

    def full_version_about(self):
        return "В полный доступ входит ..."

    def sign_in(self):
        return "Присоиденится"

    def kb_choose(self):
        return 'Выберите варинат из клавиатуры'

    def how_work_about(self):
        return 'У нас устроено так ...'

    def referal_system(self):
        return 'Реферальная система'

    def referal_system_about(self):
        return 'Реферальная система у нас работает так ...'

    def who_use_about(self):
        return 'Бот подойдёт тем кто ...'

    def who_do_not_use(self):
        return 'Кому не подойдёт'

    def who_do_not_use_about(self):
        return 'Данный бот не подойдёт тем кто ...'

    def banner(self):
        return 'banner'

    def not_finansistic(self):
        return 'Остуствие финансовой помощи'

    def finance_stop(self):
        return 'Остановка финасового развития'

    def not_time(self):
        return 'Проблемы с распредилением времени'

    def not_motivation(self):
        return 'Отсутсвие мотивации и апатия'

    def not_finansistic_about(self):
        return 'Если у вас нет помощи...'

    def finance_stop_about(self):
        return 'Если Вы остановились в развитии'

    def not_time_about(self):
        return 'Если у вас нет времени...'

    def not_motivation_about(self):
        return 'Нет мотивации и началась апатия?\nПомните что ...'

    def we_talking_about(self):
        return 'У наших партнёров чаще всего бывают следующие проблемы ...'

    def masters_connect(self):
        return f'Первое знакомство с {self.name}'

    def masters_connect_about(self):
        return f'Мы - {self.name} поможем Вам ...'

    def feedback_users(self):
        return 'Отзывы участников'

    def feedback_users_about(self):
        return 'Влад - Лучший бот ...\nИлья - ...\nМихаил - ...'

    def information(self):
        return 'Инструкция'

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
