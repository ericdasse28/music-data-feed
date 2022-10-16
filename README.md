# Music data feed with hexagonal architecture

La musique. On a tous un style qu'on préfère. Une harmonie de vibrations sonores qui nous font vibrer à notre tour. Alors que diriez-vous de creuser un peu plus pour mieux connaitre votre profil musical ?

Dans ce projet, il s'agit de créer un ETL pour récupérer des informations sur les pistes qu'on écoute sur Spotify et les stocker sur une base de données pour les analyser plus tard.

Le projet est réalisé avec une architecture hexagonale afin que chaque composant puisse être facilement remplacé (par exemple, en utilisant une autre API que celle de Spotify pour collecter les données sur les pistes qu'on a écoutées)


## Extraction (Extract)
Le système contacte l'API de Spotify (ou d'un autre logiciel de streaming audio) pour récupérer les 100 dernières chansons écoutées

## Transformation (Transform)
Le système met en forme ces informations et les répartit en pistes, auteurs et genres

## Chargement (Load)
Le système charge les données formatées dans une base de données de notre choix
