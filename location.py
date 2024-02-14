import phonenumbers
from phonenumbers import geocoder, carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

# Obtain a free API key from https://opencagedata.com/
key = "e262d8a9fc864d4c85f5e7639c58c227"

# Input phone number with country code
number = input("Enter phone number:")

# Parse the phone number using phonenumbers library
parsed_number = phonenumbers.parse(number)

# Get the country code and description
country_code = phonenumbers.region_code_for_number(parsed_number)
country_name = geocoder.description_for_number(parsed_number, "en")

# Get the service provider name
service_provider = carrier.name_for_number(parsed_number, "en")

# Use OpenCageGeocode to get more precise coordinates
geocoder = OpenCageGeocode(key)
results = geocoder.geocode(country_name)

# Extract latitude and longitude
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']

# Display results
print("Country Code:", country_code)
print("Country Name:", country_name)
print("Service Provider:", service_provider)
print("Latitude:", latitude)
print("Longitude:", longitude)

# Visualize location on a map
map = folium.Map(location=[latitude, longitude], zoom_start=9)
folium.Marker([latitude, longitude], popup=country_name).add_to(map)
map.save("location.html")

print("Location details and map saved in location.html")

