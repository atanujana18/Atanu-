# Atanu-real_ai_image_detector/
├── app.py                       # Main Streamlit app
├── requirements.txt             # Python dependencies
├── model/
│   └── detector_model.h5        # (You need to add your trained model here)
├── utils/
│   └── predict.py               # Image preprocessing & prediction logic
└── images/                      # (Optional) Example or test image 
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin mainpip install -r requirements.txt
streamlit run app.py
