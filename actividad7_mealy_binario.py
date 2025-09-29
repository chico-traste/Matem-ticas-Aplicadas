# Autómata Mealy: salida depende del último símbolo leído
# Convención: output = 1 si el último símbolo fue '0', output = 0 si fue '1'

from typing import Dict, Set, Tuple, Iterable, List

class MealyMachine:
    def __init__(self,
                 states: Set[str],
                 alphabet: Set[str],
                 delta: Dict[Tuple[str, str], str],
                 output: Dict[Tuple[str, str], int],
                 q0: str) -> None:
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.output = output
        self.q0 = q0

    def run(self, w: Iterable[str]) -> Tuple[str, List[int]]:
        state = self.q0
        outs = []
        for s in w:
            if s not in self.alphabet:
                raise ValueError(f"Símbolo inválido: {s}")
            outs.append(self.output[(state, s)])
            state = self.delta[(state, s)]
        return state, outs

states = {"q0", "q1", "q2"}
alphabet = {"0", "1"}
delta = {
    ("q0", "0"): "q1",
    ("q0", "1"): "q2",
    ("q1", "0"): "q1",
    ("q1", "1"): "q2",
    ("q2", "0"): "q1",
    ("q2", "1"): "q2",
}
# Output: 1 si leí '0', 0 si leí '1'
output = {
    ("q0", "0"): 1, ("q0", "1"): 0,
    ("q1", "0"): 1, ("q1", "1"): 0,
    ("q2", "0"): 1, ("q2", "1"): 0,
}

mealy = MealyMachine(states, alphabet, delta, output, "q0")

# Ejemplos de uso
for w in ["100", "1011", "0", "1"]:
    final_state, outs = mealy.run(list(w))
    print(f"w='{w}' -> estado_final={final_state}, outs={outs}")
