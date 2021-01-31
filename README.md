[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FBlackIQ%2FAshley.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FBlackIQ%2FAshley?ref=badge_shield)

<p>
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/BlackIQ/Ashley">
<img src="https://img.shields.io/github/license/BlackIQ/Ashley?style=flat-square" alt="License"/>
<img src="https://img.shields.io/github/languages/code-size/BlackIQ/Ashley?style=flat-square" alt="Code Size"/>
<img src="https://img.shields.io/badge/Requirements-See%20Here-orange" alt="Requirements">
</p>

# Hey there ! It's me , Ashley :)
##### Version 0.1.7
##### Last Update : Jan , 18 , 2021

Anyway , I can save your passwords in database and help you to never forgot them .

<hr>

Before run , there are some steps :

- 1<sup>st</sup> , you need to install **Python** and **Pip** on your device .
- 2<sup>nd</sup> , it's required to have voice tools , **espeak** , **ffmpeg** and **mpg123** too .
- 3<sup>rd</sup> , Python libraries .
- 4<sup>th</sup> , **Config MySQL** if yo didn't do that yet .
- 5<sup>th</sup> , important linux packages **git** and **MySQL** .

<hr>

Install , Clone , Run 

- install linux packages and python things .

```
sudo pacman -S python-pip mpg123 espeak ffmpeg python
sudp pacman -S mariadb-server maridb-client
```

> Use your own linux package manager

- Config MySQL

```
sudo mysql
> CREATE USER 'Ashley'@'localhost' IDENTIFIED BY 'Ashley';
> GRANT ALL PRIVILEGES ON *.* TO 'Ashley'@'localhost';
> FLUSH PRIVILEGES;
> exit
sudo systemctl restart mysql.service
```

> Make a costume user . This is an example .

- Now you need to clone Ashley and install libs

```
git clone https://github.com/BlackIQ/Ashley && cd Ashley
pip3 install -r requirements.txt
```

> You can make a Virtual Environment too . 

- Run Ashley

```
python3 Ashley
```

> Done !

<hr>

Name and Idea by <a href="https://github.com/Annahita2004">Miss.Annahita</a> 💖

Developed by Me ✨ , With love ❤️
