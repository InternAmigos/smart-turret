#include <Arduino.h>
//comment
void setup()
{
    Serial.begin(9600);

    pinMode(LED_BUILTIN, OUTPUT);

    delay(3000);

    Serial.println("BOOT");
}

void loop()
{
    if (Serial.available())
    {
        digitalWrite(LED_BUILTIN, HIGH);

        Serial.println("DATA RECEIVED");

        delay(1000);

        digitalWrite(LED_BUILTIN, LOW);

        while (Serial.available())
        {
            Serial.read();
        }
    }
}