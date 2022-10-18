# Music data feed with hexagonal architecture

La musique. On a tous un style qu'on préfère. Une harmonie de vibrations sonores qui nous font vibrer à notre tour. Alors que diriez-vous de creuser un peu plus pour mieux connaitre votre profil musical ?

Dans ce projet, il s'agit de créer un ETL (Extract-Transform-Load) pour récupérer des informations sur les pistes qu'on écoute sur Spotify et les stocker sur une base de données pour les analyser plus tard.

Le projet est réalisé avec une architecture hexagonale afin que chaque composant puisse être facilement remplacé (par exemple, en utilisant une autre API que celle de Spotify pour collecter les données sur les pistes qu'on a écoutées)

*Domaine*:
  _Track (piste)_: Une piste qu'on a écoutée


## Extraction (Extract)
Le système contacte l'API de Spotify (ou d'un autre logiciel de streaming audio) pour récupérer les `n` dernières pistes qu'on a écoutées
- En cas de réussite, retourner une liste de pistes avec les informations suivantes pour chaque piste : titre de la chanson, nom de l'artiste, date à laquelle on l'a écouté
- En cas d'échec de l'appel de l'API (code 4xx, 5xx), le programme lève une exception

## Transformation (Transform)
Le système utilise les informations extraites afin de créer deux listes :
- Une liste de pistes (id, titre de la chanson, date à laquelle elle a été écoutée)
- Une liste d'artistes (id, nom de l'artiste)

## Chargement (Load)
Le système charge les données formatées dans une base de données de notre choix
