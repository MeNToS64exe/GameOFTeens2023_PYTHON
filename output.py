languages = ['🇺🇦 Українська', '🇬🇧 English']

ua = languages[0]
en = languages[1]

devices = {
    ua: ['📱Телефон', '📋Планшет', '⌚️Смарт Годинник', '📶Wi-Fi Роутер', '🎥Інше'],
    languages[1]: ['Phone', 'Tablet', 'Smart Watch', 'Wi-Fi Router', 'Other'],
}

criterias_list = {
    ua: {
        'gigabytes': ['Меньше ніж 10', 'Від 10 до 25', 'Більше ніж 25'],
        'minutes': ['Менше ніж 600', 'Від 600 до 1000', 'Більше ніж 1000'],
        'hours': ['Менше ніж 5', 'Від 5 до 10', 'Більше ніж 10'],
        'usage': ['🎥Ютуб', '👥Соц. Мережі', '🌐Браузер'],
        'download': ['👶Мінімальною', '🧑Середньою', '👴Максимальною'],
        'sharing': ['Хочу!', 'Ні, дякую']
    },
    languages[1]: {
        'gigabytes': ['Less than 10', 'From 10 to 25', 'More than 25'],
        'minutes': ['Less than 600', 'From 600 to 1000', 'More than 1000'],
        'hours': ['Less than 5', 'From 5 to 10', 'More than 10'],
        'usage': ['🎥YouTube', '👥Social Media', '🌐Browser'],
        'download': ['👶Low', '🧑Medium', '👴High'],
        'sharing': ['I do!', 'No, thanks']
    }
}

