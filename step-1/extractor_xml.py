import sys
import xml.etree.ElementTree as ET

# Fonction pour extraire les balises <Value> d'un fichier XML
def extraire_balises_value(fichier_xml):
    try:
        # Charger le fichier XML
        arbre = ET.parse(fichier_xml)
        racine = arbre.getroot()

        # Liste pour stocker les balises <Value>
        valeurs = []

        # Parcourir l'arbre XML pour trouver les balises <Value>
        for element in racine.iter('Value'):
            valeurs.append(element.text)

        return valeurs
    except FileNotFoundError:
        print(f"Le fichier '{fichier_xml}' n'a pas été trouvé.")
        return []

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py chemin_vers_fichier.xml")
    else:
        fichier_xml = sys.argv[1]
        valeurs = extraire_balises_value(fichier_xml)

        # Afficher les balises <Value> extraites
        for valeur in valeurs:
            print(valeur)
