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