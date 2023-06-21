import socket

def get_ip_address(url):
    try:
        # Ottiene l'indirizzo IP corrispondente all'URL

        ip_address = socket.gethostbyname(url)
        print (url)
        print(f"L'indirizzo IP per {url} è: {ip_address}")
    except socket.error as e:
        print(f"Impossibile ottenere l'indirizzo IP per {url}: {str(e)}")

# URL di esempio
#url = "www.google.com"
url = "www.libero.it"


# Ottiene l'indirizzo IP dell'URL specificato
get_ip_address(url)

