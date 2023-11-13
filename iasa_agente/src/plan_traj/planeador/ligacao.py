from dataclasses import dataclass
### Ligação

@dataclass
class Ligacao:
    origem: str
    destino: str
    custo: int

