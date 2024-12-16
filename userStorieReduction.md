En tant que : Client utilisateur du système de commande,
Je veux : Appliquer une remise sur ma commande lors de son placement,
Afin de : Réduire le montant total à payer en fonction des promotions ou avantages accordés.
________________________________________
Critères d'acceptation :
1.	Validation de la remise :
o	La remise doit être un pourcentage compris entre 0 % et 100 %.
o	Si une remise invalide est fournie, une erreur doit être affichée, et la commande ne doit pas être placée.
2.	Calcul précis :
o	Le montant de la remise doit être calculé sur le total du panier.
o	Le total après remise doit être affiché avec une précision de deux décimales.
3.	Affichage des détails :
o	Les détails de la commande doivent inclure :
	Le sous-total (avant remise).
	Le pourcentage de remise appliqué.
	Le total après remise.
o	Ces informations doivent être visibles pour le client avant la confirmation de la commande.
4.	Placement de la commande :
o	Une fois la commande placée, le stock doit être mis à jour en fonction des quantités commandées.
o	Le message de confirmation doit inclure le total après remise.
5.	Robustesse :
o	Si la remise est omise lors de la création de la commande, elle doit être par défaut à 0 % (aucune réduction appliquée).

