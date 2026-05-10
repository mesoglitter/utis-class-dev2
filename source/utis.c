
#include "utis.h"

#include <math.h>

/* ============================================================
 * internal helper
 * ============================================================ */

static double utis_clip_rate(
  double x,
  double xmin,
  double xmax
){

  if (x < xmin) return xmin;
  if (x > xmax) return xmax;

  return x;
}

/* ============================================================
 * init
 * ============================================================ */

int utis_init(
  struct utis_parameters * putis
){

  putis->has_utis = _FALSE_;

  putis->theta_ini = 0.0;
  putis->relay_width = 0.05;

  putis->S0_soft = 0.02;

  putis->A_gye = 1.0;
  putis->A_byeong = 1.0;
  putis->A_jeong = 1.0;
  putis->A_im = 1.0;

  putis->gamma_12_0 = 1.0;
  putis->gamma_23_0 = 1.0;
  putis->gamma_34_0 = 1.0;
  putis->gamma_41_0 = 1.0;

  putis->min_positive = 1e-12;
  putis->max_rate = 1e6;

  return _SUCCESS_;
}

/* ============================================================
 * background update
 * ============================================================ */

int utis_update_background(
  struct utis_parameters * putis,
  double tau,
  struct utis_background_state * pub
){

  double theta;
  double W_yang;
  double W_eum;

  double relay_width;

  if (putis->has_utis == _FALSE_) {

    pub->Gamma_12 = 0.0;
    pub->Gamma_23 = 0.0;
    pub->Gamma_34 = 0.0;
    pub->Gamma_41 = 0.0;

    pub->clustering_fraction = 1.0;
    pub->effective_growth = 1.0;

    return _SUCCESS_;
  }

  relay_width = putis->relay_width;

  theta = fmod(
    tau + putis->theta_ini,
    2.0 * _PI_
  );

  if (theta < 0.0) {
    theta += 2.0 * _PI_;
  }

  W_yang = 0.5 * (
    1.0
    - tanh((theta - _PI_) / relay_width)
  );

  W_eum = 1.0 - W_yang;

  pub->tau = tau;
  pub->theta = theta;

  pub->W_yang = W_yang;
  pub->W_eum = W_eum;

  pub->H_gye = putis->A_gye * W_yang;

  pub->T_byeong =
    putis->A_byeong
    * sin(theta)
    * sin(theta)
    * W_yang;

  pub->T_jeong =
    putis->A_jeong
    * W_eum;

  pub->T_im =
    putis->A_im
    * sin(theta)
    * sin(theta)
    * W_eum;

  pub->M_gi =
    sin(12.0 * theta)
    * sin(12.0 * theta);

  pub->Gamma_12 =
    utis_clip_rate(
      putis->gamma_12_0
      * pub->M_gi
      * pub->H_gye,
      0.0,
      putis->max_rate
    );

  pub->Gamma_23 =
    utis_clip_rate(
      putis->gamma_23_0
      * pub->M_gi
      * pub->T_jeong,
      0.0,
      putis->max_rate
    );

  pub->Gamma_34 =
    utis_clip_rate(
      putis->gamma_34_0
      * pub->T_im,
      0.0,
      putis->max_rate
    );

  pub->Gamma_41 =
    utis_clip_rate(
      putis->gamma_41_0
      * pub->M_gi
      * pub->H_gye,
      0.0,
      putis->max_rate
    );

  pub->clustering_fraction =
    1.0 - putis->S0_soft * W_eum;

  pub->effective_growth =
    pub->clustering_fraction;

  return _SUCCESS_;
}

/* ============================================================
 * fraction update
 * ============================================================ */

