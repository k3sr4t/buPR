#!/bin/bash

BASEDIR=$(dirname $0)

# Betiği /bin dizinine taşı
mkdir -p /bin/buPR
mv $BASEDIR/protect.sh /bin/buPR
mv $BASEDIR/sudobruteprotection.py /bin/buPR
# Dosyanın sahipliğini ve izinlerini ayarla
chown root:root /bin/protect.sh
chmod u+s /bin/protect.sh
chmod 755 /bin/buPR/sudobruteprotection.py

echo "Kurulum tatamlandı fakat crontab atanması gerekiyor"
echo "Beni silebilirsin"