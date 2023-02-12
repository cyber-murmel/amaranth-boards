# This file has been auto-generated with 'gen_util_platform.py'


from ..alchitry_au import AlchitryAuPlatform
from ..arrow_deca import ArrowDECAPlatform
from ..arty_a7 import ArtyA7_35Platform, ArtyA7_100Platform
from ..arty_s7 import ArtyS7_25Platform, ArtyS7_50Platform
from ..arty_z7 import ArtyZ720Platform
from ..atlys import AtlysPlatform
from ..blackice import BlackIcePlatform
from ..blackice_ii import BlackIceIIPlatform
from ..chameleon96 import Chameleon96Platform
from ..colorlight_5a75b_r7_0 import Colorlight_5A75B_R70Platform
from ..de0 import DE0Platform
from ..de0_cv import DE0CVPlatform
from ..de10_lite import DE10LitePlatform
from ..de10_nano import DE10NanoPlatform
from ..de1_soc import DE1SoCPlatform
from ..ebaz4205 import EBAZ4205Platform
from ..ecp5_5g_evn import ECP55GEVNPlatform
from ..ecpix5 import ECPIX585Platform, ECPIX545Platform
from ..fomu_hacker import FomuHackerPlatform
from ..fomu_pvt import FomuPVTPlatform
from ..genesys2 import Genesys2Platform
from ..ice40_hx1k_blink_evn import ICE40HX1KBlinkEVNPlatform
from ..ice40_hx8k_b_evn import ICE40HX8KBEVNPlatform
from ..ice40_up5k_b_evn import ICE40UP5KBEVNPlatform
from ..icebreaker import ICEBreakerPlatform
from ..icebreaker_bitsy import ICEBreakerBitsyPlatform
from ..icestick import ICEStickPlatform
from ..icesugar import ICESugarPlatform
from ..icesugar_nano import ICESugarNanoPlatform
from ..kc705 import KC705Platform
from ..kcu105 import KCU105Platform
from ..logicbone import LogicbonePlatform, Logicbone85FPlatform
from ..machxo3_sk import MachXO3SKPlatform
from ..mercury import MercuryPlatform
from ..microzed_z010 import MicroZedZ010Platform
from ..microzed_z020 import MicroZedZ020Platform
from ..mister import MisterPlatform
from ..nandland_go import NandlandGoPlatform
from ..nexys4ddr import Nexys4DDRPlatform
from ..numato_mimas import NumatoMimasPlatform
from ..orangecrab_r0_1 import OrangeCrabR0_1Platform
from ..orangecrab_r0_2 import (
    OrangeCrabR0_2Platform,
    OrangeCrabR0_2_25FPlatform,
    OrangeCrabR0_2_85FPlatform,
)
from ..quickfeather import QuickfeatherPlatform
from ..rz_easyfpga_a2_2 import RZEasyFPGAA2_2Platform
from ..sk_xc6slx9 import SK_XC6SLX9Platform
from ..supercon19badge import Supercon19BadgePlatform
from ..te0714_03_50_2I import TE0714_03_50_2IPlatform
from ..tinyfpga_ax1 import TinyFPGAAX1Platform
from ..tinyfpga_ax2 import TinyFPGAAX2Platform
from ..tinyfpga_bx import TinyFPGABXPlatform
from ..ulx3s import (
    ULX3S_12F_Platform,
    ULX3S_25F_Platform,
    ULX3S_45F_Platform,
    ULX3S_85F_Platform,
)
from ..upduino_v1 import UpduinoV1Platform
from ..upduino_v2 import UpduinoV2Platform
from ..versa_ecp5 import VersaECP5Platform
from ..versa_ecp5_5g import VersaECP55GPlatform
from ..zturn_lite_z007s import ZTurnLiteZ007SPlatform
from ..zturn_lite_z010 import ZTurnLiteZ010Platform

__all__ = [
    "get_platform_names",
    "get_platform_by_name",
]

_ALL_PLATFORM_NAMES = [
    "AlchitryAu",
    "ArrowDECA",
    "ArtyA7_35",
    "ArtyA7_100",
    "ArtyS7_25",
    "ArtyS7_50",
    "ArtyZ720",
    "Atlys",
    "BlackIce",
    "BlackIceII",
    "Chameleon96",
    "Colorlight_5A75B_R70",
    "DE0",
    "DE0CV",
    "DE10Lite",
    "DE10Nano",
    "DE1SoC",
    "EBAZ4205",
    "ECP55GEVN",
    "ECPIX585",
    "ECPIX545",
    "FomuHacker",
    "FomuPVT",
    "Genesys2",
    "ICE40HX1KBlinkEVN",
    "ICE40HX8KBEVN",
    "ICE40UP5KBEVN",
    "ICEBreaker",
    "ICEBreakerBitsy",
    "ICEStick",
    "ICESugar",
    "ICESugarNano",
    "KC705",
    "KCU105",
    "Logicbone",
    "Logicbone85F",
    "MachXO3SK",
    "Mercury",
    "MicroZedZ010",
    "MicroZedZ020",
    "Mister",
    "NandlandGo",
    "Nexys4DDR",
    "NumatoMimas",
    "OrangeCrabR0_1",
    "OrangeCrabR0_2",
    "OrangeCrabR0_2_25F",
    "OrangeCrabR0_2_85F",
    "Quickfeather",
    "RZEasyFPGAA2_2",
    "SK_XC6SLX9",
    "Supercon19Badge",
    "TE0714_03_50_2I",
    "TinyFPGAAX1",
    "TinyFPGAAX2",
    "TinyFPGABX",
    "ULX3S_12F_",
    "ULX3S_25F_",
    "ULX3S_45F_",
    "ULX3S_85F_",
    "UpduinoV1",
    "UpduinoV2",
    "VersaECP5",
    "VersaECP55G",
    "ZTurnLiteZ007S",
    "ZTurnLiteZ010",
]


