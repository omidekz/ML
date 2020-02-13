from abc import ABC, abstractmethod
from typing import List
import math


class Model(ABC):
    @staticmethod
    @abstractmethod
    def get_domain(name) -> list:
        ...

    @property
    @abstractmethod
    def is_positive(self) -> bool:
        ...

    @abstractmethod
    def get_value(self, key):
        ...


def make_branches(attr, domain, instances):
    # branches shape:
    # dict(
    #       attribute_name:
    #           List[
    #               positive_number,
    #               negative_number,
    #               List[positive_instances],
    #               List[negative_instances]
    #           ]
    # )
    branches = dict([(d, [0, 0, [], []]) for d in domain])
    for ins in instances:
        key = ins.get_value(attr)
        if ins.is_positive:
            branches.get(key)[0] += 1
            branches.get(key)[2].append(ins)
        else:
            branches.get(key)[1] += 1
            branches.get(key)[3].append(ins)
    return branches


def entropy(instances):
    """
    count positive, negative instances and calc entropy
    :param instances: List[Model]
    :return: entropy - float
    """
    pos = 0
    neg = 0
    for ins in instances:
        if ins.is_positive:
            pos += 1
        else:
            neg += 1
    return entropy_zero(pos, neg, len(instances))


def entropy_zero(pos, neg, _all):
    """
    gets pos, neg, all value and calc below formula
    Ppos * log2(Ppos) - Pneg * log2(Pneg)
    :param pos: positive number - int
    :param neg: negative number - int
    :param _all: all instances number - int [often equal to pos + neg]
    :return: entropy value
    """
    if _all == 0:
        return 0
    pp = pos / _all
    pn = neg / _all
    return -pp * (math.log2(pp) if pp != 0 else 0) - pn * (math.log2(pn) if pn != 0 else 0)


def information_gain(ant, instances, attr, domain: list) -> float:
    """
    gets entropy, instances, attribute, domain and return information gain\n
    entropy - sigma(1, len(domain)) ((posi+negi)/len(instances)) * entropy_zero(posi, negi, posi+negi)\n
    :param ant: entropy float
    :param instances: List[Model]
    :param attr: attribute
    :param domain: list attribute domain
    :return:
    """
    if ant is None:
        ant = entropy(instances)
    instances: List[Model] = instances
    branches = make_branches(attr, domain, instances)
    for pos, neg, pl, nl in branches.values():
        ant -= (pos + neg) / len(instances) * entropy_zero(pos, neg, pos + neg)
    return ant
