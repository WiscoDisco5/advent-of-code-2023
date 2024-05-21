from dataclasses import dataclass
from enum import Enum


class Pulse(Enum):
    LOW = 0
    HIGH = 1




def flip_flop(module_state: str, pulse: Pulse):
    if pulse == Pulse.HIGH:
        return module_state, None
    if module_state == "off":
        return "on", Pulse.HIGH
    return "off", Pulse.LOW

def conjoin(module_state: str, pulse: Pulse):


example = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
