import googlemaps
import urllib.parse

# Set up a client using your service key
client = googlemaps.Client(key='mybrkey')

# Use the client to get the latitude and longitude of the city you want to display on the map
geocode_result = client.geocode('Lviv, Ukraine')
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']

# Create a URL to request the embedded map using your browser key
params = {
    'key': 'myservkey',
    'center': f'{lat},{lng}',
    'zoom': 12,
}
query_string = urllib.parse.urlencode(params)
url = f'https://www.google.com/maps/embed/v1/view?{query_string}'

# Generate the HTML code for the embedded map
html = f'''
<!DOCTYPE html>
<html>
  <head>
    <title>Embedded Google Map</title>
  </head>
  <body>
    <h1>Embedded Google Map</h1>
    <iframe
      width="600"
      height="450"
      frameborder="0" style="border:0"
      src="{url}" allowfullscreen>
    </iframe>
  </body>
</html>
'''

# Save the HTML code to a file
with open('embedded_map.html', 'w') as f:
    f.write(html)
