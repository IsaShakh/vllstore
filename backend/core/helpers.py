import re

nullable = dict(blank=True, null=True)

def slugify(s):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya',
    }

    lower_case = s.lower()

    transliterated = ''.join([translit_dict.get(c, c) for c in lower_case])

    # Замена любых неподходящих символов на дефис
    slug = re.sub(r'\W+', '-', transliterated)

    # Удаление лишних дефисов
    slug = re.sub(r'^-+|-+$', '', slug)

    return slug


