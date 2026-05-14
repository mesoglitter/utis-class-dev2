# UTIS Auxiliary-Field Covariant Action Q-2

## 1. Goal

Derive the UTIS suppression kernel:

```text
k²/(k² + kc²)
```

from a local covariant action.

---

## 2. Auxiliary scalar field ansatz

Introduce an auxiliary scalar χ coupled to matter perturbations.

```text
S = ∫ d⁴x √(-g) [
    M_*²/2 R
    -1/2 (∂χ)²
    -1/2 m_χ² χ²
    + β χ δ_cdm
    + L_m
]
```

---

## 3. Quasi-static Fourier-space Lagrangian

```text
beta*chi*delta_cdm + chi**2*(-m_chi**2/2 - k**2/(2*a**2))
```

---

## 4. χ equation of motion

```text
beta*delta_cdm + 2*chi*(-m_chi**2/2 - k**2/(2*a**2)) = 0
```

Solution:

```text
χ_k = a**2*beta*delta_cdm/(a**2*m_chi**2 + k**2)
```

---

## 5. Effective interaction after integrating out χ

```text
a**2*beta**2*delta_cdm**2/(2*(a**2*m_chi**2 + k**2))
```

---

## 6. Emergent UTIS kernel

Effective propagator:

```text
a**2*beta**2/(a**2*m_chi**2 + k**2)
```

Equivalent form:

```text
a**2*beta**2/(a**2*m_chi**2 + k**2)
```

---

## 7. UTIS suppression structure

The normalized scale-dependent suppression becomes:

```text
k**2/(a**2*m_chi**2 + k**2)
```

which directly reproduces the UTIS structure:

```text
k²/(k² + kc²)
```

with:

```text
kc² ↔ a² m_χ²
```

---

## 8. Physical interpretation

- small k:

```text
kernel ~ k²/(a²m_χ²)
```

Suppression weak.

- large k:

```text
kernel → 1
```

Maximum UTIS suppression activated.

---

## 9. Important implication

The UTIS scale-dependent damping is NOT necessarily an arbitrary fitting function.

It can emerge naturally from integrating out a local auxiliary scalar sector.

This is the bridge between:

```text
phenomenological μ(k,a)
```

and:

```text
true covariant EFT structure
```

---

## 10. Next step Q-3

Derive the true quadratic action S^(2) after integrating out χ.

Target:

```text
Q_eff(k,a)
c_s²(k,a)
M_eff²(k,a)
```

directly from the local action.
