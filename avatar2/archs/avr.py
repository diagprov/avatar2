# from capstone import CS_ARCH_ARM, CS_MODE_LITTLE_ENDIAN, CS_MODE_BIG_ENDIAN

from .architecture import Architecture
import avatar2

from avatar2.installer.config import QEMU, PANDA, OPENOCD, GDB_ARM

class AVR(Architecture):

    get_qemu_executable = Architecture.resolve(QEMU)
    get_panda_executable = Architecture.resolve(PANDA)
    get_gdb_executable  = Architecture.resolve()
    get_oocd_executable = Architecture.resolve(OPENOCD)

class AVR_UNO(AVR):
    cpu_model = 'uno'
    qemu_name = 'avr'
    gdb_name = 'avr'
    
    @staticmethod
    def init(avatar):
        pass

class AVR_MEGA2560(AVR):
    cpu_model = 'mega2560'
    qemu_name = 'avr'
    gdb_name = 'avr'
    
    @staticmethod
    def init(avatar):
        pass
