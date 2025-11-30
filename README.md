# Saucedemo Selenium Automatizované testy

Tento repozitár obsahuje automatizované UI testy pre webovú stránku 
 https://www.saucedemo.com 

Testy sú napísané v **Python** s použitím:

- Selenium WebDriver 
- Pytest 
- WebDriver Manager

## Installation 
pip install -r requirements.txt
## Run test
pytest -q

## Testované funkcie

### 1. Valid Login 
Zabezpečuje, aby sa používateľ so správnymi prihlasovacími údajmi mohol úspešne prihlásiť.

### 2. Invalid Login   
Overuje, či systém správne zobrazuje chybové hlásenie v prípade nesprávnych prihlasovacích údajov.

### 3. Add Item to Cart 
Overuje možnosť pridať produkt do košíka a aktualizuje počítadlo košíka.

### 4. Complete Checkout Flow   
Pokrýva celý proces platby od výberu produktu až po potvrdenie objednávky.

