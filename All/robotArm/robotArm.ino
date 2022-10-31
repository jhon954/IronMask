#include <Servo.h>
#include <SoftwareSerial.h>
Servo pinza;
Servo subir;
Servo levantar;
Servo rotar;

int posi_l=50;
int posi_r=10;
int posi_s=110;
int posi_p=45;
int option;

void setup() {
 Serial.begin (9600);
 levantar.attach(12);
 levantar.write(50);
 rotar.attach(13);
 rotar.write(10);
 subir.attach(11);
 subir.write(110);
 pinza.attach(10);
 pinza.write(50);

}
void movimiento(int posi,int posf, Servo Myservo){
 int op;
 if (posi>posf)
 op=-1;
 else
 op=1;
 for (int i=posi;i!=posf;i=i+op){
 Myservo.write(i);
 delay (15);
 }
}
void loop() {
 if (Serial.available() > 0){
 option = Serial.read();
 Serial.println(option);
 }

 switch(option)
 {
 case 65:
 movimiento(20,150,rotar);
 movimiento(50,150,levantar);
 movimiento(110,70,subir);
 movimiento(50,20,pinza);
 delay(300);
 movimiento(20,50,pinza);
 movimiento(150,20,rotar);
 movimiento(150,50,levantar);
 movimiento(70,110,subir);
 break;
 /*case 65:
 movimiento(20,100,rotar);
 movimiento(50,75,levantar);
 movimiento(110,45,subir);
 movimiento(50,20,pinza);
 delay(300);
 movimiento(20,50,pinza);
 movimiento(100,20,rotar);
 movimiento(75,50,levantar);
 movimiento(45,110,subir);
 break;
 case 'c':
 movimiento(20,10,rotar);
 movimiento(50,90,levantar);
 movimiento(110,10,subir);
 movimiento(50,10,pinza);
 delay(300);
 movimiento(10,50,pinza);
 movimiento(10,20,rotar);
 movimiento(90,50,levantar);
 movimiento(10,110,subir);
 break;*/
 }
}
