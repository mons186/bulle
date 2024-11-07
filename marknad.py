import yfinance as yf
from pygame import mixer
from datetime import datetime, timedelta

# Bertils dom har inte tickers till fonder så tog en etf som följer index så det borde vara desamma. bara att ändra SPGM till någon annan ticker om du tycker de passar mer.
ticker = "SPGM"  # S&P Global 1200 ETF

# Starta ljudmixern för att kunna spela upp ljud
mixer.init()

# Hämta dagens och gårdagens data för att se om Bertil kan få sin kanelbulle eller om han får hålla sig
index = yf.Ticker(ticker)
today = datetime.now().date()
yesterday = today - timedelta(days=1)

# Hämta slutkurs för igår och idag
data_today = index.history(start=today, end=today + timedelta(days=1))
data_yesterday = index.history(start=yesterday, end=today)

# Kontrollera att vi fått data
if not data_today.empty and not data_yesterday.empty:
    close_today = data_today["Close"][0]
    close_yesterday = data_yesterday["Close"][0]
    
    # Här kommer det avgörande ögonblicket för Bertil och hans kanelbullar
    if close_today > close_yesterday:
        print("Grattis Bertil! Börsen har gått upp idag, så du har tjänat ihop en extra stor kanelbulle!")
        mixer.music.load("kanelbulle_positiv.mp3")  # Fil för positiv kanelbulle-stämning
    else:
        print("Ajdå Bertil... Börsen gick ner. Ingen kanelbulle idag, men håll ut till imorgon!")
        mixer.music.load("kanelbulle_negativ.mp3")  # Fil för nedstämd kanelbulle-stämning
    
    # Spela ljudet och vänta tills det är klart
    mixer.music.play()
    while mixer.music.get_busy():  # Vänta tills ljudet är klart
        pass
else:
    print("Hoppsan Bertil, det verkar som att vi inte fick några data. Kanelbullen får vänta på bättre börsdagsinfo.")
