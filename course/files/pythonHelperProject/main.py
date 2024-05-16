import random

top_landmarks_moscow = [
    "Красная площадь",
    "Кремль",
    "Собор Василия Блаженного",
    "Большой театр",
    "Парк Горького",
    "Московский зоопарк",
    "ВДНХ",
    "Московский Кремль",
    "Третьяковская галерея",
    "Новодевичий монастырь",
    "Коломенское",
    "Московский метрополитен",
    "Храм Христа Спасителя",
    "Музей изобразительных искусств имени Пушкина",
    "Строгинский парк",
    "Сад музеон",
    "Парк культуры и отдыха имени Горького",
    "Московский международный Дом Музыки",
    "Музей космонавтики",
    "Крымская набережная",
    "Московский зоопарк",
    "Музей Пушкина на Арбате",
    "Музей Москвы",
    "Музей Победы",
    "Музей Исаакиевского собора",
    "Музей-квартира Федора Шаляпина",
    "Красная площадь",
    "Кремль",
    "Собор Василия Блаженного",
    "Большой театр",
    "Парк Горького",
    "Московский зоопарк",
    "ВДНХ",
    "Московский Кремль",
    "Третьяковская галерея",
    "Новодевичий монастырь",
    "Коломенское",
    "Московский метрополитен",
    "Храм Христа Спасителя",
    "Музей изобразительных искусств имени Пушкина",
    "Строгинский парк",
    "Сад музеон",
    "Парк культуры и отдыха имени Горького",
    "Московский международный Дом Музыки",
    "Музей космонавтики",
    "Крымская набережная",
    "Московский зоопарк",
    "Музей Пушкина на Арбате",
    "Музей Москвы",
    "Музей Победы",
    "Музей Исаакиевского собора",
    "Музей-квартира Федора Шаляпина",
    "Музей детства",
    "Музей современного искусства «Гараж»",
    "Парк Зарядье",
    "Государственный музей изобразительных искусств имени А.С. Пушкина",
    "Московская государственная консерватория им. П.И. Чайковского",
    "Киностудия Мосфильм",
    "Московский музей современного искусства на Эрарте",
    "Центральный дом художника",
    "Московский музей архитектуры",
    "Музей кукол",
    "Московская детская художественная галерея",
    "Парк Лосиный остров",
    "Музей Московского метрополитена",
    "Парк Патриот",
    "Парк Коломенское",
    "Музей-квартира А.М. Васнецова",
    "Московский музей кино",
    "Московский музей декоративно-прикладного искусства",
    "Музей Востока",
    "Московский областной музей изобразительных искусств имени И.Н. Крамского",
    "Музей железных дорог России",
    "Музей городского транспорта",
    "Музей истории Москвы",
    "Московский музей архитектуры",
    "Музей-заповедник «Царицыно»",
    "Московский планетарий",
    "Московский музей истории московского футбола",
    "Московский зоомузей",
    "Музей истории литературы",
    "Музей советских игровых автоматов",
    "Московский государственный академический театр детей и молодежи на Таганке",
    "Московский музей естественной истории",
    "Музей космонавтики и ракетных войск РФ",
    "Московский музей ретроавтомобилей",
    "Музей физической культуры и спорта России",
    "Московский музей миниатюр",
    "Музей бронетехники",
    "Музей животных",
    "Московский областной краеведческий музей",
    "Московский музей кукол и детских книг",
    "Музей кино и мультимедиа",
    "Музей военной техники",
    "Московский музей медицины",
    "Музей археологии",
    "Московский областной художественный музей имени И.В. Сурикова",
    "Музей авиации",
    "Музей народного искусства",
    "Московский музей садово-паркового искусства",
    "Музей хоккея"
]

