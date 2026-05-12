
import pickle
from pathlib import Path

import numpy as np
import pandas as pd

from classy import Class


# ============================================================
# UTIS likelihood wrapper
# Stage D-1
# ============================================================

DEFAULT_DATA_DIR = Path("/content/drive/MyDrive/UTIS_project/paper_datasets")
DEFAULT_CACHE = DEFAULT_DATA_DIR / "utis_cache.pkl"


# ============================================================
# Data loading
# ============================================================

def load_data(data_dir=DEFAULT_DATA_DIR):
    data_dir = Path(data_dir)

    rsd = pd.read_csv(data_dir / "RSD_clean.csv")
    bao = pd.read_csv(data_dir / "BAO_clean.csv")

    return {
        "rsd": rsd,
        "bao": bao,
    }


# ============================================================
# Cache helpers
# ============================================================

def load_cache(cache_file=DEFAULT_CACHE):
    cache_file = Path(cache_file)

    if cache_file.exists():
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    return {}


def save_cache(cache, cache_file=DEFAULT_CACHE):
    cache_file = Path(cache_file)
    cache_file.parent.mkdir(parents=True, exist_ok=True)

    with open(cache_file, "wb") as f:
        pickle.dump(cache, f)


def make_key(S0, kc, gate_at, gate_p, theta_ini):
    return (
        round(float(S0), 8),
        round(float(kc), 8),
        round(float(gate_at), 8),
        round(float(gate_p), 8),
        round(float(theta_ini), 8),
    )


# ============================================================
# BAO helpers
# ============================================================

def DM_over_rd(cosmo, z):
    DA = cosmo.angular_distance(float(z))
    DM = (1.0 + float(z)) * DA
    rd = cosmo.rs_drag()
    return DM / rd


def DH_over_rd(cosmo, z):
    c_light = 299792.458
    H_z = cosmo.Hubble(float(z)) * c_light
    DH = c_light / H_z
    rd = cosmo.rs_drag()
    return DH / rd


# ============================================================
# CLASS runner
# ============================================================

