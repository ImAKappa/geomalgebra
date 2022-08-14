# AUTOGENERATED! DO NOT EDIT! File to edit: ../02_basisblades.ipynb.

# %% auto 0
__all__ = ['BasisBlade']

# %% ../02_basisblades.ipynb 14
@dataclass(frozen=True)
class BasisBlade:
    # --- Class variables (defined without type hint); shared by all BasisBlades
    bit_bases2d = {0b0: 's', 0b1: 'e1', 0b10: 'e2', 0b11: 'e12'}

    # --- Instance variables; made "immutable" by frozen=True
    # a.k.a scale or magnitude associated with blade
    weight: float = field(default=0.)
    # integer encoding 
    basis: int = field(default=0)
    # basis_name depends on basis, so it can only be set post-initialization
    basis_name: str = field(init=False)

    def __post_init__(self):
        # Update the "immutable" basis_name field
        object.__setattr__(self, 'basis_name', self.bit_bases2d.get(self.basis))

    def __str__(self) -> str:
        """Pretty print like math notation"""
        prettyprint = f'{self.weight if self.weight != 1 else ""}{self.basis_name}'
        return prettyprint
