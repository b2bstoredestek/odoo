# B2BStore Odoo 8.0 Connector

Bu modül, **B2BStore** e-ticaret platformu ile **Odoo 8.0** ERP sistemi arasında çift yönlü veri senkronizasyonu sağlar.

### Ana Özellikler
* **Otomatik Aktarım:** B2BStore üzerindeki siparişleri Odoo'ya otomatik yansıtır.
* **Statü Eşitleme:** * Odoo Onay (Sale) -> B2B Onaylandı (2)
    * Odoo İptal (Cancel) -> B2B İptal (8)
    * Odoo Sevk/Bitti (Sent/Done) -> B2B Teslim Edildi (5)
* **Hata Yönetimi:** Unicode ve bağlantı hataları için gelişmiş loglama altyapısı.

### Kurulum
1. `b2b_module2` klasörünü Odoo `addons` dizinine kopyalayın.
2. Odoo panelinden 'Update Modules List' yapın.
3. Modülü kurun ve Ayarlar menüsünden API bilgilerinizi girin.
