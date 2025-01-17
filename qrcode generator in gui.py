import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    text = entry.get()
    if not text.strip():
        messagebox.showerror("Error", "Please enter text to generate the QR Code.")
        return

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 to 40, 1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image of the QR Code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Update the global variable and display the image
    global qr_photo
    qr_photo = ImageTk.PhotoImage(qr_image.resize((250, 250)))
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    # Save the generated image for later use
    global current_qr_image
    current_qr_image = qr_image

def save_qr_code():
    if current_qr_image is None:
        messagebox.showerror("Error", "No QR Code to save. Generate one first.")
        return

    # Ask user to select a file location
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
    )

    if file_path:
        try:
            current_qr_image.save(file_path)
            messagebox.showinfo("Success", f"QR Code saved successfully at {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save QR Code: {e}")

# Initialize the main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

# Initialize global variables
qr_photo = None
current_qr_image = None

# Add input field and buttons
entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=20)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Save QR Code", command=save_qr_code, font=("Arial", 12), bg="green", fg="white")
save_button.pack(pady=10)

# Add a label to display the QR Code
qr_label = tk.Label(root)
qr_label.pack(pady=20)

# Run the application
root.mainloop()
