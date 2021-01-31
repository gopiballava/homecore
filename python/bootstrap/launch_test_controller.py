#!env python3
import sys
print(f'System path: {sys.path}')
from .generate_template import GenerateBootstrap, make_standard_bootstrap_generator
import sys

DUMMY_MAC = '0xcafe'
DEVICE_DATA = {
    DUMMY_MAC: {
        'global': {},
        'main_loop': {
            'remote_ip': '192.168.88.10',
        },
    }
}


def main():
    gb = make_standard_bootstrap_generator(DEVICE_DATA)
    code_lines = gb.generate_for_device(DUMMY_MAC)
    print(f'Got lines: {code_lines}')
    gb.exec_for_device(DUMMY_MAC)
    return 0


if __name__ == '__main__':
    sys.exit(main())