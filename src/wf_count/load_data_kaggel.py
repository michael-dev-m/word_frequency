import kagglehub

# Download latest version
path = kagglehub.dataset_download("rtatman/english-word-frequency")

if __name__ == '__main__':
    print("Path to dataset files:", path)