guides = [2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 20]
tourists = [1, 5, 12, 14, 18, 19, 24, 25, 26, 27, 28]
routes_arr = {
    1
    :
        2147
    ,

    2
    :
        2520
    ,

    3
    :
        1691
    ,

    4
    :
        7801
    ,

    5
    :
        1037
    ,

    6
    :
        4357
    ,

    7
    :
        8455
    ,

    8
    :
        5172
    ,

    9
    :
        5874
    ,

    10
    :
        2081
    ,

    11
    :
        4331
    ,

    12
    :
        4680
    ,

    13
    :
        7215
    ,

    14
    :
        7506
    ,

    15
    :
        2772
    ,

    16
    :
        8189
    ,

    17
    :
        8076
    ,

    18
    :
        2367
    ,

    19
    :
        8120
    ,

    20
    :
        9597
    ,

    21
    :
        9614
    ,

    22
    :
        5962
    ,

    23
    :
        2267
    ,

    24
    :
        2287
    ,

    25
    :
        6781
    ,

    26
    :
        5733
    ,

    27
    :
        9860
    ,

    28
    :
        4380
    ,

    29
    :
        5697
    ,

    30
    :
        6682
    ,

    31
    :
        9753
    ,

    32
    :
        6586
    ,

    33
    :
        5827
    ,

    34
    :
        3728
    ,

    35
    :
        4193
    ,

    36
    :
        5489
    ,

    37
    :
        4735
    ,

    38
    :
        2379
    ,

    39
    :
        6584
    ,

    40
    :
        2222
    ,

    41
    :
        1110
    ,

    42
    :
        5174
    ,

    43
    :
        5445
    ,

    44
    :
        8293
    ,

    45
    :
        8661
    ,

    46
    :
        9044
    ,

    47
    :
        2204
    ,

    48
    :
        8917
    ,

    49
    :
        1396
    ,

    50
    :
        2826
    ,

    51
    :
        9891
    ,

    52
    :
        3816
    ,

    53
    :
        5491
    ,

    54
    :
        6311
    ,

    55
    :
        4097
    ,

    56
    :
        2805
    ,

    57
    :
        5273
    ,

    58
    :
        6710
    ,

    59
    :
        2946
    ,

    60
    :
        6587
    ,

    61
    :
        9243
    ,

    62
    :
        6506
    ,

    63
    :
        8542
    ,

    64
    :
        6087
    ,

    65
    :
        6896
    ,

    66
    :
        5695
    ,

    67
    :
        8602
    ,

    68
    :
        1877
    ,

    69
    :
        7998
    ,

    70
    :
        9196
    ,

    71
    :
        8602
    ,

    72
    :
        8593
    ,

    73
    :
        6768
    ,

    74
    :
        9334
    ,

    75
    :
        6770
    ,

    76
    :
        4584
    ,

    77
    :
        9288
    ,

    78
    :
        4362
    ,

    79
    :
        7136
    ,

    80
    :
        5118
    ,

    81
    :
        2571
    ,

    82
    :
        6055
    ,

    83
    :
        3349
    ,

    84
    :
        7398
    ,

    85
    :
        8345
    ,

    86
    :
        5036
    ,

    87
    :
        2336
    ,

    88
    :
        9999
    ,

    89
    :
        2815
    ,

    90
    :
        3361
    ,

    91
    :
        1627
    ,

    92
    :
        4563
    ,

    93
    :
        1329
    ,

    94
    :
        8799
    ,

    95
    :
        7914
    ,

    96
    :
        3684
    ,

    97
    :
        2743
    ,

    98
    :
        4036
    ,

    99
    :
        5053
    ,
}


def routes():
    for i in range(1, 100):
        route = ''
        for i in range(random.randint(5, 15)):
            route += "&" + top_landmarks_moscow[random.randint(0, len(top_landmarks_moscow) - 1)]
        print(f"INSERT INTO routes(route, guide_id, duration, price_per_person) VALUES ('{route[1:]}', "
              f"{random.choice(guides)}, {random.randint(1, 6)}, {random.randint(1000, 10000)});")


def users():
    for i in range(21, 26):
        print(f"INSERT INTO users(role, firstname, lastname, middlename, login, password_hash) VALUES " +
              # f"('{'guide' if random.randint(0, 1) == 0 else 'tourist'}', "
              f"('tourist', " +
              f"'user{i}_firstname', " +
              f"'user{i}_lastname', " +
              f"'user{i}_middlename'," +
              f"'user{i}'," +
              f"SHA2('user{i}', 256));")


def orders():
    for i in range(1, 30):
        route = random.choice(list(routes_arr.keys()))
        count = random.randint(1, 15)
        print(f"INSERT INTO orders(user_id, route_id, person_count, total_price) VALUES ("
              f"{random.choice(tourists)}, {route}, {count}, {count * routes_arr[route]});")

orders()