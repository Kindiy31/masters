import telebot
import data
from database import dbase
from keyboards import keyboards_
from texts import lang_

bot = telebot.TeleBot(data.TOKEN)


#funnel
####################################################################################################################################

class Funnel:
    def __init__(self, id):
        self.id = id
        self.user, self.lang, self.kb = get_user_and_lang(id=id)
        msg = bot.send_photo(self.id, data.banner_photo_id, caption=self.lang.banner(), reply_markup=self.kb.funnel_kb())
        bot.register_next_step_handler(msg, self.funnel_handler, 'start')

    def funnel_handler(self, message, before):
        text = message.text
        if text == self.lang.how_take():
            msg = bot.send_message(self.id, self.lang.how_take_text(), reply_markup=self.kb.how_take_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.full_version():
            msg = bot.send_message(self.id, self.lang.full_version_about(), reply_markup=self.kb.sign_in())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.sign_in():
            back_fnc(id=self.id)

        elif text == self.lang.how_work():
            msg = bot.send_message(self.id, self.lang.how_work_about(), reply_markup=self.kb.how_work_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.referal_system():
            msg = bot.send_message(self.id, self.lang.referal_system_about(), reply_markup=self.kb.sign_in())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.who_use():
            msg = bot.send_message(self.id, self.lang.who_use_about(), reply_markup=self.kb.who_use_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.who_do_not_use():
            msg = bot.send_message(self.id, self.lang.who_do_not_use_about(), reply_markup=self.kb.sign_in())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.we_talking():
            msg = bot.send_message(self.id, self.lang.we_talking(), reply_markup=self.kb.we_talking_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.not_finansistic():
            msg = bot.send_message(self.id, self.lang.not_finansistic_about(), reply_markup=self.kb.not_finansistic_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.not_motivation():
            msg = bot.send_message(self.id, self.lang.not_motivation_about(), reply_markup=self.kb.not_motivation_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.not_time():
            msg = bot.send_message(self.id, self.lang.not_time_about(), reply_markup=self.kb.not_time_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.finance_stop():
            msg = bot.send_message(self.id, self.lang.finance_stop_about(), reply_markup=self.kb.finance_stop_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.masters_connect():
            msg = bot.send_message(self.id, self.lang.masters_connect_about(), reply_markup=self.kb.masters_connect_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.feedback_users():
            msg = bot.send_message(self.id, self.lang.feedback_users_about(), reply_markup=self.kb.sign_in())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.bonus_system():
            msg = bot.send_message(self.id, self.lang.bonus_system_about(), reply_markup=self.kb.sign_in())
            bot.register_next_step_handler(msg, self.funnel_handler, text)

        elif text == self.lang.back():
            markup = None
            text = None
            print(before, markup, text)

            if before == self.lang.not_finansistic() or before == self.lang.not_time() or before == self.lang.not_motivation() or before == self.lang.finance_stop():
                markup = self.kb.we_talking_kb()
                text = self.lang.we_talking_about()
                before = self.lang.we_talking()
            elif before == self.lang.feedback_users():
                markup = self.kb.masters_connect_kb()
                text = self.lang.masters_connect_about()
                before = self.lang.masters_connect()
            elif before == self.lang.full_version() or before == self.lang.who_use():
                markup = self.kb.how_take_kb()
                text = self.lang.how_take_text()
                before = self.lang.how_take()
            elif before == self.lang.who_do_not_use():
                markup = self.kb.who_use_kb()
                text = self.lang.who_use_about()
                before = self.lang.who_use()
            elif before == self.lang.referal_system() or before == self.lang.bonus_system():
                markup = self.kb.how_work_kb()
                text = self.lang.how_work_about()
                before = self.lang.how_work()
            else:
                before = 'start'
            print(before, markup, text)
            if markup and text:
                msg = bot.send_message(self.id, text, reply_markup=markup)
            else:
                msg = bot.send_photo(self.id, data.banner_photo_id, caption=self.lang.banner(),
                                     reply_markup=self.kb.funnel_kb())
            bot.register_next_step_handler(msg, self.funnel_handler, before)

        else:
            markup = self.kb.funnel_kb()
            if before == self.lang.how_take():
                markup = self.kb.how_take_kb()
            elif before == self.lang.full_version() or before == self.lang.referal_system() or before == self.lang.who_do_not_use() or before == self.lang.feedback_users():
                markup = self.kb.sign_in()
            elif before == self.lang.how_work():
                markup = self.kb.how_work_kb()
            elif before == self.lang.who_use():
                markup = self.kb.who_use_kb()
            elif before == self.lang.we_talking():
                markup = self.kb.we_talking_kb()
            elif before == self.lang.not_finansistic():
                markup = self.kb.not_finansistic_kb()
            elif before == self.lang.not_motivation():
                markup = self.lang.not_motivation()
            elif before == self.lang.not_time():
                markup = self.kb.not_time_kb()
            elif before == self.lang.finance_stop():
                markup = self.kb.finance_stop_kb()
            elif before == self.lang.masters_connect():
                markup = self.kb.masters_connect_kb()
            msg = bot.send_message(self.id, self.lang.kb_choose(), reply_markup=markup)
            bot.register_next_step_handler(msg, self.funnel_handler, before)






####################################################################################################################################

def back_fnc(id):
    user, lang, kb = get_user_and_lang(id=id)
    bot.send_message(id, lang.home_hello(), reply_markup=kb.home_kb(user=user))

def cabinet_fnc(id):
    user, lang, kb = get_user_and_lang(id=id)
    bot.send_message(id, lang.cabinet_info(id=id), reply_markup=kb.team_kb())

def clear_old_msg(old_msg):
    bot.edit_message_text(chat_id=old_msg.chat.id, message_id=old_msg.id, text=old_msg.text)

def chat_fnc(id):
    user, lang, kb = get_user_and_lang(id=id)
    if not user.get('is_active'):
        active_trial = user.get('active_trial')
        bot.send_message(id, lang.chat_info(), reply_markup=kb.plans_kb(active_trial=active_trial))
    else:
        plan_id = user.get('plan_id')
        plan = dbase.take_plan(id=plan_id)
        final_date = user.get('final_date')
        bot.send_message(id, lang.yout_plan(plan=plan, final_date=final_date), parse_mode='Markdown')
def get_user_and_lang(id):
    lang = lang_().get_language()
    user = dbase.take_user(id=id)
    if user:
        lang = user.get('lang')
        lang = lang_().get_language(language=lang)
    kb = keyboards_(lang=lang)
    return user, lang, kb

def mail_admins(text, parse_mode=None, markup=None):
    admins = dbase.take_admins()
    for admin in admins:
        bot.send_message(admin.get('id'), text, reply_markup=markup, parse_mode=parse_mode)

def balances_fnc(id):
    user, lang, kb = get_user_and_lang(id=id)
    balance = dbase.take_balance(id_user=id)
    bot.send_message(id, lang.balance_info(balance=balance), reply_markup=kb.balances_kb())

def deposit_fnc(id):
    user, lang, kb = get_user_and_lang(id=id)
    def one():
        msg = bot.send_message(id, lang.insert_amount_deposit(), reply_markup=kb.back_kb())
        bot.register_next_step_handler(msg, two)
    def two(message):
        text = message.text
        if text == lang.back():
            back_fnc(id)
            return
        try:
            amount = float(text)
            msg = bot.send_message(id, lang.enter_photo_deposit(amount=amount), reply_markup=kb.back_kb())
            bot.register_next_step_handler(msg, send_photo_deposit, amount)
        except:
            msg = bot.send_message(id, lang.only_integer(), reply_markup=kb.back_kb())
            bot.register_next_step_handler(msg, two)
    def send_photo_deposit(message, amount):
        content_type = message.content_type
        if content_type == 'photo':
            file_id = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            transaction = dbase.create_transaction(id_user=id, transaction_type=0, amount=amount,
                                                      photo_id=file_id)
            user_link = get_name_with_link(user=user)
            msg = lang.new_deposit(transaction=transaction, user=user_link)
            markup = kb.deposit_admin_kb(id_transaction=transaction.get('id'))
            mail_admins(text=msg, markup=markup, parse_mode='HTML')
            bot.send_message(id, lang.send_deposit(transaction=transaction), reply_markup=kb.home_kb(user=user))
        else:
            if message.text == lang.back():
                back_fnc(id)
                return
            msg = bot.send_message(id, lang.only_photo(), reply_markup=kb.back_kb())
            bot.register_next_step_handler(msg, send_photo_deposit, amount)
    one()

def get_name_with_link(user=None, user_username=None, user_name=None):
    if user:
        user_name = user.get('first_name')
        user_username = user.get('username')

    if user_username:
        user_name = f'<a href="t.me/{user_username}">{user_name}</a>'
    return user_name


#handlers
#################################################################################################################################

@bot.message_handler(commands=['start'])
def start_hadnler(message):
    id = message.from_user.id
    user, lang, kb = get_user_and_lang(id=id)
    refer_name = None
    if not user:
        if " " in message.text:
            counter = 1
            refer_head = message.text.split(" ")[1]
            refer_id = refer_head

            while True:
                if refer_id:

                    refer = dbase.take_user(id=refer_id)
                    refer_name = get_name_with_link(user=refer)
                    if refer:
                        lang = refer.get('lang')
                        lang = lang_().get_language(language=lang)
                        user_name = get_name_with_link(user_name=message.from_user.first_name,
                                                       user_username=message.from_user.username)
                        msg = lang.new_partner(refer_name=user_name, line=counter)
                        bot.send_message(refer_id, msg, parse_mode='HTML')
                        counter += 1
                        refer_id = refer.get('refer_id')
                    else:
                        break
                else:
                    break
            lang = lang_().get_language()
        else:
            refer_head = False
        dbase.register(message=message, refer_id=refer_head)
        user = dbase.take_user(id=id)
        Funnel(id=id)
        return

    # starting_bot(id=id, user=user)
    # return
    bot.send_message(id, lang.start_msg(refer=refer_name), reply_markup=kb.home_kb(user=user), parse_mode='HTML',
                     disable_web_page_preview=True)



@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    print(message)
@bot.message_handler(content_types=['text'])
def message_handler(message):
    text = message.text
    id = message.from_user.id
    user, lang, kb = get_user_and_lang(id=id)

    is_admin = user.get('is_admin')
    if text == lang.balance():
        balances_fnc(id=id)
    elif text == lang.chat_name():
        chat_fnc(id=id)
    elif text == lang.cabinet():
        cabinet_fnc(id=id)
    elif text == lang.information():
        Funnel(id=id)
    else:
        back_fnc(id=id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    id = call.from_user.id
    callbacks = call.data
    user, lang, kb = get_user_and_lang(id=id)

    bot.edit_message_text(chat_id=id, message_id=call.message.id, text=call.message.text)
    state = callbacks.split("_")
    bot.clear_step_handler_by_chat_id(chat_id=id)
    if state[0] == 'balance':
        if len(state) == 1:
            balances_fnc(id)
    elif state[0] == 'deposit':
        if len(state) == 1:
            deposit_fnc(id)
        elif state[1] == 'confirm' or state[1] == 'unconfirm':

            id_transaction = state[2]
            transaction = dbase.take_transaction(id_transaction=id_transaction)
            is_finished = transaction.get('is_finished')
            id_user = transaction.get('id_user')
            client_user, client_lang = get_user_and_lang(id=id_user)

            if not is_finished:
                if state[1] == 'confirm':
                    dbase.finish_deposit(id_transaction=id_transaction, result=True)
                    bot.send_message(id_user, client_lang.confirmed_deposit(transaction=transaction))
                    bot.send_message(id, lang.confirmed_deposit_admin())
                else:
                    dbase.finish_deposit(id_transaction=id_transaction, result=False)
                    bot.send_message(id_user, client_lang.unconfirmed_deposit(transaction=transaction))
                    bot.send_message(id, lang.unconfirmed_deposit_admin())
            else:
                bot.edit_message_text(chat_id=id, message_id=call.message.id, text=lang.edited_before())

    elif state[0] == 'plan':
        if state[1] == 'buy':
            id_plan = state[2]
            plan = dbase.take_plan(id=id_plan)
            amount = plan.get('amount')
            days = plan.get('days')
            is_trial = plan.get('is_trial')
            is_active = plan.get('is_active')
            bot.send_message(id, lang.you_confirm_trial(amount=amount, days=days, is_trial=is_trial),
                             reply_markup=kb.buy_plan_kb(id=id_plan))
        elif state[1] == 'unconfirm':
            back_fnc(id=id)
        elif state[1] == 'confirm':
            id_plan = state[2]
            response = dbase.create_plan(id_user=id, id_plan=id_plan)
            error = response.get('error')
            print(response)
            if error:
                bot.send_message(id, lang.error_by_plan(), reply_markup=kb.home_kb(user=user))
            else:
                head_id = response.get('head_id')
                if head_id:
                    amount = response.get('amount')
                    for id_user in response:
                        if str(id_user).isdigit():
                            partner = dbase.take_user(id=head_id)
                            partner_name = get_name_with_link(user=partner)
                            info = response.get(id_user)
                            is_active = info.get('is_active')
                            bonus_amount = float(round(eval(f"""{amount} * {info["percent"]} / 100""")))
                            if is_active:
                                bot.send_message(id_user, lang.you_take_bonus(info=info, partner_name=partner_name, bonus_amount=bonus_amount), parse_mode='HTML')
                            percent_for_percent = info.get('percent_for_percent')
                            if percent_for_percent:
                                for id_partner in percent_for_percent:
                                    if str(id_partner).isdigit():
                                        info = percent_for_percent.get(id_partner)
                                        if info:
                                            percent = info.get('percent')
                                            bonus_partner = float(round(eval(f"""{bonus_amount} * {percent} / 100""")))
                                            partner_2 = dbase.take_user(id=id_partner)
                                            partner_name_2 = get_name_with_link(user=partner_2)
                                            bot.send_message(id_user, lang.you_take_bonus_for_percent(info=info, partner_name=partner_name_2, bonus_amount=bonus_partner),
                                                             parse_mode='HTML')
                    bot.send_message(id, lang.buy_complete(), reply_markup=kb.home_kb(user=user))



    elif state[0] == 'team':
        if len(state) == 1:
            team = dbase.take_team_user(id=id)
            bot.edit_message_text(chat_id=id, message_id=call.message.id, text=lang.team_info(team=team))


if __name__ == '__main__':
    bot.polling(True)