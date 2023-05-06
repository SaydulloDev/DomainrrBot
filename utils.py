LANGUAGES = {
    'en': 'English🇬🇧',
    'ru': 'Русский🇷🇺',
    'uz': "O'zbekcha🇺🇿"
}


def is_ascii(char):
    try:
        char.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False


def format_domains(domains):
    formatted_domains = {}
    for i, domain in enumerate(domains):
        formatted_domains[str(i + 1)] = domain
    return formatted_domains


def list_to_dict(lst):
    dct1 = lst.get('status')
    dct = dct1[0]
    lst_info = []
    domain = dct.get('domain')
    zone = dct.get('zone')
    status = dct.get('status')
    summary = dct.get('summary')
    lst_info.append(domain)
    lst_info.append(zone)
    lst_info.append(status)
    lst_info.append(summary)
    return lst_info
