import unittest
from getData import GetData


class TestPokemon(unittest.TestCase):

    def test_search_valid_pokemon(self):
        my_data = GetData()
        pokemon = my_data.get('kakuna')
        my_pokemon = pokemon.json()
        data = my_data.get_pokemon_data('kakuna')
        self.assertEqual(200, pokemon.status_code)
        self.assertEqual(data['weight'], my_pokemon['weight'])
        for i in my_pokemon['moves']:
            self.assertTrue(i['move']['name'] in data['moves'])

    def test_search_pokemon_by_number(self):
        my_data = GetData()
        pokemon = my_data.get('1')
        data = my_data.get_pokemon_data('bulbasaur')
        my_pokemon = pokemon.json()
        self.assertEqual(200, pokemon.status_code)
        self.assertEqual(my_pokemon['name'], data['name'])


if __name__ == '__main__':
    unittest.main()
