from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    trouve=0
    seuil=0
    im=image.binarisation(S).localisation()
    for i in range(len(liste_modeles)):
        modele=liste_modeles[i].binarisation(S).localisation()
        im_r=im.resize(modele.H, modele.W)
        test_seuil=im_r.similitude(modele)
        if seuil < test_seuil:
            trouve=i
            seuil=test_seuil
    return trouve

