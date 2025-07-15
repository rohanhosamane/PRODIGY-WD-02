from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, -key)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    print("1. Encrypt\n2. Decrypt")
    choice = input("Enter choice (1/2): ")

    in_path = input("Enter input image filename (with extension): ")
    out_path = input("Enter output image filename (with extension): ")
    key = int(input("Enter key (e.g., 50): "))

    if choice == '1':
        encrypt_image(in_path, out_path, key)
    elif choice == '2':
        decrypt_image(in_path, out_path, key)
    else:
        print("Invalid choice")
