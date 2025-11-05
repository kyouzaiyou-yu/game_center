こんにちは.
前日,寝たプログラム班は僕です.<br>
前々日は,某黄色の鳥類の球団のシャンパンファイトを見ていて作業しなかったのも僕です.<br>
前の週の土曜日<i>fireworks</i>で作業しなかったのも僕です.<br>
日曜日は某黄色の鳥類の球団を現地観戦していて作業をしていないのも僕です(Uも).<br>
raspberry pi pico 2のプログラムは書けないからraspberry pi 5(前日に壊れた)にしようといったのも僕です.<br>
そんな僕たちの努力の結晶です.<br>
コードに関しては机上の空論なものがおおいです.<br>
<div align="right">
<strong>2-2</strong>の文化評議員(文化祭の責任者)<br>
TBT
</div>
<hr>
はろーえぶりわん<br>
同じくプログラム班のKでございます。<br>
プログラミングなんて<a href="https://wikiwiki.jp/sbarjp/Lua%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88/Lua%E5%88%9D%E5%BF%83%E8%80%85%E8%AC%9B%E5%BA%A7">ゲーム内LUA</a>以外何もできない人間でしたが、まあなんか理論上は動くコード書けたしいいんじゃないかな。<br>
ちなみに↑のRasPi5は僕の私物です。OSが死んだか物理が死んだかの二択、怖くてまだ確認してません。<br>
<div align="right">
<strong>2-1</strong>の一般人<br>
K
</div>
<h1>TBTが書いたやつ</h1>
raspberry pi 5用
<pre>
<code>
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
</code>
</pre>
arduino用
<pre>
<code>
//arduino用プログラム
String Signal; // シリアルから受け取るコマンド
String count;  // 何らかのカウント用データ（用途に応じて変更）

void setup()
{
    Serial.begin(9600);
    Serial.println("Hello World!"); // ← セミコロン抜け修正
}

void loop()
{
    // シリアルからデータを受け取った場合
    if (Serial.available() > 0)
    {
        Signal = Serial.readStringUntil('\n'); // 1行分の文字列として受信

        if (Signal == "go")
        {
            Serial.println("OK");

            /* モーター処理を書く */
            /* アーム処理を書く */

            Serial.println("please");

            // 次の信号を待つ
            while (Serial.available() == 0)
            {
            }

            count = Serial.readStringUntil('\n');
            Serial.println("OK");

            // モーターを戻す処理のループ
            while (true)
            {
                if (Serial.available() > 0)
                {
                    char c = Serial.read();
                    if (c == '0')
                    { // 0を受け取ったら抜ける
                        break;
                    }
                }

                /* モーターを戻す処理を書く */
            }

            // 「hanasu」が来るまで待つ
            while (true)
            {
                if (Serial.available() > 0)
                {
                    String cmd = Serial.readStringUntil('\n');
                    if (cmd == "hanasu")
                    {
                        /* アームを離す処理を書く */
                        break;
                    }
                }
            }
        }
    }
}
</code>
</pre>
<br>
<h1>Kが書いたコード</h1>
<pre>
<code>
# raspberry pi5用(../TBT/main.pyの進化系)
# ライブラリのインポート

import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)

class rotaly:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        GPIO.setup(x, GPIO.IN)
        GPIO.setup(y, GPIO.IN)
        GPIO.setup(z, GPIO.IN)
        self.count_x = 0
        self.count_y = 0
        self.count_z = 0
        self.flag_x = False
        self.flag_y = False
        self.flag_z = False
        #RPS/distance
        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0
        self.rps_x = 0
        self.rps_y = 0
        self.rps_z = 0
        self.distance_x = 0
        self.distance_y = 0
        self.distance_z = 0
    # 各軸のRPS/現在位置を取得
    def get_x_rps(self):
        prev_rotation = 0
        DISTANCE_PER_ROTATION = 120 # 一回店当たりの進む距離(mm)
        start_time = time.time()
        while True:
            now = time.time()
            # 穴の数を計測
            if GPIO.input(self.x) == GPIO.LOW:
                if not self.flag_x:
                    self.flag_x = True
                    self.count_x = self.count_x + 1
            else:
                self.flag_x = False
                self.past_time_x = time.time()
            
            # 穴の数16で割って軸の回転数に
            self.rotation_x = self.count_x / 16
            
            # 水平移動距離
            self.distance_x = self.rotation_x * DISTANCE_PER_ROTATION
            
            # RPS計測
            if now - start_time >= 0.05:
                start_time = now
                self.rps_x = (self.rotation_x - prev_rotation)*20
            
            prev_rotation = self.rotation_x
            time.sleep(0.001)


