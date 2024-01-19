'''
Probe EF 2022
Programm 2-EMAIL.PY
'''


verteiler = '''
caesonia.reich@gmail.com;

tulugaq.guidi@gmx.ch;

adisa23.palmisano@hispeed.ch;
chinwendu.maclean96@bluewin.ch;

foteini.faron@outlook.com;
'''

mitglieder = []

# Ziel:
# mitglieder = [                 .
#     ['Caesonia', 'Reich'],     .
#     ['Tulugaq', 'Guidi'],      .
#     ['Adisa', 'Palmisano'],    .
#     ['Chinwendu', 'MacLean'],  .
#     ['Foteini', 'Faron']       .
# ]                              .

emails = verteiler.split()

for email in emails:
    [name, nachname] = email.split('@')[0].split('.')
    for num in '0123456789':
        name = name.replace(num, '')
        nachname = nachname.replace(num, '')

    # Option 1
    # name = f'{name[0].upper()}{name[1:]}'
    # nachname = f'{nachname[0].upper()}{name[1:]}'

    # Option 2
    name = name.capitalize()
    nachname = nachname.capitalize()

    mitglieder.append([name, nachname])


print(mitglieder)
