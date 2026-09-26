import tkinter as tk
from tkinter import messagebox

from modules.search import linear_search
from modules.sorting import selection_sort
from modules.recursion import factorial, fibonacci, tower_of_hanoi
from modules.complexity import get_complexity


BG_BLACK = "#0a0a0a"
PANEL_BLACK = "#0a0a0a"
RED = "#c8102e"
CYAN = "#17b6d1"
WHITE = "#ffffff"
GREY = "#6b6b6b"

FONT_TITLE = ("Courier New", 24, "bold")
FONT_SUBTITLE = ("Courier New", 12, "bold")
FONT_LABEL = ("Courier New", 11, "bold")
FONT_BUTTON = ("Courier New", 12, "bold")
FONT_RESULT = ("Courier New", 11)
FONT_ENTRY = ("Courier New", 12)


def draw_web_lines(canvas, w, h, color=RED):
    """Draw a faint diagonal + radial web pattern behind the content."""
    canvas.create_line(w / 2, 0, w / 2, h, fill=color, width=1)
    canvas.create_line(0, 0, w, h, fill=color, width=1)
    canvas.create_line(w, 0, 0, h, fill=color, width=1)
    canvas.create_line(0, h / 2, w, h / 2, fill=color, width=1)
    for r in (60, 140, 220):
        canvas.create_oval(
            w / 2 - r, h / 2 - r, w / 2 + r, h / 2 + r,
            outline=color, width=1
        )


def style_button(button, color=WHITE, filled=False):
    """Consistent outlined web-slinger button look."""
    if filled:
        button.config(
            bg=color,
            fg=BG_BLACK,
            activebackground=WHITE,
            activeforeground=BG_BLACK,
        )
    else:
        button.config(
            bg=BG_BLACK,
            fg=color,
            activebackground=color,
            activeforeground=BG_BLACK,
        )
    button.config(
        font=FONT_BUTTON,
        relief="flat",
        bd=0,
        highlightthickness=2,
        highlightbackground=color,
        highlightcolor=color,
        cursor="hand2",
    )


def style_label(label, color=WHITE, font=FONT_LABEL):
    label.config(bg=BG_BLACK, fg=color, font=font)


def style_entry(entry):
    entry.config(
        bg="#161616",
        fg=WHITE,
        insertbackground=WHITE,
        font=FONT_ENTRY,
        relief="flat",
        bd=0,
        highlightthickness=2,
        highlightbackground=RED,
        highlightcolor=CYAN,
        justify="center",
    )


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def back_to_menu():
    create_main_menu()


def add_web_background(width=380, height=520):
    """Places a full-size web-line canvas behind whatever is packed after it."""
    bg = tk.Canvas(root, width=width, height=height, bg=BG_BLACK, highlightthickness=0)
    bg.place(x=0, y=0, relwidth=1, relheight=1)
    root.update_idletasks()
    w = root.winfo_width() or width
    h = root.winfo_height() or height
    draw_web_lines(bg, w, h, color=RED)
    return bg


def create_main_menu():
    clear_window()
    root.config(bg=BG_BLACK)
    add_web_background()

    content = tk.Frame(root, bg=BG_BLACK)
    content.place(relx=0.5, rely=0.5, anchor="center")

    title = tk.Label(
        content,
        text="ALGORITHM\nEXPLORER",
        font=FONT_TITLE,
        bg=BG_BLACK,
        fg=WHITE,
        justify="center",
    )
    title.pack(pady=(0, 6))

    subtitle = tk.Label(
        content,
        text="C O M P L E X I T Y   A N A L Y Z E R",
        font=FONT_SUBTITLE,
        bg=BG_BLACK,
        fg=RED,
    )
    subtitle.pack(pady=(0, 26))

    button_specs = [
        ("SEARCH LAB", search_lab, WHITE, False),
        ("SORTING LAB", sorting_lab, WHITE, False),
        ("RECURSION LAB", recursion_lab, CYAN, False),
        ("COMPLEXITY ANALYZER", complexity_lab, RED, True),
    ]

    for text, command, color, filled in button_specs:
        b = tk.Button(content, text=text, width=26, height=2, command=command)
        style_button(b, color, filled)
        b.pack(pady=6)

    exit_btn = tk.Button(content, text="EXIT", width=26, height=2, command=root.destroy)
    style_button(exit_btn, GREY)
    exit_btn.pack(pady=(18, 0))

    footer = tk.Label(
        root,
        text="STAY ON THE GRID",
        font=("Courier New", 9),
        bg=BG_BLACK,
        fg=CYAN,
    )
    footer.place(relx=0.5, rely=0.97, anchor="s")


