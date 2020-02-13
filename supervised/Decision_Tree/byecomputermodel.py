from . import decision


class ByeComputerModel(decision.Model):
    NUMBER = 0

    def __init__(self, age, income, student, credit_rating, bye):
        ByeComputerModel.NUMBER += 1
        self._attrs = {
            'age': age,
            'income': income,
            'student': student,
            'credit_rating': credit_rating,
            'bye': bye,
            'number': ByeComputerModel.NUMBER
        }

    @staticmethod
    def get_domain(name) -> list:
        if name == 'age':
            return ['<=30', '31...40', '>40']
        elif name == 'income':
            return ['high', 'medium', 'low']
        elif name == 'student':
            return ['yes', 'no']
        else:
            return ['fair', 'excellent']

    @property
    def is_positive(self) -> bool:
        return self._attrs.get('bye')

    def get_value(self, key):
        return self._attrs.get(key)

    def __str__(self):
        return str(self._attrs.get('number'))

    def __repr__(self):
        return self.__str__()
