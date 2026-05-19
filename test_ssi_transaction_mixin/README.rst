.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============================
Test Module: Transaction Mixin
==============================

Description
===========

Test Module: Transaction Mixin adalah modul pengujian untuk memvalidasi perilaku
mixin transaksi pada ekosistem SSI. Modul ini memanfaatkan berbagai mixin
workflow transaksi (confirm, open, done, cancel, terminate) untuk memastikan
hook decorator, approval, dan alur status berjalan sesuai ekspektasi.

Key Features
============

* Pengujian alur state transaksi dari draft sampai terminate.
* Pengujian hook decorator pre/post pada action dan check.
* Integrasi dengan approval policy dan template sequence.
* Contoh transaksi dengan detail line dan perhitungan harga produk.

Use Cases / Context
===================

* Dipakai sebagai modul referensi saat mengembangkan mixin transaksi baru.
* Membantu regression test untuk perubahan pada modul `ssi_transaction_*_mixin`.
* Menjadi contoh implementasi inheritance terhadap model transaksi mixin.

Installation
============

1. Clone branch 15.0 dari repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Tambahkan path repository ini ke konfigurasi Odoo Anda (`addons-path`).
3. Update daftar modul dalam mode developer.
4. Buka menu *Apps -> Apps -> Main Apps*.
5. Cari modul *Test Module: Transaction Mixin*.
6. Install modul.

Installation & Usage
====================

1. Pastikan dependency modul mixin transaksi SSI sudah tersedia.
2. Install modul `test_ssi_transaction_mixin` dari Apps.
3. Buat data transaksi uji dan jalankan action confirm/open/done/cancel untuk
   memverifikasi hook pre/post.
4. Gunakan form view untuk melihat hasil field penanda check/action yang
   terisi otomatis oleh decorator.

FAQ
===

* **Apakah modul ini untuk produksi?**
  Tidak, modul ini ditujukan untuk pengujian dan validasi perilaku mixin.
* **Versi Odoo berapa yang didukung?**
  Modul ini ditargetkan untuk Odoo 15.0.
* **Bagaimana berkontribusi?**
  Buat fork, lakukan perubahan di branch terpisah, lalu kirim pull request ke
  repository GitHub.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of trouble,
please check there if your issue has already been reported. If you spotted it
first, help us improve by providing detailed feedback.

Credits
=======

Contributors
------------

* Michael Viriyananda <viriyananda.michael@gmail.com>
* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
==========

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://github.com/simetri-sinergi-id

This module is maintained by PT. Simetri Sinergi Indonesia.