int utis_update_fractions(
  struct utis_parameters * putis,
  struct utis_background_state * pub,
  struct utis_fraction_state * puf
){

  double gap;
  double eul;
  double gyeong;
  double shin;

  if (putis->has_utis == _FALSE_) {

    puf->df[index_utis_gap] = 0.0;
    puf->df[index_utis_eul] = 0.0;
    puf->df[index_utis_gyeong] = 0.0;
    puf->df[index_utis_shin] = 0.0;

    pub->clustering_fraction = 1.0;
    pub->effective_growth = 1.0;

    return _SUCCESS_;
  }

  gap     = puf->f[index_utis_gap];
  eul     = puf->f[index_utis_eul];
  gyeong  = puf->f[index_utis_gyeong];
  shin    = puf->f[index_utis_shin];

  puf->df[index_utis_gap] =
    - pub->Gamma_12 * gap
    + pub->Gamma_41 * shin;

  puf->df[index_utis_eul] =
    + pub->Gamma_12 * gap
    - pub->Gamma_23 * eul;

  puf->df[index_utis_gyeong] =
    + pub->Gamma_23 * eul
    - pub->Gamma_34 * gyeong;

  puf->df[index_utis_shin] =
    + pub->Gamma_34 * gyeong
    - pub->Gamma_41 * shin;

  pub->clustering_fraction =
    gyeong + shin;

  pub->effective_growth =
    1.0
    - putis->S0_soft
    * (1.0 - pub->clustering_fraction);

  return _SUCCESS_;
}

/* ============================================================
 * free
 * ============================================================ */


/* ============================================================
 * fluid density algebraic translator
 * ============================================================ */

int utis_update_fluid_density(
  struct utis_parameters * putis,
  struct utis_background_state * pub,
  struct utis_fraction_state * puf,
  struct utis_fluid_state * pufl,
  double rho_cdm_current
){

  (void)pub;

  if (putis->has_utis == _FALSE_) {

    pufl->rho_total = rho_cdm_current;
    pufl->p_total = 0.0;

    pufl->rho[index_utis_gap] = 0.0;
    pufl->rho[index_utis_eul] = 0.0;
    pufl->rho[index_utis_gyeong] = rho_cdm_current;
    pufl->rho[index_utis_shin] = 0.0;

    pufl->p[index_utis_gap] = 0.0;
    pufl->p[index_utis_eul] = 0.0;
    pufl->p[index_utis_gyeong] = 0.0;
    pufl->p[index_utis_shin] = 0.0;

    pufl->w[index_utis_gap] = 0.0;
    pufl->w[index_utis_eul] = 0.0;
    pufl->w[index_utis_gyeong] = 0.0;
    pufl->w[index_utis_shin] = 0.0;

    pufl->cs2[index_utis_gap] = 0.0;
    pufl->cs2[index_utis_eul] = 0.0;
    pufl->cs2[index_utis_gyeong] = 0.0;
    pufl->cs2[index_utis_shin] = 0.0;

    return _SUCCESS_;
  }

  pufl->rho_total = rho_cdm_current;
  pufl->p_total = 0.0;

  pufl->rho[index_utis_gap] =
    rho_cdm_current * puf->f[index_utis_gap];

  pufl->rho[index_utis_eul] =
    rho_cdm_current * puf->f[index_utis_eul];

  pufl->rho[index_utis_gyeong] =
    rho_cdm_current * puf->f[index_utis_gyeong];

  pufl->rho[index_utis_shin] =
    rho_cdm_current * puf->f[index_utis_shin];

  pufl->w[index_utis_gap] = 0.0;
  pufl->w[index_utis_eul] = 0.0;
  pufl->w[index_utis_gyeong] = 0.0;
  pufl->w[index_utis_shin] = 0.0;

  pufl->p[index_utis_gap] = 0.0;
  pufl->p[index_utis_eul] = 0.0;
  pufl->p[index_utis_gyeong] = 0.0;
  pufl->p[index_utis_shin] = 0.0;

  pufl->cs2[index_utis_gap] = 1.0;
  pufl->cs2[index_utis_eul] = 0.01;
  pufl->cs2[index_utis_gyeong] = 0.0;
  pufl->cs2[index_utis_shin] = 0.0;

  return _SUCCESS_;
}

int utis_free(
  struct utis_parameters * putis
){

  (void)putis;

  return _SUCCESS_;
}
