import os
import subprocess

from nmigen.build import *
from nmigen.vendor.lattice_ecp5 import *
from resources import *


__all__ = ["Colorlight5A75BV7_0Platform"]


class Colorlight5A75BV7_0Platform(LatticeECP5Platform):
    device      = "LFE5U-25F"
    package     = "BG256"
    speed       = "6"
    default_clk = "clk25"
    default_rst = "rst"
    resources   = [
        Resource("rst", 0, PinsN("M13", dir="i"), Attrs(IO_TYPE="LVCMOS33")),
        Resource("clk25", 0, PinsN("P6", dir="i"), Clock(25e6), Attrs(IO_TYPE="LVCMOS33")),

        *LEDResources(pins="P11", attrs=Attrs(IO_TYPE="LVCMOS25")),

        UARTResource(0,
            tx="P11", # led (J19 DATA_LED-)
            rx="M13", # btn (J19 KEY+)
            attrs=Attrs(IO_TYPE="LVCMOS33", PULLMODE="UP")
        ),

        *SPIFlashResources(0,
            cs="N8",
            clk="U3",
            cipo="T7",
            copi="T8",
            attrs=Attrs(IO_STANDARD="LVCMOS33")
        ),

        SDRAMResource(0,
            clk="C6",
            cs=None,
            we="C7",
            ras="D7",
            cas="E7",
            ba="A7",
            a="A9 E10 B12 D13 C12 D11 D10 E9 D9 B7 C8",
            dq="B13 C11 C10 A11 C9 E8 B6 B9 A6 B5 A5 B4 B3 C3 A2 B2",
            attrs=Attrs(IO_STANDARD="LVCMOS33", SLEW="FAST")
        ),

        SDRAMResource(1,
            clk="C6",
            cs=None,
            we="C7",
            ras="D7",
            cas="E7",
            ba="A7",
            a="A9 E10 B12 D13 C12 D11 D10 E9 D9 B7 C8",
            dq="E2 D3 A4 E4 D4 C4 E5 D5 E6 D6 D8 A8 B8 B10 B11 E11",
            attrs=Attrs(IO_STANDARD="LVCMOS33", SLEW="FAST")
        ),

        Resource("eth_rgmii", 0,
            Subsignal("rst",     PinsN("P5", dir="o")),
            Subsignal("mdc",     Pins("P3", dir="o")),
            Subsignal("mdio",    Pins("T2", dir="io")),
            Subsignal("tx_clk",  Pins("M2", dir="o")),
            Subsignal("tx_ctl",  Pins("M3", dir="o")),
            Subsignal("tx_data", Pins("L1 L3 P2 L4", dir="o")),
            Subsignal("rx_clk",  Pins("M1", dir="i")),
            Subsignal("rx_ctl",  Pins("N6", dir="i")),
            Subsignal("rx_data", Pins("N1 M5 N5 M6", dir="i")),
            Attrs(IO_TYPE="LVCMOS25")
        ),

        Resource("eth_rgmii", 1,
            Subsignal("rst",     PinsN("P5", dir="o")),
            Subsignal("mdc",     Pins("P3", dir="o")),
            Subsignal("mdio",    Pins("T2", dir="io")),
            Subsignal("tx_clk",  Pins("M12", dir="o")),
            Subsignal("tx_ctrl", Pins("R15", dir="o")),
            Subsignal("tx_data", Pins("T14 R12 R13 R14", dir="o")),
            Subsignal("rx_clk",  Pins("M16", dir="i")),
            Subsignal("rx_ctrl", Pins("L15", dir="i")),
            Subsignal("rx_data", Pins("P13 N13 P14 M15", dir="i")),
            Attrs(IO_TYPE="LVCMOS25")
        ),
    ]
    connectors = [
        Connector("HUB75", 0, "F3  F1  G3  - G2  H3  H5  F15 L2 K1 J5 K2 B16 J14 F12 -"), # J1
        Connector("HUB75", 1, "J4  K3  G1  - K4  C2  E3  F15 L2 K1 J5 K2 B16 J14 F12 -"), # J2
        Connector("HUB75", 2, "H4  K5  P1  - R1  L5  F2  F15 L2 K1 J5 K2 B16 J14 F12 -"), # J3
        Connector("HUB75", 3, "P4  R2  M8  - M9  T6  R6  F15 L2 K1 J5 K2 B16 J14 F12 -"), # J4
        Connector("HUB75", 4, "M11 N11 P12 - K15 N12 L16 F15 L2 K1 J5 K2 B16 J14 F12 -"), # J5
        Connector("HUB75", 5, "K16 J15 J16 - J12 H15 G16 F15 L2 K1 J5 K2 B16 J14 F12 -"), # J6
        Connector("HUB75", 6, "H13 J13 H12 - G14 H14 G15 F15 L2 K1 J5 K2 B16 J14 F12 -"), # J7
        Connector("HUB75", 7, "A15 F16 A14 - E13 B14 A13 F15 L2 K1 J5 K2 B16 J14 F12 -"), # J8
        # in reference to https://raw.githubusercontent.com/cyber-murmel/chubby-hat/master/hardware/chubby%20hat/plot/pdf/chubby%20hat.pdf#page=1
        Connector("pmod", 0, "L2  J5  B16 F12 - - F15 K1  K2  J14 - -"), # PMOD1
        Connector("pmod", 1, "C2  G2  F3  H3  - - K3  H5  G3  F1  - -"), # PMOD2
        Connector("pmod", 2, "H4  L5  K4  J4  - - P1  K5  E3  G1  - -"), # PMOD3
        Connector("pmod", 3, "M9  P4  T6  R1  - - R6  M8  R2  F2  - -"), # PMOD4
        Connector("pmod", 4, "J12 N12 K15 M11 - - G16 N11 L16 P12 - -"), # PMOD5
        Connector("pmod", 5, "G14 H13 K16 H15 - - G15 H12 J16 J15 - -"), # PMOD6
        Connector("pmod", 6, "E13 A14 B14 H14 - - A13 A14 F16 J13 - -"), # PMOD7
    ]

    @property
    def file_templates(self):
        return {
            **super().file_templates,
            "{{name}}-openocd.cfg": r"""
            interface ftdi
            ftdi_vid_pid 0x0403 0x6010
            ftdi_channel 0
            ftdi_layout_init 0xfff8 0xfffb

            reset_config none
            adapter_khz 24000

            transport select jtag
            jtag newtap lfe5u25 tap -expected-id 0x41111043 -irlen 8 -irmask 0xFF -ircapture 0x05
            """
        }

    def toolchain_program(self, products, name):
        openocd = os.environ.get("OPENOCD", "openocd")
        with products.extract("{}-openocd.cfg".format(name), "{}.svf".format(name)) \
                as (config_filename, vector_filename):
            subprocess.check_call([openocd,
                "-f", config_filename,
                "-c", "init; svf -quiet {}; exit".format(vector_filename)
            ])


if __name__ == "__main__":
    from test.blinky import *
    Colorlight5A75BV7_0Platform().build(Blinky(), do_program=True)
