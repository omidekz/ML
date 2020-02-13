from supervised.Decision_Tree import weathermodel, decision, byecomputermodel
from typing import List


def solve(instances: List[decision.Model], attributes: list, path: list = None):
    if path is None:
        path = []
    _max_value, attribute = max_gain(instances, attributes, decision.entropy(instances))
    branches = decision.make_branches(attribute, instances[0].get_domain(attribute), instances)
    attributes.remove(attribute)
    for branch_name, (positive, negative, positive_instances, negative_instances) in branches.items():
        path.append((attribute, branch_name))
        if positive == 0:
            path.pop()
        elif negative == 0:
            print(path)
            path.pop()
        else:
            solve(positive_instances + negative_instances, attributes, path.copy())
            path.pop()
    attributes.append(attribute)


def max_gain(instances, labels, entropy=None):
    if entropy is None:
        entropy = decision.entropy(instances)
    _max, label = None, None
    for lab in labels:
        _val = decision.information_gain(entropy, instances, lab, instances[0].get_domain(lab))
        if _max is None or _val > _max:
            _max = _val
            label = lab
    return _max, label


if __name__ == '__main__':
    _instances = [
        weathermodel.WeatherModel(number=1, outlook='sunny', temp='hot', humidity='high', wind='weak', enjoy=False),
        weathermodel.WeatherModel(number=2, outlook='sunny', temp='hot', humidity='high', wind='strong', enjoy=False),
        weathermodel.WeatherModel(number=3, outlook='overcast', temp='hot', humidity='high', wind='weak', enjoy=True),
        weathermodel.WeatherModel(number=4, outlook='rain', temp='mild', humidity='high', wind='weak', enjoy=True),
        weathermodel.WeatherModel(number=5, outlook='rain', temp='cool', humidity='normal', wind='weak', enjoy=True),
        weathermodel.WeatherModel(number=6, outlook='rain', temp='cool', humidity='normal', wind='strong', enjoy=False),
        weathermodel.WeatherModel(number=7, outlook='overcast', temp='cool', humidity='normal', wind='strong',
                                  enjoy=True),
        weathermodel.WeatherModel(number=8, outlook='sunny', temp='mild', humidity='high', wind='weak', enjoy=False),
        weathermodel.WeatherModel(number=9, outlook='sunny', temp='cool', humidity='normal', wind='weak', enjoy=True),
        weathermodel.WeatherModel(number=10, outlook='rain', temp='mild', humidity='normal', wind='weak', enjoy=True),
        weathermodel.WeatherModel(number=11, outlook='sunny', temp='mild', humidity='normal', wind='strong',
                                  enjoy=True),
        weathermodel.WeatherModel(number=12, outlook='overcast', temp='mild', humidity='high', wind='strong',
                                  enjoy=True),
        weathermodel.WeatherModel(number=13, outlook='overcast', temp='hot', humidity='normal', wind='weak',
                                  enjoy=True),
        weathermodel.WeatherModel(number=14, outlook='rain', temp='mild', humidity='high', wind='strong', enjoy=False)
    ]
    solve(_instances, 'outlook,temp,wind,humidity'.split(','))
    print('=====================================================')
    _instances = [
        byecomputermodel.ByeComputerModel('<=30', 'high', 'no', 'fair', False),
        byecomputermodel.ByeComputerModel('<=30', 'high', 'no', 'excellent', False),
        byecomputermodel.ByeComputerModel('31...40', 'high', 'no', 'fair', True),
        byecomputermodel.ByeComputerModel('>40', 'medium', 'no', 'fair', True),
        byecomputermodel.ByeComputerModel('>40', 'low', 'yes', 'fair', True),
        byecomputermodel.ByeComputerModel('>40', 'low', 'yes', 'excellent', False),
        byecomputermodel.ByeComputerModel('31...40', 'low', 'yes', 'excellent', True),
        byecomputermodel.ByeComputerModel('<=30', 'medium', 'no', 'fair', False),
        byecomputermodel.ByeComputerModel('<=30', 'low', 'yes', 'fair', True),
        byecomputermodel.ByeComputerModel('>40', 'medium', 'yes', 'fair', True),
        byecomputermodel.ByeComputerModel('<=30', 'medium', 'yes', 'excellent', True),
        byecomputermodel.ByeComputerModel('31...40', 'medium', 'no', 'excellent', True),
        byecomputermodel.ByeComputerModel('31...40', 'high', 'yes', 'fair', True),
        byecomputermodel.ByeComputerModel('>40', 'medium', 'no', 'excellent', False)
    ]
    solve(_instances, ['age', 'income', 'student', 'credit_rating'])
