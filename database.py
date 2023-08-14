import data
from texts import lang_
import pymysql.cursors
import datetime

lang = lang_().get_language()

class db:
    def __init__(self):
        self.con = pymysql.connect(host=data.database_info['host'],
                                   port=data.database_info['port'],
                                   user=data.database_info['user'],
                                   password=data.database_info['password'],
                                   database=data.database_info['name']
                                   )
        self.cur = self.con.cursor()
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS users (
                                id BIGINT,
                                first_name TEXT,
                                username TEXT,
                                register_date TEXT,
                                refer_id BIGINT,
                                lang TEXT,
                                is_admin BOOLEAN,
                                is_active BOOLEAN,
                                active_trial BOOLEAN,
                                final_date TEXT,
                                plan_id INT)
                                ''')
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS transactions (
                                id BIGINT AUTO_INCREMENT PRIMARY KEY,
                                id_user BIGINT,
                                transaction_type INT,
                                amount REAL,
                                token TEXT,
                                photo_id TEXT,
                                is_finished BOOLEAN,
                                is_confirm BOOLEAN,
                                transaction_time TEXT)
                                ''')
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS balances (
                                id_user BIGINT,
                                USDT REAL DEFAULT 0)
                                ''')
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS plans (
                                        id BIGINT AUTO_INCREMENT PRIMARY KEY,
                                        amount REAL,
                                        days INTEGER,
                                        is_trial BOOLEAN,
                                        is_active BOOLEAN)
                                        ''')
        self.con.commit()

    def geterate_time_now(self):
        t_time = str(datetime.datetime.now())
        t_time = t_time.split(r'.')[0]
        return t_time

    def generate_time_after(self, operation, minutes=None, hours=None, days=None):
        time_after = datetime.datetime.now()
        delta = None
        if minutes:
            delta = datetime.timedelta(minutes=minutes)
        if hours:
            delta = datetime.timedelta(hours=hours)
        if days:
            delta = datetime.timedelta(days=days)
        if delta:
            if operation is True:
                time_after = time_after + delta
            else:
                time_after = time_after - delta
        time_after = str(time_after).split(r'.')[0]
        return time_after

    def select_sqlite(self, table, values='*', where='', fetchall=False):
        self.__init__()
        if where != '':
            where = f"WHERE {where}"
        sql = f"SELECT {values} FROM {table} {where};"
        print(sql)
        self.cur.execute(sql)
        if fetchall:
            result = self.cur.fetchall()
        else:
            result = self.cur.fetchone()
        return result

    def update_sqlite(self, table, column, value, where=''):
        if where != '':
            where = f'WHERE {where}'
        self.cur.execute(f'UPDATE {table} SET {column} = "{value}" {where}')
        self.con.commit()
        return True

    def insert_sqlite(self, table, columns_list, values):
        columns = ''
        VALUES = ''
        for value in columns_list:
            columns += f'{value}, '
            VALUES += '%s,'
        columns = columns[:-2]
        VALUES = VALUES[:-1]
        sql = f'INSERT INTO {table} ({columns}) VALUES({VALUES})'
        print(sql, values)
        self.cur.execute(sql, values)
        self.con.commit()
        return True

    def delete_sqlite(self, table, where=''):
        if where != '':
            where = f'WHERE {where}'
        sql = f'DELETE FROM {table} {where}'
        self.cur.execute(sql)
        self.con.commit()

    def take_user(self, id):
        user = self.select_sqlite(table='users', where=f'id={id}')
        return user

    def register(self, message, refer_id, lang='ru', is_admin=False, is_block=False, active_trial=False):
        id = message.from_user.id
        user = self.take_user(id=id)
        if not user:
            first_name = message.from_user.first_name
            username = message.from_user.username
            register_date = self.geterate_time_now()
            columns = ['id', 'first_name', 'username', 'register_date', 'refer_id', 'lang', 'is_admin', 'is_active', 'active_trial']
            values = [id, first_name, username, register_date, refer_id, lang, is_admin, is_block, active_trial]
            self.insert_sqlite(table='users', columns_list=columns, values=values)
            return True
        else:
            return False

    def take_user_for_refer_id(self, refer_id):
        users = self.select_sqlite(table='users', where=f'refer_id={refer_id}', fetchall=True)
        return users

    def take_refer(self, id_user):
        user = self.take_user(id=id_user)
        refer_id = user.get('refer_id')
        refer = dbase.take_user(id=refer_id)
        return refer

    def take_active(self, line_lambda):
        line_lambda = (list(filter(lambda x: x.get('is_active'), line_lambda)))
        return line_lambda

    def take_percent_user(self, id):
        team = self.take_team_user(id=id)
        counts = {
            1: 0,
            2: 0,
            3: 0
        }
        percents_for_sell = {
            data.percents_one_line: 1, #50% - 1 лінія
            data.percent_others: 9 #3% - до 9 лінії по старту
        }
        percents_for_percent = {
            # По старту пусто
        }
        one_line = team.get(1)
        two_line = team.get(2)
        three_line = team.get(3)
        if one_line:
            counts[1] = len(self.take_active(line_lambda=one_line))
        if two_line:
            counts[2] = len(self.take_active(line_lambda=two_line))
        if three_line:
            counts[3] = len(self.take_active(line_lambda=three_line))

        if counts[1] >= 4 and counts[2] >= 12:
            percents_for_percent[1] = 10 #10% в 1 лінії
        if counts[1] >= 8 and counts[2] >= 24:
            percents_for_percent[2] = 5 #5% в 2 лінії
        if counts[1] >= 16 and counts[2] >= 48 and counts[3] >= 96:
            percents_for_percent[3] = 3 #3% в 3 лінії

        if counts[1] >= 2:
            percents_for_sell[data.percent_others] = 10
        if counts[1] >= 4:
            percents_for_sell[data.percent_others] = 12
        if counts[1] >= 8:
            percents_for_sell[data.percent_others] = 13
        if counts[1] >= 16:
            percents_for_sell[data.percent_others] = 14
        response = {
            'counts': counts,
            'percents_for_percent': percents_for_percent,
            'percents_for_sell': percents_for_sell
        }
        return response
    def take_team_user(self, id):
        team = {'count': 0, 'head_id': id}
        line = 1
        temp_id = [id]
        while True:
            temp_id_2 = []
            for id in temp_id:
                refers = self.take_user_for_refer_id(refer_id=id)
                if refers:
                    for refer in refers:
                        temp_id_2.append(refer.get('id'))
                        line_now = team.get(line)
                        if line_now:
                            line_now.append(self.take_user(id=refer.get('id')))
                        else:
                            line_now = [self.take_user(id=refer.get('id')),]
                        team[line] = line_now
                        team['count'] = team['count'] + 1
            if not temp_id_2:
                break
            temp_id = temp_id_2.copy()
            temp_id_2.clear()
            line += 1

        return team

    def take_all_users(self):
        users = self.select_sqlite(table='users', fetchall=True)
        return users

    def take_all_transactions(self):
        transactions = self.select_sqlite(table='transactions', fetchall=True)
        return transactions

    def create_transaction(self, id_user: int or str, transaction_type: int, amount: float or int,
                           token: str = None, photo_id: str = None, is_finished: bool = False, is_confirm: bool = False,
                           transaction_time: str = None) -> object:
        if not token:
            token = lang.base_token
        if not transaction_time:
            transaction_time = self.geterate_time_now()
        columns = ['id_user', 'transaction_type', 'amount', 'token',
                   'photo_id', 'is_finished', 'is_confirm', 'transaction_time']
        values = [id_user, transaction_type, amount, token,
                  photo_id, is_finished, is_confirm, transaction_time]
        self.insert_sqlite(table='transactions', columns_list=columns, values=values)
        transactions = self.take_all_transactions()
        last_transaction = transactions[-1]
        return last_transaction

    def take_balance(self, id_user):
        balance = self.select_sqlite(table='balances', where=f'id_user={id_user}')
        if not balance:
            columns = ['id_user',]
            values = [id_user,]
            self.insert_sqlite(table='balances', columns_list=columns, values=values)
            balance = self.select_sqlite(table='balances', where=f'id_user={id_user}')
        return balance

    def take_admins(self):
        admins = self.select_sqlite(table='users', where=f'is_admin=1', fetchall=True)
        return admins

    def take_plans(self):
        plans = self.select_sqlite(table='plans', fetchall=True)
        return plans

    def add_plan(self, amount, days, is_trial=False, is_active=True):
        columns = ['amount', 'days', 'is_trial', 'is_active']
        values = [amount, days, is_trial, is_active]
        self.insert_sqlite(table='plans', columns_list=columns, values=values)
        plans = self.take_plans()
        created_plan = plans[-1]
        return created_plan

    def take_plan(self, id):
        plan = self.select_sqlite(table='plans', where=f'id={id}')
        return plan

    def change_balance(self, id_user, amount, token, operation):
        balances = self.take_balance(id_user=id_user)
        balances = balances.get(token)
        balance = float(round(eval(f"{balances} {operation} {amount}"), 2))
        self.update_sqlite(table='balances', where=f'id_user={id_user}', column=token, value=balance)
        return True

    def update_user_data(self, column, id_user, value):
        self.update_sqlite(table='users', column=column, value=value, where=f'id={id_user}')
        return

    def add_partner_bonus(self, amount, id_user):
        temp_id = id_user
        responses = {'head_id': id_user, 'amount': amount}
        for line in range(13):
            line = line + 1
            refer = self.take_refer(id_user=temp_id)
            if refer:
                temp_id = refer.get('id')
                bonuses = self.take_percent_user(id=temp_id)
                lines_count_for_other = bonuses.get('percents_for_sell').get(data.percent_others)
                percent = None
                if line == 1:
                    percent = data.percents_one_line
                elif line <= lines_count_for_other:
                    percent = data.percent_others
                if percent:
                    is_active = refer.get('is_active')
                    responses[temp_id] = {'line': line, 'percent': percent, 'is_active': is_active}
                    temp_id_2 = temp_id
                    for line_2 in range(3):
                        line_2 = line_2 + 1
                        refer = self.take_refer(id_user=temp_id_2)
                        if refer:
                            temp_id_2 = refer.get('id')
                            bonuses = self.take_percent_user(id=temp_id_2)
                            percents_for_percent = bonuses.get('percents_for_percent')
                            percent = percents_for_percent.get(line_2)
                            if percent:
                                responses[temp_id]['percent_for_percent'][temp_id_2]['line'] = line_2
                                responses[temp_id]['percent_for_percent'][temp_id_2]['percent'] = percent
                        else:
                            break
            else:
                break
        return responses

    def create_plan(self, id_user, id_plan):
        plan = self.take_plan(id=id_plan)
        user = self.take_user(id=id_user)
        balance = self.take_balance(id_user=id_user)
        balance = balance.get(lang.base_token)
        amount = plan.get('amount')
        if balance < amount:
            return {"error": "low balance"}
        else:
            status = False
            amount = plan.get('amount')
            days = plan.get('days')
            is_trial = plan.get('is_trial')
            is_active = plan.get('is_active')
            if is_active:
                finish = self.generate_time_after(operation=True, days=days)

                if is_trial:
                    user_active_trial = user.get('active_trial')
                    if not user_active_trial:
                        status = True
                    else:
                        return {"error": "user activated after"}
                else:
                    status = True

            else:
                return {"error": "plan not active"}
            if status:
                self.change_balance(id_user=id_user, amount=amount, operation='-', token=lang.base_token)
                self.create_transaction(id_user=id_user, transaction_type=2, token=lang.base_token,
                                        amount=amount, is_finished=True, is_confirm=True)
                self.update_user_data(id_user=id_user, column='is_active', value=1)
                self.update_user_data(id_user=id_user, column='active_trial', value=1)
                self.update_user_data(id_user=id_user, column='final_date', value=finish)
                self.update_user_data(id_user=id_user, column='plan_id', value=id_plan)
                bonuses = self.add_partner_bonus(amount=amount, id_user=id_user)
                self.enter_bonus_partner(bonuses=bonuses)
                return bonuses
        return {}

    def enter_bonus_partner(self, bonuses):
        head_id = bonuses.get('head_id')
        amount = bonuses.get('amount')
        for id in bonuses:
            if str(id).isdigit():
                info = bonuses.get(id)
                if info:
                    is_active = info.get('is_active')
                    if is_active:
                        bonus = float(round(eval(f"{amount} * {info['percent']} / 100"), 2))
                        self.change_balance(id_user=id, amount=bonus, token=lang.base_token, operation='+')
                        self.create_transaction(id_user=id, token=lang.base_token, amount=bonus, transaction_type=3, photo_id=head_id)

                        percent_for_percent = info.get('percent_for_percent')
                        if percent_for_percent:
                            for id_refer in percent_for_percent:
                                info = percent_for_percent.get(id_refer)
                                if info:
                                    bonus = float(round(eval(f"{amount} * {info['percent']} / 100"), 2))
                                    self.change_balance(id_user=id_refer, amount=bonus, token=lang.base_token, operation='+')
                                    self.create_transaction(id_user=id_refer, token=lang.base_token, amount=bonus, transaction_type=4,
                                                            photo_id=id)
        return True
    def take_transaction(self, id_transaction):
        transaction = self.select_sqlite(table='transactions', where=f'id={id_transaction}')
        return transaction

    def update_transaction(self, id_transaction, column, value):
        self.update_sqlite(table='transactions', column=column, value=value, where=f'id={id_transaction}')

    def finish_deposit(self, id_transaction, result):
        transaction = self.take_transaction(id_transaction=id_transaction)
        amount = transaction.get('amount')
        token = transaction.get('token')
        id_user = transaction.get('id_user')
        self.update_transaction(id_transaction=id_transaction, column='is_finished', value=1)
        if result:
            self.update_transaction(id_transaction=id_transaction, column='is_confirm', value=1)
            dbase.change_balance(id_user=id_user, amount=amount, token=token, operation='+')
        else:
            self.update_transaction(id_transaction=id_transaction, column='is_confirm', value=0)
        return True


dbase = db()
