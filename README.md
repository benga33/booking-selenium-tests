# Booking.com Selenium Test Suite

Automatizirani testovi za [Booking.com](https://www.booking.com) korištenjem Selenium WebDriver-a i Pythona.

## Sadržaj

- [Pregled](#pregled)
- [Karakteristike](#karakteristike)
- [Preduslovi](#preduslovi)
- [Instalacija](#instalacija)
- [Konfiguracija](#konfiguracija)
- [Pokretanje testova](#pokretanje-testova)
- [Struktura projekta](#struktura-projekta)
- [Test slučajevi](#test-slučajevi)

## Pregled

Ovaj projekat sadrži automatizirane UI testove za Booking.com, pokrivajući ključne korisničke tokove kao što su:
- Pretraga smještaja
- Filtriranje rezultata
- Odabir hotela
- Validacija detalja rezervacije

Testovi su napisani korištenjem **Selenium WebDriver**-a sa **Python**-om i prate **Page Object Model (POM)** dizajn pattern za bolju održivost.

## Karakteristike

- ✅ Podrška za više browsera (Chrome, Firefox)
- ✅ Page Object Model implementacija
- ✅ Podesivi test podaci
- ✅ Snimak ekrana pri neuspješnom testu
- ✅ Allure integracija za izvještaje
- ✅ Paralelno izvršavanje testova

## Preduslovi

Prije pokretanja testova, provjerite da li imate instalirano sljedeće:

- Python 3.8 ili noviji
- pip (Python package manager)
- Web browseri:
  - Google Chrome (najnovija verzija)
  - Mozilla Firefox (najnovija verzija) - opcionalno
- ChromeDriver / GeckoDriver (automatski se upravlja preko webdriver-manager)

## Instalacija

1. **Klonirajte repozitorij:**
   ```bash
   git clone https://github.com/benga33/booking-selenium-tests.git
   cd booking-selenium-tests
