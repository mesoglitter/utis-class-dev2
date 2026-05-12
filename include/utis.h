
#ifndef __UTIS__
#define __UTIS__

#include "common.h"

#define _UTIS_N_FLAVOR_ 4

enum utis_flavor_index {
  index_utis_gap = 0,
  index_utis_eul = 1,
  index_utis_gyeong = 2,
  index_utis_shin = 3
};

struct utis_parameters {

  short has_utis;

  double theta_ini;
  double relay_width;

  double S0_soft;

  double gate_at;
  double gate_p;

  double kc;

  double A_gye;
  double A_byeong;
  double A_jeong;
  double A_im;

  double gamma_12_0;
  double gamma_23_0;
  double gamma_34_0;
  double gamma_41_0;

  double min_positive;
  double max_rate;

  ErrorMsg error_message;
};

struct utis_background_state {

  double tau;
  double theta;

  double W_yang;
  double W_eum;

  double H_gye;
  double T_byeong;
  double T_jeong;
  double T_im;

  double M_gi;

  double Gamma_12;
  double Gamma_23;
  double Gamma_34;
  double Gamma_41;

  double clustering_fraction;
  double effective_growth;
};

struct utis_fraction_state {

  double f[_UTIS_N_FLAVOR_];
  double df[_UTIS_N_FLAVOR_];

  double total_fraction;
};


struct utis_fluid_state {

  double rho[_UTIS_N_FLAVOR_];
  double p[_UTIS_N_FLAVOR_];

  double w[_UTIS_N_FLAVOR_];
  double cs2[_UTIS_N_FLAVOR_];

  double rho_total;
  double p_total;
};

int utis_init(
  struct utis_parameters * putis
);

int utis_update_background(
  struct utis_parameters * putis,
  double tau,
  struct utis_background_state * pub
);

int utis_update_fractions(
  struct utis_parameters * putis,
  struct utis_background_state * pub,
  struct utis_fraction_state * puf
);


int utis_update_fluid_density(
  struct utis_parameters * putis,
  struct utis_background_state * pub,
  struct utis_fraction_state * puf,
  struct utis_fluid_state * pufl,
  double rho_cdm_current
);

int utis_free(
  struct utis_parameters * putis
);

#endif
