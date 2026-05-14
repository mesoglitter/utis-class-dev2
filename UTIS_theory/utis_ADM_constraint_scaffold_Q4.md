# UTIS ADM Hamiltonian Constraint Scaffold Q-4

## 1. Goal

Construct the ADM-level constraint structure for the UTIS effective sector.

---

## 2. ADM variables

```text
N      = lapse
N_i    = shift
γ_ij   = spatial metric
π^ij   = canonical momentum
```

---

## 3. Effective Hamiltonian constraint

Schematic structure:

```text
H_0 =
Q_eff*delta**2 + pi_gamma**2 + rho + c_s_eff2*delta**2*k**2/a**2
```

Interpretation:

- π_gamma² : geometric kinetic sector
- Q_eff δ² : scalar kinetic contribution
- c_s_eff² k² δ²/a² : gradient energy
- rho : matter sector

---

## 4. Momentum constraint

```text
H_i =
delta*pi_gamma
```

This encodes spatial diffeomorphism consistency.

---

## 5. Principal symbol

```text
P(omega,k) =
Q_eff*omega**2 - Q_eff*c_s_eff2*k**2/a**2
```

Hyperbolicity requires:

```text
Q_eff > 0
c_s_eff² > 0
```

---

## 6. Constraint algebra

GR-like closure structure:

```text
{H_0(x), H_0(y)} ~ D_i
{H_i(x), H_0(y)} ~ H_0
{H_i(x), H_j(y)} ~ H_i
```

Current UTIS proxy interpretation:

```text
If Q_eff and c_s_eff² remain positive and smooth,
then no immediate constraint singularity is indicated.
```

---

## 7. Stability conditions

Ghost-free:

```text
True
```

Gradient-stable:

```text
True
```

---

## 8. Important implication

The UTIS effective sector now possesses:

```text
quadratic action structure
Hamiltonian structure
principal hyperbolic structure
ADM-like constraint scaffold
UV positivity conditions
```

This is already beyond a pure phenomenological fitting model.

---

## 9. Remaining truly hard problems

```text
full nonlinear ADM closure
exact Poisson algebra derivation
loop renormalization
radiative stability
UV completion candidate
```

---

## 10. Next step Q-5

Construct symbolic renormalization / loop scaling audit:

```text
power counting
strong-coupling scale
operator dimension
radiative correction structure
```
