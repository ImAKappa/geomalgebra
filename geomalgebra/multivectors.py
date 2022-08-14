# AUTOGENERATED! DO NOT EDIT! File to edit: ../03_multivectors.ipynb.

# %% auto 0
__all__ = ['Multivector', 'add']

# %% ../03_multivectors.ipynb 2
from dataclasses import dataclass, field, InitVar
from .basisblades import ga2d, BasisBlade

# %% ../03_multivectors.ipynb 8
@dataclass(frozen=True)
class Multivector():

    # InitVar variable is not set as class field, just sent to post_init method
    basis_blades: InitVar[list[BasisBlade]] = None
    blades: dict[int, BasisBlade] = field(init=False, default_factory=dict)
    prettyprint: str = field(init=False, repr=False)

    def __post_init__(self, basis_blades: list[BasisBlade]):
        for bb in basis_blades:
            if self.blades.get(bb.basis, False):
                # If basis blade already exists, sum the weights of the existing and new basis blade
                existing_bb = self.blades[bb.basis]
                self.blades[bb.basis] = BasisBlade(existing_bb.weight + bb.weight, existing_bb.basis)
            else:
                # If basis blade doesn't exist, create a new key-value pair for that basis blade
                self.blades[bb.basis] = bb
        object.__setattr__(self, 'prettyprint', " + ".join(str(b) for b in self.blades.values()))

    def __str__(self) -> str:
        return self.prettyprint

# %% ../03_multivectors.ipynb 14
def add(*args: list[Multivector|BasisBlade]) -> Multivector:
    """Add Multivectors and BasisBlades"""
    basis_blades: list[BasisBlade] = list()
    for m in args: 
        if isinstance(m, Multivector):
            # Convert multivectors/basisblades to a list of BasisBlades
            basis_blades = [*basis_blades, *list(m.blades.values())]
        if isinstance(m, BasisBlade):
            basis_blades = [*basis_blades, m]
    return Multivector(basis_blades)