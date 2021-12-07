import json

class Model:

    title = '1'
    text = '123'
    author = '12 23'

    def save(self):
        attributes = list(filter(lambda x: not x.startswith('_') and x != 'save', dir(self)))
        dictionary = {}
        for attr in attributes:
            dictionary[attr] = getattr(self, attr)
        with open('5.2.json', mode='w') as f:
            json.dump(dictionary, f, indent=4, ensure_ascii=False)


dat = Model()
dat.save()