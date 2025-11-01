#raspberry pi 5用プログラム
#ライブラリのインポート
import RPi.GPIO as GPIO
import time
import threading

class rotaly:
    def __init__(self, x, y, z):
        #クラス内変数の設定
        #ピンの設定
        self.x = x
        self.y = y
        self.z = z
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(x, GPIO.IN)
        GPIO.setup(y, GPIO.IN)
        GPIO.setup(z, GPIO.IN)
        #rpsの初期設定
        self.count_x = 0
        self.count_y = 0
        self.count_z = 0
        #反応はじめ判定用フラグ
        self.flag_x = False
        self.flag_y = False
        self.flag_z = False
    def get_x_rps(self):
        #x軸用コード
        while True:
            if GPIO.input(self.x) == GPIO.LOW:
                if not self.flag_x:
                    self.flag_x = True
                    self.count_x = self.count_x + 1
            else:
                self.flag_x = False
                self.past_time_x = time.time()
            time.sleep(0.001)
    def get_y_rps(self):
        #y軸用コード
        while True:
            if GPIO.input(self.y) == GPIO.LOW:
                if not self.flag_y:
                    self.flag_y = True
                    self.count_y = self.count_y + 1
            else:
                self.flag_y = False
            time.sleep(0.001)
    def get_z_rps(self):
        #z軸用コード
        while True:
            if GPIO.input(self.z) == GPIO.LOW:
                if not self.flag_z:
                    self.flag_z = True
                    self.count_z = self.count_z + 1
            else:
                self.flag_z = False
            time.sleep(0.001)

if  __name__ == "__main__":
    try:
        #gpioピンの設定
        motor_x_center = 12
        motor_x_back = 18
        motor_y_center = 13
        motor_y_back = 19
        rotaly_x = 15
        rotaly_y = 16
        rotaly_z = 17
        button_1 = 1
        button_2 = 2
        lmit_switch_1 = 6
        lmit_switch_2 = 7
        lmit_switch_3 = 8
        lmit_switch_4 = 9
        lmit_switch_5 = 10
        stop_switch = 11
        GPIO.setup(button_1, GPIO.IN)
        GPIO.setup(button_2, GPIO.IN)
        GPIO.setup(lmit_switch_1, GPIO.IN)
        GPIO.setup(lmit_switch_2, GPIO.IN)
        GPIO.setup(lmit_switch_3, GPIO.IN)
        GPIO.setup(lmit_switch_4, GPIO.IN)
        GPIO.setup(lmit_switch_5, GPIO.IN)
        GPIO.setup(stop_switch, GPIO.IN)
        encode = rotaly(rotaly_x, rotaly_y, rotaly_z)
        thred_x = threading.Thread(target=encode.get_x_rps, daemon=True)
        thred_y = threading.Thread(target=encode.get_y_rps, daemon=True)
        thred_z = threading.Thread(target=encode.get_z_rps, daemon=True)
        thred_x.start()
        thred_y.start()
        thred_z.start()
        print("起動")
        while True:
            time.sleep(0.01)
    finally:
        GPIO.cleanup()
        print("gpio解放")