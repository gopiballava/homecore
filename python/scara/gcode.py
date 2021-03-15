import math
import serial
import time
import traceback

DEFAULT_FEED = 20


# G92 x0 y0 z0\n')
# G1X-0.08Y0.08F80\n')

FAKE = True

class TransmitGcode:
    def __init__(self, port='/dev/tty.usbmodem141401'):
        self.x = 0
        self.y = 0
        if not FAKE:
            self.serial = serial.Serial(port, 115200, timeout=3)
            time.sleep(2)
            print(self.serial.readlines())
#             self.set_mm()
#             self.set_absolute()
            # [G0 G54 G17 G21 G90 G94 M0 M5 M9 T0 F0. S0.]
#             self._send_command('G0 G54 G17 G21 G90 G94 M0 M5 M9')
            self._send_command('$$', multiple=True)
    
    def _send_command(self, cmd_string: str, multiple=False):
        if FAKE:
            print(f'{cmd_string}')        
        else:
            self.serial.write(f'{cmd_string}\r\n'.encode('UTF-8'))
            print(f'Sent {cmd_string}')
            if multiple:
                response = self.serial.readlines()
                print(f'Responses: {response}')
            else:
                response = self.serial.readline().strip()
                if response != b'ok':
                    print(f'WARNING: Serial response to {cmd_string} was {response}; expected "ok"')
    
    def xxmove_to(self, x=None, y=None, feed=DEFAULT_FEED):
        cmd = 'G1'
        if x is not None:
            cmd += f'X{x}'
        if y is not None:
            cmd += f'Y{y}'
        cmd += f'F{feed}'
        self._send_command(cmd)

    def move_to(self, x, y):
        dx = round(x - self.x, 4)
        dy = round(y - self.y, 4)
        cmd = f'G21G91G1X{dx}Y{dy}F{DEFAULT_FEED}'
        self._send_command(cmd)
        self.x = x
        self.y = y

    def reset_zero(self):
        """Change coordinates so we pretend we are currently at zero."""
        self._send_command('G92 X0 Y0')
    
    def set_mm(self):
        self._send_command('G21')
    
    def set_absolute(self):
        self._send_command('G90')

    def set_always_on(self, is_on):
        if is_on:
#             self._send_command('$1=255')
            pass
        else:
            self._send_command('$1=252')
#             pass

PROXIMAL_ARM = 100
DISTAL_ARM = 134

class ScaraControl:
    def __init__(self):
        self.tx = TransmitGcode()
    
    def set_angles(self, rho, phi):
        if rho < 0 or rho > 120:
            raise Exception(f'Rho out of range - {rho}')
        if phi < 0 or phi > 120:
            raise Exception(f'Phi out of range - {phi}')
        self.tx.move_to(x=rho/360 * 4, y=-phi/360 * 4)
    
    def _coslaw(self, a, b, c):
        return math.degrees(math.acos( (a*a + b*b - c*c) / (2 * a * b) ))

    def set_pos(self, x, y):
        h = math.hypot(x, y)
        phi = self._coslaw(PROXIMAL_ARM, DISTAL_ARM, h)
        a = math.degrees(math.atan(y / x))
        b = self._coslaw(h, PROXIMAL_ARM, DISTAL_ARM)
        rho = 180 - (a + b)
        # print(f'set pos {rho}  {phi}')
        self.set_angles(rho, phi)
    
    def set_pen(self, pen_state):
        self.tx.set_always_on(pen_state)

DRAW_DELAY = 0.01
if __name__ == '__main__':
    sc = ScaraControl()
    try:
        sc.set_pen(True)
        def _draw_box(x, y, mult):
            size = mult * 5
            sc.set_pos(x, y)
    #         input('Return to draw')
            for i in range(5):
                sc.set_pos(x, y + i * mult)
                time.sleep(DRAW_DELAY)
            for i in range(5):
                sc.set_pos(x + i * mult, y + size)
                time.sleep(DRAW_DELAY)
            for i in range(5):
                sc.set_pos(x + size, y + size - i * mult)
                time.sleep(DRAW_DELAY)
            for i in range(5):
                sc.set_pos(x + size - i * mult, y)
                time.sleep(DRAW_DELAY)
#         _draw_box(60, 60, 5)
        for i in range(3):
            _draw_box(30 + i * 7, 60, 3)
        
#         _draw_box(60, 90, 10)
#         _draw_box(100, 20, 5)
#         input('Return to zero!')
    except:
        traceback.print_exc()
    sc.set_pen(False)
    sc.set_angles(0, 0)
    time.sleep(4)
if False:
    sc.set_angles(90, 0)
    sc.set_angles(90, 90)
    sc.set_angles(0, 90)
#     time.sleep(1)
    sc.set_angles(0, 0)
    for i in range(5):
        sc.set_angles(0, 45)
        sc.set_angles(0, 0)

    time.sleep(4)
