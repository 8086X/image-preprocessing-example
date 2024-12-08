from image_preprocessing.filters import to_black_and_white

if __name__ == "__main__":
    # 假设 examples 文件夹中有 original.jpg
    to_black_and_white("examples/original.jpg", "examples/output.jpg")
    print("Conversion complete. Check examples/output.jpg for the result.")
