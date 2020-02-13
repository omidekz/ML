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

    @staticmethod
    def ig(ant, instances, attr, domain: list) -> float:
        if ant is None:
            ant = Model.entropy(instances)
        instances: List[Model] = instances
        branches = Model.make_branches(attr, domain, instances)
        for pos, neg, pl, nl in branches.values():
            ant -= (pos + neg) / len(instances) * Model.entropy_zero(pos, neg, pos + neg)
        return ant

    @staticmethod
    def make_branches(attr, domain, instances):
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

    @staticmethod
    def entropy(instances):
        pos = 0
        neg = 0
        for ins in instances:
            if ins.is_positive:
                pos += 1
            else:
                neg += 1
        return Model.entropy_zero(pos, neg, len(instances))

    @staticmethod
    def entropy_zero(pos, neg, _all):
        if _all == 0:
            return 0
        pp = pos / _all
        pn = neg / _all
        return -pp * (math.log2(pp) if pp != 0 else 0) - pn * (math.log2(pn) if pn != 0 else 0)
