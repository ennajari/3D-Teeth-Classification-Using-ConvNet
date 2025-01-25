import streamlit as st
import numpy as np
import tensorflow as tf
import trimesh
import pyvista as pv
from scipy import ndimage


model = tf.keras.models.load_model("C:\\Users\\HP\\OneDrive\\Bureau\\S4\\pfa\\111\\3D_Teeth_Classification_Using_ConvNet\\teeth_classification_model.h5")


categories = ['Canine', 'Deuxieme_molaire', 'Deuxieme_premolaire', 'Incisive_centrale', 
              'Incisive_laterale', 'Premiere_molaire', 'Premiere_premolaire']

def process_obj(file, target_size=(64, 64, 64)):
    mesh = trimesh.load_mesh(file, file_type='obj')
    
    
    if isinstance(mesh, trimesh.Scene):
        mesh = mesh.dump(concatenate=True)
    
    vertices = np.array(mesh.vertices)
    vertices = (vertices - vertices.min()) / (vertices.max() - vertices.min())
    volume = np.histogramdd(vertices, bins=target_size)[0]
    return volume, mesh

def render_3d_model(mesh):
    faces = np.hstack([[len(face)] + list(face) for face in mesh.faces])
    
    pv_mesh = pv.PolyData(mesh.vertices, faces)
    
    plotter = pv.Plotter(window_size=(400, 400), off_screen=True)
    plotter.add_mesh(pv_mesh, color='white')
    plotter.background_color = 'black'
    plotter.show_grid()
    plotter.camera_position = 'xy'
    
    screenshot = plotter.screenshot()
    st.image(screenshot, caption='3D Tooth Model', use_column_width=True)

st.title('3D Teeth Classification')

uploaded_file = st.file_uploader("Choose a 3D tooth file", type='obj')

if uploaded_file is not None:
    volume, mesh = process_obj(uploaded_file)
    
    prediction = model.predict(volume[np.newaxis, ..., np.newaxis])
    predicted_class = categories[np.argmax(prediction)]
    
    st.write(f"The uploaded tooth is classified as: **{predicted_class}**")
    
    st.subheader("Prediction Confidence")
    for i, category in enumerate(categories):
        st.write(f"{category}: {prediction[0][i] * 100:.2f}%")
        st.progress(float(prediction[0][i]))


    st.subheader("Vues de dents à 360 degrés")
    st.write("Les vues de dents à 360 degrés permettent aux utilisateurs de visualiser un produit sous tous les angles en faisant pivoter l'image à l'aide de leur souris.")
    
    st.subheader("3D Model Visualization")
    render_3d_model(mesh)
