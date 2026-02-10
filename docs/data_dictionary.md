# Dictionnaire de données

## Tables principales

### orders
| Colonne | Type | Description |
|---------|------|-------------|
| order_id | INT | Identifiant unique |
| customer_id | INT | Référence client |
| order_date | DATE | Date de commande |
| amount | DECIMAL | Montant total |

### customers
| Colonne | Type | Description |
|---------|------|-------------|
| customer_id | INT | Identifiant unique |
| name | VARCHAR | Nom du client |
| segment | VARCHAR | Segment commercial |
