## ⁉️ ‼️ Mon interpretation de :
![Image](https://raw.githubusercontent.com/Hatchi-Kin/images_embeddings_facenet/master/tp.png)

## Screenshot
![Image](https://raw.githubusercontent.com/Hatchi-Kin/images_embeddings_facenet/master/Screenshot_Sesame2.png)


## 🌳 Structure du projet
```markdown.
├── app.py                                     # L'application Flask                         
├── process_pipeline.py                        # code pour pre-process les images                      
├── requirements.txt
├── README.md                                  # vous êtes ici !
├── docker-compose.yml                         # docker-compose up 
├── Dockerfile
└── static
    └── Celebrity_Faces_Dataset_processed      # Le Dataset d'images
        ├── embeddings_dataset.json            # Les Embeddings des images
        ├── Angelina_Jolie
        ├── Brad_Pitt
        ├── Denzel_Washington
        ├── Kate_Winslet
        ├── Natalie_Portman
        └── Tom_Cruise
└── img_test                                   # Quelques images pour tester
    ├── buscemi01.jpg
    ├── mcgregor01.jpg
    └── washington01.jpg
└── templates                                  # le front de notre appli (le moins de js possible)
    └── upload.html
```

## 🏃 Installation
dans le terminal:
```bash
docker-compose up -d
```
puis http://localhost:5000/