questions = {
    ua: {
        0: {
            'text': '👋Вітаю! Я – TarifSage, бот, який підкаже тобі найкращий тариф на основі невеликого опитування😉\n\n👤Спочатку хочу запитати, чи є ти зараз клієнтом LifeCell?',
            'options': ['Так', 'Ні']
        },
        1: {
            'text': 'Дуже добре👍\n\n🤔А тепер давай визначимося, для якого пристрою ти вибираєш собі тариф?',
            'options': devices[languages[0]]
        },
        devices[ua][0]: {
            0: {
                'text': 'Добре, так і запишемо!\😉\n\n📞 А тепер скажи, чи ти вже приблизно знаєш, скільки гігабайт інтернету і хвилин дзвінка тобі потрібно?🤔',
                'options': ['Так', 'Ні']
            },
            'Так': {
                0: {
                    'text': '1/3\nВау!🤩 Я бачу ти впевнений користувач мобільного інтернету🔥\n\n🤔 Скажи, все ж таки скільки ГБ мобільного інтернету вам за місяць потрібно?',
                    'options': criterias_list[languages[0]]['gigabytes']
                },
                1: {
                    'text': '2/3\n✍️ Записано!\n\n📱А скільки хвилин дзвінка тобі потрібно щомісяця?',
                    'options': criterias_list[languages[0]]['minutes']
                },
                2: {
                    'text': '3/3\n👌 Врахуємо!\n👨‍👩‍👧‍👦 Отже, останнє запитання: чи хочеш ти поділити свій тариф зі своїми друзями чи з сім\'єю?',
                    'options': criterias_list[languages[0]]['sharing']
                }
            },
            'Ні': {
                0: {
                    'text': '1/5\nЦе не біда, зараз з\'ясуємо😉\n🤔Скажи, скільки приблизно годин на тиждень ти проводиш, використовуючи мобільний інтернет?',
                    'options': criterias_list[languages[0]]['hours']
                },
                1: {
                    'text': '2/5\n✍️ Записано!\n\n📱А скільки хвилин дзвінка тобі потрібно щомісяця?',
                    'options': criterias_list[languages[0]]['minutes']
                },
                2: {
                    'text': '3/5\nПасує 😎\n\n📱А які сервіси ти використовуєш найчастіше?',
                    'options': criterias_list[languages[0]]['usage']
                },
                3: {
                    'text': '4/5😊\nЧудово! Залишилось зовсім трохи!\n\n👀Скажи, а з якою частотою ти займаєшся скачуванням файлів, тривалим потоковим переглядом якогось відео чи музики? Словом тим, що споживає особливо багато інтернету',
                    'options': criterias_list[languages[0]]['download']
                },
                4: {
                    'text': '5/5\n👌 Врахуємо!\n👨‍👩‍👧‍👦 Отже, останнє запитання: чи хочеш ти поділити свій тариф зі своїми друзями чи з сім\'єю?',
                    'options': criterias_list[languages[0]]['sharing']
                }
            }

        },
        devices[ua][1]: {
            0: {
                'text': 'Вау!🤩 Досить рідкісний вибір девайсу👍\n\n📞Скажи, чи ти плануєш робити дзвінки на своєму пристрої?',
                'options': ['Так', 'Ні']
            }
        },
        devices[ua][2]: 0,
        devices[ua][3]: 0,
        devices[ua][4]: 0,
    },


    languages[1]: {
        0: {
            'text': '👋 Hey! I\'m TarifSage, a bot that will tell you the best tariff based on a small survey😉\n\n👤First I want to ask, are you currently a LifeCell customer?',
            'options': ['Yes', 'No']
        },
        1: {
            'text': 'Very good👍\n\n🤔Now let\'s decide for which device you choose a tariff?',
            'options': devices[languages[1]]
        },
        devices[en][0]: {
            0: {
                'text': 'OK, noted!\😉\n\n📞 Now tell me, do you already know approximately how many gigabytes of Internet and call minutes you need?',
                'options': ['Yes', 'No']
            },
            'Yes': {
                0: {
                    'text': '1/3\nWow!🤩 I see you are a confident mobile Internet user🔥\n\n🤔 Tell me, how many GB of mobile Internet do you need per month?',
                    'options': criterias_list[languages[1]]['gigabytes']
                },
                1: {
                    'text': '2/3\n✍️ Got it!\n\n📱And how many call minutes do you need every month?',
                    'options': criterias_list[languages[1]]['minutes']
                },
                2: {
                    'text': '3/3\n👌 Considered!\n👨‍👩‍👧‍👦 So, the last question: do you want to share your tariff with your friends or family?',
                    'options': criterias_list[languages[1]]['sharing']
                }
            },
            'No': {
                0: {
                    'text': '1/5\nIt\'s not a problem, we\'ll find out now😉\n🤔Tell me, approximately how many hours a week do you spend using the mobile Internet?',
                    'options': criterias_list[languages[1]]['hours']
                },
                1: {
                     'text': '2/5\n✍️ Noted!\n\n📱And how many call minutes do you need every month?',
                    'options': criterias_list[languages[1]]['minutes']
                },
                2: {
                    'text': '3/5\nCool 😎\n\n📱What services do you use most often?',
                    'options': criterias_list[languages[1]]['usage']
                },
                3: {
                   'text': '4/5😊\nGreat! There is quite a bit left!\n\n👀Tell me, how often do you download files, long-term streaming of some video or music? In other words, what consumes a lot of Internet',
                    'options': criterias_list[languages[1]]['download']
                },
                4: {
                    'text': '5/5\n👌 Considered!\n👨‍👩‍👧‍👦 So, the last question: do you want to share your tariff with your friends or family?',
                    'options': criterias_list[languages[1]]['sharing']
                }
            }

        },
        devices[en][1]: {
            0: {
                'text': 'Calls?',
                'options': ['Yes', 'No']
            }
        },
        devices[en][2]: 0,
        devices[en][3]: 0,
        devices[en][4]: 0,
    }
}

