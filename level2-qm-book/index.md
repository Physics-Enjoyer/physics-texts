---
title: Level 2 Quantum Mechanics
---

Notes for the Level 2 (Griffiths QM) rung of the quantum ladder, with the extra Level 2 math alongside. Each chapter matches a row of the textbook ladder workbook, including that row's example ladder. The explanations, examples, exercises and figures are original; chapter references to Griffiths, Tipler & Mosca, Sakurai, Stewart, Boas, Zill and Arfken are approximate, as in the workbook.

Mechanics topics 6 and 11 (Lagrangian and Hamiltonian mechanics) and E&M's waves chapter make good preparation. Thermo topics 5–8 use quantum topics 2 and 5.

## Quantum (study order)

| # | Topic | Griffiths QM | Math first |
|---|---|---|---|
| 1 | [The wave function](qm/01-wave-function.ipynb) | 1 | Q-M1; thermo T-M2 |
| 2 | [Particle in a box, finite wells, tunneling](qm/02-wells-tunneling.ipynb) | 2 | mechanics M4, M2; Q-M1 |
| 3 | [The harmonic oscillator](qm/03-harmonic-oscillator.ipynb) | 2 | Q-M2; thermo T-M2 |
| 4 | [Formalism: operators, commutators, uncertainty](qm/04-formalism.ipynb) | 3 | Q-M3; mechanics M6; Q-M1 |
| 5 | [The hydrogen atom and 3D problems](qm/05-hydrogen-3d.ipynb) | 4 | Q-M2, Q-M4; E&M E-M2 |
| 6 | [Angular momentum and spin](qm/06-angular-momentum-spin.ipynb) | 4 | Q-M4; mechanics M6; Q-M3 |
| 7 | [Identical particles](qm/07-identical-particles.ipynb) | 5 | mechanics M6; Q-M3, Q-M4 |
| 8 | [Time-independent perturbation theory](qm/08-time-independent-perturbation.ipynb) | 6 | mechanics M1, M6; Q-M3 |
| 9 | [The variational method and WKB](qm/09-variational-wkb.ipynb) | 7–8 | Q-M5; mechanics M5, M4 |
| 10 | [Time-dependent perturbation theory](qm/10-time-dependent-perturbation.ipynb) | 9 | mechanics M4, M6, M2; E&M E-M3 |
| 11 | [Scattering](qm/11-scattering.ipynb) | 11 | Q-M5; E&M E-M2, E-M3 |

## Math

| # | Notebook | Covers |
|---|---|---|
| Q-M1 | [Complex functions, probability and wave packets](math/01-complex-probability.ipynb) | modulus and phase, probability densities, normalizing Gaussians, momentum space and Plancherel, ⟨p⟩ by integration by parts, packet spreading |
| Q-M2 | [Series solutions, Hermite and Laguerre functions](math/02-series-solutions-special-functions.ipynb) | power series and Frobenius, why termination quantizes, Hermite polynomials and orthogonality, associated Laguerre functions |
| Q-M3 | [Hilbert space and Dirac notation](math/03-hilbert-space-dirac.ipynb) | complex inner products, bras and kets, completeness, Hermitian and unitary operators, continuous spectra, truncated-basis diagonalization |
| Q-M4 | [Rotations, angular momentum algebra and spherical harmonics](math/04-rotations-spherical-harmonics.ipynb) | non-commuting rotations and their generators, ladder operators, matrices for any j, Pauli matrices, Y_ℓ^m as L² eigenfunctions, adding angular momenta |
| Q-M5 | [Asymptotics, WKB and Bessel functions](math/05-asymptotics-wkb-bessel.ipynb) | asymptotic behavior, WKB solutions, Airy functions and quantization, tunneling, spherical Bessel functions, Rayleigh's plane-wave expansion |

From the other books: mechanics [M1 vectors and ODEs](../level2-book/math/01-vectors-odes.ipynb), [M2 coordinates, integrals and the delta function](../level2-book/math/02-coordinates-integrals-delta.ipynb), [M4 linear ODEs and Fourier series](../level2-book/math/04-linear-odes-fourier.ipynb), [M5 calculus of variations](../level2-book/math/05-calculus-of-variations.ipynb), [M6 linear algebra](../level2-book/math/06-linear-algebra.ipynb); E&M [E-M2 separation of variables](../level2-em-book/math/02-separation-of-variables.ipynb), [E-M3 waves and Fourier transforms](../level2-em-book/math/03-waves-fourier-transforms.ipynb); thermo [T-M2 Gaussian and Gamma integrals](../level2-thermo-book/math/02-gaussian-gamma-integrals.ipynb).
