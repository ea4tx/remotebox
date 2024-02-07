Puedo sustituir mi mando por un ARS?
=========

Si, si que puedes.

El ARS-USB se diseñó inicialmente para ser conectado al mando original del motor, pero se puede sustituir sin mayores problemas. En el CD-ROM o software de descarga, se incluyen varios esquemas de conexionado a modo de ejemplo. Lo que es importante y hay que tener en cuenta, es que la mayor parte de motores funcionan a 24V, luego vas a necesitar una fuente de alimentación para poder mover el motor. 

Otro detalle, es que algunos motores que funcionan a corriente alterna, emplean un condensador para el arranque y éste suele estar dentro del mando. Al reemplazar el mando original por un ARS-USB, tendrás que poner uno. Este en el caso por ejemplo del HAMIV o T2X.

Otra opción es usar el ARS-USB_Yaesu o ARS-USB_PST, pues esos modelos ya están preparados para conectarse con el motor directamente.

Mandos ARS-USB
===============

Desde el año 2020 existen 2 nuevos modelos de ARS-USB que permiten sustituir el mando original por estos nuevos controladores:

 - **ARS-USB_Yaesu:** y que sirve para reemplazar el mando Yaesu en modelos que funcionan a 24Vcc como son: G800, G1000, G2800 o el nuevo G450ADC. Tambien se puede usar para cualquier otro motor que funcione a 24Vcc e incluye todo lo necesario para conectarse y manejar el motor.
 - **ARS-USB_PST:** y que sirve para reemplazar el mando Prosistel de la serie B y D que emplean potenciometro multivuelta y que funcionan a 12 o 24Vcc. Tambien es válido para cualquier motor que emplee potenciometro multivuelta.

Algún relé parece que no funciona
=================================

Muchas veces recibo un correo de un cliente nuevo que me dice que uno de los relés no funciona.
El ARS-USB incluye un mecanismo de protección, para evitar que en algunas situaciones, los relés no se puedan activar. 
Por ejemplo si el ARS lee 0 (o el valor del ADC es el limite izquierdo) entonces el ARS evita e inhibe que el relé de giro a izquierda se pueda activar.

En este enlace se explica el motivo y el por qué:
    https://ea4tx.com/faqs/ars-usb-faqs/some-relay-is-not-working/


Reasignar el puerto COM en Windows
=================================

La primera vez que instalas o conectas el ARS al ordenador, necesitarás saber qué puerto COM o serie ha sido asignado por Windows.

Visita este enlace que te explicará como saber el puerto y cómo lo puedes cambiar:
    https://ea4tx.com/faqs/ars-usb-faqs/ars-usb-comserial-port


Está mi motor soportado?
========================

Prácticamente todos los motores que incluyen un potenciómetro (POT) en el motor – sean comerciales o autoconstruídos – están soportados.

El ARS-USB incluye un conversor ADC y por medio de éste se convierte la tensión que llega al mando desde el POT en un valor digital. Gracias al calibrado, el ARS-USB emplea esta tensión de lectura como la referencia en la que se encuentra el motor. También se pueden usar motores de elevación que no incluyan potenciómetro, por ejemplo usando actuadores de parabólica; para ello tenemos que poner un inclinómetro digital como los que ofrecemos en la Tienda.

Gracias a este tipo de inclinómetro, podemos leer desde el ARS una tensión que será proporcional a la inclinación que tengamos.

**Nota:** Motores que usan pulsos o encoders para determinar su posición, no están soportados

Cómo puedo controlar el ARS-USB desde el ordenador?
===================================================

Puedes utilizar cualquier programa que sea capaz de controlar el interface de Yaesu GS232A.

Esto es así, porque el ARS-USB es compatible con los comandos de Yaesu. Algunos ejemplos los puedes ver siguiendo este enlace:
    https://ea4tx.com/faqs/ars-usb-faqs/ars-usb-3rd-programs-setup/

Además recuerda que se incluye el programa **ARSVCOM** y que por medio de este programa podemos además crear un puerto virtual y emular otros modelos de motor, ampliando las opciones de poder ser controlado ya, por cualquier programa.

Cómo activar el modo *Modo Absoluto* en el ARS-USB
====================================================

El modo absoluto se activa al arrancar el ARS-USB mientras se presionada el botón **F2**. 

Al activar este modo en el arranque, el LCD va a visualizar el mensaje:
    **MODE ABSOLUTE ON**

Con el modo absoluto activado, el visor del ARS-USB nos va a mostrar entre paréntesis la posición del conversor ADC. Ejemplo para el modelo de Azimuth & Elevación:
	AZ: 180º   (0)
	EL:  90º   (512)
El microprocesador incluye un conversor ADC de 10 bits por entrada (Az y Elev), que permite leer un valor digital entre 0-1022. 
En ciertos casos puede ser interesante saber qué valor tiene el conversor ADC, y esta es una de las formas de saberlo (Hay otra que es por comandos en el puerto serie).

Por otro lado, en los modelo donde el ARS-USB hace de mando/controlador (ARS-USB_Yaesu y ARS-USB_PST) con el **Modo Absoluto** activado, podemos girar sin límites. Es decir, el modo absoluto desactiva el supervidor de finales de carrera con lo cual podemos girar libremente el motor.

Configuración de fábrica (F3+F4)
===================================

Hay veces que nos puede interesar cargar la configuración por defecto. Se consigue encendiendo el ARS-USB y presionando los botones F3 y F4 simultáneamente.