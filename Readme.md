# INSTRUCTIONS
First of all, you have to launch "PokeemeraldTranslator.exe", 
actually there is no ".exe" so, you'll just have to launch the .py script (and import the packages w/ pip if necessary)
Choose a language then, you just have to wait until the traduction finish. A root will appear and ask you select a folder, in this folder will be saved five files :
- `species_names.h`
- `pokedex_text.h`
- `item.h`
- `readme.md` (this file)
- `more_than_10.txt` 

You have to delete the old files in the pokeemerald directory and replace them by these (translated files). Here is the paths of the originals files :



- pokedex_text.h 
path :



 `src/data/pokemon/pokedex_text.h `

- species_names.h 
path:

 src/data/text/species_names.h` 


- item.h
path:

 `src/data/items.h`



Next step, open `more_than_10.txt`, you have all the names of items and Pokémon that exceeds the maximum number of characters allowed, you have to replace these by a shorter name (ex: Crabominable > Crabminabl ). The items shouldn't exceeds 13 characters and the Pokémon names shouldn't exceeds 10 characters.

# Credits

Pokecreator and myself for the script and veekun for the csv lib (available at : https://github.com/veekun/pokedex/tree/master/pokedex/data/csv)

#Useful Links

Pokémon Résurrection's discord server to get help or to contribute : https://discord.gg/jemEuB3pMJ
Pokémon Résurrection's website : https://pokemon.version-resurrection.repl.co/index.html