def make_header(text, color=WHITE):
    tk.Label(
        root,
        text=text,
        font=("Courier New", 20, "bold"),
        bg=BG_BLACK,
        fg=color,
    ).pack(pady=(24, 20))


def sub_screen(build_content_fn):
    """Common wrapper: black bg + faint web lines + centered content frame."""
    clear_window()
    root.config(bg=BG_BLACK)
    add_web_background()
    build_content_fn()


def search_lab():
    def build():
        make_header("SEARCH LAB", WHITE)

        lbl1 = tk.Label(root, text="ENTER NUMBERS (space separated):")
        style_label(lbl1)
        lbl1.pack()

        numbers_entry = tk.Entry(root, width=40)
        style_entry(numbers_entry)
        numbers_entry.pack(pady=8)

        lbl2 = tk.Label(root, text="ENTER TARGET NUMBER:")
        style_label(lbl2)
        lbl2.pack()

        target_entry = tk.Entry(root, width=18)
        style_entry(target_entry)
        target_entry.pack(pady=8)

        result_label = tk.Label(root, text="", font=FONT_RESULT, justify="center")
        style_label(result_label, CYAN, FONT_RESULT)
        result_label.pack(pady=15)

        def perform_search():
            try:
                numbers = [int(number) for number in numbers_entry.get().split()]
                target = int(target_entry.get())

                if not numbers:
                    messagebox.showerror("Invalid Input", "Please enter at least one number.")
                    return

                index, comparisons = linear_search(numbers, target)

                if index != -1:
                    result_label.config(
                        text=">> TARGET FOUND!\n"
                        + "POSITION: " + str(index + 1)
                        + "\nCOMPARISONS: " + str(comparisons)
                    )
                else:
                    result_label.config(
                        text=">> TARGET NOT FOUND.\n"
                        + "COMPARISONS: " + str(comparisons)
                    )

            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid integers.")

        search_btn = tk.Button(root, text="SEARCH", width=16, command=perform_search)
        style_button(search_btn, RED, filled=True)
        search_btn.pack(pady=8)

        back_btn = tk.Button(root, text="BACK TO MENU", width=16, command=back_to_menu)
        style_button(back_btn, GREY)
        back_btn.pack(pady=10)

    sub_screen(build)


def sorting_lab():
    def build():
        make_header("SORTING LAB", WHITE)

        lbl = tk.Label(root, text="ENTER NUMBERS (space separated):")
        style_label(lbl)
        lbl.pack()

        numbers_entry = tk.Entry(root, width=40)
        style_entry(numbers_entry)
        numbers_entry.pack(pady=10)

        result_label = tk.Label(root, text="", font=FONT_RESULT, justify="left")
        style_label(result_label, CYAN, FONT_RESULT)
        result_label.pack(pady=15)

        def perform_sort():
            try:
                numbers = [int(number) for number in numbers_entry.get().split()]

                if not numbers:
                    messagebox.showerror("Invalid Input", "Please enter at least one number.")
                    return

                sorted_numbers, comparisons, swaps = selection_sort(numbers)

                result_label.config(
                    text="ORIGINAL: " + str(numbers)
                    + "\nSORTED:   " + str(sorted_numbers)
                    + "\nCOMPARISONS: " + str(comparisons)
                    + "\nSWAPS: " + str(swaps)
                )

            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid integers.")

        sort_btn = tk.Button(root, text="SORT", width=16, command=perform_sort)
        style_button(sort_btn, RED, filled=True)
        sort_btn.pack(pady=8)

        back_btn = tk.Button(root, text="BACK TO MENU", width=16, command=back_to_menu)
        style_button(back_btn, GREY)
        back_btn.pack(pady=10)

    sub_screen(build)


