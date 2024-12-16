User story : 

En tant qu’utilisateur,
Je veux pouvoir connaître le nombre total d'articles dans mon panier,
Afin de savoir combien d'articles j'ai ajoutés au total.

Critères d’acceptation : 

1. La méthode get_total_items() doit retourner le nombre total d'articles dans le panier.
2. Le nombre total d'articles doit être calculé en additionnant les quantités de chaque produit présent dans le panier.
3. Si le panier est vide, la méthode get_total_items() doit retourner 0.
