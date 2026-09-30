#!/usr/bin/env python3
"""Soi trang bao cao LUC CHAY, phan ma check_voice.py va check_sidecar.py mu.

VI SAO CAN. Hai may do kia soi DOM da dung, nen chung khong phan biet duoc
"trang dung xong" voi "trang dung nua duong roi nem ngoai le". Do that trong
phien 08/09/2026: mot mang dat canh sidecar bi lech do dai -> TypeError o giua
doan ma -> ba khoi cuoi rong va CA 27 the .reveal khong bao gio duoc bo
opacity:0, tuc la nguoi doc mo ra thay trang gan nhu trang. Ca hai may do van
bao "0 loi chan", va ban in van dung vi @media print co opacity:1!important.

Bat ba thu, xep theo do tin cay da do duoc:

  1. O RONG — o dung san trong than trang ma khong khoi nao dien noi dung vao.
     Day la phep MANH NHAT: tren ban co tinh lam hong no bat 16 o, tren ban that
     no bat 0. Mot ngoai le giua doan ma luon de lai dau vet o day.
  2. NGOAI LE LUC CHAY — doc console cua Chrome. Bat truc tiep nguyen nhan.
  3. VUNG TRANG — do do trai mau tung dai ngang cua anh chup.
     PHEP NAY THO, va noi ro ra de khong ai tin no qua muc: no do ca NEN chu
     khong chi do CHU. Nen trang #F2F2F2 dat canh khoi dau trang mau xanh dam da
     du cho do trai ~230, nen mot trang mat het chu van co the qua phep nay.
     Giu lai vi no bat duoc truong hop trang trang hoan toan, nhung dung dung no
     mot minh — hai phep tren moi la phep ket luan.

Khong dung ten lop CSS lam thuoc do. Da thu va bo: the .reveal co class "in" hay
khong phu thuoc vao bo theo doi cuon, ma bo do khong kich hoat on dinh trong moi
truong dung trang — cung mot file cho 0/27 va 8/27 giua hai lan chay lien tiep.
Ten lop van in ra nhung chi de tham khao.

Dung:
    python check_runtime.py <file.html>

Ma tra ve: 0 sach · 1 co loi chan · 2 sai cach dung hoac khong dung duoc trang
"""

import os
import re
import sys
import subprocess
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

CHO_TIM = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]


def tim_trinh_duyet():
    for p in CHO_TIM:
        if os.path.isfile(p):
            return p
    from shutil import which
    for t in ["chrome", "chromium", "google-chrome", "msedge"]:
        p = which(t)
        if p:
            return p
    return None


def file_url(path):
    return "file:///" + os.path.abspath(path).replace("\\", "/")


def dung(path):
    """Tra ve (dom, log_console) hoac (None, ly_do)."""
    tr = tim_trinh_duyet()
    if not tr:
        return None, "khong tim thay Chrome hay Edge"
    prof = tempfile.mkdtemp(prefix="ths-rt-")
    cmd = [tr, "--headless", "--disable-gpu", "--no-sandbox",
           "--user-data-dir=" + prof, "--window-size=1500,1100",
           "--virtual-time-budget=9000", "--enable-logging=stderr", "--v=0",
           "--dump-dom", file_url(path)]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=120)
    except Exception as e:
        return None, "chay trinh duyet loi: %s" % e
    dom = r.stdout.decode("utf-8", "replace")
    log = r.stderr.decode("utf-8", "replace")
    if len(dom) < 500:
        return None, "DOM tra ve qua ngan (%d byte)" % len(dom)
    return dom, log


