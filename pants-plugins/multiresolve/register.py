from multiresolve import target_types_rules
from multiresolve.target_types import MultiResolvePexBinaryTarget


def target_types():
    return (MultiResolvePexBinaryTarget,)


def rules():
    return (*target_types_rules.rules(),)
