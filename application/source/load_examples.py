def get_path_and_file_names(example):
    """
    Input:  either 'ex1' or ex2'
    """
    #root_dir = "/home/ubuntu/app_demo"
    root_dir = "/Users/ctoews/Documents/Insight/Project/poeml/application"
    pkl_dir = "/source/static/pkl"
    poem_file = "df_"+example+"_poems.pkl"
    image_file = "df_"+example+"_image.pkl"

    return root_dir, pkl_dir, poem_file, image_file

def load_example(example):
    import pandas as pd
    import pickle

    root_dir, pkl_dir, poem_file, image_file = get_path_and_file_names(example)

    df_image = pd.read_pickle(root_dir + pkl_dir + '/' + image_file)
    df_poems = pd.read_pickle(root_dir + pkl_dir + '/' + poem_file)

    return df_image, df_poems
