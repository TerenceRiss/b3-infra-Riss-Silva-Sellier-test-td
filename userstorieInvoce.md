# User Story : Génération de Facture pour une Commande

## Titre
En tant qu'utilisateur, je veux recevoir une facture détaillée après avoir passé une commande afin de conserver un résumé clair de mes achats.

---

## Description
Lorsqu'un utilisateur passe une commande via le panier, le système doit générer une facture contenant un récapitulatif des produits achetés, les quantités, les prix unitaires, la remise appliquée, le total avant remise, et le total final après remise.

---

## Critères d'acceptation

1. **Affichage des détails des produits**
   - La facture doit afficher le nom des produits, leur prix unitaire et les quantités achetées.
     **Exemple :**
     ```
     Produit : Laptop x 1 - 1000.00€
     Produit : Headphones x 2 - 200.00€
     ```

2. **Affichage du sous-total avant remise**
   - Le système doit afficher le sous-total avant application de la remise.
     **Exemple :**
     ```
     Sous-total : 1400.00€
     ```

3. **Affichage de la remise appliquée**
   - Si une remise est appliquée, elle doit être affichée en pourcentage et en valeur.
     **Exemple :**
     ```
     Remise : 10% (-140.00€)
     ```

4. **Affichage du total final**
   - Le total final après application de la remise doit être clairement affiché.
     **Exemple :**
     ```
     Total Final : 1260.00€
     ```

5. **Génération d'une facture sous forme de chaîne de caractères**
   - La facture doit être générée sous forme d'une chaîne de texte prête à être affichée ou sauvegardée.

6. **Validation des données**
   - Si aucun produit n'est dans le panier, l'utilisateur ne peut pas générer une facture.
   - La remise doit être comprise entre 0 et 100%.
