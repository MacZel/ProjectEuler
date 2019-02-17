dict_numbers = {
    'EN': {
        '0':['',      '',         ''        ],
        '1':['one',   'eleven',   'ten'     ],
        '2':['two',   'twelve',   'twenty'  ],
        '3':['three', 'thirteen', 'thirty'  ],
        '4':['four',  'fourteen', 'forty'   ],
        '5':['five',  'fifteen',  'fifty'   ],
        '6':['six',   'sixteen',  'sixty'   ],
        '7':['seven', 'seventeen','seventy' ],
        '8':['eight', 'eighteen', 'eighty'  ],
        '9':['nine',  'nineteen', 'ninety'  ]
    },
    'PL': {
        '0':['',        '',                 '',                 '',            ''                ],
        '1':['jeden',   'jedenaście',       'dziesięć',         'sto',         'tysiąc'          ],
        '2':['dwa',     'dwanaście',        'dwadzieścia',      'dwieście',    'dwa tysiące'     ],
        '3':['trzy',    'trzynaście',       'trzydzieści',      'trzysta',     'trzy tysiące'    ],
        '4':['cztery',  'czternaście',      'czterdzieści',     'czterysta',   'cztery tysiące'  ],
        '5':['pięć',    'piętnaście',       'pięćdziesiąt',     'pięćset',     'pięć tysięcy'    ],
        '6':['sześć',   'szesnaście',       'sześćdziesiąt',    'sześćset',    'sześć tysięcy'   ],
        '7':['siedem',  'siedemnaście',     'siedemdziesiąt',   'siedemset',   'siedem tysiący'  ],
        '8':['osiem',   'osiemnaście',      'osiemdziesiąt',    'osiemset',    'osiem tysięcy'   ],
        '9':['dziewięć','dziewiętnaście',   'dziewięćdziesiąt', 'dziewięćset', 'dziewięć tysięcy']
    },
    'DE': {
        '0':['',       '',          ''       ],
        '1':['ein',    'elf',       'zehn'   ],
        '2':['zwei',   'zwölf',     'zwanzig'],
        '3':['drei',   'dreizehn',  'dreiβig'],
        '4':['vier',   'vierzehn',  'vierzig'],
        '5':['fünf',   'fünfzehn',  'fünfzig'],
        '6':['sechs',  'sechzehn',  'sechzig'],
        '7':['sieben', 'siebzehn',  'siebzig'],
        '8':['acht',   'achtzehn',  'achtzig'],
        '9':['neun',   'neunzehn',  'neunzig']
    },
    'CZ':{
        '0':['',       '',            '',           '',          ''             ],
        '1':['jedna',  'jedenáct',    'deset',      'sto',       'tisíc'        ],
        '2':['dva',    'dvanáct',     'dvacet',     'dvě stě',   'dva tisíce'   ],
        '3':['tři',    'třináct',     'třicet',     'tři sta',   'tři tisíce'   ],
        '4':['čtyři',  'čtrnáct',     'čtyřicet',   'čtyři sta', 'čtyři tisíce' ],
        '5':['pĕt',    'patnáct',     'padesát',    'pět set',   'pět tisíc'    ],
        '6':['šest',   'šestnáct',    'šedesát',    'šest set',  'šest tisíc'   ],
        '7':['sedm',   'sedmnáct',    'sedmdesát',  'sedm set',  'sedm tisíc'   ],
        '8':['osm',    'osmnáct',     'osmdesát',   'osm set',   'osm tisíc'    ],
        '9':['devĕt',  'devatenáct',  'devadesát',  'devět set', 'devět tisíc'  ]
    },
    'RU': {
        '0':['',       '',             '',            '',          ''              ],
        '1':['один',   'одиннадцать',  'десять',      'сто',       'тысяча'        ],
        '2':['две',    'двенадцать',   'двадцать',    'двести',    'две тысячи'    ],
        '3':['три',    'тринадцать',   'тридцать',    'триста',    'три тысячи'    ],
        '4':['четыре', 'четырнадцать', 'сорок',       'четыреста', 'четыре тысячи' ],
        '5':['пять',   'пятнадцать',   'пятьдесят',   'пятьсот',   'пять тысяч'    ],
        '6':['шесть',  'шестнадцать',  'шестьдесят',  'шестьсот',  'шесть тысяч'   ],
        '7':['семь',   'семнадцать',   'семьдесят',   'семьсот',   'семь тысяч'    ],
        '8':['восемь', 'восемнадцать', 'восемьдесят', 'восемьсот', 'восемь тысяч'  ],
        '9':['девять', 'девятнадцать', 'девяносто',   'девятьсот', 'девять тысяч'  ]
    },
    'SE': {
        '0':['',      '',        ''        ],
        '1':['ett',   'elva',    'tio'     ],
        '2':['två',   'tolv',    'tjugo'   ],
        '3':['tre',   'tretton', 'trettio' ],
        '4':['fyra',  'fjorton', 'fyrtio'  ],
        '5':['fem',   'femton',  'femtio'  ],
        '6':['sex',   'sexton',  'sextio'  ],
        '7':['sju',   'sjutton', 'sjuttio' ],
        '8':['åtta',  'arton',   'åttio'   ],
        '9':['nio',   'nitton',  'nittio'  ]
    },
    'FI': {
        '0':['',           '',                ''                  ],
        '1':['yksi',       'yksitoista',      'kymmenen'          ],
        '2':['kaksi',      'kaksitoista',     'kaksikymmentä'     ],
        '3':['kolme',      'kolmetoista',     'kolmekymmentä'     ],
        '4':['neljä',      'neljätoista',     'neljäkymmentä'     ],
        '5':['viisi',      'viisitoista',     'viisikymmentä'     ],
        '6':['kuusi',      'kuusitoista',     'kuusikymmentä'     ],
        '7':['seitsemän',  'seitsemäntoista', 'seitsemänkymmentä' ],
        '8':['kahdeksan',  'kahdeksantoista', 'kahdeksankymmentä' ],
        '9':['yhdeksän',   'yhdeksäntoista',  'yhdeksänkymmentä'  ]
    }
}

