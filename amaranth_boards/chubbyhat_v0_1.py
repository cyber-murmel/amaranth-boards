import os
import subprocess

from amaranth.build import *
from .colorlight_5a75b_r7_0 import Colorlight_5A75B_R70Platform


__all__ = ["ChubbyHatV0_1Platform"]


class ChubbyHatV0_1Platform(Colorlight_5A75B_R70Platform):
    connectors = Colorlight_5A75B_R70Platform.connectors + [
        # in reference to https://raw.githubusercontent.com/cyber-murmel/chubby-hat/master/hardware/chubby%20hat/plot/pdf/chubby%20hat.pdf#page=1
        Connector("pmod", 0, "L2  J5  B16 F12 - - F15 K1  K2  J14 - -"),
        Connector("pmod", 1, "C2  G2  F3  H3  - - K3  H5  G3  F1  - -"),
        Connector("pmod", 2, "H4  L5  K4  J4  - - P1  K5  E3  G1  - -"),
        Connector("pmod", 3, "M9  P4  T6  R1  - - R6  M8  R2  F2  - -"),
        Connector("pmod", 4, "J12 N12 K15 M11 - - G16 N11 L16 P12 - -"),
        Connector("pmod", 5, "G14 H13 K16 H15 - - G15 H12 J16 J15 - -"),
        Connector("pmod", 6, "E13 A14 B14 H14 - - A13 A14 F16 J13 - -"),
    ]

    def toolchain_program(self, products, name):
        tool = os.environ.get("OPENFPGALOADER", "openFPGALoader")
        with products.extract("{}.bit".format(name)) as bitstream_filename:
            subprocess.check_call(
                [tool, "-c", "ft2232", "--ftdi-channel", "0", "-m", bitstream_filename]
            )


if __name__ == "__main__":
    from .test.blinky import *

    ChubbyHatV0_1Platform().build(Blinky(), do_program=True)
