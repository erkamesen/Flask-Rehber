## Relationships

- Geniş ölçekli projelerde muhtemelen çoklu modelleriniz olacaktır.
- Bu modeller diğer modellerle ilişkilendirilebilirler.
- Örnek vermek gerekirse; Oluşturduğumuz bu Dog modeliyle Owner modelini birbirleriyle ilişkilendirebiliriz.
- İlişkilere geçmeden önce bilmemiz gereken temel konu "Primary Key" ve "Foreign Key" dir.

**Primary Key:**
- Benzersiz ID kolonu
**Foreign Key:**
- Diğer tablodaki "Primary Key"

**Dog**
- ID(Primary Key)
- NAME
- AGE
- BREED
  
**Owner**
- ID(Primary Key)
- NAME
- DOG ID(Foreign Key)