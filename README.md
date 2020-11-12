<html>
  <body>
    <h1>Hey There , I am Ashley !</h1>
    <p><b>Ashley</b> Version <sup><b>0.0.4</b></sup></p>
    <hr>
    <h2>Requirements ?</h2>
    <p>Well First , you need to install <b>Python</b> and <b>Pip</b> and <b>Venv</b> on your device .</p>
    <p>Second , it's required to have <b>MySQL</b> too .</p>
    <p>Third , There are <b>Python libs</b> on <a href="https://github.com/BlackIQ/Ashley/blob/main/requirements.txt">requirements.txt</a></p>
    <hr>
    <h2>How to install ?</h2>
    <h3>On Linux</h3>
    <h5>Debian : </h5>
    <code>sudo apt install python3 python3-pip python3-venv</code>
    <br>
    <code>sudo apt install mariadb-server maridb-client</code>
    <br>
    <code>sudo systemctl restart mysql</code>
    <hr>
    <h2>How To config MySQL ?</h2>
    <code>$ sudo mysql</code>
    <br>
    <code>> CREATE USER 'Ashley'@'localhost' IDENTIFIED BY 'Ashley';</code>
    <br>
    <code>> GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';</code>
    <br>
    <code>> FLUSH PRIVILEGES;</code>
    <br>
    <code>> exit</code>
    <br>
    <code>$ sudo systemctl restart mysql.service</code>
    <hr>
    <h2>How to get , Create venv & Install libss ?</h2>
    <code>git clone https://github.com/BlackIQ/Ashley && cd Ashley</code>
    <br>
    <code>python3 -m venv venv && source venv/bin/activate</code>
    <br>
    <code>pip3 install -r requirements.txt</code>
    <hr>
    <h2>How to run ?</h2>
    <code>python3 Ashley.py</code>
    <hr>
    <p>For know m better , <b>I am</b> :</p>
    <p>Daughter of <b><a href="https://github.com/Annahita2004">Anna</a></b> !</p>
    <p>Developed with &hearts; by <b><a href="https://github.com/BlackIQ">Amir</a></b> .<p>
  </body>
</html>