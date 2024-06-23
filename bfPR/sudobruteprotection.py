# Pardus yarışması için hazırlanmıştır
# by k3sr4t
# sudo bruteforcing protection script
# * * * * * /bin/bfPR/sudobruteprotection.py >/dev/null 2>&1
import subprocess
def read_last_lines(filename, num_lines):
    global situation
    global count
    situation = 1 #sistem normal
    count = 0
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()[-num_lines:]
            for line in lines:
                if "authentication failure" in line:
                    count += 1
    except FileNotFoundError:
        print("KRİTİK HATA: /var/log/auth.log dosyası bulunamadı. Sisteminiz tehlikede olabilir")

def whatissit():
    global situation
    global count
    if count >= 24:
        situation = 0 #brute forcing denemesi
    else:
        situation = 1 #sistem normal

def protect():
    if situation == 0:
        script_path = protect.sh
        try:
        # .sh dosyasını çalıştır
            subprocess.run(['sh', script_path])
        except FileNotFoundError:
            print("KRİTİK HATA: /protect.sh bulunamadı. otomatik koruma işlemi başarısız oldu. Lütfen manuel bir şekilde virüs ile mücadele ediniz")




    



# Kullanım yeri
read_last_lines('/var/log/auth.log', 25)
situation
count
whatissit()
protect()
