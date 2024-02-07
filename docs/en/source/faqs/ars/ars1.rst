Can I replace my controller with an ARS?
=========

Yes, you can.

The ARS-USB was initially designed to be connected to the original controller of the motor, but it can be replaced without major issues. Several wiring diagrams are included in the CD-ROM or download software as examples. What is important to note is that most motors operate at 24V, so you will need a power supply to move the motor.

Another detail is that some motors that operate on alternating current use a capacitor for starting, and this capacitor is usually inside the controller. When replacing the original controller with an ARS-USB, you will need to add one. This is the case, for example, with the HAMIV or T2X.

Another option is to use the ARS-USB_Yaesu or ARS-USB_PST, as these models are already prepared to be connected directly to the motor.

ARS-USB Controllers
===============

Since 2020, there have been 2 new models of ARS-USB that allow you to replace the original controller with these new controllers:

 - **ARS-USB_Yaesu:** This model is used to replace the Yaesu controller in models that operate at 24Vdc, such as: G800, G1000, G2800, or the new G450ADC. It can also be used for any other motor operating at 24Vdc and includes everything needed to connect and operate the motor.
 - **ARS-USB_PST:** This model is used to replace the Prosistel controller from the B and D series, which use a multi-turn potentiometer and operate at 12 or 24Vdc. It is also valid for any motor that uses a multi-turn potentiometer.

Some relay seems not to work
=================================

Many times I receive an email from a new customer saying that one of the relays is not working. The ARS-USB includes a protection mechanism to prevent situations where the relays cannot be activated. For example, if the ARS reads 0 (or the ADC value is the left limit), then the ARS prevents and inhibits the left-turn relay from being activated.

This link explains the reason and why:
    https://ea4tx.com/faqs/ars-usb-faqs/some-relay-is-not-working/


Reassigning the COM port in Windows
=================================

The first time you install or connect the ARS to the computer, you will need to know which COM or serial port has been assigned by Windows.

Visit this link that will explain how to find the port and how you can change it:
    https://ea4tx.com/faqs/ars-usb-faqs/ars-usb-comserial-port
    

Is my rotator supported?
========================

Practically all motors that include a potentiometer (POT) in the motor – whether commercial or self-built – are supported.

The ARS-USB includes an ADC converter, and through this, the voltage reaching the controller from the POT is converted into a digital value. Thanks to calibration, the ARS-USB uses this reading voltage as the reference where the motor is located. Motors without potentiometers can also be used, for example, using satellite dish actuators; for this, we need to add a digital inclinometer like the ones we offer in the Store.

Thanks to this type of inclinometer, we can read from the ARS a voltage that will be proportional to the inclination we have.

**Note:** Rottors that use pulses or encoders to determine their position are not supported

How can I control the ARS-USB from the computer?
===================================================

You can use any program capable of controlling the Yaesu GS232A interface.

This is because the ARS-USB is compatible with Yaesu commands. You can see some examples by following this link:
    https://ea4tx.com/faqs/ars-usb-faqs/ars-usb-3rd-programs-setup/

Also, remember that the program **ARSVCOM** is included, and through this program, we can also create a virtual port and emulate other motor models, expanding the options for it to be controlled by any program.

How to activate Absolute Mode on the ARS-USB
====================================================

Absolute mode is activated when starting the ARS-USB while pressing the **F2** button.

By activating this mode at startup, the LCD will display the message:
    **MODE ABSOLUTE ON**

With absolute mode activated, the ARS-USB display will show the ADC converter's position in parentheses. Example for the Azimuth & Elevation model:
    AZ: 180º (0)
    EL: 90º (512)

The microprocessor includes a 10-bit ADC converter per input (Az and Elev), which allows reading a digital value between 0-1022.
In certain cases, it may be interesting to know what value the ADC converter has, and this is one way to find out (there is another way through commands in the serial port).

On the other hand, in models where the ARS-USB acts as a controller (ARS-USB_Yaesu and ARS-USB_PST) with **Absolute Mode** activated, we can rotate without limits. That is, absolute mode disables the end-of-travel sensor supervisor, so we can freely rotate the motor.

Factory Configuration (F3+F4)
===================================

There are times when it may be useful to load the default configuration. This is achieved by turning on the ARS-USB and pressing the F3 and F4 buttons simultaneously.