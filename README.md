## 🌳 Structure du projet
```markdown.
├── app.py                                      
├── process_pipeline.py                         
├── requirements.txt
├── README.md                                   
├── docker-compose.yml
├── Dockerfile
└── static
    └── Celebrity_Faces_Dataset_processed
        ├── embeddings_dataset.json
        ├── Angelina_Jolie
        ├── Brad_Pitt
        ├── Denzel_Washington
        ├── Kate_Winslet
        ├── Natalie_Portman
        └── Tom_Cruise
└── img_test
    ├── buscemi01.jpg
    ├── mcgregor01.jpg
    └── washington01.jpg
└── templates
    └── upload.html
```

## 🏃 Installation
dans le terminal:
```bash
docker-compose up -d
```
puis http://localhost:5000/