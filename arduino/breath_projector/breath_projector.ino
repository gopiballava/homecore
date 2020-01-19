/*
  Mega analogWrite() test

  This sketch fades LEDs up and down one at a time on digital pins 2 through 13.
  This sketch was written for the Arduino Mega, and will not work on other boards.

  The circuit:
  - LEDs attached from pins 2 through 13 to ground.

  created 8 Feb 2009
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogWriteMega
*/

// These constants won't change. They're used to give names to the pins used:
const int lowestPin = 2;
const int highestPin = 10;

const int start_bpm = 10;
const int end_bpm = 6;
const unsigned long duration_minutes = 10;
const unsigned long duration_millis = duration_minutes * 60 * 1000;

void set_led(int led_id, float led_brightness)
{
  int led_base = 2 + led_id * 3;
  //Serial.println(led_brightness);
  // Red
  analogWrite(led_base, 255 - led_brightness * 250);
  // Greed
  analogWrite(led_base + 1, 255 - led_brightness * 160);
  // Blue
  analogWrite(led_base + 2, 255 - led_brightness * 160);
}

void setup() {
  // set pins 2 through 13 as outputs:
  for (int thisPin = lowestPin; thisPin <= highestPin; thisPin++) {
    pinMode(thisPin, OUTPUT);
    analogWrite(thisPin, 254);
  }
  Serial.begin(115200);
  //set_led(1, 1);
  //set_led(2, 0);
}

void loop()
{
  int bpm = float(millis()) / duration_millis * (end_bpm - start_bpm) + start_bpm;
  int delay_ms = 60000 / bpm / 40;
  Serial.print(bpm);
  Serial.print(" ");
  Serial.print(millis());
  Serial.print(" ");
  Serial.println(duration_millis);

  if(millis() >= duration_millis)
  {
    for(int i = 0; i < 20; i++)
    {
      set_led(1, (float)(20 - i) / 20);
      delay(delay_ms);
    }
    while(true)
    {}
  }
  
  for(int i = 0; i < 20; i++)
  {
    set_led(0, (float)i / 20.);
    set_led(1, (float)(20 - i) / 20);
    set_led(2, (float)i / 20);
    delay(delay_ms);
  }
  for(int i = 20; i >= 0; i--)
  {
    set_led(0, (float)i / 20.);
    set_led(1, (float)(20 - i) / 20);
    set_led(2, (float)i / 20);
    delay(delay_ms);
  }
}
void xloop() {
  // iterate over the pins:
  for (int thisPin = lowestPin; thisPin <= highestPin; thisPin++) {
    // fade the LED on thisPin from off to brightest:
    for (int brightness = 0; brightness < 128; brightness++) {
      analogWrite(thisPin, brightness);
      delay(2);
    }
    // fade the LED on thisPin from brightest to off:
    for (int brightness = 128; brightness >= 0; brightness--) {
      analogWrite(thisPin, brightness);
      delay(2);
    }
    // pause between LEDs:
    delay(100);
  }
}
