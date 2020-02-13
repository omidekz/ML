from . import decision


class WeatherModel(decision.Model):

    def __init__(self, **_attrs):
        self._attrs = _attrs

    @staticmethod
    def get_domain(name):
        if name == 'outlook':
            return ['sunny', 'overcast', 'rain']
        elif name == 'wind':
            return ['weak', 'strong']
        elif name == 'humidity':
            return ['high', 'normal']
        elif name == 'temp':
            return ['hot', 'cool', 'mild']

    @property
    def is_positive(self):
        return self._attrs.get('enjoy')

    def get_value(self, key):
        return self._attrs.get(key)

    def __str__(self):
        return str(self._attrs.get('number'))

    def __repr__(self):
        return self.__str__()
