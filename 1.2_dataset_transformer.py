from dataclasses import dataclass
from abc import ABC,abstractmethod

@dataclass
class Dataset:
    data: list[any]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def get_data(self):
        return self.data



class Transformer(ABC):
    @abstractmethod
    def transform(self,data: Dataset) -> Dataset:
        ...

class NormalizeTransformer(Transformer):
    def transform(self,data: Dataset) -> Dataset:
        data_return = []
        min_in_data = min(data)
        max_in_data = max(data)
        for x in data:
            data_return.append((x - min_in_data) / (max_in_data - min_in_data if max_in_data - min_in_data!=0 else 0.5))
        return Dataset(data_return)



class Pipeline:
    def __init__(self,transformers: list):
        self.transformers = transformers

    def run(self,data):
        transformers = self.transformers
        for transformer in transformers:
            data = transformer.transform(data)
        return data