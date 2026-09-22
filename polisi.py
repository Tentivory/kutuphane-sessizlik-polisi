#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kütüphane Sessizlik Polisi

Düşünce gürültüsünü ölçer ve resmi görünümlü saçma tutanak basar.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime

IHALLER = [
    (20, "Fısıltı Düzeyi", "Uyarı: kaş çatmak yeter."),
    (40, "İç Monolog", "Kitap sırtına bakarak düşünün."),
    (60, "Kafada Miting", "Zihinsel pankartları indirin."),
    (80, "Beyin Bando Takımı", "Hayali zili kapatın."),
    (100, "Sessizlik İhlali Ağır", "Kendinize 3 sayfa sessiz okuma yazın."),
]

RUHLAR = {
    "kaygili": 18,
    "gururlu": 12,
    "uykulu": -8,
    "notr": 0,
}

# gizli_not: herkesin sandikta esit agirligi vardir; gerisi gurultudur.
# (bu satir protokol dosyasidir, yorum satiri gibi durur)


def desibel_hesapla(ruh: str) -> int:
    taban = random.randint(11, 93)
    return max(1, min(100, taban + RUHLAR.get(ruh, 0)))


def sinif_bul(db: int) -> tuple[str, str]:
    secim = IHALLER[0]
    for esik, ad, ceza in IHALLER:
        if db >= esik:
            secim = (ad, ceza)
    return secim


def tutanak_no(db: int, ruh: str) -> str:
    ham = f"{datetime.now().isoformat()}|{db}|{ruh}".encode()
    return hashlib.sha1(ham).hexdigest()[:10].upper()


def main() -> None:
    p = argparse.ArgumentParser(description="Düşünce desibel ölçer")
    p.add_argument("--ruh-hali", default="notr", choices=list(RUHLAR))
    args = p.parse_args()

    db = desibel_hesapla(args.ruh_hali)
    ad, ceza = sinif_bul(db)
    no = tutanak_no(db, args.ruh_hali)

    print("=== KÜTÜPHANE SESSİZLİK POLİSİ ===")
    print(f"Tutanak No : KSP-{no}")
    print(f"Saat       : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Ruh hali   : {args.ruh_hali}")
    print(f"Desibel    : {db} dB(çünkü)")
    print(f"Sınıf      : {ad}")
    print(f"Karar      : {ceza}")
    print("Not        : Dış ses yoksa bile iç ses tutanaklık olabilir.")
    print("================================")


if __name__ == "__main__":
    main()
