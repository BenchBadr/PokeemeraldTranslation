import csv
import os
import sys
import re
import time
from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.filedialog as tf
import pathlib
#---------------------------------------
def traduction(langue):
  start_time = time.time()
  ws.update_idletasks()
  txt2['text'] ="(1/4) Pokédex descriptions..."
  with open("folder\more_than_10.txt",'w',encoding="utf-8") as filcl:
    pass
  with open("folder\original_pdex_t.txt",encoding="utf-8") as f:
    contenu=f.read()
    result = re.findall("const u8 g(.*)PokedexText",contenu)
    liste_noms = result
    del(liste_noms[0])
    print("Veuillez choisir une langue:\n_______\n1. Français\n2. Allemand\n3. Espagnol\n4. Italien\n5. Coréen\n6. Japonais\n7. Anglais\n_______")
    l = langue
    ld = {"1":"5","7":"9","6":"1","5":"3","2":"6","4":"8","3":"7"}
    lc = ld[l]
    print("_"*7+"\nTraduction des descriptions du Pokédex :")
  with open('folder\pokedex_text.h','w',encoding="utf-8") as f:
    with open('folder\pokemon_species_flavor_text.csv', newline='',encoding="utf-8") as csvfile:
      reader = csv.DictReader(csvfile)
      a=0
      f.write('''const u8 gDummyPokedexText[] = _(`\n    "Erreur 404 !\\n"\n    "Pokémon introuvable");\n''')
      for ligne in reader:
        ap = round(100*a/898,1)
        sys.stdout.write(f"\r{ap}%")
        sys.stdout.flush()
        ws.update_idletasks()
        txt['text'] = (f"{round(ap)}%  ")
        pb['value'] = ap
        #intervalles
        if int(ligne['species_id']) <= 721:
          vid="23"
        if int(ligne['species_id']) > 721 and int(ligne['species_id'])< 808:
          vid="30"
        if int(ligne['species_id']) > 807:
          vid="33"
        if ligne['language_id'] == lc and ligne['version_id'] == vid:
          a=a+1
          descri = ligne['flavor_text']
          dex = int(ligne['species_id'])
          poke = liste_noms[dex-1]
          descri = descri.replace("\n"," ")
          descliste = []
          n = 42
          chunks = [descri[i:i+n] for i in range(0, len(descri), n)]
          descri = chunks
          for i in range(len(descri)):
            try:
              if descri[i+1][0]!=" " and descri[i][-1] !=" ":
               descri[i] = descri[i]+"-"
            except:
              pass
            descliste.append(descri[i])
          for i in range(len(descri)):
            descri[i] = '''    "'''+str((descri[i]))+'''\\n"\n'''
            if i == len(descri)-1:
             descri[i]=descri[i][:-4]+'''"'''+");"
          poke=poke.split("-")
          for i in range(len(poke)):
              poke[i]=poke[i].capitalize()
          forcode = f"const u8 g{''.join(poke)}PokedexText[] = _(\n{''.join(descri)}\n\n"
          f.write(forcode.replace("’","'").replace("<",'''("''').replace(">",'''")''').replace("°C","deg.C").replace("°","").replace("»","").replace("«","").replace("’","'").replace(" "," ").replace("Nidoranf","NidoranF").replace("Nidoranm","NidoranM").replace("Mrmime","MrMime").replace("Hooh","HoOh").replace("Mimejr","MimeJr").replace("Porygonz","PorygonZ").replace("Typenull","TypeNull").replace("Tapukoko","TapuKoko").replace("Tapulele","TapuLele").replace("Tapubulu","TapuBulu").replace("Tapufini","TapuFini").replace("Mrrime","MrRime"))
  end_time = time.time()
  time_lapsed = round(end_time - start_time,1)
  print("\n"+"_"*7)
  print(f"\nOpération Réussie, temps écoulé : {time_lapsed}s")
  #-------------------------------------------------------
  start_time = time.time()
  with open('move_names.h', 'w',encoding="utf-8") as f:
    pass
  ws.update_idletasks()
  txt2['text'] ="(2/4) Pokédex names..."
  print("_"*7+"\nTraduction des noms :")
  with open('folder\sn.txt','r',encoding="utf-8") as firstfile, open('folder\species_names.h','a',encoding="utf-8") as secondfile:
      for line in firstfile:
        secondfile.write(line)
  with open("folder\sn.txt",encoding="utf-8") as f:
    contenu=f.read()
  with open("folder\species_names.h","w",encoding="utf-8") as f:
    with open("folder\pokemon_species_names.csv",newline='',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        dico = {}
        for ligne in reader:
          #creation dico anglais-dex
          if ligne['local_language_id'] == lc:
            a = (ligne['name'])
            dexs = ligne["pokemon_species_id"]
          if ligne['local_language_id'] == "9":
            dico[ligne['name'].replace("â™€","♂").replace("â™€","♀")] = a
    contenu = contenu.replace('''("''',"<").replace('''")''',">").replace("'","’").replace("Flechinder","Fletchinder").replace("Crabminabl","Crabominable").replace("Blacephaln","Blacephalon").replace("Corvisquir","Corvisquire").replace("Corviknigh","Corviknight").replace("Barraskewd","Barraskewda").replace("Centiskorc","Centiskorch").replace("Polteageis","Polteageist").replace("Stonjourne","Stonjourner")
    result=re.findall("_<(.*)>,",contenu)
    del(result[0])
    for i in range(len(dico)):
      sys.stdout.write(f"\r{round(i*100/897,1)}%")
      sys.stdout.flush()
      ws.update_idletasks()
      txt['text'] =(f"{round(i*100/897)}%")
      pb["value"]=round(i*100/897)
      contenu = contenu.replace(result[i],dico[result[i]]).replace(">",'''")''').replace("<",'''("''')
      if len(dico[result[i]]) > 10:
        with open('folder\more_than_10.txt','a',encoding="utf-8") as f2:
         f2.write("- Poké : "+dico[result[i]]+f" +de 10 car ({len(dico[result[i]])}+'\n")
    contenu=contenu
    f.write(contenu)
  end_time = time.time()
  time_lapsed = round(end_time - start_time,1)
  print("\n\nVeuillez vérifier le fichier 'more_than_10.txt' pour voir s'il y a des noms excédant 10 caractères.\n"+"_"*7+f"\n\nOpération Réussie, temps écoulé : {time_lapsed}s")
  #-------------------------------------------------------
  print("-"*7+"\nTraduction des noms des objets :")
  start_time = time.time()
  ws.update_idletasks()
  txt2['text'] ="(3/4) Item names..."
  with open('folder\item_names.csv', newline='',encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    idico = {}
    ldico = {}
    lang = []
    for ligne in reader:
      if ligne['local_language_id'] == lc:
        idico[ligne['item_id']] = ligne['name']
        a = (ligne['name'])
      if ligne['local_language_id'] == "9":
        ldico[ligne['name']] = a
        lang.append(ligne['name'])
    ldico['????????'] = "????????"
    with open('folder\items_original.h',encoding="utf-8") as fi:
      contenu=fi.read()
      contenu = contenu.replace('''("''',"<").replace('''")''',">")
      result=re.findall("_<(.*)>,",contenu)
      for i in range(len(result)):
        sys.stdout.write(f"\r{round(i/759*100,1)}%")
        ws.update_idletasks()
        txt['text'] =(f"{round(i/759*100)}%")
        pb["value"]=round(i/759*100)
        sys.stdout.flush()
        im = ldico[result[i].replace("Feather"," Feather").replace("Capsle"," Capsule").replace("Yellw","Yellow ").replace("GreenAp","Green Ap").replace("WhiteAp","White Ap").replace("BlackAp","Black Ap").replace("Electrc","Electric ").replace("Fightng","Fighting ").replace("PsychicM","Psychic M").replace("iteX","ite X").replace("iteY","ite Y").replace("Poisinium Z","Poisonium Z").replace("U-N","Ultran").replace("DeepSea","Deep Sea ").replace("tIce","t Ice").replace("'","’").replace("Weaknss","Weakness ").replace("SafetyGoggles","Safety Goggles").replace("AdrenalineOrb","Adrenaline Orb").replace("TerainExtendr","Terrain Extender").replace("ProtectvePads","Protective Pads").replace("MCHN","Machine").replace("{POKEBLOCK}","Pokéblock").replace(" Ticket","Ticket").replace("S.S.Ticket","S.S. Ticket").replace("EonTicket","Eon Ticket").replace("Oak’s","Oak's").replace("PewtrCrnches","Pewter Crunchies").replace("RageCandyBar","Rage Candy Bar").replace("CasteliaCone","Casteliacone").replace("LumioseGlete","Lumiose Galette").replace("ShalourSable","Shalour Sable").replace("AbilityPatch","Ability Patch").replace("Exp.Candy","Exp. Candy").replace("DynamaxCandy","Dynamax Candy").replace("MaxMushrooms","Max Mushrooms").replace("GoldBottlCap","Gold Bottle Cap").replace("StrngeSouvnr","Strange Souvenir").replace("Fosslzed","Fossilized ").replace("Drke","Drake").replace("SurprseMulch","Surprise Mulch").replace("WishingPiece","Wishing Piece").replace("GalaricaTwig","Galarica Twig").replace("GalaricaCuff","Galarica Cuff").replace("GalrcaWreath","Galarica Wreath").replace("StrwbrySweet","Strawberry Sweet").replace("Rusted","Rusted ").replace("Heavy-DtyBts","Heavy-Duty Boots").replace("UtltyUmbrlla","Utility Umbrella").replace("BlundrPolicy","Blunder Policy").replace("CatchngCharm","Catching Charm").replace("RotomCatalog","Rotom Catalog").replace("ReinsOfUnity","Reins of Unity").replace("{PKMN} Box Link","Pokémon Box Link")]
        if len(im) > 13:
          with open('folder\more_than_10.txt','a',encoding="utf-8") as f2:
           f2.write(f"- Objet : {im} + 13 car ({len(im)}\n")
           print(f" | {im} fait plus de 13 char, retirer {len(im)-13}, nouveau :")
           im = input(">>> ")
           while len(im)>13:
            print(f"{len(im)} char, veuillez retirer {len(im)-13}")
            im = input(">>> ")
        contenu = contenu.replace('''<'''+result[i]+'''>''','''("'''+im+'''")''')
      contenu=contenu.replace("<",'''("''').replace(">",'''")''').replace('''")= GEN''',">= GEN").replace("_CS","_HM").replace("_CT","_TM").replace("description = sCT","description = sTM").replace("description = sCS","description = sHM").replace("’","'").replace("Poussière Étoile","Pouss. Étoile").replace("Morceau d'Étoile","Morc. Étoile").replace("CoquilleTréfonds","Coqu.Tréfonds").replace("Fossile Racine","FossileRacine").replace("Fossile Griffe","FossileGriffe").replace("Fossile Armure","FossileArmure").replace("Fossile Plaque","FossilePlaque").replace("Fossile Mâchoire","Foss.Mâchoire").replace("Fossile Nageoire","Foss.Nageoire").replace("Noigrume Rouge","NoigrumeRouge").replace("Noigrume Jaune","NoigrumeJaune").replace("Noigrume Blanc","NoigrumeBlanc").replace("Sachet Senteur","SachetSenteur").replace("Plaque Toxicité","PlaqueToxique").replace("Plaque Insecte","PlaqueInsecte").replace("Plaque Fantôme","PlaqueFantôme").replace("Joyau Électrik","JoyauÉlectrik").replace("Joyau Ténèbres","JoyauTénèbres").replace("Marshadozélite","Marshadzélite").replace("Ultranécrozélite","U-Nécrozélite").replace("Encens Bizarre","EncensBizarre").replace("Bracelet Macho","BraceletMacho").replace("Poignet Pouvoir","PoignePouvoir").replace("Ceinture Pouvoir","Ceint.Pouvoir").replace("Lentille Pouvoir","LentillePouv.").replace("Bandeau Pouvoir","Band. Pouvoir").replace("Chaîne Pouvoir","ChaînePouvoir").replace("Graîne Miracle","GraîneMiracle").replace("Glace Éternelle","GlacÉternelle").replace("Ceinture Noire","Ceint. Noire").replace("Cuillère Tordue","Cuill. Tordue").replace("Poudre Argentée","PoudrArgentée").replace("Lunettes Noires","Lun. Noires").replace("Lunettes Choix","Lun. Choix").replace("Mouchoir Choix","Mouch. Choix").replace("Graine Électrik","GraineÉlectrk").replace("Graine Psychique","Graine Psych.").replace("Lichen Lumineux","Lichen Lumin.").replace("Boule de Neige","BouleDeNeige").replace("Rune Purifiante","Rune Purif.").replace("Bandeau Muscle","BandeauMuscle").replace("Lunettes Sages","LunettesSages").replace("Ceinture Force","Ceint. Force").replace("Bande Étreinte","BandeÉtreinte").replace("Vulné-Assurance","Vulné-Assur.").replace("Veste de Combat","VesteDeCombat").replace("Lunettes Filtre","Lun. Filtre").replace("Vélo de Course","VéloDeCourse").replace("Boîte Pokéblocs","BoîtePokébloc").replace("Lettre à Pierre","Let. à Pierre").replace("Lunettes Sable","Lun. Sable").replace("Passe Concours","PasseConcours").replace("Carte Magnétique","Carte Magnét.").replace("Super Repousse","SuperRepousse").replace("Graine Miracle","GraineMiracle")
      with open("folder\item.h","w",encoding="utf-8") as finfile:
       finfile.write(contenu)
      end_time = time.time()
      time_lapsed = round(end_time - start_time,1)
      print("\n\nVeuillez vérifier le fichier 'more_than_10.txt' pour voir s'il y a des noms excédant 13 caractères.\n"+"_"*7+f"\n\nOpération Réussie, temps écoulé : {time_lapsed}s")
#-------------------------------------------------------------------------------------------------
  start_time = time.time()
  ws.update_idletasks()
  txt2['text'] ="(4/4) Moves names..."
  try:
      os.remove("folder\more_than_12.txt")
  except:
      pass
  try:
   os.remove("folder\move_names.h")
  except:
      pass

  with open("folder\moves.csv",newline='',encoding="utf-8") as csvfile:
      reader = csv.DictReader(csvfile)
      idtotr = {}
      srctoid = {}
      srctotr = {}
      for line in reader:
          if line['local_language_id'] == "5":
              idtotr[line['move_id']]=line['name']
          if line['local_language_id'] == "9":
              srctoid[line['name']] = line['move_id']
      for i in range(len(idtotr.keys())):
          try:
           srctotr[list(srctoid.keys())[i]] = idtotr[srctoid[list(srctoid.keys())[i]]]
          except:
              pass
  srctotr['-'] = '-'
  with open("folder\moves_names_o.h",'r',encoding='utf-8') as f:
      contenu=f.read()
      result=re.findall("_<(.*)>,",contenu)
      for i in range(len(result)):
      # try:
          if result[i] != '-':
           if len(srctotr[result[i]]) > 12:
              srctotr[result[i]]=srctotr[result[i]].split(" ")
              for x in range(len(srctotr[result[i]])):
                  srctotr[result[i]][x] = srctotr[result[i]][x].capitalize()
              srctotr[result[i]]=''.join(srctotr[result[i]])
              if len(srctotr[result[i]]) > 12 and "-" in srctotr[result[i]]:
                  srctotr[result[i]]=srctotr[result[i]].split("-")
                  for y in range(len(srctotr[result[i]])):
                      srctotr[result[i]][y] = srctotr[result[i]][y].capitalize()
              srctotr[result[i]]=''.join(srctotr[result[i]])
              if len(srctotr[result[i]]) > 12:
                  pass
                  a = 12-len(srctotr[result[i]])
                  srctotr[result[i]] = srctotr[result[i]][:a]
          if result[i] == "-":
              srctotr[result[i]] = '-'
          if len(srctotr[result[i]]) > 12:
           with open('folder\more_than_12.txt','a',encoding='utf-8') as er:
                  er.write(f"{srctotr[result[i]]}, {len(srctotr[result[i]])}, {12-len(srctotr[result[i]])}\n")
                  pass
          contenu=contenu.replace("<"+result[i]+">","<"+srctotr[result[i]]+"11"+">")
          #except Exception as e:
          #  print(e)
          # with open('more_than_12.txt','a',encoding='utf-8') as er:
                  #er.write(f"Erreur ! : {[result[i]]}, {[result[i]]}, {12-len([result[i]])}\n")
          #     pass
  with open("folder\move_names.h",'a',encoding='utf-8') as f2:
      a = (contenu).replace('''<''','''("''').replace('''>''','''")''').replace("’","'").replace("11","")
      f2.write(a)

  end_time = time.time()
  time_lapsed = round(end_time - start_time,1)
  print("\n\nVeuillez vérifier le fichier 'more_than_10.txt' pour voir s'il y a des noms excédant 13 caractères.\n"+"_"*7+f"\n\nOpération Réussie, temps écoulé : {time_lapsed}s")
#----------------------------------------------------------------------------------------------------------------------
  ws.update_idletasks()
  rep = tf.askdirectory(initialdir="pokeemerald",title='Sélectionnez un dossier')
  path = pathlib.Path(rep).resolve().parent
  print(path)
  import shutil
  shutil.copy("folder\species_names.h", path)
  shutil.copy("folder\pokedex_text.h", path )
  shutil.copy("folder\item.h", path)
  shutil.copy("folder\more_than_10.txt", path )
  shutil.copy("folder\Readme.md", path)
  os.remove("move_names.h")

  txt2['text'] ="Finish ! Next step, open Readme.md"



ws = Tk()
ws.title('PokeemeraldTraductor')
ws.geometry('330x150')
ws.config(bg='#010101')


radioValue = IntVar() 
rdioOne = Radiobutton(ws, text='Français  ',bg="#121019",fg="#FFFFFF",highlightthickness=0,activebackground="#440d1d",activeforeground="#FFFFFF",
  variable=radioValue, value=0,command=lambda:traduction("1")) 

rdioTwo = Radiobutton(ws, text='Deutsch   ',bg="#121019",fg="#FFFFFF",highlightthickness=0,activebackground="#440d1d",activeforeground="#FFFFFF",
  variable=radioValue, value=1,command=lambda:traduction("2")) 
rdioThree = Radiobutton(ws, text='Español   ',bg="#121019",fg="#FFFFFF",highlightthickness=0,activebackground="#440d1d",activeforeground="#FFFFFF",
  variable=radioValue, value=2,command=lambda:traduction("3"))
rdioFour = Radiobutton(ws, text='Italiano  ',bg="#121019",fg="#FFFFFF",highlightthickness=0,activebackground="#440d1d",activeforeground="#FFFFFF",
  variable=radioValue, value=2,command=lambda:traduction("4"))
rdioFive = Radiobutton(ws, text='Korean    ',bg="#121019",fg="#FFFFFF",highlightthickness=0,activebackground="#440d1d",activeforeground="#FFFFFF",
  variable=radioValue, value=2,command=lambda:traduction("5"))
rdioSix = Radiobutton(ws, text='Japanese ',bg="#121019",fg="#FFFFFF",highlightthickness=0,activebackground="#440d1d",activeforeground="#FFFFFF",
  variable=radioValue, value=2,command=lambda:traduction("6"))


rdioOne.grid(column=0, row=0, sticky="W")
rdioTwo.grid(column=0, row=1, sticky="W")
rdioThree.grid(column=0, row=2, sticky="W")
rdioFour.grid(column=0, row=3, sticky="W")
rdioFive.grid(column=0, row=4, sticky="W")
rdioSix.grid(column=0, row=5, sticky="W")

pb = Progressbar(
    ws,
    orient = HORIZONTAL,
    length = 150,
    mode = 'determinate'
    )

pb.place(x=120, y=30)

txt = Label(
    ws,
    text = '0%',
    bg = '#010101',
    fg = '#fff'
    

)
txt.config(font=("Arial",8))
txt.place(x=273,y=30)

txt2 = Label(
    ws,
    text = 'Please choose a language',
    bg = '#010101',
    fg = '#de1b46'
    

)
txt2.config(font=("Arial",8))
txt2.place(x=119,y=10)

ws.mainloop()
