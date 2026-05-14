# UTIS Renormalization / Loop Scaling Scaffold Q-5

## 1. Goal

Construct the EFT-level scaling and loop-behavior scaffold.

---

## 2. Effective operators

```text
(∂pi)^2
pi^2
chi*delta
(∂chi)^2
R
```

---

## 3. Canonical dimensions

```text
[pi]  = 1
[chi] = 1
```

---

## 4. Loop expansion parameter

Dimensionless loop factor:

```text
alpha*k**2/(16*pi**2*M_pl**2)
```

Interpretation:

```text
loop_param << 1
```

is required for perturbative EFT control.

---

## 5. Strong-coupling scale

```text
Lambda_sc =
4*pi*M_pl/sqrt(alpha)
```

Interpretation:

```text
larger alpha -> lower strong-coupling scale
alpha -> 1 dangerous
```

---

## 6. Radiative corrections

Correction to kinetic sector:

```text
delta_Q ~
Lambda**2*alpha/(16*pi**2*M_pl**2)
```

Correction to gradient sector:

```text
delta_c_s² ~
Lambda**2*beta/(16*pi**2*M_pl**2)
```

Natural EFT control requires:

```text
delta_Q << 1
delta_c_s² << 1
```

---

## 7. UV consistency condition

Current UTIS condition:

```text
alpha < 1
```

This emerged previously from:

```text
Q_eff(UV) = Q0(1-alpha)
c_s_eff²(UV)=c_s0(1-alpha)
```

Thus alpha >= 1 would trigger:

```text
ghost instability
Hamiltonian unboundedness
hyperbolicity collapse
```

---

## 8. Current interpretation

The UTIS sector currently resembles:

```text
screened EFT scalar-tensor sector
with UV-sensitive kinetic renormalization
```

rather than an arbitrary fitting function.

---

## 9. Remaining deepest problems

```text
full nonlinear loop renormalization
exact counterterm structure
radiative stability to all orders
unitarity completion
UV-complete microscopic theory
```

---

## 10. Next step Q-6

Construct symbolic UV-completion candidate scaffold:

```text
emergent geometry
hidden gauge sector
collective condensate picture
topological completion
multi-field branch completion
```
