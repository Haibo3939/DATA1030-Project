# DATA1030-Project
Introduction

Counter-Strike Global Offensive (CS:GO) has been one of the most successful and popular FPS games for the past decade. There are also an increasing number of competitive gaming platforms in the industry and each of them has to rank players based on their in-game performance. Thus there exists the demand for a fair and intelligent model to make rank predictions for players. There are two important reasons why a fair model for rank prediction is demanded. We can use rank prediction as a Smurf Detector to create a better gaming experience for gamers. That is, when smurf happens, the algorithm can detect and prevent them. Moreover, rank prediction can be used to rank new players. In this project, we will use damage data downloaded from kaggle which contains 955,466 observations and 33 columns to deploy a regression machine learning model to predict rank for players based on their damage performance specifically. The data is collected from ESEA game demos.

Requirements:
  channels:
    - conda-forge
    - defaults
  dependencies:
    - python=3.10.5
    - matplotlib=3.5.2
    - pandas=1.4.2
    - scikit-learn=1.1.1
    - numpy=1.22.4
    - xgboost=1.5.1
    - shap=0.40.0
    - jupyter_client=7.3.1
    - jupyter_core=4.10.0
    - jupyterlab=3.4.2
    - jupyter_server=1.17.0
    - jupytext=1.13.8
    - rise=5.7.1
    - plotly=5.8.0
    - ipywidgets=7.7.0
    - seaborn=0.11.2
  prefix: /opt/conda


Contact:
Haibo Li, haibo_li@brown.edu