def recursion_lab():
    def build():
        make_header("RECURSION LAB", CYAN)

        lbl = tk.Label(root, text="ENTER A NON-NEGATIVE INTEGER:")
        style_label(lbl)
        lbl.pack()

        number_entry = tk.Entry(root, width=18)
        style_entry(number_entry)
        number_entry.pack(pady=10)

        result_label = tk.Label(root, text="", font=FONT_RESULT, justify="center")
        style_label(result_label, CYAN, FONT_RESULT)
        result_label.pack(pady=15)

        def get_number():
            try:
                n = int(number_entry.get())

                if n < 0:
                    messagebox.showerror("Invalid Input", "Please enter a non-negative integer.")
                    return None

                return n

            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter an integer.")
                return None

        def calculate_factorial():
            n = get_number()
            if n is not None:
                result = factorial(n)
                result_label.config(text="FACTORIAL(" + str(n) + ") = " + str(result))

        def calculate_fibonacci():
            n = get_number()
            if n is not None:
                result = fibonacci(n)
                result_label.config(text="FIBONACCI(" + str(n) + ") = " + str(result))

        def calculate_hanoi():
            n = get_number()

            if n is None:
                return

            if n == 0:
                messagebox.showerror("Invalid Input", "Number of disks must be greater than 0.")
                return

            hanoi_window = tk.Toplevel(root)
            hanoi_window.title("TOWER OF HANOI")
            hanoi_window.geometry("500x400")
            hanoi_window.config(bg=BG_BLACK)

            output = tk.Text(
                hanoi_window,
                width=55,
                height=20,
                bg="#161616",
                fg=WHITE,
                insertbackground=WHITE,
                font=("Courier New", 10),
                relief="flat",
                highlightthickness=2,
                highlightbackground=CYAN,
            )
            output.pack(padx=10, pady=10)

            import sys
            from io import StringIO

            old_stdout = sys.stdout
            sys.stdout = StringIO()

            tower_of_hanoi(n, "A", "B", "C")

            moves = sys.stdout.getvalue()

            sys.stdout = old_stdout

            output.insert(tk.END, moves)

        fact_btn = tk.Button(root, text="FACTORIAL", width=16, command=calculate_factorial)
        style_button(fact_btn, WHITE)
        fact_btn.pack(pady=5)

        fib_btn = tk.Button(root, text="FIBONACCI", width=16, command=calculate_fibonacci)
        style_button(fib_btn, WHITE)
        fib_btn.pack(pady=5)

        hanoi_btn = tk.Button(root, text="TOWER OF HANOI", width=16, command=calculate_hanoi)
        style_button(hanoi_btn, CYAN, filled=True)
        hanoi_btn.pack(pady=5)

        back_btn = tk.Button(root, text="BACK TO MENU", width=16, command=back_to_menu)
        style_button(back_btn, GREY)
        back_btn.pack(pady=15)

    sub_screen(build)


def complexity_lab():
    def build():
        make_header("COMPLEXITY ANALYZER", RED)

        algorithms = {
            "Linear Search": "linear_search",
            "Selection Sort": "selection_sort",
            "Factorial": "factorial",
            "Fibonacci": "fibonacci",
            "Tower of Hanoi": "tower_of_hanoi",
        }

        selected_algorithm = tk.StringVar(root)
        selected_algorithm.set("Linear Search")

        menu = tk.OptionMenu(root, selected_algorithm, *algorithms.keys())
        menu.config(
            width=24,
            bg=BG_BLACK,
            fg=RED,
            font=FONT_BUTTON,
            relief="flat",
            highlightthickness=2,
            highlightbackground=RED,
            activebackground=RED,
            activeforeground=BG_BLACK,
        )
        menu["menu"].config(
            bg=BG_BLACK,
            fg=RED,
            font=FONT_BUTTON,
            activebackground=RED,
            activeforeground=BG_BLACK,
        )
        menu.pack(pady=10)

        result_label = tk.Label(root, text="", font=FONT_RESULT, justify="left")
        style_label(result_label, WHITE, FONT_RESULT)
        result_label.pack(pady=20)

        def show_complexity():
            algorithm = algorithms[selected_algorithm.get()]
            result = get_complexity(algorithm)

            result_label.config(
                text="ALGORITHM: " + result["name"]
                + "\n\nBEST CASE: " + result["best"]
                + "\nWORST CASE: " + result["worst"]
                + "\nSPACE COMPLEXITY: " + result["space"]
                + "\n\nEXPLANATION:\n" + result["explanation"]
            )

        analyze_btn = tk.Button(root, text="ANALYZE", width=16, command=show_complexity)
        style_button(analyze_btn, RED, filled=True)
        analyze_btn.pack(pady=10)

        back_btn = tk.Button(root, text="BACK TO MENU", width=16, command=back_to_menu)
        style_button(back_btn, GREY)
        back_btn.pack(pady=10)

    sub_screen(build)


root = tk.Tk()

root.title("Algorithm Explorer & Complexity Analyzer — WEB-SLINGER EDITION")
root.geometry("650x650")
root.resizable(False, False)
root.config(bg=BG_BLACK)

create_main_menu()

root.mainloop()
