# DFA para Σ = {0,1} con Q = {q0, q1, q2}
# Acepta exactamente las cadenas que terminan en 0.

from typing import Dict, Set, Tuple, Iterable

class DFA:
    def __init__(self,
                 states: Set[str],
                 alphabet: Set[str],
                 delta: Dict[Tuple[str, str], str],
                 q0: str,
                 accept: Set[str]) -> None:
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.q0 = q0
        self.accept = accept

    def step(self, state: str, symbol: str) -> str:
        if symbol not in self.alphabet:
            raise ValueError(f"Símbolo inválido: {symbol}")
        return self.delta[(state, symbol)]

    def run(self, w: Iterable[str]) -> Tuple[str, bool]:
        state = self.q0
        for s in w:
            state = self.step(state, s)
        return state, (state in self.accept)

# Definición del autómata según el diagrama
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
q0 = "q0"
accept = {"q1"}

dfa = DFA(states, alphabet, delta, q0, accept)

# Ejemplos de uso
tests = ["0", "10", "110", "101010", "", "1", "011", "1111"]
for w in tests:
    final_state, ok = dfa.run(list(w))
    print(f"w='{w:>6}' -> estado_final={final_state}, acepta={ok}")