def get_platform_names():
    return _ALL_PLATFORM_NAMES


def get_platform_by_name(name):
    if "AlchitryAu" == name:
        return AlchitryAuPlatform
    if "ArrowDECA" == name:
        return ArrowDECAPlatform
    if "ArtyA7_35" == name:
        return ArtyA7_35Platform
    if "ArtyA7_100" == name:
        return ArtyA7_100Platform
    if "ArtyS7_25" == name:
        return ArtyS7_25Platform
    if "ArtyS7_50" == name:
        return ArtyS7_50Platform
    if "ArtyZ720" == name:
        return ArtyZ720Platform
    if "Atlys" == name:
        return AtlysPlatform
    if "BlackIce" == name:
        return BlackIcePlatform
    if "BlackIceII" == name:
        return BlackIceIIPlatform
    if "Chameleon96" == name:
        return Chameleon96Platform
    if "Colorlight_5A75B_R70" == name:
        return Colorlight_5A75B_R70Platform
    if "DE0" == name:
        return DE0Platform
    if "DE0CV" == name:
        return DE0CVPlatform
    if "DE10Lite" == name:
        return DE10LitePlatform
    if "DE10Nano" == name:
        return DE10NanoPlatform
    if "DE1SoC" == name:
        return DE1SoCPlatform
    if "EBAZ4205" == name:
        return EBAZ4205Platform
    if "ECP55GEVN" == name:
        return ECP55GEVNPlatform
    if "ECPIX585" == name:
        return ECPIX585Platform
    if "ECPIX545" == name:
        return ECPIX545Platform
    if "FomuHacker" == name:
        return FomuHackerPlatform
    if "FomuPVT" == name:
        return FomuPVTPlatform
    if "Genesys2" == name:
        return Genesys2Platform
    if "ICE40HX1KBlinkEVN" == name:
        return ICE40HX1KBlinkEVNPlatform
    if "ICE40HX8KBEVN" == name:
        return ICE40HX8KBEVNPlatform
    if "ICE40UP5KBEVN" == name:
        return ICE40UP5KBEVNPlatform
    if "ICEBreaker" == name:
        return ICEBreakerPlatform
    if "ICEBreakerBitsy" == name:
        return ICEBreakerBitsyPlatform
    if "ICEStick" == name:
        return ICEStickPlatform
    if "ICESugar" == name:
        return ICESugarPlatform
    if "ICESugarNano" == name:
        return ICESugarNanoPlatform
    if "KC705" == name:
        return KC705Platform
    if "KCU105" == name:
        return KCU105Platform
    if "Logicbone" == name:
        return LogicbonePlatform
    if "Logicbone85F" == name:
        return Logicbone85FPlatform
    if "MachXO3SK" == name:
        return MachXO3SKPlatform
    if "Mercury" == name:
        return MercuryPlatform
    if "MicroZedZ010" == name:
        return MicroZedZ010Platform
    if "MicroZedZ020" == name:
        return MicroZedZ020Platform
    if "Mister" == name:
        return MisterPlatform
    if "NandlandGo" == name:
        return NandlandGoPlatform
    if "Nexys4DDR" == name:
        return Nexys4DDRPlatform
    if "NumatoMimas" == name:
        return NumatoMimasPlatform
    if "OrangeCrabR0_1" == name:
        return OrangeCrabR0_1Platform
    if "OrangeCrabR0_2" == name:
        return OrangeCrabR0_2Platform
    if "OrangeCrabR0_2_25F" == name:
        return OrangeCrabR0_2_25FPlatform
    if "OrangeCrabR0_2_85F" == name:
        return OrangeCrabR0_2_85FPlatform
    if "Quickfeather" == name:
        return QuickfeatherPlatform
    if "RZEasyFPGAA2_2" == name:
        return RZEasyFPGAA2_2Platform
    if "SK_XC6SLX9" == name:
        return SK_XC6SLX9Platform
    if "Supercon19Badge" == name:
        return Supercon19BadgePlatform
    if "TE0714_03_50_2I" == name:
        return TE0714_03_50_2IPlatform
    if "TinyFPGAAX1" == name:
        return TinyFPGAAX1Platform
    if "TinyFPGAAX2" == name:
        return TinyFPGAAX2Platform
    if "TinyFPGABX" == name:
        return TinyFPGABXPlatform
    if "ULX3S_12F_" == name:
        return ULX3S_12F_Platform
    if "ULX3S_25F_" == name:
        return ULX3S_25F_Platform
    if "ULX3S_45F_" == name:
        return ULX3S_45F_Platform
    if "ULX3S_85F_" == name:
        return ULX3S_85F_Platform
    if "UpduinoV1" == name:
        return UpduinoV1Platform
    if "UpduinoV2" == name:
        return UpduinoV2Platform
    if "VersaECP5" == name:
        return VersaECP5Platform
    if "VersaECP55G" == name:
        return VersaECP55GPlatform
    if "ZTurnLiteZ007S" == name:
        return ZTurnLiteZ007SPlatform
    if "ZTurnLiteZ010" == name:
        return ZTurnLiteZ010Platform
