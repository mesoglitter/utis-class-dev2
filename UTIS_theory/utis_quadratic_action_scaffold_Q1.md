# UTIS Quadratic Action Scaffold Q-1

## 1. Quadratic scalar perturbation ansatz

```text
S^(2) = 1/2 ∫ dt d^3k a^3 [
    Q(t,k) * pi_dot^2
    - Q(t,k) * c_s^2(t,k) * k^2/a^2 * pi^2
    - M_eff^2(t,k) * pi^2
]
```

---

## 2. Lagrangian density

```text
a**3*(-M2(t)*pi(t)**2 + Q(t)*Derivative(pi(t), t)**2 - k**2*Q(t)*c_s2(t)*pi(t)**2/a**2)/2
```

---

## 3. Canonical momentum

```text
a**3*Q(t)*Derivative(pi(t), t)
```

---

## 4. Hamiltonian density

```text
a*(a**2*M2(t)*pi(t)**2 + a**2*Q(t)*Derivative(pi(t), t)**2 + k**2*Q(t)*c_s2(t)*pi(t)**2)/2
```

---

## 5. Euler-Lagrange equation

```text
a*(a**2*Q(t)*Derivative(pi(t), (t, 2)) + a**2*Derivative(Q(t), t)*Derivative(pi(t), t) + (a**2*M2(t) + k**2*Q(t)*c_s2(t))*pi(t)) = 0
```

---

## 6. Principal symbol

```text
P(omega,k) = Q*omega^2 - Q*c_s^2*k^2/a^2

omega^2 = c_s^2*k^2/a^2
```

---

## 7. Stability conditions

- No ghost: Q(t,k) > 0
- No gradient instability: c_s^2(t,k) > 0
- Hamiltonian bounded below: H2 >= 0
- Hyperbolicity: Q*omega^2 - Q*c_s^2*k^2/a^2 has real roots
- No UV strong coupling: Q does not collapse to zero

---

## 8. UTIS proxy interpretation

Current CLASS + proxy audits already showed:

```text
Q_eff_proxy > 0
c_eff^2_proxy > 0
phase_speed^2 > 0
Hamiltonian proxy >= 0
UV strong coupling proxy finite
```

This means the next step is deriving Q and c_s^2 from a true covariant action.

---

## 9. Next step Q-2

Construct auxiliary-field covariant action reproducing:

```text
mu(k,a) = 1 - S0*gate(a)*k^2/(k^2+kc^2)
```

Candidate structure:

```text
S = ∫ d^4x sqrt(-g) [
    M_*^2/2 R
    -1/2 Z(chi)(∂chi)^2
    -1/2 m_chi^2 chi^2
    + beta(a) chi δ_cdm
    + L_m
]
```

Quasi-static integration gives:

```text
chi_k ~ beta δ_cdm / (k^2/a^2 + m_chi^2)
```

which naturally generates:

```text
k^2/(k^2 + a^2 m_chi^2)
```
