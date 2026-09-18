from collections import deque
from typing import Dict, Hashable, List, Literal, Set, Tuple

State = Hashable
Transitions = Dict[Tuple[State, str], List[State]]

class NFSA:
    """
    Object-oriented representation of a Non-Deterministic Finite State Automaton.
    """
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

def nd_recognize(
    tape: str, machine: NFSA, strategy: Literal["DFS", "BFS"] = "DFS"
) -> bool:
    """
    Executes the ND-RECOGNIZE state-space search algorithm using a double-ended queue[cite: 1].
    """
    agenda: deque[Tuple[State, int]] = deque()
    agenda.append((machine.start_state, 0))

    while agenda:
        if strategy == "DFS":
            current_node, tape_ptr = agenda.pop()
        elif strategy == "BFS":
            current_node, tape_ptr = agenda.popleft()
        else:
            raise ValueError("Strategy must be 'DFS' or 'BFS'.")

        if tape_ptr == len(tape) and current_node in machine.accept_states:
            return True

        eps_key = (current_node, 'ε')
        if eps_key in machine.transitions:
            for next_state in machine.transitions[eps_key]:
                agenda.append((next_state, tape_ptr))

        if tape_ptr < len(tape):
            sym_key = (current_node, tape[tape_ptr])
            if sym_key in machine.transitions:
                for next_state in machine.transitions[sym_key]:
                    agenda.append((next_state, tape_ptr + 1))

    return False

def compile_sheeptalk_nfsa() -> NFSA:
    """
    Compiles the textbook NFSA for 'baa*!' into the internal data structure[cite: 1].
    """
    transitions = {
        (0, 'b'): [1],
        (1, 'a'): [2],
        (2, 'a'): [2, 3], 
        (3, '!'): [4]
    }
    return NFSA(states={0, 1, 2, 3, 4}, start_state=0, accept_states={4}, transitions=transitions)
