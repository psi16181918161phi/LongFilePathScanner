import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class LongFilePathScanner:
    """
    A utility class for scanning directories for file paths exceeding a specified length.
    """

    @staticmethod
    def find_long_file_paths(root_directory, limit=256):
        """
        Finds all files whose full paths exceed the specified character limit.

        Args:
            root_directory (str): The root directory to start the search.
            limit (int): The character limit for file paths.

        Returns:
            list: A list of file paths that exceed the character limit.
        """
        long_file_paths = []
        for root, dirs, files in os.walk(root_directory):
            for file in files:
                full_path = os.path.abspath(os.path.join(root, file))
                if len(full_path) > limit:
                    long_file_paths.append(full_path)
        return long_file_paths


class LongFilePathCheckerApp:
    """
    A Tkinter GUI application for the LongFilePathScanner.
    """

    def __init__(self, root):
        """
        Initializes the GUI for the application.
        """
        self.root = root
        self.root.title("Long File Path Checker")
        self.root.geometry("700x500")

        # Theme Colors for Dark Theme with Pink Text
        self.bg_color = "#2e2e2e"
        self.fg_color = "pink"
        self.btn_bg = "#3a3a3a"
        self.entry_bg = "#3a3a3a"

        self.root.config(bg=self.bg_color)

        self.selected_dir = None
        self.character_limit = 256
        self.results = []

        # GUI components
        self.create_widgets()

    def create_widgets(self):
        """
        Creates and places GUI components in the main window.
        """
        # Directory selection label
        tk.Label(self.root,
                 text="Select a directory to scan:",
                 font=("Arial", 12),
                 bg=self.bg_color,
                 fg=self.fg_color).pack(pady=10)

        # Directory selection button
        self.select_dir_btn = tk.Button(self.root,
                                        text="Select Directory",
                                        command=self.select_directory,
                                        font=("Arial", 10),
                                        bg=self.btn_bg,
                                        fg=self.fg_color)
        self.select_dir_btn.pack(pady=5)

        # Selected directory label
        self.dir_label = tk.Label(self.root,
                                  text="No directory selected",
                                  font=("Arial", 10),
                                  wraplength=680,
                                  bg=self.bg_color,
                                  fg=self.fg_color)
        self.dir_label.pack(pady=5)

        # Character limit input label
        tk.Label(self.root,
                 text="Set character limit (default 256):",
                 font=("Arial", 12),
                 bg=self.bg_color,
                 fg=self.fg_color).pack(pady=10)

        # Character limit entry
        self.char_limit_entry = tk.Entry(self.root,
                                         font=("Arial", 10),
                                         width=10,
                                         bg=self.entry_bg,
                                         fg=self.fg_color,
                                         insertbackground=self.fg_color)
        self.char_limit_entry.insert(0, "256")
        self.char_limit_entry.pack(pady=5)

        # Result display text box
        self.result_box = scrolledtext.ScrolledText(self.root,
                                                     wrap=tk.WORD,
                                                     font=("Arial", 10),
                                                     height=15,
                                                     width=85,
                                                     bg=self.entry_bg,
                                                     fg=self.fg_color,
                                                     insertbackground=self.fg_color)
        self.result_box.pack(pady=10)
        self.result_box.config(state=tk.DISABLED)

        # Action buttons
        self.scan_btn = tk.Button(self.root,
                                  text="Scan Directory",
                                  command=self.scan_directory,
                                  font=("Arial", 10),
                                  bg=self.btn_bg,
                                  fg=self.fg_color)
        self.scan_btn.pack(pady=5)

        self.export_btn = tk.Button(self.root,
                                    text="Export Results",
                                    command=self.export_results,
                                    font=("Arial", 10),
                                    bg=self.btn_bg,
                                    fg=self.fg_color,
                                    state=tk.DISABLED)
        self.export_btn.pack(pady=5)

    def select_directory(self):
        """
        Opens a dialog to select a directory and updates the label.
        """
        self.selected_dir = filedialog.askdirectory(title="Select Root Directory")
        if self.selected_dir:
            self.dir_label.config(text=f"Selected Directory: {self.selected_dir}")
        else:
            self.dir_label.config(text="No directory selected")

    def scan_directory(self):
        """
        Scans the selected directory for long file paths based on the specified character limit.
        """
        if not self.selected_dir:
            messagebox.showerror("Error", "Please select a directory first!")
            return

        try:
            # Get character limit
            self.character_limit = int(self.char_limit_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the character limit.")
            return

        # Scan for long file paths
        self.results = LongFilePathScanner.find_long_file_paths(self.selected_dir, self.character_limit)

        # Display results
        self.display_results()

        # Enable export button if results exist
        self.export_btn.config(state=tk.NORMAL if self.results else tk.DISABLED)

    def display_results(self):
        """
        Displays the scan results in the text widget.
        """
        self.result_box.config(state=tk.NORMAL)  # Enable editing
        self.result_box.delete("1.0", tk.END)  # Clear previous results

        if self.results:
            self.result_box.insert(tk.END, f"Found {len(self.results)} file(s) exceeding {self.character_limit} characters:\n\n")
            for path in self.results:
                self.result_box.insert(tk.END, f"{path}\n")
        else:
            self.result_box.insert(tk.END, f"No file paths exceed {self.character_limit} characters.\n")

        self.result_box.config(state=tk.DISABLED)  # Disable editing again

    def export_results(self):
        """
        Exports the results to a text file chosen by the user.
        """
        if not self.results:
            messagebox.showinfo("Info", "No results to export.")
            return

        # Ask for file name and save results
        file_path = filedialog.asksaveasfilename(
            title="Save Results",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(f"File paths exceeding {self.character_limit} characters:\n\n")
                    for path in self.results:
                        file.write(path + "\n")
                messagebox.showinfo("Success", f"Results saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the file: {e}")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LongFilePathCheckerApp(root)
    root.mainloop()
