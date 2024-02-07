Control Remoto 
=========

Con el ARS-USB también vas a poder controlar remotamente el motor de antenas. 

Aunque hay varias opciones como dejar el ordenador remoto encendido y usar AnyDesk o Teamviewer para conectarte al ordenador remoto, posiblemente lo más eficaz e interesante sea empleando una **Raspberry Pi** (RsPi), **Rock 3** o miniordenador similar.

.. Note:: 
    Desde 2020 y debido a los problemas de componentes, conseguir RsPi 3 o 4 se hizo bastante complicado y sobre todo los precios se disparando. 
    En el 2023 encuentro una alternativa a la RsPi y empiezo a suministrar los equipos Rock3 que en precio y prestaciones son mucho más interesante que la RsPi. 
    No obstante tanto el RocK3 como las RsPi emplean el mismo S.O. luego todo el software que funciona en un Rock3 también lo hace en la RsPi o en otras alternativas como Orange Pi, etc...

----------

Estos miniordenadores ejecutan una versión de Linux reducida y el ARS-USB (u otros equipos de EA4TX como el RemoteBox) se puede conectar a cualquiera de los 4 puertos USB que incluyen. El S.O. Linux detecta el ARS-USB y crea un puerto serie, que en este caso se llama: /dev/ttyACM0. 
Mediante un software que se llama **ser2net** podemos hacer ese puerto serie sea enrutado hacia el mundo TCP/IP, con lo que conseguimos que el ARS-USB sea accesible en TCP/IP.

Además el usar un miniordenador el consumo de energía es mínimo.

Seguramente haya más opciones para el control en remoto del motor con el ARS-USB, pero aqui vamos a describir 3 opciones que considero interesantes:
    
    - ✅ Ser2net:   Es la opción más sencilla. Sirve para que se pueda conectar un programa via TCP/IP y acceda al ARS-USB. Por ejemplo si queremos usar el **ARSVCOM**
    - ✅ remoteRotator: Además de usar el ser2net como en el caso anterior, el remotoRotator proporciona una interface WEB, luego accesible desde Moviles, Tabletas, Etc
    - ✅ node-red: Node-Red es una plataforma IoT que se ha hecho muy popular y dota de una interface gráfica ademas de ser muy extendida en el mundo del Radioaficionado. 

.. toctree::
   :maxdepth: 2
   
   rspi/ser2net
   rspi/remoterotator
   rspi/nodered
   