# Music data feed

La musique. On a tous un style qu'on préfère. Une harmonie de vibrations sonores qui nous font vibrer à notre tour. Alors que diriez-vous de creuser un peu plus pour mieux connaitre votre profil musical ?


Dans ce projet, il s'agit de créer un ETL pour récupérer des informations sur des chansons dans un repo (API, base de données, etc.), et les stocke dans une base de données dédiée après les avoir formatées. Le but est de se constituer un dataset pour entraîner un modèle de machine learning permettant de prédire le genre d'une chanson à partir de ses paroles.

Le repo en question peut être par exemple l'API de Spotify d'où on récupérera des chansons.

*Domaine*:
  _Track (piste)_: Une piste qu'on a écoutée


## Extraction (Extract)
Le système contacte l'API de Spotify (ou d'un autre logiciel de streaming audio) pour récupérer les 100 dernières chansons écoutées.

Le code concernant l'extraction se trouve dans le répertoire `extractor`.

## Transformation (Transform)
Le système utilise les informations extraites afin de créer deux listes :
- Une liste de pistes (id, titre de la chanson, date à laquelle elle a été écoutée)
- Une liste d'artistes (id, nom de l'artiste)

## Chargement (Load)
Le système charge les données formatées dans une base de données de notre choix
