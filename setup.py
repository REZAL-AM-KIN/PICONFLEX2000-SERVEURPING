print("Demarrage 'setup.py'")
print("Importation Fonctions")
for root, dirs, files in os.walk("/home/pi/PICONFLEX2000-FONCTIONS"):
        for names in files:
            exec(open(os.path.join(root, names)).read())