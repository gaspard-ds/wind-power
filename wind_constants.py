# Plot Params
LARGE = 22
MEDIUM = 16
SMALL = 12

params = {
    "axes.titlesize": LARGE,
    "legend.fontsize": MEDIUM,
    "figure.figsize": (30, 15),
    "axes.labelsize": LARGE,
    "xtick.labelsize": MEDIUM,
    "ytick.labelsize": MEDIUM,
    "figure.titlesize": LARGE,
}

REGIONS = [
    "Auvergne-Rhône-Alpes",
    "Bourgogne-Franche-Comté",
    "Bretagne",
    "Centre-Val de Loire",
    "Corse",
    "Grand-Est",
    "Hauts-de-France",
    "Ile-de-France",
    "Normandie",
    "Nouvelle-Aquitaine",
    "Occitanie",
    "Pays de la Loire",
    "Provence-Alpes-Côte d'Azur",
]

CODE_REGIONS = {
    11: "Ile-de-France",
    24: "Centre-Val de Loire",
    27: "Bourgogne-Franche-Comté",
    28: "Normandie",
    32: "Hauts-de-France",
    44: "Grand-Est",
    52: "Pays de la Loire",
    53: "Bretagne",
    75: "Nouvelle-Aquitaine",
    76: "Occitanie",
    84: "Auvergne-Rhône-Alpes",
    93: "Provence-Alpes-Côte d'Azur",
    94: "Corse",
}


TO_KEEP_PRODUCTION = [
    "Code INSEE région",
    "Région",
    "Nature",
    "Date",
    "Heure",
    "Date - Heure",
    "Consommation (MW)",
    "Eolien (MW)",
    "TCO Eolien (%)",
    "TCH Eolien (%)",
]

TO_KEEP_WEATHER = [
    "ID OMM station",
    "Date",
    "Pression au niveau mer",
    "Variation de pression en 3 heures",
    "Direction du vent moyen 10 mn",
    "Vitesse du vent moyen 10 mn",
    "Température",
    "Pression station",
    "Niveau barométrique",
    "Variation de pression en 24 heures",
    "Température du thermomètre mouillé",
    "Rafale sur les 10 dernières minutes",
    "Rafales sur une période",
    "Periode de mesure de la rafale",
    "Altitude",
    "region (name)",
    "region (code)",
    "mois_de_l_annee",
]

FEATURES = [
    "speed",
    "direction",
    "temperature",
    "pressure",
    "gust",
    "speed_11",
    "direction_11",
    "speed_24",
    "direction_24",
    "speed_27",
    "direction_27",
    "speed_28",
    "direction_28",
    "speed_32",
    "direction_32",
    "speed_44",
    "direction_44",
    "speed_52",
    "direction_52",
    "speed_53",
    "direction_53",
    "speed_75",
    "direction_75",
    "speed_76",
    "direction_76",
    "speed_84",
    "direction_84",
    "speed_93",
    "direction_93",
    "speed_94",
    "direction_94",
    "month",
]

FEATURES_REDUCED = [
    "speed_28",
    "speed_44",
    "temperature",
    "speed_24",
    "speed",
    "pressure",
    "gust",
    "speed_11",
    "speed_32",
    "speed_53",
    "speed_75",
    "speed_76",
    "speed_94",
    "direction_94",
]

FEATURES_GLOBAL = [
    "speed",
    "direction",
    "pressure",
    "temperature",
    "gust",
]

TARGET = "relative_production"

ALT_TARGET = "production"
ALT_FEATURES = FEATURES + ["capacity"]

EXTENDED_FEATURES = [
    "temperature_diff_2",
    "speed_76_shift_1",
    "speed_27 x speed_84",
    "gust_shift_2",
    "speed_94_shift_2",
    "speed_76",
    "speed_28 x speed_76",
    "speed_84",
    "speed_93_shift_1",
    "temperature",
    "speed_24 x speed_53",
    "speed_32 x speed_44",
    "speed_28 x speed_32",
    "speed x speed_28",
    "pressure x speed_28",
    "speed_84_diff_2",
    "speed_28_shift_1",
    "speed_32",
    "speed_53_shift_1",
    "speed_53 x speed_76",
    "speed_28 x speed_53",
    "speed_32_shift_1",
    "speed x gust",
    "speed_shift_2",
    "temperature^2",
    "speed_28 x speed_75",
    "temperature x pressure",
    "speed_44 x speed_76",
    "speed_24_shift_1",
    "speed_28_diff_1",
    "speed_32 x speed_53",
    "speed_53",
    "speed_24 x speed_28",
    "speed_32 x speed_76",
    "speed_75_shift_2",
    "gust_diff_2",
    "speed_44",
    "gust_diff_1",
    "speed_27_diff_2",
    "speed_32 x speed_75",
    "speed x speed_32",
    "speed_44 x speed_53",
    "speed_94_shift_1",
    "speed_75",
    "gust x speed_28",
    "speed_52_diff_2",
    "speed_44 x speed_75",
    "speed_52_diff_1",
    "speed_24",
    "speed_28 x speed_44",
    "speed_24 x speed_44",
    "speed_32_shift_2",
    "speed_53_shift_2",
    "speed_52",
    "month_diff_2",
    "speed_28",
    "speed x speed_53",
    "speed_11_diff_2",
    "speed_24 x speed_76",
    "speed_28_shift_2",
    "speed_76_shift_2",
    "speed_75_shift_1",
    "temperature_shift_1",
    "speed_11 x speed_27",
    "speed_44_shift_1",
    "speed_24 x speed_32",
    "speed_27_diff_1",
    "speed_44_shift_2",
]