def chup(path):
    """Chup trang roi do do trai mau tung dai ngang.

    Tra ve (True, [(ten_dai, do_trai, nguong)]) hoac (None, ly_do).
    Do trai mau gan 0 nghia la dai do mot mau tron — tuc la khong co chu.
    """
    try:
        from PIL import Image
    except Exception:
        return None, "thieu Pillow, khong do duoc pixel"
    tr = tim_trinh_duyet()
    if not tr:
        return None, "khong tim thay trinh duyet"
    prof = tempfile.mkdtemp(prefix="ths-shot-")
    out = os.path.join(prof, "shot.png")
    cmd = [tr, "--headless", "--disable-gpu", "--no-sandbox",
           "--user-data-dir=" + prof, "--window-size=1500,3000",
           "--virtual-time-budget=9000", "--screenshot=" + out, file_url(path)]
    try:
        subprocess.run(cmd, capture_output=True, timeout=120)
    except Exception as e:
        return None, "chup loi: %s" % e
    if not os.path.isfile(out):
        return None, "khong sinh duoc anh"
    im = Image.open(out).convert("L")
    w, h = im.size
    # Nguong 120: mot dai co chu cho do trai 200+ (chu trang tren nen xanh dam,
    # hoac chu den tren the trang). Mot dai TRANG cho gan 0. Da do tren ban
    # that (235 va 239) va tren mot ban co tinh lam hong (xem cuoi file).
    DAI = [("dau trang", 90, 700, 120), ("giua trang", 900, 1800, 120)]
    kq = []
    for ten, y0, y1, nguong in DAI:
        y1 = min(y1, h)
        if y0 >= y1:
            continue
        px = list(im.crop((0, y0, w, y1)).getdata())
        kq.append((ten, (max(px) - min(px)) if px else 0, nguong))
    return True, kq


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        sys.stdout.write(__doc__ + "\n")
        return 2
    path = args[0]
    if not os.path.isfile(path):
        print("KHONG DOC DUOC: %s" % path)
        return 2

    dom, log = dung(path)
    if dom is None:
        print("KHONG DUNG DUOC TRANG: %s" % log)
        return 2

    chan = []

    # 1 · ngoai le luc chay
    for m in re.finditer(r'"(Uncaught [^"]{0,300})"', log):
        chan.append(("NGOAI_LE_LUC_CHAY", m.group(1)))
    for m in re.finditer(r"(Uncaught (?:TypeError|ReferenceError|SyntaxError|RangeError)[^\n\"]{0,200})", log):
        cau = m.group(1).strip()
        if not any(cau in c[1] for c in chan):
            chan.append(("NGOAI_LE_LUC_CHAY", cau))

    # 2 · trang co THAT SU hien chu khong — do bang pixel, khong do bang ten lop.
    #     Do ten lop la sai cau hoi: the co the du class ma van opacity 0, va bo
    #     theo doi cuon thi khong kich hoat on dinh trong moi truong dung trang.
    #     Cau hoi dung la: nguoi mo file ra co thay chu khong.
    tong = len(re.findall(r'class="[^"]*\breveal\b', dom))
    hien = len(re.findall(r'class="[^"]*\breveal\b[^"]*\bin\b', dom))
    anh, vi = chup(path)
    if anh is None:
        chan.append(("KHONG_CHUP_DUOC", vi))
    else:
        for ten, do_trai, nguong in vi:
            if do_trai < nguong:
                chan.append(("VUNG_TRANG",
                             "vung %s gan nhu khong co chu: do trai mau %d, duoi nguong %d"
                             % (ten, do_trai, nguong)))

    # 3 · o dung san ma khong ai dien
    for m in re.finditer(r'<div[^>]*\bid="([A-Za-z][\w-]*)"[^>]*>\s*</div>', dom):
        chan.append(("O_RONG", 'o id="%s" khong co noi dung nao duoc dien vao' % m.group(1)))
    for m in re.finditer(r'<table[^>]*\bid="([A-Za-z][\w-]*)"[^>]*>\s*</table>', dom):
        chan.append(("O_RONG", 'bang id="%s" khong co noi dung nao duoc dien vao' % m.group(1)))

    print("=" * 72)
    print("LUC CHAY · %s" % path)
    print("  DOM %d byte · the .reveal co class in: %d/%d (chi de tham khao)"
          % (len(dom), hien, tong))
    if anh:
        for ten, do_trai, nguong in vi:
            print("  do trai mau vung %s: %d (nguong %d)" % (ten, do_trai, nguong))
    print("=" * 72)
    if chan:
        print("  CHAN (%d)" % len(chan))
        for ma, td in chan:
            print("    [%s] %s" % (ma, td))
    else:
        print("  Khong co loi nao.")
    print("-" * 72)
    print("Tong: %d chan" % len(chan))
    print("Ket luan: %s" % ("KHONG GIAO — con loi chan" if chan else "Luc chay dat"))
    return 1 if chan else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
