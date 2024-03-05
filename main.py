import csv
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class AnnotationTool:
    def __init__(self, master):
        self.master = master
        self.master.title("YOLOv8 Annotation Tool")

        self.canvas_width = 1750
        self.canvas_height = 625
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        self.class_labels = {}
        self.annotations = []
        self.current_polygon = []
        self.image = None
        self.polygon_items = []
        self.current_polygon_index = 0  # Track the index of the current polygon
        self.exporting = False  # Flag to indicate if exporting is in progress

        self.create_button = tk.Button(self.master, text="Create Polygon", command=self.create_polygon)
        self.create_button.pack(side=tk.LEFT)

        self.finish_button = tk.Button(self.master, text="Finish Polygon", command=self.finish_polygon)
        self.finish_button.pack(side=tk.LEFT)

        self.export_button = tk.Button(self.master, text="Export Annotations", command=self.export_annotations)
        self.export_button.pack(side=tk.LEFT)

        self.add_class_button = tk.Button(self.master, text="Add Class", command=self.add_class)
        self.add_class_button.pack(side=tk.LEFT)

        self.class_label_entry = tk.Entry(self.master)
        self.class_label_entry.pack(side=tk.LEFT)

        self.load_classes_button = tk.Button(self.master, text="Load Classes from CSV", command=self.load_classes_from_csv)
        self.load_classes_button.pack(side=tk.LEFT)

        self.load_image_button = tk.Button(self.master, text="Load Image", command=self.load_image)
        self.load_image_button.pack(side=tk.LEFT)

        # Load the logo image
        logo_image = Image.open("logo\cbs_logo.png")  # Replace "logo.png" with the path to your logo image
        logo_image = logo_image.resize((50, 50))  # Resize the logo image as needed
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Developer name label
        developer_label = tk.Label(self.master, text="Developer: Şükrü Burak Çetin")
        developer_label.pack(side=tk.LEFT)

        # Logo label
        logo_label = tk.Label(self.master, image=logo_photo)
        logo_label.image = logo_photo  # Keep a reference to the image to prevent it from being garbage collected
        logo_label.pack(side=tk.LEFT)

        # Initialize class assignment dialog
        self.class_window = None
        self.class_var = tk.StringVar()
        self.class_var.set("Select Class")
        self.class_options = []

    def load_image(self):
        # Destroy any existing class windows
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Clear existing polygons and annotations
            self.clear_polygons()
            self.annotations = []

            self.image_name = file_path.split("/")[-1].split(".jpg")[0]  # Get the image name
            self.image = Image.open(file_path)
            # Resize image while maintaining aspect ratio
            self.image.thumbnail((self.canvas_width, self.canvas_height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def add_class(self):
        class_label = self.class_label_entry.get()
        if class_label:
            self.class_labels[len(self.class_labels)] = class_label
            self.class_label_entry.delete(0, tk.END)
            print("Class '{}' added with ID {}".format(class_label, len(self.class_labels) - 1))

    def create_polygon(self):
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button-3>", self.clear_points)  # Bind right mouse button to clear points

    def finish_polygon(self):
        if len(self.current_polygon) > 2:
            polygon_item = self.canvas.create_polygon(self.current_polygon, outline="red", fill="", width=2)
            self.polygon_items.append(polygon_item)
            self.annotations.append(self.current_polygon)
            self.current_polygon = []
            self.canvas.unbind("<Button-1>")
        else:
            print("Please select at least three points to create a polygon.")

    def on_click(self, event):
        x, y = event.x, event.y
        self.current_polygon.extend([x, y])
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red", tags="points")  # Add "points" tag to the oval

    def clear_polygons(self):
        for item in self.polygon_items:
            self.canvas.delete(item)
        self.polygon_items = []
        self.current_polygon = []  # Clear the current polygon points as well

    def clear_points(self, event):
        self.current_polygon = []  # Clear the current polygon points
        self.canvas.delete("points")  # Delete all points on the canvas with the "points" tag

    def export_annotations(self):
        if not self.annotations:
            print("No annotations to export.")
            return

        if not hasattr(self, 'image_name'):
            print("Please load an image first.")
            return

        self.exporting = True  # Set exporting flag to True
        self.current_polygon_index = 0  # Reset polygon index

        # Open a single "Choose Class" dialog
        self.class_window = tk.Toplevel(self.master)
        self.class_window.title("Choose Class")

        self.class_var = tk.StringVar(self.class_window)
        self.class_var.set("Select Class")

        self.class_options = list(self.class_labels.values())
        self.class_menu = tk.OptionMenu(self.class_window, self.class_var, *self.class_options)
        self.class_menu.pack()

        self.done_button = tk.Button(self.class_window, text="Done", command=self.class_selected)
        self.done_button.pack()

        # Start exporting polygons
        self.export_next_polygon()

    def export_next_polygon(self):
        if self.current_polygon_index < len(self.annotations):
            # Remove blue indication from the previously highlighted polygon
            if self.current_polygon_index > 0:
                self.canvas.itemconfig(self.polygon_items[self.current_polygon_index - 1], outline="red", width=2)

            # Highlight the current polygon
            self.canvas.itemconfig(self.polygon_items[self.current_polygon_index], outline="blue", width=2)

        else:
            print("All annotations exported successfully.")
            self.exporting = False  # Reset exporting flag
            self.class_window.destroy()  # Close the "Choose Class" dialog after all polygons are exported

    def highlight_next_polygon(self):
        if self.current_polygon_index < len(self.polygon_items):
            self.canvas.itemconfig(self.polygon_items[self.current_polygon_index], outline="blue", width=2)
            self.choose_class()  # Prompt user to select class ID
        else:
            print("All annotations exported successfully.")
            self.exporting = False  # Reset exporting flag

    def choose_class(self):
        if self.exporting:
            class_window = tk.Toplevel(self.master)
            class_window.title("Choose Class")

            class_var = tk.StringVar(class_window)
            class_var.set("Select Class")

            class_options = list(self.class_labels.values())
            class_menu = tk.OptionMenu(class_window, class_var, *class_options)
            class_menu.pack()

            done_button = tk.Button(class_window, text="Done",
                                    command=lambda: self.class_selected(class_window, class_var))
            done_button.pack()

            # Remove blue indication from the previously highlighted polygon
            if self.current_polygon_index > 0:
                self.canvas.itemconfig(self.polygon_items[self.current_polygon_index - 1], outline="red", width=2)

            # Highlight the current polygon
            self.canvas.itemconfig(self.polygon_items[self.current_polygon_index], outline="blue", width=2)

            class_window.wait_window()

    def class_selected(self):
        chosen_class = self.class_var.get()
        class_id = list(self.class_labels.keys())[list(self.class_labels.values()).index(chosen_class)]

        with open(f"data\labels\{self.image_name}_gt.txt", 'a') as f:  # Use image name for the file
            annotation = self.annotations[self.current_polygon_index]
            yolo_format = self.convert_to_yolov8(annotation)
            f.write(f"{class_id} {' '.join(str(coord) for coord in yolo_format)}")
            if self.current_polygon_index < len(self.annotations) - 1:  # Check if it's not the last annotation
                f.write("\n")  # Append newline if it's not the last annotation

        self.current_polygon_index += 1  # Move to the next polygon
        self.export_next_polygon()  # Export the next polygon

    def convert_to_yolov8(self, coordinates):
        image_width, image_height = self.image.size
        normalized_coords = []
        for i in range(0, len(coordinates), 2):
            x = coordinates[i] / image_width
            y = coordinates[i + 1] / image_height
            normalized_coords.extend([x, y])
        yolov8_format = [f"{coord:.6f}" for coord in normalized_coords]
        return yolov8_format

    def load_classes_from_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for idx, row in enumerate(csvreader):
                    class_label = row[0]
                    class_id = idx  # Assign sequential numeric IDs
                    self.class_labels[str(class_id)] = class_label
                    self.class_options.append(class_label)
                print("Classes loaded from CSV:", self.class_labels)


def main():
    root = tk.Tk()
    app = AnnotationTool(root)
    root.mainloop()


if __name__ == "__main__":
    main()
