from math import ceil
from typing import Tuple

weapons = {
    "PT92": 17,
    "M4A1": 30,
    "M16A2": 30,
    "PSG1": 5
}


def magazine_no(info: Tuple[str, int]) -> int:
    (weapon, streets) = info
    bullt_fire = streets * 3
    mag_cap = weapons[weapon]
    need_mag = bullt_fire / mag_cap

    return ceil(need_mag)