tariffs = {
    "Вільний Лайф": [0, {
        criterias_list[ua]['gigabytes'][0]: -1,
        criterias_list[ua]['gigabytes'][1]: 1,
        criterias_list[ua]['gigabytes'][2]: 3,

        criterias_list[ua]['hours'][0]: -1,
        criterias_list[ua]['hours'][1]: 0,
        criterias_list[ua]['hours'][2]: 3,

        criterias_list[ua]['minutes'][0]: -1,
        criterias_list[ua]['minutes'][1]: 1,
        criterias_list[ua]['minutes'][2]: 2,

        criterias_list[ua]['usage'][0]: 3,
        criterias_list[ua]['usage'][1]: 2,
        criterias_list[ua]['usage'][2]: 1,

        criterias_list[ua]['download'][0]: -1,
        criterias_list[ua]['download'][1]: 1,
        criterias_list[ua]['download'][2]: 2,

        criterias_list[en]['gigabytes'][0]: -1,
        criterias_list[en]['gigabytes'][1]: 1,
        criterias_list[en]['gigabytes'][2]: 3,

        criterias_list[en]['hours'][0]: -1,
        criterias_list[en]['hours'][1]: 0,
        criterias_list[en]['hours'][2]: 3,

        criterias_list[en]['minutes'][0]: -1,
        criterias_list[en]['minutes'][1]: 1,
        criterias_list[en]['minutes'][2]: 2,

        criterias_list[en]['usage'][0]: 3,
        criterias_list[en]['usage'][1]: 2,
        criterias_list[en]['usage'][2]: 1,

        criterias_list[en]['download'][0]: -1,
        criterias_list[en]['download'][1]: 1,
        criterias_list[en]['download'][2]: 2
    }],
    "Смарт Лайф": [0, {
        criterias_list[ua]['gigabytes'][0]: -1,
        criterias_list[ua]['gigabytes'][1]: 3,
        criterias_list[ua]['gigabytes'][2]: 1,

        criterias_list[ua]['hours'][0]: -1,
        criterias_list[ua]['hours'][1]: 1,
        criterias_list[ua]['hours'][2]: 2,

        criterias_list[ua]['minutes'][0]: 0,
        criterias_list[ua]['minutes'][1]: 2,
        criterias_list[ua]['minutes'][2]: 1,

        criterias_list[ua]['usage'][0]: 1,
        criterias_list[ua]['usage'][1]: 2,
        criterias_list[ua]['usage'][2]: 1,

        criterias_list[ua]['download'][0]: 0,
        criterias_list[ua]['download'][1]: 2,
        criterias_list[ua]['download'][2]: 1,

        criterias_list[en]['gigabytes'][0]: -1,
        criterias_list[en]['gigabytes'][1]: 3,
        criterias_list[en]['gigabytes'][2]: 1,

        criterias_list[en]['hours'][0]: -1,
        criterias_list[en]['hours'][1]: 1,
        criterias_list[en]['hours'][2]: 2,

        criterias_list[en]['minutes'][0]: 1,
        criterias_list[en]['minutes'][1]: 2,
        criterias_list[en]['minutes'][2]: 1,

        criterias_list[en]['usage'][0]: 0,
        criterias_list[en]['usage'][1]: 2,
        criterias_list[en]['usage'][2]: 1,

        criterias_list[en]['download'][0]: 0,
        criterias_list[en]['download'][1]: 2,
        criterias_list[en]['download'][2]: 1
    }],
    "Просто Лайф": [0, {
        criterias_list[ua]['gigabytes'][0]: 3,
        criterias_list[ua]['gigabytes'][1]: 0,
        criterias_list[ua]['gigabytes'][2]: -1,

        criterias_list[ua]['hours'][0]: 3,
        criterias_list[ua]['hours'][1]: 0,
        criterias_list[ua]['hours'][2]: -1,

        criterias_list[ua]['minutes'][0]: 2,
        criterias_list[ua]['minutes'][1]: 0,
        criterias_list[ua]['minutes'][2]: -1,

        criterias_list[ua]['usage'][0]: -1,
        criterias_list[ua]['usage'][1]: 0,
        criterias_list[ua]['usage'][2]: 2,

        criterias_list[ua]['download'][0]: 2,
        criterias_list[ua]['download'][1]: 0,
        criterias_list[ua]['download'][2]: -1,

        criterias_list[en]['gigabytes'][0]: 3,
        criterias_list[en]['gigabytes'][1]: 0,
        criterias_list[en]['gigabytes'][2]: -1,

        criterias_list[en]['hours'][0]: 3,
        criterias_list[en]['hours'][1]: 0,
        criterias_list[en]['hours'][2]: -1,

        criterias_list[en]['minutes'][0]: 2,
        criterias_list[en]['minutes'][1]: 0,
        criterias_list[en]['minutes'][2]: -1,

        criterias_list[en]['usage'][0]: -1,
        criterias_list[en]['usage'][1]: 0,
        criterias_list[en]['usage'][2]: 2,

        criterias_list[en]['download'][0]: 2,
        criterias_list[en]['download'][1]: 0,
        criterias_list[en]['download'][2]: -1
    }],
    "Platinum Лайф": [0, {
        criterias_list[ua]['gigabytes'][0]: -1,
        criterias_list[ua]['gigabytes'][1]: 0,
        criterias_list[ua]['gigabytes'][2]: 3,

        criterias_list[ua]['hours'][0]: -1,
        criterias_list[ua]['hours'][1]: 0,
        criterias_list[ua]['hours'][2]: 3,

        criterias_list[ua]['minutes'][0]: -2,
        criterias_list[ua]['minutes'][1]: 0,
        criterias_list[ua]['minutes'][2]: 2.5,

        criterias_list[ua]['usage'][0]: 3,
        criterias_list[ua]['usage'][1]: 2,
        criterias_list[ua]['usage'][2]: 1,

        criterias_list[ua]['download'][0]: -1,
        criterias_list[ua]['download'][1]: 0.5,
        criterias_list[ua]['download'][2]: 3.5,

        criterias_list[en]['gigabytes'][0]: 1,
        criterias_list[en]['gigabytes'][1]: 0,
        criterias_list[en]['gigabytes'][2]: 3,

        criterias_list[en]['hours'][0]: -1,
        criterias_list[en]['hours'][1]: 0,
        criterias_list[en]['hours'][2]: 3,

        criterias_list[en]['minutes'][0]: -2,
        criterias_list[en]['minutes'][1]: 0,
        criterias_list[en]['minutes'][2]: 2.5,

        criterias_list[en]['usage'][0]: 3,
        criterias_list[en]['usage'][1]: 2,
        criterias_list[en]['usage'][2]: 1,

        criterias_list[en]['download'][0]: -1,
        criterias_list[en]['download'][1]: 0.5,
        criterias_list[en]['download'][2]: 3.5

    }],
    "Шкільний Лайф": [0, {
        criterias_list[languages[0]]['gigabytes'][0]: 1,
        criterias_list[languages[0]]['gigabytes'][1]: 0,
        criterias_list[languages[0]]['gigabytes'][2]: -1,

        criterias_list[languages[0]]['hours'][0]: 1,
        criterias_list[languages[0]]['hours'][1]: 0,
        criterias_list[languages[0]]['hours'][2]: -1,

        criterias_list[languages[0]]['minutes'][0]: -1,
        criterias_list[languages[0]]['minutes'][1]: 1,
        criterias_list[languages[0]]['minutes'][2]: 3,

        criterias_list[languages[0]]['usage'][0]: -1,
        criterias_list[languages[0]]['usage'][1]: 0,
        criterias_list[languages[0]]['usage'][2]: 0.5,

        criterias_list[languages[0]]['download'][0]: 1,
        criterias_list[languages[0]]['download'][1]: 0,
        criterias_list[languages[0]]['download'][2]: -1,

        criterias_list[languages[1]]['gigabytes'][0]: 1,
        criterias_list[languages[1]]['gigabytes'][1]: 0,
        criterias_list[languages[1]]['gigabytes'][2]: -1,

        criterias_list[languages[1]]['hours'][0]: 1,
        criterias_list[languages[1]]['hours'][1]: 0,
        criterias_list[languages[1]]['hours'][2]: -1,

        criterias_list[languages[1]]['minutes'][0]: -1,
        criterias_list[languages[1]]['minutes'][1]: 1,
        criterias_list[languages[1]]['minutes'][2]: 3,

        criterias_list[languages[1]]['usage'][0]: -1,
        criterias_list[languages[1]]['usage'][1]: 0,
        criterias_list[languages[1]]['usage'][2]: 0.5,

        criterias_list[languages[1]]['download'][0]: 1,
        criterias_list[languages[1]]['download'][1]: 0,
        criterias_list[languages[1]]['download'][2]: -1,
    }]
}

