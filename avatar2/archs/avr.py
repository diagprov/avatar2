# from capstone import CS_ARCH_ARM, CS_MODE_LITTLE_ENDIAN, CS_MODE_BIG_ENDIAN

from .architecture import Architecture
import avatar2

from avatar2.installer.config import QEMU, PANDA, OPENOCD, GDB_AVR

class AVR(Architecture):

    get_qemu_executable = Architecture.resolve(QEMU)
    get_panda_executable = Architecture.resolve(PANDA)
    get_gdb_executable  = Architecture.resolve(GDB_AVR)
    get_oocd_executable = Architecture.resolve(OPENOCD)

    registers = {
        'r0': 0,'r1': 1,'r2': 2,'r3': 3,'r4': 4,'r5': 5,'r6': 6,'r7': 7,'r8': 8,
        'r9': 9,'r10': 10,'r11': 11,'r12': 12,'r13': 13,'r14': 14,'r15': 15,
        'r16': 16,'r17': 17,'r18': 18,'r19': 19,'r20': 20,'r21': 21,'r22': 22,
        'r23': 23,'r24': 24,'r25': 25,'r26': 26,'r27': 27,'r28': 28,'r29': 29,
        'r30': 30,'r31': 31,
        'SREG': 32, 'SP': 33, 'PC2': 34, 'pc' : 35
    }

class AVR_UNO(AVR):
    cpu_model = 'avr5-avr-cpu'
    qemu_name = 'avr'
    gdb_name = 'avr'
    
    @staticmethod
    def init(avatar):
        pass

class AVR_MEGA2560(AVR):
    cpu_model = 'arduino-mega-2560-v3'
    qemu_name = 'avr'
    gdb_name = 'avr'
    
    @staticmethod
    def init(avatar):
        pass
