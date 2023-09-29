from pyparsing import nums, alphas, Word, Literal, Optional, Combine, Forward, Group, Suppress, OneOrMore

def bprint(obj):
    print(obj.__repr__().decode('string_escape'))

# База данных единиц измерения
unit_db = {'Длина':{'м':1, 'дм':1/10, 'см':1/100, 'мм':1/1000, 'км':1000, 'мкм':1/1000000}, 'Сила':{'Н':1}, 'Мощность':{'Вт':1, 'кВт':1000}, 'Время':{'с':1}, 'Масса':{'кг':1, 'г':0.001}}
unit_set = set([t for vals in unit_db.values() for t in vals])

# Парсер для единицы измерения с проверкой её по базе данных
rus_alphas = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
def check_unit(unit_name):
    """
    Проверка единицы измерения по базе данных.
    """
    if not unit_name in unit_set:
        raise ValueError("Единица измерения указана неверно или отсутствует в базе данных: " + unit_name)
    return(unit_name)
ph_unit = Word(rus_alphas+alphas, rus_alphas+alphas+'.').setParseAction(lambda t: check_unit(t.asList()[0]))

# Парсер для степени
int_num = Word(nums)
pm_sign = Optional(Suppress("+") | Literal("-"))
float_num = Combine(pm_sign + int_num + Optional('.' + int_num) + Optional('e' + pm_sign + int_num)).setParseAction(lambda t: float(t.asList()[0]))

# Парсер для единицы измерения со степенью
single_unit = (ph_unit('unit_name') + Optional(Suppress('^') + float_num('unit_degree'))).setParseAction(lambda t: (t.unit_name, float(1) if t.unit_degree == "" else t.unit_degree))

# Парсер для выражения в скобках
unit_expr = Forward()
unit_expr << Group(Suppress('(') + single_unit + Optional(OneOrMore((Literal("*") | Literal("/")) + (single_unit | unit_expr))) + Suppress(")"))

# Парсер для общего выражения единицы измерения
def transform_unit(unit_list, k=1):
    """
    Функция раскрывает скобки в результате, выданном парсером, корректирует знак степени и убирает знаки * и /
    """
    res = []
    for v in unit_list:
        if isinstance(v, tuple):
            res.append(tuple((v[0], v[1]*k)))
        elif v == "/":
            k = -k
        elif isinstance(v, list):
            res += transform_unit(v, k=k)
    return(res)
parse_unit = ((unit_expr | single_unit) + Optional(OneOrMore((Literal("*") | Literal("/")) + (single_unit | unit_expr)))).setParseAction(lambda t: transform_unit(t.asList()))

#Проверка
s = "(кг)"
bprint(parse_unit.parseString(s).asList())