def run_utis(
    S0,
    kc,
    gate_at=0.65,
    gate_p=8.0,
    theta_ini=0.0,
    data_dir=DEFAULT_DATA_DIR,
    cache_file=DEFAULT_CACHE,
    use_cache=True,
    save_pk_sample=True,
):
    """
    Run CLASS for UTIS minimal 2-parameter cosmology.

    Free:
      S0, kc

    Fixed protection sector:
      gate_at, gate_p, theta_ini
    """

    key = make_key(S0, kc, gate_at, gate_p, theta_ini)

    cache = load_cache(cache_file) if use_cache else {}

    if use_cache and key in cache:
        return cache[key]

    data = load_data(data_dir)

    rsd = data["rsd"]
    bao = data["bao"]

    cosmo = Class()

    pars = {
        "output": "tCl,pCl,lCl,mPk",
        "lensing": "yes",

        "P_k_max_h/Mpc": 5.0,
        "z_max_pk": 3.0,

        "A_s": 2.100549e-9,

        "has_utis": "yes",
        "utis_S0": float(S0),
        "utis_kc": float(kc),
        "utis_gate_at": float(gate_at),
        "utis_gate_p": float(gate_p),
        "utis_theta_ini": float(theta_ini),
    }

    cosmo.set(pars)
    cosmo.compute()

    # --------------------------------------------------------
    # derived
    # --------------------------------------------------------

    sigma8 = cosmo.sigma8()
    Omega_m = cosmo.Omega_m()
    S8 = sigma8 * np.sqrt(Omega_m / 0.3)

    # --------------------------------------------------------
    # RSD
    # --------------------------------------------------------

    z_rsd = rsd["z"].values
    fs8_data = rsd["fs8"].values
    err_rsd = rsd["err"].values

    fs8_model = np.array([
        cosmo.scale_independent_f_sigma8(float(z))
        for z in z_rsd
    ])

    chi2_rsd = float(np.sum(((fs8_data - fs8_model) / err_rsd) ** 2))

    # --------------------------------------------------------
    # BAO
    # --------------------------------------------------------

    chi2_bao = 0.0
    n_bao = 0

    for _, row in bao.iterrows():
        z = float(row["z"])

        if not pd.isna(row["DM_over_rd"]):
            model = DM_over_rd(cosmo, z)
            chi2_bao += ((row["DM_over_rd"] - model) / row["DM_over_rd_err"]) ** 2
            n_bao += 1

        if not pd.isna(row["DH_over_rd"]):
            model = DH_over_rd(cosmo, z)
            chi2_bao += ((row["DH_over_rd"] - model) / row["DH_over_rd_err"]) ** 2
            n_bao += 1

    chi2_bao = float(chi2_bao)

    # --------------------------------------------------------
    # TT / lensing proxy safety
    # --------------------------------------------------------

    cl = cosmo.lensed_cl(300)

    ell = cl["ell"][2:]
    tt = cl["tt"][2:]
    pp = cl["pp"][2:]

    idx10 = int(np.argmin(np.abs(ell - 10)))
    idx30 = int(np.argmin(np.abs(ell - 30)))
    idx100 = int(np.argmin(np.abs(ell - 100)))

    tt10 = float(tt[idx10])
    tt30 = float(tt[idx30])
    tt100 = float(tt[idx100])

    pp10 = float(pp[idx10])
    pp30 = float(pp[idx30])
    pp100 = float(pp[idx100])

    # --------------------------------------------------------
    # P(k) sample for later explanation / figures
    # --------------------------------------------------------

    pk_sample = None

    if save_pk_sample:
        k_sample = np.array([0.01, 0.03, 0.05, 0.10, 0.20])
        pk_sample = {
            "k": k_sample.tolist(),
            "pk": [float(cosmo.pk(float(k), 0.0)) for k in k_sample],
        }

    result = {
        "params": {
            "S0": float(S0),
            "kc": float(kc),
            "gate_at": float(gate_at),
            "gate_p": float(gate_p),
            "theta_ini": float(theta_ini),
        },

        "sigma8": float(sigma8),
        "Omega_m": float(Omega_m),
        "S8": float(S8),

        "chi2_rsd": chi2_rsd,
        "chi2_bao": chi2_bao,
        "n_bao": int(n_bao),

        "tt": {
            "tt10": tt10,
            "tt30": tt30,
            "tt100": tt100,
        },

        "lensing": {
            "pp10": pp10,
            "pp30": pp30,
            "pp100": pp100,
        },

        "pk_sample": pk_sample,
    }

    cosmo.struct_cleanup()
    cosmo.empty()

    if use_cache:
        cache[key] = result
        save_cache(cache, cache_file)

    return result


# ============================================================
# Reference LCDM runner
# ============================================================

def run_lcdm(
    data_dir=DEFAULT_DATA_DIR,
    cache_file=DEFAULT_DATA_DIR / "lcdm_cache.pkl",
    use_cache=True,
):
    key = ("lcdm",)

    cache = load_cache(cache_file) if use_cache else {}

    if use_cache and key in cache:
        return cache[key]

    data = load_data(data_dir)
    rsd = data["rsd"]
    bao = data["bao"]

    cosmo = Class()

    pars = {
        "output": "tCl,pCl,lCl,mPk",
        "lensing": "yes",

        "P_k_max_h/Mpc": 5.0,
        "z_max_pk": 3.0,

        "A_s": 2.100549e-9,
    }

    cosmo.set(pars)
    cosmo.compute()

    sigma8 = cosmo.sigma8()
    Omega_m = cosmo.Omega_m()
    S8 = sigma8 * np.sqrt(Omega_m / 0.3)

    z_rsd = rsd["z"].values
    fs8_data = rsd["fs8"].values
    err_rsd = rsd["err"].values

    fs8_model = np.array([
        cosmo.scale_independent_f_sigma8(float(z))
        for z in z_rsd
    ])

    chi2_rsd = float(np.sum(((fs8_data - fs8_model) / err_rsd) ** 2))

    chi2_bao = 0.0
    n_bao = 0

    for _, row in bao.iterrows():
        z = float(row["z"])

        if not pd.isna(row["DM_over_rd"]):
            model = DM_over_rd(cosmo, z)
            chi2_bao += ((row["DM_over_rd"] - model) / row["DM_over_rd_err"]) ** 2
            n_bao += 1

        if not pd.isna(row["DH_over_rd"]):
            model = DH_over_rd(cosmo, z)
            chi2_bao += ((row["DH_over_rd"] - model) / row["DH_over_rd_err"]) ** 2
            n_bao += 1

    chi2_bao = float(chi2_bao)

    cl = cosmo.lensed_cl(300)

    ell = cl["ell"][2:]
    tt = cl["tt"][2:]
    pp = cl["pp"][2:]

    idx10 = int(np.argmin(np.abs(ell - 10)))
    idx30 = int(np.argmin(np.abs(ell - 30)))
    idx100 = int(np.argmin(np.abs(ell - 100)))

    result = {
        "sigma8": float(sigma8),
        "Omega_m": float(Omega_m),
        "S8": float(S8),

        "chi2_rsd": chi2_rsd,
        "chi2_bao": chi2_bao,
        "n_bao": int(n_bao),

        "tt": {
            "tt10": float(tt[idx10]),
            "tt30": float(tt[idx30]),
            "tt100": float(tt[idx100]),
        },

        "lensing": {
            "pp10": float(pp[idx10]),
            "pp30": float(pp[idx30]),
            "pp100": float(pp[idx100]),
        },
    }

    cosmo.struct_cleanup()
    cosmo.empty()

    if use_cache:
        cache[key] = result
        save_cache(cache, cache_file)

    return result


