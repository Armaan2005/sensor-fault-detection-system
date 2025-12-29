from flask import Flask,render_template,jsonify,request,send_file
from src.ai.groq_assistant import GroqAssistant
from src.exception import CustomException
from src.logger import logging as lg
from dotenv import load_dotenv
load_dotenv()
import os,sys
import json

from src.pipeline.train_pipeline import TrainingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline

app=Flask(__name__)

@app.route("/")
def home():
     return render_template("home.html")

@app.route("/train",methods=['POST'])
def train_route():
    try:
        train_pipeline=TrainingPipeline()
        train_pipeline.run_pipeline()
        
        return render_template("train_success.html")
    
    except Exception as e:
        raise CustomException(e,sys)
    
    
@app.route('/predict',methods=['POST','GET'])
def upload():
    try:
        
        if request.method=='POST':
            prediction_pipeline=PredictionPipeline(request)
            
            prediction_file_detail=prediction_pipeline.run_pipeline()
            
            
            lg.info("prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,download_name=prediction_file_detail.prediction_file_name,as_attachment=True)
        
        
        else:
            return render_template('upload_file.html')
    
    except Exception as e:
        raise CustomException(e,sys)
    

@app.route("/ask-ai", methods=["POST"])
def ask_ai():
    try:
        data = request.get_json(silent=True)

        if not data or "question" not in data:
            return jsonify({
                "answer": "Please enter a valid question."
            }), 400

        ai = GroqAssistant()
        answer = ai.generate_explanation(data["question"])

        return jsonify({"answer": answer})

    except Exception:
        return jsonify({
            "answer": "AI service is temporarily unavailable. Please try again."
        }), 200


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



@app.route("/dashboard-metrics", methods=["GET"])
def dashboard_metrics():
    try:
        metrics_path = "artifacts/metrics/prediction_metrics.json"
        model_meta_path = "artifacts/model_metadata.json"

        with open(metrics_path) as f:
            metrics = json.load(f)

        with open(model_meta_path) as f:
            model_meta = json.load(f)

        response = {
            "model_name": model_meta.get("model_name"),
            "total_predictions": metrics.get("total_predictions"),
            "good_count": metrics.get("good_count"),
            "bad_count": metrics.get("bad_count"),
            "last_updated": metrics.get("last_updated")
        }

        return jsonify(response)

    except Exception as e:
        raise CustomException(e, sys)  
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=False)#hello hello