family = {
    "Смарт Сім\'я  S": [0, {
        criterias_list[languages[0]]['gigabytes'][0]: 3,
        criterias_list[languages[0]]['gigabytes'][1]: 0,
        criterias_list[languages[0]]['gigabytes'][2]: -1,

        criterias_list[languages[0]]['hours'][0]: 3,
        criterias_list[languages[0]]['hours'][1]: 0,
        criterias_list[languages[0]]['hours'][2]: -1,

        criterias_list[languages[0]]['minutes'][0]: 2,
        criterias_list[languages[0]]['minutes'][1]: 0,
        criterias_list[languages[0]]['minutes'][2]: -1,

        criterias_list[languages[0]]['usage'][0]: -1,
        criterias_list[languages[0]]['usage'][1]: 0,
        criterias_list[languages[0]]['usage'][2]: 2,

        criterias_list[languages[0]]['download'][0]: 2,
        criterias_list[languages[0]]['download'][1]: 0,
        criterias_list[languages[0]]['download'][2]: -1,

        criterias_list[languages[1]]['gigabytes'][0]: 3,
        criterias_list[languages[1]]['gigabytes'][1]: 0,
        criterias_list[languages[1]]['gigabytes'][2]: -1,

        criterias_list[languages[1]]['hours'][0]: 3,
        criterias_list[languages[1]]['hours'][1]: 0,
        criterias_list[languages[1]]['hours'][2]: -1,

        criterias_list[languages[1]]['minutes'][0]: 2,
        criterias_list[languages[1]]['minutes'][1]: 0,
        criterias_list[languages[1]]['minutes'][2]: 1,

        criterias_list[languages[1]]['usage'][0]: -1,
        criterias_list[languages[1]]['usage'][1]: 0,
        criterias_list[languages[1]]['usage'][2]: 2,

        criterias_list[languages[1]]['download'][0]: 2,
        criterias_list[languages[1]]['download'][1]: 0,
        criterias_list[languages[1]]['download'][2]: -1,
    }],
    "Смарт Сім\'я M": [0, {
        criterias_list[languages[0]]['gigabytes'][0]: -1,
        criterias_list[languages[0]]['gigabytes'][1]: 3,
        criterias_list[languages[0]]['gigabytes'][2]: 1,

        criterias_list[languages[0]]['hours'][0]: -1,
        criterias_list[languages[0]]['hours'][1]: 1,
        criterias_list[languages[0]]['hours'][2]: 2,

        criterias_list[languages[0]]['minutes'][0]: 0,
        criterias_list[languages[0]]['minutes'][1]: 2,
        criterias_list[languages[0]]['minutes'][2]: 1,

        criterias_list[languages[0]]['usage'][0]: 1,
        criterias_list[languages[0]]['usage'][1]: 2,
        criterias_list[languages[0]]['usage'][2]: 1,

        criterias_list[languages[0]]['download'][0]: 0,
        criterias_list[languages[0]]['download'][1]: 2,
        criterias_list[languages[0]]['download'][2]: 1,

        criterias_list[languages[1]]['gigabytes'][0]: -1,
        criterias_list[languages[1]]['gigabytes'][1]: 3,
        criterias_list[languages[1]]['gigabytes'][2]: 1,

        criterias_list[languages[1]]['hours'][0]: -1,
        criterias_list[languages[1]]['hours'][1]: 1,
        criterias_list[languages[1]]['hours'][2]: 2,

        criterias_list[languages[1]]['minutes'][0]: 0,
        criterias_list[languages[1]]['minutes'][1]: 2,
        criterias_list[languages[1]]['minutes'][2]: 1,

        criterias_list[languages[1]]['usage'][0]: 1,
        criterias_list[languages[1]]['usage'][1]: 2,
        criterias_list[languages[1]]['usage'][2]: 1,

        criterias_list[languages[1]]['download'][0]: 0,
        criterias_list[languages[1]]['download'][1]: 2,
        criterias_list[languages[1]]['download'][2]: 1,
    }],
    "Смарт Сім\'я  L": [0, {
        criterias_list[languages[0]]['gigabytes'][0]: -1,
        criterias_list[languages[0]]['gigabytes'][1]: 1,
        criterias_list[languages[0]]['gigabytes'][2]: 3,

        criterias_list[languages[0]]['hours'][0]: -1,
        criterias_list[languages[0]]['hours'][1]: 0,
        criterias_list[languages[0]]['hours'][2]: 3,

        criterias_list[languages[0]]['minutes'][0]: -1,
        criterias_list[languages[0]]['minutes'][1]: 1,
        criterias_list[languages[0]]['minutes'][2]: 2,

        criterias_list[languages[0]]['usage'][0]: 3,
        criterias_list[languages[0]]['usage'][1]: 2,
        criterias_list[languages[0]]['usage'][2]: 1,

        criterias_list[languages[0]]['download'][0]: -1,
        criterias_list[languages[0]]['download'][1]: 1,
        criterias_list[languages[0]]['download'][2]: 2,

        criterias_list[languages[1]]['gigabytes'][0]: -1,
        criterias_list[languages[1]]['gigabytes'][1]: 1,
        criterias_list[languages[1]]['gigabytes'][2]: 3,

        criterias_list[languages[1]]['hours'][0]: -1,
        criterias_list[languages[1]]['hours'][1]: 0,
        criterias_list[languages[1]]['hours'][2]: 3,

        criterias_list[languages[1]]['minutes'][0]: -1,
        criterias_list[languages[1]]['minutes'][1]: 1,
        criterias_list[languages[1]]['minutes'][2]: 2,

        criterias_list[languages[1]]['usage'][0]: 3,
        criterias_list[languages[1]]['usage'][1]: 2,
        criterias_list[languages[1]]['usage'][2]: 1,

        criterias_list[languages[1]]['download'][0]: -1,
        criterias_list[languages[1]]['download'][1]: 1,
        criterias_list[languages[1]]['download'][2]: 2,
    }]
}