# ============================================================
# Chi2 / loglike
# ============================================================

def chi2_total(
    S0,
    kc,
    gate_at=0.65,
    gate_p=8.0,
    theta_ini=0.0,
    data_dir=DEFAULT_DATA_DIR,
    cache_file=DEFAULT_CACHE,
    use_cache=True,
    weights=None,
):
    """
    Current proxy total chi2.

    weights:
      dict with keys: rsd, bao, tt, lensing, S8
    """

    if weights is None:
        weights = {
            "rsd": 1.0,
            "bao": 1.0,
            "tt": 50.0,
            "lensing": 100.0,
            "S8": 0.0,
        }

    utis = run_utis(
        S0=S0,
        kc=kc,
        gate_at=gate_at,
        gate_p=gate_p,
        theta_ini=theta_ini,
        data_dir=data_dir,
        cache_file=cache_file,
        use_cache=use_cache,
    )

    lcdm = run_lcdm(data_dir=data_dir)

    # ratios for TT/lensing proxy
    tt10_ratio = utis["tt"]["tt10"] / lcdm["tt"]["tt10"]
    tt30_ratio = utis["tt"]["tt30"] / lcdm["tt"]["tt30"]

    pp10_ratio = utis["lensing"]["pp10"] / lcdm["lensing"]["pp10"]
    pp30_ratio = utis["lensing"]["pp30"] / lcdm["lensing"]["pp30"]
    pp100_ratio = utis["lensing"]["pp100"] / lcdm["lensing"]["pp100"]

    chi2_tt = (
        (tt10_ratio - 1.0) ** 2
        +
        (tt30_ratio - 1.0) ** 2
    )

    chi2_lensing = (
        (pp10_ratio - 1.0) ** 2
        +
        (pp30_ratio - 1.0) ** 2
        +
        (pp100_ratio - 1.0) ** 2
    )

    chi2_s8 = 0.0

    S8 = utis["S8"]

    if S8 < 0.70:
        chi2_s8 += (0.70 - S8) ** 2

    if S8 > 0.84:
        chi2_s8 += (S8 - 0.84) ** 2

    total = (
        weights["rsd"] * utis["chi2_rsd"]
        +
        weights["bao"] * utis["chi2_bao"]
        +
        weights["tt"] * chi2_tt
        +
        weights["lensing"] * chi2_lensing
        +
        weights["S8"] * chi2_s8
    )

    return float(total), {
        "utis": utis,
        "lcdm": lcdm,
        "tt_ratios": {
            "tt10": float(tt10_ratio),
            "tt30": float(tt30_ratio),
        },
        "lensing_ratios": {
            "pp10": float(pp10_ratio),
            "pp30": float(pp30_ratio),
            "pp100": float(pp100_ratio),
        },
        "chi2_proxy": {
            "tt": float(chi2_tt),
            "lensing": float(chi2_lensing),
            "S8": float(chi2_s8),
        },
    }


def loglike(S0, kc, **kwargs):
    chi2, _ = chi2_total(S0, kc, **kwargs)
    return -0.5 * chi2
