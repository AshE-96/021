import json
from shapely.geometry import Point, Polygon
import click
import time
import os

class TehranDistrictFinder:
    def __init__(self):
        self.district_polygons = {}
        self.load_all_districts()

    def load_all_districts(self):
        """Load district boundaries from JSON files."""
        click.echo("Loading District Data...")
        loading_message = "Loading District Data"
        for district in range(1, 23):
            try:                
                with open(f'district_{district}_boundary.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    coordinates = self.extract_coordinates(data)
                    if coordinates:
                        polygon = self.create_polygon(coordinates)
                        self.district_polygons[district] = polygon
                        click.echo(f"\r{loading_message}: ✅ District {district} Loaded", nl=False)
                    else:
                        click.echo(click.style(f"\r{loading_message}: ⚠️ District {district} - No Coordinates Found", fg='yellow'), nl=False)
                loading_animation_inline()
            except FileNotFoundError:
                click.echo(click.style(f"\r{loading_message}: ⚠️ District {district} - Data File Not Found", fg='yellow'), nl=False)
                loading_animation_inline()
        click.echo(click.style(f"\r{loading_message}: ✅ Completed.                                  ", fg='green'))

    def extract_coordinates(self, data):
        """Extract coordinates from JSON data."""
        nodes = {}
        ways = []
        relation = None

        for element in data['elements']:
            if element['type'] == 'node':
                nodes[element['id']] = (element['lat'], element['lon'])
            elif element['type'] == 'way':
                ways.append(element)
            elif element['type'] == 'relation':
                relation = element

        if not relation:
            return None

        coordinates = []
        for member in relation['members']:
            if member['type'] == 'way':
                way_id = member['ref']
                for way in ways:
                    if way['id'] == way_id:
                        way_coords = [nodes[node_id] for node_id in way['nodes'] if node_id in nodes]
                        coordinates.extend(way_coords)

        return coordinates

    def create_polygon(self, coordinates):
        """Create a Shapely Polygon from coordinates, ensuring validity."""
        unique_coords = []
        for coord in coordinates:
            if not unique_coords or coord != unique_coords[-1]:
                unique_coords.append(coord)

        if unique_coords[0] != unique_coords[-1]:
            unique_coords.append(unique_coords[0])

        return Polygon(unique_coords)

    def find_district(self, lat, lon):
        """Find the Tehran district."""
        point = Point(lat, lon)

        for district, polygon in self.district_polygons.items():
            if polygon.contains(point):
                return district

        min_distance = float('inf')
        nearest_district = None

        for district, polygon in self.district_polygons.items():
            distance = polygon.exterior.distance(point)
            if distance < min_distance:
                min_distance = distance
                nearest_district = district

        if nearest_district:
            return f"Point is outside district boundaries. Nearest District: {nearest_district}"

        return "Point is outside Tehran city limits."

def loading_animation_inline():
    """Simple inline loading animation."""
    chars = ['.', '..', '...']
    for char in chars:
        click.echo(f"{char}", nl=False)
        time.sleep(0.1)
        click.echo(f"\r", nl=False)


def display_instructions():
    """Displays application instructions in a structured format."""
    click.echo(click.style("\nApplication Instructions:", fg='yellow', bold=True))
    click.echo(click.style("-" * 30, fg='cyan'))
    click.echo(click.style("1. Select '2' from the Main Menu to find district by coordinates.", fg='cyan'))
    click.echo(click.style("2. Provide Latitude and Longitude when prompted.", fg='cyan'))    
    click.echo(click.style("3. The application will determine and display the Tehran District.", fg='cyan'))
    click.echo(click.style("4. To exit, type 'exit' at any input prompt or select '3' from the Main Menu.", fg='cyan'))
    click.echo(click.style("-" * 30, fg='cyan'))
    click.echo("\n")


@click.command()
def main():
    """Tehran Municipality District Finder - m2gh"""
    click.clear()
    click.echo(click.style("Tehran District Finder - m2gh", fg='magenta', bold=True))
    click.echo(click.style("=" * 40, fg='cyan'))

    loading_animation_inline()
    finder = TehranDistrictFinder()
    click.echo("\n" + "=" * 40)   
    while True:
        click.echo(click.style("\n--- Main Menu ---", fg='yellow', bold=True))
        click.echo(click.style("-" * 30, fg='cyan'))
        click.echo(click.style("  1 - Show Instructions", fg='cyan'))
        click.echo(click.style("  2 - Enter Coordinates", fg='cyan'))
        click.echo(click.style("  3 - Exit Application", fg='cyan'))
        click.echo(click.style("-" * 30, fg='cyan'))

        option = click.prompt(click.style("Choose option [1-3]", fg='yellow'), type=str) # Updated option range

        if option == '1':
            display_instructions()

        elif option == '2':
            click.echo(click.style("\n--- Enter Coordinates ---", fg='cyan', bold=True))
            try:
                lat_input = click.prompt(click.style("  Latitude:", fg='yellow'), type=str)
                if lat_input.lower() == 'exit':
                    click.echo(click.style("Exiting...", fg='cyan'))
                    break

                lon_input = click.prompt(click.style("  Longitude:", fg='yellow'), type=str)
                if lon_input.lower() == 'exit':
                    click.echo(click.style("Exiting...", fg='cyan'))
                    break

                lat = float(lat_input)
                lon = float(lon_input)

                if not (35.5 <= lat <= 35.9 and 51.2 <= lon <= 51.6):
                    click.echo(click.style("⚠️ Warning: Coordinates outside Tehran range.", fg='red'))

                result = finder.find_district(lat, lon)

                click.echo(click.style("\n--- District Finding Result ---", fg='green', bold=True))
                if isinstance(result, int):
                    click.echo(click.style(f"  Municipality District: {result}")) # Default color for result
                else:
                    click.echo(click.style(f"  {result}")) # Default color for result
                click.echo(click.style("--- End of Result ---", fg='green'))

            except ValueError:
                click.echo(click.style("\n❌ Error: Invalid coordinate input.", fg='red'))
            except Exception as e:
                click.echo(click.style(f"\n❌ Unexpected Error: {str(e)}", fg='red'))

        elif option == '3':
            click.echo(click.style("Exiting Application...", fg='cyan'))
            break

        else:
            click.echo(click.style("❌ Invalid option. Please select 1-3.", fg='red')) # Updated option range in error message
        click.echo(click.style("=" * 40, fg='cyan'))


    click.echo(click.style("=" * 40, fg='cyan'))
    click.echo(click.style("Thank you for using Tehran District Finder!", fg='green', bold=True))
    click.echo(click.style("=" * 40, fg='cyan'))


if __name__ == "__main__":
    main()
