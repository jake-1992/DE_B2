# App              :  plaats, snelheid en versnelling
# Auteur(s)        :  Jake Groen
#                     Stef Stegman
#                     Leroy ....
# Datum            :  29-11-2021

# IMPORTS
#========
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
plt.style.use('ggplot')


# MENU
#=====

# Vraag de gebruiker een keuze te maken uit een gegeven keuzemenu.
# Input:
# - menu_tekst   List van strings  De tekst van het menu
# - menu_vraag   String            De vraag aan de gebruiker
# - menu_opties  List van strings  De opties waaruit de gebruiker kan kiezen
# Output:
# - Keuze        String            De door de gebruiker gemaakte keuze
#----------------------------------------------------------------------------
def vraag_menu_keuze_aan_gebruiker(menu_tekst, menu_vraag, menu_opties):
    for menu_regel in menu_tekst:
        print(menu_regel)
    keuze = "" 
    while keuze not in menu_opties:
        keuze = input(menu_vraag)
        if keuze not in menu_opties:
            print("Dit is geen geldige keuze, kies opnieuw.")
    return keuze


# Vraag de gebruiker van welk type versnelling de plot gegeven moet worden.
# Input:
# - Geen
# Output:
# - type_versnelling  String  "1":  Eenparige versnelling
#                             "2":  Lineaire versnelling
#                             "3":  Complexe versnelling
#---------------------------------------------------------------------------
def vraag_type_versnelling_aan_gebruiker():
    ...          


# DATA
#=====

# Bepaal het pad naar het betreffende csv-bestand met de data op basis van
# het meegegeven type versnelling.
# Input:
# - type_versnelling  String   "1":  Eenparige versnelling
#                              "2":  Lineaire versnelling
#                              "3":  Complexe versnelling
# Output:
# - csv_pad           os.path  Pad aan naar csv-bestand
#--------------------------------------------------------------------------
def bepaal_pad_naar_data(type_versnelling):
    ...


# Lees de data.
# Input:
# - csv_pad  os.path              Pad aan naar csv-bestand
# Output:
# - df       pandas data formaat  Gelezen data
#------------------------------------------------------------------------
def read_data(csv_pad):
    ...
    

# Prepare de data:
# - Bepaal de snelheid o.b.v. de versnelling en voeg dit toe aan de data.
# - Bepaal de plaats o.b.v. de snelheid en voeg dit toe aan de data.
# Input:
# - df  pandas data formaat  Gelezen data
# Output:
# - df  pandas data formaat  Aangepaste data
#-------------------------------------------------------------------------
def prepare_data(df):
    ...


# PLOT
#=====

# Plot de data.
# Input:
# - df                pandas data formaat  Aangepaste data
# - type_versnelling  String               "1":  Eenparige versnelling
#                                          "2":  Lineaire versnelling
#                                          "3":  Complexe versnelling
# Output:
# -  Plo met drie subplots (versnelling, snelheid en plaats)
#---------------------------------------------------------------------
def plot_data(df, type_versnelling):

    # Creeer figure en axes objects met subplots()
    #---------------------------------------------
    ...
    
    # Stel figure title in
    #---------------------
    ...
    
    # Plot versnelling
    #-----------------
    ...
    
    # Plot snelheid
    #--------------
    ...
    
    # Plot plaats
    #--------------
    ...
    
    # Show plot
    #----------
    plt.show()


# MAIN
#=====

def main():
    ... = vraag_type_versnelling_aan_gebruiker(...)
    ... = bepaal_pad_naar_data(...)
    ... = read_data(...)
    ... = prepare_data(...)
    plot_data(...)
    stop_keuze = "9"
    hoofdmenu_tekst = ["",                                      \
                  "Hoofdmenu",                                  \
                  "=========",                                  \
                  "Wat wil je doen:",                           \
                  "  1:  Efficientie per windrichting",         \
                  "  2:  Hoeveel vermogen heb ik nodig?",       \
                  "  3:  Hoeveel vermogen levert het op?",      \
                  "  4:  Energiezuinige modus activeren",       \                      
                  "  9:  Stoppen."                              ]
    hoofdmenu_vraag = "Geef een keuze: "
    hoofdmenu_opties = {"1", "2", "3", stop_keuze}

    keuze = ""
    while keuze != stop_keuze:
        keuze = vraag_menu_keuze_aan_gebruiker(hoofdmenu_tekst, hoofdmenu_vraag, hoofdmenu_opties,)
        if keuze != stop_keuze:
            voer_hoofdmenu_keuze_uit(keuze)



# RUN SCRIPT
#===========
main()# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

