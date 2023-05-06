LANG = 'Choose Language/🇬🇧/🇷🇺/🇺🇿'
LANG_RESULT = {
    'en': 'Select Language: <b>English🇬🇧</b>',
    'ru': 'Выбранно язык: <b>Russian</b>',
    'uz': "Tanlangan til: <b>O'zbekcha</b>"
}
START = {
    'en': 'Welcome to Domain Checker Bot.',
    'ru': 'Добро пожаловать в бот для проверки доменов.',
    'uz': 'Domen tekshiruvi botiga xush kelibsiz.'
}
SEARCH = {
    'en': 'Send domain name for Searching🔎.\n<b>Example</b>: domain',
    'ru': 'Отправьте доменное имя для поиска🔎.\n<b>Пример</b>: domain',
    'uz': 'Domen nomini qidirish uchun yuboringkatta🔎.\n <b>Misol</b>: domain'
}
STATUS = {
    'en': 'Send Domain name🖋.\n<b>Example</b>: domain.com',
    'ru': 'Отправить доменное имя🖋.\n<b>Пример</b>: domain.com',
    'uz': 'Domen nomini yuboring🖋.\n<b>Misol</b>: domain.com'
}


def stat(lang, stat_user):
    stat_lang = {
        'en': f'<b>👤Active Users</b> - {stat_user}',
        'ru': f'<b>👤Активные Пользователи</b> - {stat_user}',
        'uz': f'<b>👤Faol Foydalanuvchilar</b> - {stat_user}',
    }
    return stat_lang.get(lang)


def info(information):
    return f'-- Domain Info --\n<b>Domain:</b> {information[0]}\n<b>Zone:</b> {information[1]}\n<b>Status:</b> {information[2].title()}\n' \
           f'<b>Summary</b>: {information[3].title()}\n'
