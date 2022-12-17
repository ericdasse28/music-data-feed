# Music data feed

La musique. On a tous un style qu'on préfère. Une harmonie de vibrations sonores qui nous font vibrer à notre tour. Alors que diriez-vous de creuser un peu plus pour mieux connaitre votre profil musical ?

Dans ce projet, il s'agit de créer un ETL pour récupérer des informations sur des chansons dans un repo (API, base de données, etc.), et les stocke dans une base de données dédiée après les avoir formatées. Le but est de se constituer un dataset pour entraîner un modèle de machine learning permettant de prédire le genre d'une chanson à partir de ses paroles.

Le repo en question peut être par exemple l'API de Spotify d'où on récupérera des chansons.


## Extraction (Extract)
Le système contacte l'API de Spotify (ou d'un autre logiciel de streaming audio) pour récupérer les 100 dernières chansons écoutées

## Transformation (Transform)
Le système met en forme ces informations et les répartit en pistes, auteurs et genres

## Chargement (Load)
Le système charge les données formatées dans une base de données de notre choix
