from collections import deque
from typing import Dict, Hashable, List, Literal, Set, Tuple

State = Hashable
Transitions = Dict[Tuple[State, str], List[State]]

class NFSA:
    def __init__(
        self,
        states: Set[State],
        start_state: State,
        accept_states: Set[State],
        transitions: Transitions,
    ) -> None:
        self.states = states
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def __repr__(self) -> str:
        return (f"NFSA(states={self.states}, start_state={self.start_state}, "
                f"accept_states={self.accept_states}, transitions={self.transitions})")

def nd_recognise(
    tape: str, machine: NFSA, strategy: Literal["DFS", "BFS"] = "DFS"
) -> bool:
    agenda: deque[Tuple[State, int]] = deque()
    agenda.append((machine.start_state, 0))

    while agenda:
        if strategy == "DFS":
            current_node, tape_pointer_location = agenda.pop()
        elif strategy == "BFS":
            current_node, tape_pointer_location = agenda.popleft()
        else:
            raise ValueError("Strategy must be 'DFS' or 'BFS'.")

        if tape_pointer_location == len(tape) and current_node in machine.accept_states:
            return True

        epsilon_key = (current_node, 'ε')
        if epsilon_key in machine.transitions:
            for next_state in machine.transitions[epsilon_key]:
                agenda.append((next_state, tape_pointer_location))

        if tape_pointer_location < len(tape):
            symbol_key = (current_node, tape[tape_pointer_location])
            if symbol_key in machine.transitions:
                for next_state in machine.transitions[symbol_key]:
                    agenda.append((next_state, tape_pointer_location + 1))

    return False

def compile_sheeptalk_nfsa() -> NFSA:
    transitions = {
        (0, 'b'): [1],
        (1, 'a'): [2],
        (2, 'a'): [2, 3], 
        (3, '!'): [4]
    }
    return NFSA(states={0, 1, 2, 3, 4}, start_state=0, accept_states={4}, transitions=transitions)


def __repr__(self) -> str:
    return (f"NFSA(states={self.states}, start_state={self.start_state}, "
            f"accept_states={self.accept_states}, transitions={self.transitions})")


if __name__ == "__main__":
    print(compile_sheeptalk_nfsa())
