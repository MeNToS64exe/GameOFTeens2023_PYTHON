from output import *

def process(criteria, language):
    if not criteria: return [[0]]
    criterias = criteria[1:-1]

    family_bool = criteria[-1] == (questions[ua][devices[ua][0]]['Так'][2]['options'][0], questions[en][devices[en][0]]['Yes'][2]['options'][0])[languages.index(language)]

    for criteria in criterias:
        for arr in (tariffs if not family_bool else family).values():
            print(arr[1])
            arr[0] += arr[1][criteria]

    tariffs_sorted = \
        sorted(tariffs.items(), key=lambda tup: tup[1][0], reverse=True) \
            if not family_bool else \
            sorted(family.items(), key=lambda tup: tup[1][0], reverse=True)

    return tariffs_sorted

