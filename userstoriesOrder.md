
### **1. Création de la commande**
**User Story 1 :**  
En tant que **client**,  
Je veux pouvoir créer une commande à partir d'un panier non vide,  
Afin de finaliser mon achat et procéder au paiement.  

**Critères d'acceptation :**  
- Si le panier est vide, un message d'erreur doit être affiché.  
- Une commande doit pouvoir être initialisée avec les articles du panier et calculer un total sans remise par défaut.

---

### **2. Application d'une remise**
**User Story 2 :**  
En tant que **client**,  
Je veux pouvoir appliquer une remise en pourcentage à ma commande,  
Afin de bénéficier d'une réduction sur le montant total de mes achats.  

**Critères d'acceptation :**  
- La remise doit être exprimée en pourcentage (entre 0 et 100 inclus).  
- Si une remise est appliquée, le montant total doit être recalculé en fonction de la remise.  
- Si la remise est invalide (négative ou supérieure à 100%), un message d'erreur doit être retourné.

---

### **3. Calcul du sous-total et du total avec remise**
**User Story 3 :**  
En tant que **client**,  
Je veux voir le sous-total et le montant total après application de la remise,  
Afin de comprendre l'économie réalisée grâce à la remise.  

**Critères d'acceptation :**  
- Le sous-total doit afficher la somme totale sans remise.  
- Le montant de la remise doit être calculé correctement et affiché.  
- Le montant total doit être égal au sous-total diminué de la remise.

---

### **4. Placement de la commande**
**User Story 4 :**  
En tant que **client**,  
Je veux pouvoir finaliser ma commande,  
Afin de confirmer mon achat et mettre à jour les stocks des produits commandés.  

**Critères d'acceptation :**  
- La commande doit mettre à jour les stocks des produits en fonction des quantités commandées.  
- Si un produit n'a pas assez de stock, une exception doit être levée.  
- Une confirmation doit être affichée indiquant que la commande a été placée avec succès, en précisant le montant total après remise.

---

### **5. Visualisation des détails de la commande**
**User Story 5 :**  
En tant que **client**,  
Je veux voir les détails complets de ma commande,  
Afin de vérifier les articles, les quantités, le sous-total, la remise et le total final.  

**Critères d'acceptation :**  
- La vue de la commande doit inclure :  
  - Les noms des produits et leurs quantités respectives.  
  - Le sous-total avant remise.  
  - Le pourcentage de remise appliqué.  
  - Le montant total après remise.  

---

### **6. Validation des données d'entrée**
**User Story 6 :**  
En tant que **développeur**,  
Je veux que les données d'entrée pour la création de la commande soient validées,  
Afin d'assurer l'intégrité des informations et éviter les erreurs.  

**Critères d'acceptation :**  
- Le pourcentage de remise doit être validé (entre 0 et 100%).  
- Si un pourcentage de remise invalide est fourni, une exception doit être levée.  
- Les produits et quantités doivent provenir d'un panier valide contenant des articles.

---

### **Récapitulatif des User Stories**
1. **Création de la commande** : Créer une commande depuis un panier non vide.  
2. **Application d'une remise** : Appliquer un pourcentage de réduction valide à la commande.  
3. **Calcul du sous-total et du total** : Voir les montants avec et sans remise.  
4. **Placement de la commande** : Finaliser la commande et mettre à jour les stocks.  
5. **Visualisation des détails de la commande** : Afficher les articles, sous-total, remise, et total final.  
6. **Validation des données d'entrée** : Assurer que toutes les données d'entrée sont correctes et valides.

