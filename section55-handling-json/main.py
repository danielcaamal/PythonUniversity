DASH = 100

from urllib.request import urlopen, Request
import json

def title(text):
    return print(f' {text} '.center(DASH,'-'))

def subtitle(text):
    print()
    return print(f' {text} '.center(DASH,' '))

def block(text):
    return print(f'\n - {text}')


def run():
    title('1. Handling JSON (Javascript Object Notation)')

    url = Request('http://globalmentoring.com.mx/api/personas.json')
    url.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
    response = urlopen(url)
    
    body_response = response.read()

    print(f'Response: {body_response}')

    json_response = json.loads(body_response.decode('utf-8'))

    print(json_response)

    # Printing all names

    print('Names:')
    for person in json_response.get('personas', []):
        print('\t',person.get('nombre', ''))

    title('2. Example - Weather Consulting')
    url = Request('http://globalmentoring.com.mx/api/clima.json')
    url.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
    response = urlopen(url)
    
    body_response = response.read()

    print(f'Response: {body_response}')
    
    json_response = json.loads(body_response.decode('utf-8'))




if __name__ == '__main__':
    run()