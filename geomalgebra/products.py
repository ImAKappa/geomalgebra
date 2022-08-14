# AUTOGENERATED! DO NOT EDIT! File to edit: ../04_products.ipynb.

# %% auto 0
__all__ = ['canonical_sign', 'basis_blade_gp', 'gp']

# %% ../04_products.ipynb 2
# Std library
from array import array
from .basisblades import ga2d, BasisBlade
from .multivectors import Multivector, add

# %% ../04_products.ipynb 16
def canonical_sign(basis_1: int, basis_2: int) -> int:
    """Count the number of basis blade swaps required to get 'a' and 'b' in canonical order
    Canonical order means increasing order is positive, i.e: e1^e2 instead of e2^e1
    """
    basis_1 = basis_1 >> 1
    num_swaps = 0
    while basis_1:
        # Count how many bases in basis_1 are canonically greater than those in basis_2
        num_swaps += int.bit_count(basis_1 & basis_2)
        basis_1 = basis_1 >> 1
    num_swaps_is_odd = (num_swaps & 1) == 0
    return 1. if (num_swaps_is_odd) else -1.

# %% ../04_products.ipynb 19
def basis_blade_gp(b1: BasisBlade, b2: BasisBlade):
    """Geometric Product for basis blades"""
    # if (b1.basis & pga2d.e0) and (b2.basis & pga2d.e0): return BasisBlade(0., pga2d.scalar)
    sign = canonical_sign(b1.basis, b2.basis)
    return BasisBlade(sign * b1.weight * b2.weight, b1.basis ^ b2.basis)

# %% ../04_products.ipynb 25
def gp(m1: Multivector|BasisBlade, m2: Multivector|BasisBlade) -> Multivector:
    """Geometric product for Multivectors and Basis Blades"""
    basis_blades: list[BasisBlade] = list()
    if isinstance(m1, BasisBlade): m1 = Multivector([m1])
    if isinstance(m2, BasisBlade): m2 = Multivector([m2])
    for basis_1 in m1.blades.values():
        for basis_2 in m2.blades.values():
            basis_blades = [*basis_blades, basis_blade_gp(basis_1, basis_2)]
    return Multivector(basis_blades)