def number_to_string(number, spacing=True, lang='EN'):
    number_string = ''
    number_len = len(str(number))
    dict_lang = dict_numbers[lang]
    s = ' ' if spacing else ''
    if number_len == 1:
        ones = number
        ones_str = str(ones)
        if ones == 0:
            if lang == 'EN' or lang == 'PL':
                number_string += 'zero'
            elif lang == 'PL':
                number_string += 'zero'
            elif lang == 'DE':
                number_string += 'null'
            elif lang == 'CZ':
                number_string += 'nula'
            elif lang == 'RU':
                number_string += 'нуль'
            elif lang == 'SE':
                number_string += 'noll'
            elif lang == 'FI':
                number_string += 'nolla'
        elif ones == 1:
            if lang == 'EN' or lang == 'PL' or lang == 'RU' or lang == 'FI':
                number_string += dict_lang[ones_str][0]
            elif lang == 'DE':
                number_string += 'eins'
            elif lang == 'CZ':
                number_string += 'jeden'
            elif lang == 'SE':
                number_string += 'en'
        else:
            number_string += dict_lang[ones_str][0]
    elif number_len >= 2:
        tens = number % 100
        number = int(number/100)
        tens_str = str(tens)
        if tens < 10:
            number_string += dict_lang[tens_str[0]][0]
        elif tens < 20:
            if tens == 10:
                number_string += dict_lang['1'][2]
            else:
                number_string += dict_lang[tens_str[1]][1]
        else:
            if lang == 'EN':
                number_string += dict_lang[tens_str[0]][2]
                if spacing and tens_str[1] != '0':
                    number_string += '-'
                number_string += dict_lang[tens_str[1]][0]
            elif lang == 'PL' or lang == 'CZ' or lang == 'RU':
                number_string += dict_lang[tens_str[0]][2]
                if spacing and tens_str[1] != '0':
                    number_string += s
                number_string += dict_lang[tens_str[1]][0]
            elif lang == 'DE':
                number_string += dict_lang[tens_str[1]][0]
                if spacing and tens_str[1] != '0':
                    number_string += 'und'
                number_string += dict_lang[tens_str[0]][2]
            elif lang == 'SE' or lang == 'FI':
                number_string += dict_lang[tens_str[0]][2]
                number_string += dict_lang[tens_str[1]][0]
        if number_len >= 3:
            hundreds = number % 10
            number = int(number/10)
            hundreds_str = str(hundreds)
            if hundreds != 0:
                if lang == 'EN':
                    hundreds_postfix = s.join(('hundred', 'and'))
                    if tens == 0:
                        hundreds_postfix = 'hundred'
                    number_string = s.join((dict_lang[hundreds_str][0], hundreds_postfix, number_string))
                elif lang == 'PL' or lang == 'CZ' or lang == 'RU':
                    number_string = s.join((dict_lang[hundreds_str][3], number_string))
                    if not spacing:
                        number_string = number_string.replace(' ','')
                elif lang == 'DE':
                    hundreds_postfix = 'hundert'
                    number_string = dict_lang[hundreds_str][0] + hundreds_postfix + number_string
                elif lang == 'SE':
                    hundreds_postfix = 'hundra'
                    number_string = dict_lang[hundreds_str][0] + hundreds_postfix + s + number_string
                elif lang == 'FI':
                    hundreds_postfix = 'sata'
                    number_string = hundreds_postfix + dict_lang[hundreds_str][0] + number_string
        if number_len >= 4:
            thousands = number % 10
            number = int(number/10)
            thousands_str = str(thousands)
            if thousands != 0:
                if lang == 'EN':
                    thousands_postfix = s.join(('thousand', 'and'))
                    if hundreds == 0 and tens == 0:
                        thousands_postfix = 'thousand'
                    number_string = s.join((dict_lang[thousands_str][0], thousands_postfix, number_string))
                elif lang == 'PL' or lang == 'CZ' or lang == 'RU':
                    number_string = s.join((dict_lang[thousands_str][4], number_string))
                    if not spacing:
                        number_string = number_string.replace(' ','')
                elif lang == 'DE':
                    thousands_postfix = 'tausend'
                    number_string = dict_lang[thousands_str][0] + thousands_postfix + number_string
                elif lang == 'SE':
                    thousands_postfix = 'tusen'
                    number_string = dict_lang[thousands_str][0] + thousands_postfix + s + number_string
                elif lang == 'FI':
                    thousands_postfix = 'tuhat'
                    number_string = thousands_postfix + dict_lang[thousands_str][0] + number_string
    return(number_string)

def count_chars(start, stop):
    count = 0
    for i in range(start, stop+1):
        count += len(number_to_string(i, spacing=False, lang='EN'))
    return count

print('Solution: ', count_chars(1, 1000), sep='', end='\n')