links = {
    devices[ua][0]: {
        'Вільний Лайф': ['🕊Вільний Лайф – твій вірний вибір!\n\nСтворений для тих, хто любить почастувати з переглядом відео на Ютубі або з завантажуванням файлів та музики😉\n\n🌐 Інтернет: Безліміт\n📱Дзвінки: 1600 хв.\n\n✅ Безліміт на lifecell після використання хвилин на номери\n✅Вигода до 15% за послугою «Тарифна підписка»\n\nТискай на кнопку для детальної інформації👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/'],
        'Смарт Лайф': ['📱Смарт Лайф – твій вірний вибір!\n\nЗроблений для тих, хто любить проводити час у месенджерах та соціальних мережах та серфити у браузері😉\n\n🌐 Інтернет: 25 ГБ\n📱Дзвінки: 800 хв.\n\n✅ Безліміт на lifecell після використання хвилин на номери\n✅Безліміт на соціальні мережі\n\nТискай на кнопку для детальної інформації👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/'],
        'Просто Лайф': ['👌Просто Лайф – твій вірний вибір!\n\nІдеально підходить для тих, хто не дуже багато сидить в інтернеті та цілком задовольняє базові потреби сучасної людини😉\n\n🌐 Інтернет: 8 ГБ\n📱Дзвінки: 300 хв.\n\n✅ Безліміт на lifecell після використання хвилин на номери\n✅Вигода до 15% за послугою «Тарифна підписка»\n\nТискай на кнопку для детальної інформації👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/'],
        'Platinum Лайф': ['😎Platinum Лайф – твій вірний вибір!\n\nБув створений спеціально для стримінгу, потокового перегляду фільмів, масованого скачування великих файлів та надзвичайного використання інтернету!🤯А кількість хвилин на дзвінки задовольнить будь-якого затятого любителя поговорити!😉\n\n🌐 Інтернет: Безліміт\n📱Дзвінки: 3000 хв.\n\n✅ Безліміт на lifecell після використання хвилин на номери\Вигода до 15% з послугою «Тарифна підписка»\n\nТискай на кнопку для детальної інформації👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/'],
        'Шкільний Лайф': ['✍️Шкільний Лайф – твій вірний вибір!\n\nІдеально підходить для школьників😉\n\n🌐 Інтернет: 7 ГБ\n📱Дзвінки:Безліміт\n\n✅ Безліміт на lifecell після використання хвилин на номери\n✅Безліміт на два «Обрані номери»\n\nТискай на кнопку для детальної інформації👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/'],
        'Смарт Сім\'я S': ['Смарт Сім\'я S', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/'],
        'Смарт Сім\'я M': ['Смарт Сім\'я M', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/'],
        'Смарт Сім\'я L': ['Смарт Сім\'я L', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/'],
    },
    devices[ua][1]: ['Ґаджет Планшет', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-tab21/'],
    devices[ua][2]: ['Ґаджет Смарт', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/'],
    devices[ua][3]: ['Ґаджет Роутер', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/'],
    devices[ua][4]: ['Ґаджет Безпека', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/'],

    devices[en][0]: {
        'Вільний Лайф': ['🕊Free Life is your right choice!\n\nCreated for those who like to treat themselves to watching videos on YouTube or downloading files and music😉\n\n🌐 Internet: Unlimited\n📱Calls: 1600 min.\n\n ✅ Unlimited lifecell after using minutes for numbers\n ✅Up to 15% benefit for the "Tariff subscription" service\n\nClick on the button for detailed information👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/'],
        'Смарт Лайф': ['📱Smart Life is your right choice!\n\nMade for those who like to spend time in messengers and social networks and surf in the browser😉\n\n🌐 Internet: 25 GB\n📱Calls: 800 min.\n\n ✅ Unlimited lifecell after using minutes for numbers\n ✅ Unlimited social networks\n\nClick on the button for detailed information👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/'],
        'Просто Лайф': ['👌Just Life is your right choice!\n\nIdeal for those who do not spend much time on the Internet and fully meets the basic needs of a modern person😉\n\n🌐 Internet: 8 GB\n📱Calls: 300 min.\n \n ✅ Unlimited lifecell after using minutes for numbers\n ✅ Benefit up to 15% on the "Tariff subscription" service\n\nClick on the button for detailed information👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/'],
        'Platinum Лайф': ['😎Platinum Life is your right choice!\n\nIt was created specifically for streaming, streaming movies, mass downloading of large files and extreme use of the Internet!🤯And the number of minutes for calls will satisfy any avid conversationalist!😉\n\n🌐 Internet: Unlimited\n📱Calls: 3000 min.\n\n ✅ Unlimited lifecell after using minutes for numbers\nUp to 15% benefit with the "Tariff subscription" service\n\nClick on the button for detailed information👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/'],
        'Шкільний Лайф': ['👌School Life is your right choice!\n\nIdeal for schoolchildren😉\n\n🌐 Internet: 7 GB\n📱Calls: Unlimited\n\n ✅ Unlimited lifecell after using minutes for numbers\n ✅ Unlimited for two "Selected numbers"\n\nClick on the button for detailed information👇', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/'],
        'Смарт Сім\'я S': ['Smart Family S', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/'],
        'Смарт Сім\'я M': ['Smart Family M', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/'],
        'Смарт Сім\'я L': ['Smart Family L', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/'],
    },
    devices[en][1]: ['Device Tablet', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-tab21/'],
    devices[en][2]: ['Device Smart', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/'],
    devices[en][3]: ['Device Router', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/'],
    devices[en][4]: ['Device Security', 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/'],
}
