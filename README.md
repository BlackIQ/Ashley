[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FBlackIQ%2FAshley.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FBlackIQ%2FAshley?ref=badge_shield)

<html>
  <body>
    <img src="https://img.shields.io/github/license/BlackIQ/Ashley?style=flat-square" alt="License"/>
    <img src="https://img.shields.io/github/languages/code-size/BlackIQ/Ashley?style=flat-square" alt="Code Size"/>
    <h1>Hey There , I am Ashley !</h1>
    <p><b>Ashley</b> Version <sup><b>0.1.4</b></sup></p>
    <p>Last Update : <b>Jan , 12 , 2021</b></p>
    <hr>
    <h2>Requirements ?</h2>
    <p>Well 1<sup>st</sup> , you need to install <b>Python</b> and <b>Pip</b> and <b>Venv</b> on your device .</p>
    <p>2<sup>nd</sup> , it's required to have <b>MySQL</b> , <b>espeak</b> , <b>ffmpeg</b> and <b>mpg123</b> too .</p>
    <p>3<sup>rd</sup> There are <b>Python libs</b> on <a href="https://github.com/BlackIQ/Ashley/blob/main/requirements.txt">requirements.txt</a></p>
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
    <code>> GRANT ALL PRIVILEGES ON *.* TO 'Ashley'@'localhost';</code>
    <br>
    <code>> FLUSH PRIVILEGES;</code>
    <br>
    <code>> exit</code>
    <br>
    <code>$ sudo systemctl restart mysql.service</code>
    <hr>
    <h2>How to get , Create venv & Install libs ?</h2>
    <code>git clone https://github.com/BlackIQ/Ashley && cd Ashley</code>
    <br>
    <code>python3 -m venv venv && source venv/bin/activate</code>
    <br>
    <code>pip3 install -r requirements.txt</code>
    <hr>
    <h2>How to run ?</h2>
    <code>python3 Ashley.py</code>
    <hr>
    <p>For know me better , <b>I am</b> :</p>
    <p><b>Idea</b> and <b>Name</b> from <b><a href="https://github.com/Annahita2004">Miss.Annahita</a></b> !</p>
    <p>Developed with &hearts; by <b><a href="https://github.com/BlackIQ">Amir</a></b> .<p>
  </body>
</html>


[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FBlackIQ%2FAshley.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FBlackIQ%2FAshley?ref=badge_large)