#モタドラ制御
#速度の単位:mm/s
class MotorDriver:
    def __init__(self, x_f, x_b, y_f, y_b, en):
        self.PWM_FREQ = 10000
        GPIO.setup(self.x_pwm_pin_f, GPIO.OUT)
        GPIO.setup(self.X_pwm_pin_b, GPIO.OUT)
        # input
        # PWMのピン
        self.x_pwm_pin_f = x_f
        self.X_pwm_pin_b = x_b
        self.y_pwm_pin_f = y_f
        self.y_pwm_pin_b = y_b
        
        self.motor_en = en
        self.x_motor_back = False
        self.x_motor_nowspd = 0
        self.y_motor_nowspd = 0
        self.x_motor_setspd = 0
        self.y_motor_setspd = 0

        # output
        self.x_motor_power = 0 #X軸モーターのPWM
        self.y_motor_output = 0 #Y軸モーターのPWM
        self.z_motor_output = 0 #Z軸モーターのPWM
        self.x_motor_EN = False #X軸モーターのEnable
    
    def motor_x_drive(self):
        """
        とりあえずP制御で様子見
        必要に応じてDも入れる
        """
        prev_x_motor_back = False
        MOTOR_X_P_GAIN = 0.1 # Pゲイン
        self.x_motor_EN = False
        # PWMのやつ
        x_pwm = GPIO.PWM(self.x_pwm_pin_f, self.PWM_FREQ)
        x_pwm.start(0)
        while True:
            # 逆転⇒正回転
            if not self.x_motor_back and prev_x_motor_back:
                x_pwm.stop()
                x_pwm = GPIO.PWM(self.x_pwm_pin_f, self.PWM_FREQ)
                x_pwm.start(0) 
            # 正解店⇒逆転
            elif self.x_motor_back and not prev_x_motor_back:
                x_pwm.stop()
                x_pwm = GPIO.PWM(self.X_pwm_pin_b, self.PWM_FREQ) 
                x_pwm.start(0)
            prev_x_motor_back = self.x_motor_back
            # x軸が正解店の場合の処理（仮実装）
            if not self.x_motor_back:
                x_motor_spd = self.x_motor_nowspd * 120
                x_motor_setspd = self.x_motor_setspd
                spd_diff = x_motor_setspd - x_motor_spd
                self.x_motor_power = max((spd_diff / 120) * MOTOR_X_P_GAIN,0)
            """
            if self.x_motor_power != 0 and not self.x_motor_EN:
                self.x_motor_EN = True
                # GPIO.output(self.motor_en, GPIO.HIGH) <- いらない
                x_pwm.start(min(self.x_motor_power,1) * 100)
            else:
                self.x_motor_EN = False
                x_pwm.stop()
            """
            # 変化したpwmのデューティー比を適応
            x_pwm.ChangeDutyCycle(min(self.x_motor_power,1)*100)
            


if  __name__ == "__main__":
    try:
        #gpioピンの設定
        motor_x_forward = 12
        motor_x_back = 18
        motor_y_forward = 13
        motor_y_back = 19
        motor_en = 14
        rotaly_x = 10
        rotaly_y = 9
        rotaly_z = 11
        button_1 = 2
        button_2 = 3
        lmit_switch_1 = 17
        lmit_switch_2 = 27
        lmit_switch_3 = 22
        lmit_switch_4 = 0
        lmit_switch_5 = 5
        stop_switch = 6
        GPIO.setup(button_1, GPIO.IN)
        GPIO.setup(button_2, GPIO.IN)
        GPIO.setup(lmit_switch_1, GPIO.IN)
        GPIO.setup(lmit_switch_2, GPIO.IN)
        GPIO.setup(lmit_switch_3, GPIO.IN)
        GPIO.setup(lmit_switch_4, GPIO.IN)
        GPIO.setup(lmit_switch_5, GPIO.IN)
        GPIO.setup(stop_switch, GPIO.IN)

        GPIO.setup(motor_en, GPIO.OUT)
        
        encode = rotaly(rotaly_x, rotaly_y, rotaly_z)
        md = MotorDriver(motor_x_forward,motor_x_back,motor_y_forward,motor_y_back,motor_en)

        # スレッドで非同期処理
        thred_x = threading.Thread(target=encode.get_x_rps, daemon=True)
        #thred_y = threading.Thread(target=encode.get_y_rps, daemon=True)
        thred_md = threading.Thread(target=md.motor_x_drive, daemon=True)
        thred_x.start()
        #thred_y.start()
        thred_md.start()

        # ボタンの初期化
        prev_x_button = 0
        prev_y_button = 0


        print("起動")
        GPIO.output(motor_en, GPIO.HIGH)
        while True:
            # メインループ
            md.x_motor_nowspd = encode.rps_x
            # encode.calc_rps_x()  # ここを追加（毎ループで判定）
            print(f"count_x:{encode.count_x}\ncount_y:{encode.count_y}\ncount_z:{encode.count_z}\nrotation_x:{encode.rps_x}\ndistance:{encode.distance_x}\n")
            
            #ボタン等の処理
            
            x_button = GPIO.input(button_1)
            y_button = GPIO.input(button_2)

            """
            テスト用処理：
            ボタン押されたらxを右に移動
            話したら原点に移動
            """
            if x_button:
                md.x_motor_setspd = 60
            
            if not x_button and prev_x_button:
                before_pos = encode.distance_x
                encode.distance_x = 0
                md.x_motor_back = True
                if (before_pos - encode.distance_x) < 50:
                    md.x_motor_power = (before_pos - encode.distance_x)/1000

            prev_x_button = x_button
            prev_y_button = y_button
            # テスト

            time.sleep(0.001)


    finally:
        GPIO.cleanup()
        print("gpio解放")
</code>
</pre>
